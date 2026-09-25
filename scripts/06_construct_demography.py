"""Phase 6: demography_country_year panel from UN WPP 2024.

Inputs : data/raw/un_wpp/WPP2024_Demographic_Indicators_Medium.csv.gz
         data/raw/un_wpp/WPP2024_Population1JanuaryByAge5GroupSex_Medium.csv.gz
Output : data/processed/demography_country_year.parquet
"""
import pandas as pd, numpy as np

dem = pd.read_csv("data/raw/un_wpp/WPP2024_Demographic_Indicators_Medium.csv.gz",
                  compression="gzip", low_memory=False)
dem = dem[(dem.LocTypeID == 4)]  # countries/areas
keep = {"ISO3_code":"iso3","Time":"year","TPopulation1Jan":"pop_total_1000",
        "PopDensity":"pop_density","PopSexRatio":"pop_sex_ratio",
        "MedianAgePop":"median_age","NatChange":"nat_change_1000",
        "PopChange":"pop_change_1000","PopGrowthRate":"pop_growth_rate_pct",
        "Births":"births_1000","Deaths":"deaths_1000","CNMR":"net_migration_rate",
        "TFR":"tfr","LEx":"life_expectancy","Q5":"under5_mortality",
        "CBR":"cbr","CDR":"cdr"}
cols = [c for c in keep if c in dem.columns]
dem = dem[cols].rename(columns=keep)
dem = dem[dem.iso3.notna() & (dem.year >= 1960) & (dem.year <= 2024)]

age = pd.read_csv("data/raw/un_wpp/WPP2024_Population1JanuaryByAge5GroupSex_Medium.csv.gz",
                  compression="gzip", low_memory=False)
age = age[age.ISO3_code.notna()]
age = age[["ISO3_code","Time","AgeGrpStart","PopTotal"]].rename(
    columns={"ISO3_code":"iso3","Time":"year","AgeGrpStart":"age_start","PopTotal":"pop_1000"})
age = age[(age.year >= 1960) & (age.year <= 2024)]
age["age_start"] = pd.to_numeric(age["age_start"], errors="coerce")
def grp(a):
    if a < 15: return "child"
    if a < 65: return "working"
    return "old"
age["grp"] = age.age_start.map(grp)
g = age.groupby(["iso3","year","grp"]).pop_1000.sum().unstack("grp").fillna(0)
g["pop_total"] = g.sum(axis=1)
g["share_0_14"] = g.child / g.pop_total
g["share_15_64"] = g.working / g.pop_total
g["share_65plus"] = g.old / g.pop_total
g["dependency_ratio"] = (g.child + g.old) / g.working
g["youth_dependency"] = g.child / g.working
g["old_dependency"] = g.old / g.working
g = g.drop(columns=["child","working","old","pop_total"]).reset_index()

out = dem.merge(g, on=["iso3","year"], how="left")
out.to_parquet("data/processed/demography_country_year.parquet", index=False)
print(out.shape, out.iso3.nunique(), out.year.min(), out.year.max())

lines = ["# PHASE 6 — Demography panel", "",
 f"- rows: {len(out):,}; countries: {out.iso3.nunique()}; years {int(out.year.min())}-{int(out.year.max())}",
 f"- missing share_0_14: {out.share_0_14.isna().sum()}",
 f"- missing tfr: {out.tfr.isna().sum()}",
 f"- mean dependency_ratio: {out.dependency_ratio.mean():.3f}"]
open("results/audits/PHASE_6_DEMOGRAPHY_PANEL.md","w").write("\n".join(lines))
