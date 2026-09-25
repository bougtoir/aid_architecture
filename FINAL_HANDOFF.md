# FINAL HANDOFF — Aid Architecture research project

## What was produced (Phases 0–30, all executed)

| Phase | Output | Location |
|---|---|---|
| 0 | Configs, variable ontology, source registry, audit logs | config/, results/audits/PHASE_0* |
| 1 | Hostile literature map, 50 entries, 45 Crossref-verified | data/metadata/literature_evidence_table.csv |
| 2 | Data feasibility audit | results/audits/PHASE_2* |
| 3 | Raw acquisition + sha256 manifests (38 files, all verified) | data/raw/, data/metadata/*_manifest.csv |
| 4 | Donor×recipient×year architecture panel (145,790 rows) | data/processed/aid_architecture_donor_recipient_year.parquet |
| 5 | Procurement panels (partial WB notices — 76k awards) | data/processed/procurement_* |
| 6 | Demography panel (WPP 2024, 237 countries) | data/processed/demography_country_year.parquet |
| 7 | Outcomes panel (WDI, 217 countries) | data/processed/outcomes_country_year.parquet |
| 8 | Master panel (4,169 recipient-years, 141 countries) | data/processed/master_panel.parquet |
| 9 | Descriptives + figures | results/tables/, results/figures/ |
| 10–11 | Identification strategy + frozen estimands | results/audits/PHASE_10_11* |
| 12 | Main + lag-window models (320 coefficients) | results/tables/model_coefficients_all.csv |
| 13 | Donor decomposition | results/tables/donor_decomposition.csv |
| 14 | Procurement linkage (exploratory) | results/audits/PHASE_14* |
| 15 | Demographic adjustment stability | results/tables/adjustment_stability.csv |
| 16 | Falsification suite (lead/pseudo-outcome/shuffle) | results/tables/falsification_results.csv |
| 17 | Support diagnostics + extrapolation flags | results/dashboard/support_flags.csv |
| 18 | Dashboard-ready exports (JSON/CSV + metadata) | results/dashboard/ |
| 19 | Prototype dashboard (single-file HTML, fixed-total reallocation only) | dashboard/prototype.html |
| 20 | Canonical numbers table (programmatic) | results/tables/canonical_numbers.csv |
| 21 | Journal selection: World Development | results/audits/PHASE_21* |
| 22–25 | Vancouver refs (27, verified), figures, manuscript draft | manuscript/manuscript_draft.md |
| 26 | Hostile reviewer report | results/audits/PHASE_26* |
| 27 | Consistency audit (no unresolved placeholders) | integrity check + MISSING scan |
| 28 | Integrity check: 38/38 raw files sha256-verified | results/audits/integrity_check.csv |
| 29 | Submission package | submission/ |
| 30 | This handoff + public sync | FINAL_HANDOFF.md |

## Headline findings (Level B — adjusted association only)

- Donor identity is a first-order determinant of the aid architecture a
  recipient faces (dyad decomposition: donor+year FE r² ≈ 0.5–0.67 on key
  shares).
- Holding ODA volume constant, technical-cooperation share associates with
  lower subsequent GDP pc (β≈−0.19, w3–5) and manufacturing VA/GDP (β≈−4.1).
  Passes lead-placebo and within-year shuffle tests (real β beyond 97% of
  shuffles); flagged as associational throughout.
- Budget-support share coefficients are small/imprecise.

## Known limitations (declared)

- No causal identification; sorting on unobservables unresolved.
- Procurement sample partial (~7% of notices, recent-biased).
- Tying under-reported post-2005.
- OECD SDMX CRS dataflow returned 500s server-side; bulk parquet used.
- UN dataportal API needed a token; WPP bulk files used instead.

## Reproduce

`pip install -r environment/requirements.txt`, then run scripts/01→12 in
order. Raw data already in data/raw/ with manifests; scripts regenerate all
processed panels and results deterministically (seed 20260925).
