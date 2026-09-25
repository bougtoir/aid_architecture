"""Phase 8: master analysis panel — recipient x year.

Joins recipient-year aid architecture + demography + outcomes.
"""
import pandas as pd, numpy as np

aid = pd.read_parquet("data/processed/aid_architecture_recipient_year.parquet")
dem = pd.read_parquet("data/processed/demography_country_year.parquet")
out = pd.read_parquet("data/processed/outcomes_country_year.parquet")

a = aid.dropna(subset=["iso3"]).copy()
master = (a.merge(dem, on=["iso3","year"], how="left")
           .merge(out.drop(columns=["iso2Code","country_name"], errors="ignore"),
                  on=["iso3","year"], how="left"))

# CRS disbursement columns are in USD MILLIONS (constant, DAC-deflator base);
# NY.GDP.MKTP.KD is constant 2015 US$ dollars -> multiply by 1e6.
master["oda_pc_usd"] = master.oda_disb_defl_usd*1e6 / (master.pop_total_1000*1000)
master["oda_pct_gdp"] = master.oda_disb_defl_usd*1e6 / master["NY.GDP.MKTP.KD"]
master["lny_gdppc"] = np.log(master["NY.GDP.PCAP.KD"])
master["ln_oda_pc"] = np.log(master.oda_pc_usd.clip(lower=0.001))

master.to_parquet("data/processed/master_panel.parquet", index=False)
print("master:", master.shape, "countries:", master.iso3.nunique())

cov = master[["oda_disb_defl_usd","NY.GDP.PCAP.KD","NE.GDI.FTOT.ZS","NV.IND.MANF.ZS",
              "GC.TAX.TOTL.GD.ZS","EG.ELC.ACCS.ZS","pop_total_1000","share_0_14",
              "tfr","median_age"]].notna().mean()
lines = ["# PHASE 8 — Master panel","",
         "rows: %d; countries: %d; years %d-%d" %
         (len(master), master.iso3.nunique(), master.year.min(), master.year.max()),
         "","## key variable coverage:", cov.to_string(),
         "","- rows with aid but no iso3 dropped: %d" % (len(aid)-len(a))]
open("results/audits/PHASE_8_MASTER_PANEL.md","w").write("\n".join(lines))
print(cov)
