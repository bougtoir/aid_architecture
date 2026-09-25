# PHASE 2 — Data source audit

Probed live endpoints 2026-09-25. Full inventory:
`data/metadata/source_inventory.csv`, join map: `data/metadata/source_join_map.csv`.

## Status summary
| Source | Status | Notes |
|--------|--------|-------|
| OECD CRS | STRONG GO | SDMX API + stats.oecd.org bulk CSV reachable |
| OECD DAC aggregates | STRONG GO | SDMX v1 reachable |
| OECD untied awards | GO | bulletin coverage uneven → coverage metrics required |
| WDI | STRONG GO | API verified live |
| UN WPP (dataportal) | STRONG GO | dataportal API verified |
| WB STEP notices | GO | API verified; award coverage partial |
| AidData | GO | public download, manual step acceptable |
| WGI | GO | WDI-consistent country-year |
| JICA IATI | WEAK GO | datastore requires auth |
| DFAT | WEAK GO | endpoint unstable; supplementary only |
| ILOSTAT | WEAK GO | endpoint unverified; WDI labor fallback |
| EM-DAT | WEAK GO | registration wall; substitute with public summaries |

## Configuration decision
Primary stack: **OECD CRS + DAC aggregates + WDI + WPP** — all four confirmed
machine-accessible. Procurement layer: **OECD untied awards + WB STEP**,
kept as separate source-specific panels (never pooled before validation).
Secondary layers (JICA IATI, DFAT, AidData, ILOSTAT, EM-DAT) treated as
validation/robustness only; none is load-bearing.

Downstream stop conditions NOT triggered: all core exposures measurable.
