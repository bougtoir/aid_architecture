"""Phase 4: canonical donor x recipient x year aid-architecture panel.

Input : data/raw/oecd_crs/CRS-reduced.parquet (6.24M activity rows)
Output: data/processed/aid_architecture_donor_recipient_year.parquet
        data/processed/aid_architecture_recipient_year.parquet
        results/audits/PHASE_4_PANEL_VALIDATION.md

Exposure metric: gross disbursements in constant USD (usd_disbursement_defl).
ODA rows only (category==10). Shares are disbursement-weighted.
"""
import pandas as pd, numpy as np, csv, os

CRS = "data/interim/crs_cols2.parquet"  # full CRS incl aid_t/TC cols
REC = "data/interim/codelists/Recipient.csv"
os.makedirs("data/processed", exist_ok=True)

# ---- recipient code -> ISO3 / region / income / fragile ----
rec = pd.read_csv(REC)
rec = rec.rename(columns={rec.columns[0]:"recipient_code", rec.columns[3]:"iso3"})
rec["recipient_code"] = pd.to_numeric(rec["recipient_code"], errors="coerce")
rec = rec[["recipient_code","iso3","Region","DAC_IncomeGroup","LandLocked","SIDS","FragileState"]].dropna(subset=["recipient_code"])
rec["recipient_code"] = rec["recipient_code"].astype(int)

# ---- donor code -> ISO3 ----
don = pd.read_csv("data/interim/codelists/Donor.csv", header=None, skiprows=3)
don.columns = [f"c{i}" for i in range(don.shape[1])]
def _panel(off):
    p = don[[f"c{off}",f"c{off+1}",f"c{off+2}"]].copy()
    p.columns = ["donor_code","donor_iso","donor_name"]
    p["donor_code"] = pd.to_numeric(p.donor_code, errors="coerce")
    return p.dropna(subset=["donor_code","donor_name"])
donor_map = pd.concat([_panel(o) for o in (0,5,10,15) if f"c{o+2}" in don.columns])
donor_map["donor_code"] = donor_map["donor_code"].astype(int)
donor_map["donor_iso"] = donor_map["donor_iso"].astype(str).str.strip()
donor_map["donor_name"] = donor_map["donor_name"].astype(str).str.strip()
donor_map = donor_map.drop_duplicates("donor_code")

# ---- sector mapping ----
def sector_group(sc):
    if pd.isna(sc): return "other"
    s = int(sc); hundred = s // 100; ten = s - s % 10
    if hundred == 1:
        return {110:"education", 120:"health", 130:"health",
                140:"water_sanitation", 150:"governance", 160:"other_social"}.get(ten, "other_social")
    if hundred == 2:
        return {210:"infrastructure", 220:"infrastructure", 230:"energy",
                240:"finance_business", 250:"finance_business"}.get(ten, "infrastructure")
    if hundred == 3:
        return {310:"agriculture", 320:"industry", 330:"trade"}.get(ten, "productive")
    if hundred == 4:
        return {410:"environment", 430:"multisector", 400:"multisector"}.get(ten, "multisector")
    if hundred == 5:
        return "program_support" if s >= 500 else "other"
    if hundred == 6:
        return "debt"
    if hundred == 7:
        return "humanitarian"
    if hundred == 9:
        return "admin_refugee_other"
    return "other"

def channel_group(cc):
    if pd.isna(cc): return "unknown"
    c = int(cc); th = c // 1000
    return {11:"public_donor",12:"public_recipient",13:"public_third",
            20:"ngo",21:"ngo",22:"ngo",23:"ngo",
            30:"ppp_network",31:"ppp_network",32:"ppp_network",
            40:"multilateral",41:"multilateral",42:"multilateral",43:"multilateral",
            44:"multilateral",45:"multilateral",46:"multilateral",47:"multilateral",
            50:"other",51:"university",52:"other",
            60:"private_sector",61:"private_donor",62:"private_recipient",63:"private_third",
            90:"other"}.get(th,"other")

def aidtype_group(a):
    if pd.isna(a): return "other"
    a = str(a)
    if a in ("A01","A02"): return "budget_support"
    if a == "B01": return "ngo_core"
    if a in ("B02","B03","B04","B021","B022","B031","B032","B033"): return "pooled_earmarked"
    if a == "C01": return "project"
    if a in ("D01","D02"): return "technical_cooperation"
    if a in ("E01","E02"): return "scholarships_students"
    if a == "F01": return "debt_relief_aidtype"
    if a in ("G01","H01","H02"): return "admin_refugee_awareness"
    return "other"

