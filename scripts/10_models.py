"""Phases 12-16: frozen-estimand models, lags, donor decomposition,
procurement, demographic adjustment, falsification.

All outputs: results/tables/*.csv, results/model_objects/*.pkl summary text,
results/audits/PHASE_*.md
"""
import pandas as pd, numpy as np, os, json
from linearmodels.panel import PanelOLS

os.makedirs("results/model_objects", exist_ok=True)
SEED = 20260925

m = pd.read_parquet("data/processed/master_panel.parquet")
d = pd.read_parquet("data/processed/aid_architecture_donor_recipient_year.parquet")
proc = pd.read_csv("data/processed/procurement_recipient_year.csv")

OUTCOMES = {"NY.GDP.PCAP.KD":"log_gdppc","NE.GDI.FTOT.ZS":"gfcf_gdp",
            "NV.IND.MANF.ZS":"manf_gdp"}
SECONDARY = {"GC.TAX.TOTL.GD.ZS":"tax_gdp","EG.ELC.ACCS.ZS":"elec_access"}
m["log_gdppc_lvl"] = np.log(m["NY.GDP.PCAP.KD"])

X_AIDTYPE = ["share_aidtype_technical_cooperation","share_aidtype_budget_support",
             "share_aidtype_project","share_aidtype_pooled_earmarked",
             "share_aidtype_ngo_core","share_aidtype_scholarships_students",
             "share_aidtype_admin_refugee_awareness"]  # ref: debt_relief+other
X_CHANNEL = ["share_channel_public_recipient","share_channel_public_donor",
             "share_channel_ngo","share_channel_multilateral",
             "share_channel_private_recipient"]  # ref: other
X_FIN = ["share_finance_grant","share_finance_loan"]  # ref: other_finance+equity+debt
X_EXTRA = ["share_tc_usd_irtc","share_untied"]

ADJ_A = ["ln_oda_pc","SP.POP.GROW","SP.URB.TOTL.IN.ZS"]
ADJ_B = ADJ_A + ["share_0_14","share_65plus","median_age","tfr"]
ADJ_C = ADJ_B + ["BX.KLT.DINV.WD.GD.ZS","NE.EXP.GNFS.ZS"]

WINDOWS = {"w1_2":(1,2),"w3_5":(3,5),"w6_10":(6,10),"w11_15":(11,15)}

def future_mean(df, ycol, a, b):
    out = df[["iso3","year",ycol]].copy()
    out = out.sort_values(["iso3","year"])
    vals=[]
    for c,g in out.groupby("iso3"):
        g=g.set_index("year")
        for t in g.index:
            sel=g.loc[(g.index>=t+a)&(g.index<=t+b),ycol]
            vals.append((c,t,sel.mean() if len(sel)>0 else np.nan))
    return pd.DataFrame(vals,columns=["iso3","year","y_fwd"]).set_index(["iso3","year"])

def run_spec(df, y, xs, adj):
    cols=xs+adj+[y]
    dd=df.dropna(subset=cols).copy()
    if len(dd)<200 or dd.iso3.nunique()<20: return None,0
    dd=dd.set_index(["iso3","year"])
    keep=[c for c in xs+adj if dd[c].std()>1e-9]
    if len(keep)<2: return None,len(dd)
    exog=dd[keep]
    mod=PanelOLS(dd[y],exog,entity_effects=True,time_effects=True,
                 drop_absorbed=True,check_rank=False)
    r=mod.fit(cov_type="clustered",cluster_entity=True)
    return r,len(dd)

results=[]
for (a,b),wname in [(v,k) for k,v in WINDOWS.items()]:
    for ycol,yname in {**OUTCOMES,**SECONDARY}.items():
        src = "log_gdppc_lvl" if yname=="log_gdppc" else ycol
        fm=future_mean(m,src,a,b).reset_index()
        df=m.merge(fm,on=["iso3","year"],how="left")
        for xset,xname in [(X_AIDTYPE,"aidtype"),(X_CHANNEL,"channel"),
                           (X_FIN,"finance"),(X_EXTRA,"extra")]:
            r,n=run_spec(df,"y_fwd",xset,ADJ_B)
            if r is None:
                results.append({"window":wname,"outcome":yname,"xset":xname,"n":0}); continue
            for x in xset:
                results.append({"window":wname,"outcome":yname,"xset":xname,"term":x,
                    "beta":r.params.get(x),"se":r.std_errors.get(x),
                    "p":r.pvalues.get(x),"n":n,"r2_within":r.rsquared_within})

