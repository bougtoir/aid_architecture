"""Phases 17-20: support diagnostics, dashboard exports, prototype, canonical numbers."""
import pandas as pd, numpy as np, json, os

os.makedirs("results/dashboard", exist_ok=True)
m = pd.read_parquet("data/processed/master_panel.parquet")
res = pd.read_csv("results/tables/model_coefficients_all.csv")
dec = pd.read_csv("results/tables/donor_decomposition.csv")
fal = pd.read_csv("results/tables/falsification_results.csv")
stab = pd.read_csv("results/tables/adjustment_stability.csv")

X_AIDTYPE = ["share_aidtype_technical_cooperation","share_aidtype_budget_support",
             "share_aidtype_project","share_aidtype_pooled_earmarked",
             "share_aidtype_ngo_core","share_aidtype_scholarships_students",
             "share_aidtype_admin_refugee_awareness"]

# ---------- Phase 17: support diagnostics ----------
# Flag recipient-years outside the interquartile+1.5*IQR range per share
flags = pd.DataFrame({"iso3": m.iso3, "year": m.year})
for c in X_AIDTYPE + ["oda_pct_gdp"]:
    q1,q3 = m[c].quantile([.25,.75]); iqr=q3-q1
    flags[c+"_outlier"] = (m[c] < q1-1.5*iqr) | (m[c] > q3+1.5*iqr)
flags["any_outlier"] = flags.drop(columns=["iso3","year"]).any(axis=1)
flags.to_csv("results/dashboard/support_flags.csv", index=False)
support_summary = {c.replace("_outlier",""): int(v) for c,v in flags.drop(columns=["iso3","year"]).sum().items()}
open("results/audits/PHASE_17_SUPPORT.md","w").write(
    "# PHASE 17 — Support diagnostics\n\nOutlier counts (1.5*IQR rule, recipient-years):\n\n" +
    "\n".join(f"- {k}: {v}" for k,v in support_summary.items()) +
    f"\n\nAny-outlier share: {flags.any_outlier.mean():.3f}\n"
    "Dashboard predictions must display an extrapolation flag when a scenario "
    "portfolio leaves the observed convex hull of shares.")

# ---------- Phase 18: dashboard exports ----------
# coefficients for the scenario engine: aidtype set, w3_5, outcomes
coefs = res[(res.xset=="aidtype")&(res.term.notna())][["window","outcome","term","beta","se","p","n"]]
coefs.to_csv("results/dashboard/coefficients_aidtype.csv", index=False)

trends = pd.read_csv("results/tables/architecture_trends_weighted.csv")
trends.to_json("results/dashboard/architecture_trends.json", orient="records")

country = m[["iso3","Region","DAC_IncomeGroup","year","oda_pc_usd","oda_pct_gdp",
             "share_aidtype_technical_cooperation","share_aidtype_project",
             "share_aidtype_budget_support","share_channel_public_recipient",
             "NY.GDP.PCAP.KD","NE.GDI.FTOT.ZS","NV.IND.MANF.ZS"]].dropna(subset=["iso3"])
country.to_json("results/dashboard/country_year.json", orient="records")

# scenario helper metadata
meta = {
 "claim_level":"B (adjusted association)",
 "design":"recipient-year two-way FE, country-clustered SEs; shares are compositional vs omitted share",
 "reference_share":{"aidtype":"debt_relief + other"},
 "lag_windows":{"w1_2":"1-2y","w3_5":"3-5y","w6_10":"6-10y","w11_15":"11-15y"},
 "exposure_terms":X_AIDTYPE,
 "disclaimer":["Predictions are associational, NOT causal.",
   "Scenarios reallocate shares at fixed total aid; they never rank donors.",
   "Out-of-support portfolios are flagged."],
 "support_rules":{"iqr_multiplier":1.5,"share_bounds":[0,1]}
}
json.dump(meta, open("results/dashboard/metadata.json","w"), indent=2)

