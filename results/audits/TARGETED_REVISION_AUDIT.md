# TARGETED_REVISION_AUDIT

Targeted revision pass over the existing (non-restarted) pipeline, per
devin_aid_architecture_targeted_revision_single_vm.txt. All substantive
analysis remained frozen except where a concrete defect required re-execution.

## Defect verification and disposition

### 2.1 Numeric formatting / type leakage — REAL, FIXED
- Canonical numbers stored as float (e.g. `145790.0`); manuscript now
  interpolates counts via integer formatting (`145,790`, `4,169`,
  `141`, `1995–2024`). No trailing `.0` remains in prose.
- No [MISSING] placeholders in the generated draft.

### 2.2 ODA/GDP scale + Figure 3 — REAL DATA ERROR, FIXED
- Confirmed CRS `usd_disbursement_defl`/`usd_commit_defl_usd` are **USD
  millions** (DAC deflator base). `oda_pc_usd` and `oda_pct_gdp` were off by
  10^6 in `scripts/08_merge_master_panel.py` → true transformation error.
- Fixed with ×1e6; post-fix ODA/GDP mean 6.8%, median 2.6%, median ODA
  $52.9/capita — plausible magnitudes.
- Figure 3 regenerated; x-axis now correctly labeled "ODA disbursements /
  GDP (%)" over 0–50 (clipped at 50pp for display).
- Estimates changed slightly (β_TC w3_5 log-gdppc: −0.190 → −0.203; manf:
  −4.11 → −4.34) because `ln_oda_pc.clip(0.001)` bound different rows.

### 2.3 Figure 2 blank — REAL, FIXED (root cause deeper than rendering)
- Root cause: `scripts/04_construct_aid_panel.py` donor codelist parser
  dropped every donor name (codelist has 4 side-by-side panels; codes parsed
  as floats so `isdigit()` failed). `donor_name`/`donor_iso` were 100% NaN,
  the top-20 donor table was empty, and imshow of an empty array rendered a
  blank axes.
- Parser rewritten to read all four panels (DAC / multilateral / non-DAC /
  private). Donor panel repopulated (US $997bn, Germany $573bn, EU $455bn
  cumulative 1995–2024); script 04 re-run, panels regenerated.
- Figure 2 is now a heatmap (recipient-govt channel share, TC share, untied
  share) for the top-20 donors, with cell annotations; no quality ranking.

### 2.4 Donor decomposition claim — CLAIM TOO STRONG, FIXED
- Added incremental-R² decomposition to `scripts/10_models.py`:
  baseline recipient+year FE vs +donor FE.
- Results (donor incremental R²): recipient-govt channel 0.131, TC share
  0.28, budget support 0.17, project share 0.225 vs recipient incremental
  0.28 — manuscript now states donor identity contributes a *substantial but
  not unilateral* share; for project-type shares the recipient dimension
  contributes comparably. Full-model R² is no longer cited as proof.
- `share_tc_usd_irtc` R² ≈ 0.004 everywhere: TC-component amounts are
  nearly all idiosyncratic (documented).

### 2.5 Compositional interpretation — FIXED
- Manuscript §3 specifies the omitted shares (aid type: debt relief +
  other; channel: other; finance: residual) and rewrites every coefficient
  as a reallocation contrast at fixed total aid, including a
  10-percentage-point interpretation of the headline coefficient.

### 2.6 Reference integrity — FIXED
- 18 entries corrected in `data/metadata/literature_evidence_table.csv`;
  working-paper DOIs replaced with journal versions where they exist
  (verified via Crossref: B&D AER 2000, Rajan&Subramanian REStat 2008,
  Boone EER 1996, Alesina&Dollar JEG 2000, Kilby&Dreher EconLett 2010,
  Easterly&Pfutze JEP 2008, Knack SEJ 2001, Kenny EJDR 2008, Minoiu&Reddy
  QREF 2010, Bulir&Hamann WD 2008, Feyzioglu et al WBER 1998
  10.1093/wber/12.1.29, Galiani et al JoEG 2017 10.1007/s10887-016-9137-4,
  Doucouliagos&Paldam EJPE 2011).
- B&D 2004 "Revisiting the Evidence" kept as World Bank Policy Research WP
  3251 (correct label; no journal DOI exists in Crossref).
- Clay/Geddes/Natali relabeled as DIIS report (no DOI); Fukuda-Parr/Lopes/
  Malik relabeled as Earthscan/UNDP edited volume; Jepma 1991 as book
  chapter. Galiani et al wrong Kyklos DOI replaced.

## Other defects found in passing
- `weighted_tc_share_mean` semantics verified: aid-type D (technical
  cooperation) is only ~1.6–2.4% of ODA disbursements by value — TC is
  mostly embedded in project-type aid. Manuscript §3 and §6 now carry this
  definitional caveat explicitly.
- Headline β_TC is imprecise (p=0.252 at w3_5); abstract now states
  imprecision instead of implying significance.

## Re-execution log (minimal, defect-driven)
04 (donor map fix) → 09 (figs 1–3) → 10 (decomp columns already added;
results unchanged from this revision's prior run) → 11 (canonical numbers
+ new median keys) → 12 (full prose rewrite) → 13 (revised docx outputs).
Unit fix in 08 was executed earlier in this revision (documented above).

## Dashboard consistency audit (audit only)
- results/dashboard/coefficients_aidtype.csv merges against
  results/tables/model_coefficients_all.csv with max |Δ| ≤ 5e-15 on
  beta/se/p — exports already reflect the frozen model.
- results/dashboard/metadata.json carries claim level B, omitted-share
  reference, lag-window map, and disclaimers — consistent.
- Two dashboard dirs exist: `dashboard/` (prototype stub, empty data
  subdirs) and `results/dashboard/` (real exports). Noted; not merged.