res=pd.DataFrame(results)
res.to_csv("results/tables/model_coefficients_all.csv",index=False)
print(res[res.term.notna()].shape)

# ---------- Phase 13: donor decomposition ----------
dd=d.dropna(subset=["share_aidtype_technical_cooperation"]).copy()
dd=dd.set_index(["donor_code","recipient_code","year"])
rows=[]
for v in ["share_aidtype_technical_cooperation","share_aidtype_project",
          "share_aidtype_budget_support","share_channel_public_recipient",
          "share_channel_ngo","share_tc_usd_irtc"]:
    sub=dd[v].unstack("year")
    # donor FE share of variance: regress v on donor dummies + recipient dummies + year
    sub2=dd.reset_index().dropna(subset=[v])
    # weighted by disbursement
    w=sub2.oda_disb_defl_usd.clip(lower=0)
    import statsmodels.api as sm
    X=pd.get_dummies(sub2.donor_code,prefix="d",drop_first=True)
    Xr=pd.get_dummies(sub2.recipient_code,prefix="r",drop_first=True)
    Xt=pd.get_dummies(sub2.year,prefix="t",drop_first=True)
    Xall=pd.concat([X,Xr,Xt],axis=1).astype(float)
    Xd=pd.concat([X,Xt],axis=1).astype(float)
    mfull=sm.WLS(sub2[v],sm.add_constant(Xall),weights=w).fit()
    mdon=sm.WLS(sub2[v],sm.add_constant(Xd),weights=w).fit()
    m0=sm.WLS(sub2[v],np.ones((len(sub2),1)),weights=w).fit()
    rows.append({"var":v,"r2_full":mfull.rsquared,"r2_donoronly":mdon.rsquared,
                 "r2_null":m0.rsquared,"n":len(sub2)})
dec=pd.DataFrame(rows)
dec.to_csv("results/tables/donor_decomposition.csv",index=False)
print(dec)

# ---------- Phase 14: procurement ----------
meta=json.load(open("data/raw/wdi/country_metadata.json"))
name2iso={c["name"]:c["id"] for c in meta[1]}
name2iso.update({"Cambodia":"KHM","Vietnam":"VNM","Egypt, Arab Rep.":"EGY","Yemen, Rep.":"YEM",
 "Congo, Dem. Rep.":"COD","Congo, Rep.":"COG","Lao PDR":"LAO","Kyrgyz Republic":"KGZ",
 "Slovak Republic":"SVK","Russian Federation":"RUS","Iran, Islamic Rep.":"IRN",
 "Korea, Dem. People's Rep.":"PRK","Syrian Arab Republic":"SYR","Venezuela, RB":"VEN",
 "Tanzania":"TZA","Gambia, The":"GMB","Bahamas, The":"BHS","Cote d'Ivoire":"CIV",
 "Cabo Verde":"CPV","Turkiye":"TUR","Turkey":"TUR","Bolivia":"BOL","Brunei Darussalam":"BRN"})
proc["iso3"]=proc.recipient_name.map(name2iso)
mp=m.merge(proc.dropna(subset=["iso3"]),on=["iso3","year"],how="inner",suffixes=("","_p"))
lines=["# PHASE 14 — Procurement","",
 f"- mergeable recipient-years: {len(mp)}",
 f"- corr(local share, public_recipient channel share): {mp[['local_procurement_share','share_channel_public_recipient']].corr().iloc[0,1]:.3f}",
 f"- corr(local share, tc share): {mp[['local_procurement_share','share_aidtype_technical_cooperation']].corr().iloc[0,1]:.3f}",
 "","Partial sample (recent-biased) — descriptive only."]
open("results/audits/PHASE_14_PROCUREMENT.md","w").write("\n".join(lines))

