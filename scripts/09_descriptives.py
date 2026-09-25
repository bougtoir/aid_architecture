"""Phase 9: descriptive statistics + figures of aid architecture."""
import pandas as pd, numpy as np
import matplotlib; matplotlib.use("Agg")
import matplotlib.pyplot as plt
import os

os.makedirs("results/figures", exist_ok=True)
os.makedirs("results/tables", exist_ok=True)
os.makedirs("results/audits", exist_ok=True)

m = pd.read_parquet("data/processed/master_panel.parquet")
d = pd.read_parquet("data/processed/aid_architecture_donor_recipient_year.parquet")

exposures = ["share_aidtype_technical_cooperation","share_aidtype_budget_support",
             "share_aidtype_project","share_aidtype_pooled_earmarked",
             "share_channel_public_recipient","share_channel_public_donor",
             "share_channel_ngo","share_channel_multilateral","share_channel_private_recipient",
             "share_finance_grant","share_finance_loan","share_untied","share_tc_usd_irtc"]

# Table 1: recipient-year descriptive stats
t1 = m[exposures + ["oda_pc_usd","oda_pct_gdp","n_donors"]].describe(percentiles=[.25,.5,.75]).T
t1.to_csv("results/tables/table1_descriptives.csv")

# trends over time (disbursement-weighted global shares)
w = lambda g,c: np.average(g[c].fillna(0), weights=g.oda_disb_defl_usd)
tr = m.groupby("year").apply(lambda g: pd.Series({c: w(g,c) for c in exposures}), include_groups=False)
tr.to_csv("results/tables/architecture_trends_weighted.csv")

fig, ax = plt.subplots(1,2, figsize=(12,4))
for c in ["share_aidtype_technical_cooperation","share_aidtype_budget_support",
          "share_aidtype_project","share_aidtype_pooled_earmarked"]:
    ax[0].plot(tr.index, tr[c], label=c.replace("share_aidtype_",""))
ax[0].legend(fontsize=8); ax[0].set_title("Aid type shares (weighted)"); ax[0].set_xlabel("year")
for c in ["share_channel_public_recipient","share_channel_public_donor","share_channel_ngo",
          "share_channel_multilateral","share_channel_private_recipient"]:
    ax[1].plot(tr.index, tr[c], label=c.replace("share_channel_",""))
ax[1].legend(fontsize=8); ax[1].set_title("Delivery channel shares (weighted)"); ax[1].set_xlabel("year")
plt.tight_layout(); plt.savefig("results/figures/fig_architecture_trends.png", dpi=150); plt.close()

# donor heterogeneity: mean TC share and recipient-govt share by donor (top donors by volume)
top = d.groupby("donor_name").oda_disb_defl_usd.sum().sort_values(ascending=False).head(20)
sub = d[d.donor_name.isin(top.index)].copy()
for c,new in [("share_aidtype_technical_cooperation","tc_share"),
              ("share_channel_public_recipient","govt_share"),("share_untied","untied")]:
    sub["_w_"+new] = sub[c].fillna(0)*sub.oda_disb_defl_usd
dd = sub.groupby("donor_name").agg(vol=("oda_disb_defl_usd","sum"),
    tc_share=("_w_tc_share","sum"), govt_share=("_w_govt_share","sum"), untied=("_w_untied","sum"))
dd[["tc_share","govt_share","untied"]] = dd[["tc_share","govt_share","untied"]].div(dd.vol, axis=0)
dd["vol_bn"] = dd.vol/1e9
dd = dd.sort_values("vol_bn", ascending=False)
dd.to_csv("results/tables/table_donor_architecture.csv")

fig, ax = plt.subplots(figsize=(8,5))
x=np.arange(len(dd))
ax.bar(x, dd.govt_share, label="recipient-govt channel")
ax.bar(x, dd.tc_share, bottom=dd.govt_share, label="technical cooperation")
ax.set_xticks(x); ax.set_xticklabels(dd.index, rotation=60, ha="right", fontsize=8)
ax.set_ylabel("share of disbursed ODA"); ax.legend()
plt.tight_layout(); plt.savefig("results/figures/fig_donor_architecture.png", dpi=150); plt.close()

# aid/GDP distribution
fig, ax = plt.subplots(figsize=(6,4))
ax.hist(m.oda_pct_gdp.dropna().clip(0,0.5)*100, bins=60)
ax.set_xlabel("ODA disbursements / GDP (%)"); ax.set_ylabel("recipient-years")
plt.tight_layout(); plt.savefig("results/figures/fig_oda_gdp_hist.png", dpi=150); plt.close()

lines=["# PHASE 9 — Descriptives","",
 "Files:","- results/tables/table1_descriptives.csv","- results/tables/architecture_trends_weighted.csv",
 "- results/tables/table_donor_architecture.csv",
 "- results/figures/fig_architecture_trends.png","- results/figures/fig_donor_architecture.png",
 "- results/figures/fig_oda_gdp_hist.png","",
 f"master panel rows: {len(m)}, countries {m.iso3.nunique()}, years {int(m.year.min())}-{int(m.year.max())}",
 f"dyad panel rows: {len(d)}",
 "","Top-5 donor architecture table:", dd.head().to_string()]
open("results/audits/PHASE_9_DESCRIPTIVES.md","w").write("\n".join(lines))
print("done")
