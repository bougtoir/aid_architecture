# COMPUTATIONAL_INTEGRITY_CHECK — WD resubmission

## No numerical hardcoding in manuscript prose

Method: scripts/15_world_development.py builds manuscript_wd.md as a single
f-string; every empirical numeral is interpolated via num() (canonical
_numbers.csv), get() (model_coefficients_all.csv), dx()
(donor_decomposition.csv), wshare() (dyad panel), fpct()/cint(), or regex
extraction from PHASE_14_PROCUREMENT.md (PROC_N=32, PROC_CORR=-0.161).

Audit: after stripping all {…} interpolations, the remaining digit-bearing
lines were enumerated (50 lines). Every residual literal is non-result
content: section cross-references, calendar years (1973–2024 coverage,
2013 AidData cutoff, WPP 2024), CRS purpose category 10, age-band labels
(0–14, 65+), design constants (200 permutation draws, windows 1–2/3–5/
6–10/11–15, top-20 donors), or illustrative examples ("a dyad-year in
which 60% of aid runs through one channel", "moving 10 percentage
points"). One genuine hardcode was found and fixed: "13–28 percentage
points" → {IR2_RANGE} computed from donor_decomposition.csv.

## Provenance of headline numbers

| Quantity | Source |
|---|---|
| n=145,790 dyad-years; 4,169 recipient-years; 141 countries | canonical_numbers.csv ← pipeline |
| TC β=-0.2031 (se 0.1773) at w3_5, log_gdppc, set B | model_coefficients_all.csv |
| Incremental donor R² 13–28pp | donor_decomposition.csv |
| Composition 40.5/21.8/7.2/2.1%; channels 28.1/19.1% | dyad panel via wshare() |
| public_recipient β=+0.253 (0.071); admin_refugee β=-2.585 (0.557) | model_coefficients_all.csv |
| procurement n=32, corr=-0.161 | PHASE_14_PROCUREMENT.md |

## Reproduction

A targeted re-run of the primary specification (TC share → forward 3–5y
mean log GDP pc, recipient+year FE, cluster-robust, adjustment set B)
reproduces the stored coefficient exactly: beta=-0.2031, se=0.1773,
n=3,538 — MATCH (see PUBLIC_CODE_PRINCIPAL_REPRODUCTION.md). A full
scripts/10_models.py re-run exceeded VM memory during the 320-cell grid
phase; stored canonical outputs were restored byte-identical and the
targeted rerun used the same spec code paths.