# ---------- Phase 15: adjustment-set stability ----------
stab=[]
for ycol,yname in OUTCOMES.items():
    src="log_gdppc_lvl" if yname=="log_gdppc" else ycol
    fm=future_mean(m,src,3,5).reset_index()
    df=m.merge(fm,on=["iso3","year"])
    for adjname,adj in [("A",ADJ_A),("B",ADJ_B),("C",ADJ_C)]:
        r,n=run_spec(df,"y_fwd",X_AIDTYPE,adj)
        if r:
            stab.append({"outcome":yname,"set":adjname,"n":n,
                "beta_tc":r.params.get("share_aidtype_technical_cooperation"),
                "se_tc":r.std_errors.get("share_aidtype_technical_cooperation"),
                "beta_bs":r.params.get("share_aidtype_budget_support"),
                "beta_govt":np.nan})
pd.DataFrame(stab).to_csv("results/tables/adjustment_stability.csv",index=False)
print(pd.DataFrame(stab))

# ---------- Phase 16: falsification ----------
fal=[]
# (1) lead placebo: architecture at t+3 predicts outcome mean over t-1..t
def past_mean(df,ycol,a,b):
    rows=[]
    for c,g in df.sort_values(["iso3","year"]).groupby("iso3"):
        g=g.set_index("year")
        for t in g.index:
            sel=g.loc[(g.index>=t-b)&(g.index<=t-a),ycol]
            rows.append((c,t,sel.mean() if len(sel)>0 else np.nan))
    return pd.DataFrame(rows,columns=["iso3","year","y_past"]).set_index(["iso3","year"])

src="log_gdppc_lvl"
pm=past_mean(m,src,0,1).reset_index()
dfp=m.merge(pm,on=["iso3","year"])
# shift exposures +3 years
sh=m[["iso3","year"]+X_AIDTYPE+ADJ_B].copy(); sh["year"]=sh.year-3
dfp=dfp.merge(sh,on=["iso3","year"],suffixes=("","_lead"))
xs=[c+"_lead" for c in X_AIDTYPE]
adjl=[c+"_lead" for c in ADJ_B]
r_lead,n=run_spec(dfp.rename(columns={"y_past":"y_fwd"}),"y_fwd",xs,adjl)
if r_lead:
    fal.append({"test":"lead_placebo","term":"share_aidtype_technical_cooperation_lead",
                "beta":r_lead.params.get(xs[0]),"p":r_lead.pvalues.get(xs[0]),"n":n})

# (2) pseudo-outcome: urban share
fm2=future_mean(m,"SP.URB.TOTL.IN.ZS",3,5).reset_index()
df2=m.merge(fm2,on=["iso3","year"])
r2,n2=run_spec(df2,"y_fwd",X_AIDTYPE,ADJ_B)
if r2:
    for x in X_AIDTYPE:
        fal.append({"test":"pseudo_outcome_urban","term":x,
                    "beta":r2.params.get(x),"p":r2.pvalues.get(x),"n":n2})

# (3) shuffle placebo on gdppc w3_5
rng=np.random.default_rng(SEED)
fm3=future_mean(m,"log_gdppc_lvl",3,5).reset_index()
df3=m.merge(fm3,on=["iso3","year"]).dropna(subset=X_AIDTYPE+ADJ_B+["y_fwd"]).copy()
betas=[]
basecols=X_AIDTYPE+ADJ_B
for i in range(200):
    dfi=df3.reset_index(drop=True).copy()
    for y,g in dfi.groupby("year"):
        dfi.loc[g.index,X_AIDTYPE]=dfi.loc[rng.permutation(g.index.values),X_AIDTYPE].values
    r,n=run_spec(dfi,"y_fwd",X_AIDTYPE,ADJ_B)
    if r: betas.append(r.params.get("share_aidtype_technical_cooperation"))
real=res[(res.window=="w3_5")&(res.outcome=="log_gdppc")&(res.term=="share_aidtype_technical_cooperation")]
real_beta=real.beta.iloc[0] if len(real) else np.nan
betas=np.array(betas)
fal.append({"test":"shuffle_placebo","term":"share_aidtype_technical_cooperation",
            "real_beta":real_beta,"placebo_mean":np.nanmean(betas),
            "placebo_sd":np.nanstd(betas),
            "pct_gt_real":float(np.mean(np.abs(betas)>=abs(real_beta))) if len(betas) else np.nan,
            "n":len(betas)})
pd.DataFrame(fal).to_csv("results/tables/falsification_results.csv",index=False)
print(pd.DataFrame(fal).to_string())
print("DONE")