def finance_group(ft):
    if pd.isna(ft): return "unknown"
    f = int(ft)
    if f == 110: return "grant"
    if 420 <= f < 440: return "loan"
    if 510 <= f < 540: return "equity"
    if 610 <= f < 640: return "debt_relief"
    if 1100 <= f <= 1102: return "guarantee"
    return "other_finance"

print("loading CRS ...")
df = pd.read_parquet(CRS)
df = df[df.year >= 1995]
df = df[df.recipient_code.notna() & df.donor_code.notna()]
df["sector_grp"] = df.sector_code.map(sector_group)
df["channel_grp"] = df.parent_channel_code.fillna(df.channel_code).map(channel_group)
df["finance_grp"] = df.finance_t.map(finance_group)
df["aidtype_grp"] = df.aid_t.map(aidtype_group)
df["oda"] = (df.category == 10).astype(float)
oda = df[df.category == 10].copy()   # ODA only for architecture
print("ODA rows:", len(oda))

# keep OOF/others as separate totals
other = df[df.category != 10].groupby(["donor_code","recipient_code","year"], as_index=False).agg(
    nonoda_disb_defl=("usd_disbursement_defl","sum"), nonoda_commit_defl=("usd_commitment_defl","sum"))

amt = "usd_disbursement_defl"
oda[amt] = oda[amt].fillna(0.0)
for col in ["usd_amount_untied_defl","usd_amount_partial_tied_defl","usd_amounttied_defl"]:
    oda[col] = oda[col].fillna(0.0)

# ---- pivot shares ----
def share_pivot(d, col, prefix):
    p = d.groupby(["donor_code","recipient_code","year",col])[amt].sum().unstack(col).fillna(0)
    tot = p.sum(axis=1).replace(0, np.nan)
    return (p.div(tot, axis=0).fillna(0)
             .rename(columns={k: f"{prefix}_{k}" for k in p.columns}))

sec = share_pivot(oda, "sector_grp", "share_sector")
chn = share_pivot(oda, "channel_grp", "share_channel")
fin = share_pivot(oda, "finance_grp", "share_finance")
aty = share_pivot(oda, "aidtype_grp", "share_aidtype")

# technical-cooperation amount share (usd_irtc is the TC component of a project)
irtc = oda.groupby(["donor_code","recipient_code","year"]).apply(
    lambda g: g.usd_irtc.fillna(0).sum()/max(g[amt].sum(),1e-9), include_groups=False).rename("share_tc_usd_irtc")
gnd = oda.groupby(["donor_code","recipient_code","year"]).apply(
    lambda g: g.loc[g.gender.isin([1,2]), amt].sum()/max(g[amt].sum(),1e-9), include_groups=False).rename("share_gender_marker")

# bi_multi -> bilateral share / multilateral earmarked share
oda["multi_earmarked"] = (oda.bi_multi == 2).astype(float)
bm = oda.groupby(["donor_code","recipient_code","year"]).apply(
    lambda g: g.loc[g.bi_multi==2, amt].sum()/max(g[amt].sum(),1e-9), include_groups=False).rename("share_earmarked_multilateral")

agg = oda.groupby(["donor_code","recipient_code","year"], as_index=False).agg(
    oda_disb_defl_usd=("usd_disbursement_defl","sum"),
    oda_commit_defl_usd=("usd_commitment_defl","sum"),
    oda_grant_equiv_defl=("usd_grant_equiv_defl" if "usd_grant_equiv_defl" in oda.columns else "usd_disbursement_defl","sum"),
    untied_defl=("usd_amount_untied_defl","sum"),
    partial_tied_defl=("usd_amount_partial_tied_defl","sum"),
    tied_defl=("usd_amounttied_defl","sum"),
    n_activities=("usd_disbursement_defl","size"))