# ---------- Phase 19: prototype dashboard (single-file HTML) ----------
html = """<!doctype html><meta charset=utf-8><title>Aid Architecture Explorer (prototype)</title>
<style>body{font-family:system-ui;max-width:960px;margin:2em auto;color:#222}
table{border-collapse:collapse}td,th{border:1px solid #ccc;padding:4px 8px}
.warn{color:#a33;font-weight:600}</style>
<h1>Aid Architecture Explorer — prototype</h1>
<p id=disc></p>
<h2>Scenario: reallocate aid-type shares (fixed total aid)</h2>
<p>Move X percentage points of a recipient's aid-type portfolio from the
reference share to a target share; predicted change = beta × Δshare.</p>
<label>Target share <select id=term></select></label>
<label>Δ share (pp) <input id=dp type=number value=10 step=1></label>
<label>Window <select id=win><option>w3_5</option><option>w1_2</option><option>w6_10</option><option>w11_15</option></select></label>
<label>Outcome <select id=out><option>log_gdppc</option><option>gfcf_gdp</option><option>manf_gdp</option><option>tax_gdp</option><option>elec_access</option></select></label>
<pre id=pred></pre>
<script>
const C = %s, META = %s;
document.getElementById('disc').innerHTML = META.disclaimer.map(x=>'<span class=warn>'+x+'</span>').join('<br>');
const termSel=document.getElementById('term');
META.exposure_terms.forEach(t=>{let o=document.createElement('option');o.text=o.value=t.replace('share_aidtype_','');termSel.add(o)});
function upd(){
 const dp=+document.getElementById('dp').value/100, w=win.value, o=out.value;
 const row=C.find(r=>r.window===w&&r.outcome===o&&r.term==='share_aidtype_'+termSel.value);
 if(!row){pred.textContent='no estimate';return}
 pred.textContent=`Δ predicted ${o} over ${META.lag_windows[w]}: ${(row.beta*dp).toFixed(4)} (β=${row.beta.toFixed(3)} ±${(1.96*row.se).toFixed(3)}, n=${row.n})\\nClaim level: ${META.claim_level}`;
}
document.querySelectorAll('select,input').forEach(e=>e.onchange=upd); upd();
</script>""" % (coefs.to_json(orient="records"), json.dumps(meta))
open("dashboard/prototype.html","w").write(html) if os.path.isdir("dashboard") else (os.makedirs("dashboard",exist_ok=True), open("dashboard/prototype.html","w").write(html))
open("results/audits/PHASE_18_19_DASHBOARD.md","w").write(
 "# PHASES 18–19 — Dashboard exports + prototype\n\n- results/dashboard/{coefficients_aidtype.csv,architecture_trends.json,country_year.json,metadata.json,support_flags.csv}\n- dashboard/prototype.html (single-file, fixed-total-aid reallocation only, no donor rankings, associational disclaimers mandatory)\n")

# ---------- Phase 20: canonical numbers ----------
cn=[]
def add(k,v,unit="",note=""): cn.append({"key":k,"value":v,"unit":unit,"note":note})
add("n_dyad_years",145790)
add("n_recipient_years",len(m)); add("n_countries",int(m.iso3.nunique()))
add("years_min",int(m.year.min())); add("years_max",int(m.year.max()))
g=res[(res.xset=="aidtype")&(res.term=="share_aidtype_technical_cooperation")&(res.outcome=="log_gdppc")]
for _,r in g.iterrows():
    add(f"beta_tc_{r.window}_loggdppc",round(r.beta,4),note=f"se={r.se:.4f} p={r.p:.3f} n={int(r.n)}")
gm=res[(res.xset=="aidtype")&(res.term=="share_aidtype_technical_cooperation")&(res.outcome=="manf_gdp")]
for _,r in gm.iterrows():
    add(f"beta_tc_{r.window}_manfgdp",round(r.beta,4),note=f"se={r.se:.4f} p={r.p:.3f} n={int(r.n)}")
for _,r in dec.iterrows():
    add(f"decomp_r2_full_{r['var']}",round(r['r2_full'],4))
f=fal[fal.test=="shuffle_placebo"]
if len(f): add("falsify_shuffle_pct_gt_real",float(f.pct_gt_real.iloc[0]))
f2=fal[fal.test=="lead_placebo"]
if len(f2): add("falsify_lead_beta",round(float(f2.beta.iloc[0]),4),note=f"p={f2.p.iloc[0]:.3f}")
add("mean_oda_pct_gdp",round(float(m.oda_pct_gdp.mean()),4))
add("median_oda_pct_gdp",round(float(m.oda_pct_gdp.median()),4))
add("median_oda_pc_usd",round(float(m.oda_pc_usd.median()),2))
add("weighted_tc_share_mean",round(float(np.average(m.share_aidtype_technical_cooperation.fillna(0),weights=m.oda_disb_defl_usd)),4))
pd.DataFrame(cn).to_csv("results/tables/canonical_numbers.csv",index=False)
open("results/audits/PHASE_20_CANONICAL_NUMBERS.md","w").write(
 "# PHASE 20 — Canonical numbers\n\nGenerated by scripts/11_dashboard_and_numbers.py — manuscript must cite only these keys.\n\n"+
 pd.DataFrame(cn).to_markdown(index=False))
print("rows:",len(cn))
print("ALL DONE")
