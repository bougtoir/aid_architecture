"""Phase 7: outcomes_country_year panel from WDI downloads.

Input : data/raw/wdi/*.json  (list payload: [meta, rows])
Output: data/processed/outcomes_country_year.parquet
"""
import json, glob, os, pandas as pd

meta = json.load(open("data/raw/wdi/country_metadata.json"))
countries = meta[1] if isinstance(meta, list) else meta
ctry = pd.DataFrame(countries)
ctry = ctry[["id","iso2Code","name","region","incomeLevel","lendingType"]]
ctry["region_name"] = ctry.region.map(lambda r: r.get("value") if isinstance(r, dict) else r)
ctry["income_name"] = ctry.incomeLevel.map(lambda r: r.get("value") if isinstance(r, dict) else r)
ctry = ctry[["id","iso2Code","name","region_name","income_name"]].rename(columns={"id":"iso3","name":"country_name"})
ctry = ctry[ctry.region_name != "Aggregates"]

frames = []
for f in sorted(glob.glob("data/raw/wdi/*.json")):
    if f.endswith("country_metadata.json"):
        continue
    ind = os.path.basename(f).replace(".json","")
    try:
        d = json.load(open(f))
    except Exception:
        continue
    if not isinstance(d, list) or len(d) < 2 or not isinstance(d[1], list):
        continue
    rows = [{"iso3": r.get("countryiso3code") or None,
             "year": int(r["date"]) if str(r.get("date","")).isdigit() else None,
             ind: r.get("value")} for r in d[1]]
    frames.append(pd.DataFrame(rows))

out = None
for fr in frames:
    ind = [c for c in fr.columns if c not in ("iso3","year")][0]
    fr = fr.dropna(subset=["iso3","year"]).groupby(["iso3","year"], as_index=False)[ind].mean()
    out = fr if out is None else out.merge(fr, on=["iso3","year"], how="outer")

out = out.merge(ctry, on="iso3", how="inner")  # keep only real countries
out = out[out.year.between(1960, 2025)].sort_values(["iso3","year"])
out.to_parquet("data/processed/outcomes_country_year.parquet", index=False)
print(out.shape, out.iso3.nunique())

cov = out.drop(columns=["iso3","year","iso2Code","country_name","region_name","income_name"]).notna().mean().sort_values()
lines = ["# PHASE 7 — Outcomes panel","",
 f"- rows: {len(out):,}; countries: {out.iso3.nunique()}",
 "","## Coverage (share non-missing):", cov.to_string()]
open("results/audits/PHASE_7_OUTCOMES_PANEL.md","w").write("\n".join(lines))
print(cov.tail(10))