panel = agg.merge(sec, on=["donor_code","recipient_code","year"], how="left") \
           .merge(chn, on=["donor_code","recipient_code","year"], how="left") \
           .merge(fin, on=["donor_code","recipient_code","year"], how="left") \
           .merge(aty, on=["donor_code","recipient_code","year"], how="left") \
           .merge(irtc, on=["donor_code","recipient_code","year"], how="left") \
           .merge(gnd, on=["donor_code","recipient_code","year"], how="left") \
           .merge(bm, on=["donor_code","recipient_code","year"], how="left") \
           .merge(other, on=["donor_code","recipient_code","year"], how="left") \
           .merge(rec, on="recipient_code", how="left") \
           .merge(donor_map, on="donor_code", how="left")

tying_total = panel.untied_defl + panel.partial_tied_defl + panel.tied_defl
panel["share_untied"] = np.where(tying_total>0, panel.untied_defl/tying_total, np.nan)
panel["share_partially_tied"] = np.where(tying_total>0, panel.partial_tied_defl/tying_total, np.nan)
panel["share_tied"] = np.where(tying_total>0, panel.tied_defl/tying_total, np.nan)
panel["tying_reported"] = tying_total > 0
panel = panel.drop(columns=["untied_defl","partial_tied_defl","tied_defl"])

out = "data/processed/aid_architecture_donor_recipient_year.parquet"
panel.to_parquet(out, index=False)
print("wrote", out, panel.shape)

# ---- recipient-year aggregate (portfolio across donors) ----
ry = oda.groupby(["recipient_code","year"], as_index=False).agg(
    oda_disb_defl_usd=(amt,"sum"), oda_commit_defl_usd=("usd_commitment_defl","sum"),
    n_donors=("donor_code","nunique"), n_activities=(amt,"size"))
for g in ["sector_grp","channel_grp","finance_grp","aidtype_grp"]:
    p = oda.groupby(["recipient_code","year",g])[amt].sum().unstack(g).fillna(0)
    p = p.div(p.sum(axis=1).replace(0,np.nan), axis=0).fillna(0)
    p.columns = [f"share_{g.replace('_grp','')}_{c}" for c in p.columns]
    ry = ry.merge(p.reset_index(), on=["recipient_code","year"], how="left")
irtc_ry = oda.groupby(["recipient_code","year"]).apply(
    lambda g: pd.Series({
        "share_tc_usd_irtc": g.usd_irtc.fillna(0).sum()/max(g[amt].sum(),1e-9),
        "share_gender_marker": g.loc[g.gender.isin([1,2]), amt].sum()/max(g[amt].sum(),1e-9),
        "share_untied": g.usd_amount_untied_defl.fillna(0).sum()/max(
            g[["usd_amount_untied_defl","usd_amount_partial_tied_defl","usd_amounttied_defl"]].fillna(0).sum(axis=1).sum(),1e-9),
        "share_tied": g.usd_amounttied_defl.fillna(0).sum()/max(
            g[["usd_amount_untied_defl","usd_amount_partial_tied_defl","usd_amounttied_defl"]].fillna(0).sum(axis=1).sum(),1e-9)}),
    include_groups=False).reset_index()
ry = ry.merge(irtc_ry, on=["recipient_code","year"], how="left")
ry = ry.merge(rec, on="recipient_code", how="left")
ry.to_parquet("data/processed/aid_architecture_recipient_year.parquet", index=False)
print("wrote recipient-year", ry.shape)

# ---- validation ----
tot_by_year = panel.groupby("year").oda_disb_defl_usd.sum()/1e9
lines = ["# PHASE 4 — Aid architecture panel validation","",
 f"- ODA activity rows used (1995+, category==10): {len(oda):,}",
 f"- Dyad-year panel: {panel.shape[0]:,} rows, {panel.shape[1]} cols",
 f"- Donors: {panel.donor_code.nunique()}, recipients: {panel.recipient_code.nunique()}",
 f"- Years: {panel.year.min()}-{panel.year.max()}","",
 "## ODA disbursement (deflated USD bn) by year:",
 tot_by_year.to_string(),
 "",
 "## Checks:",
 f"- sector share sums ~1: mean {(panel.filter(like='share_sector_').sum(axis=1)).mean():.4f}",
 f"- channel share sums ~1: mean {(panel.filter(like='share_channel_').sum(axis=1)).mean():.4f}",
 f"- finance share sums ~1: mean {(panel.filter(like='share_finance_').sum(axis=1)).mean():.4f}",
 f"- negative disbursements: {(panel.oda_disb_defl_usd<0).sum()} rows",
]
open("results/audits/PHASE_4_PANEL_VALIDATION.md","w").write("\n".join(lines))
print("audit written")
