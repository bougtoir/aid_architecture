# FINAL_REVISION_HANDOFF — Beyond Aid Volume (targeted revision)

## 1. Defects found and corrected
- (2.1) Numeric formatting: counts interpolated as integers now (no ".0").
- (2.2) ODA/GDP scale: real unit error — CRS amounts are USD millions;
  oda_pc_usd and oda_pct_gdp off by 10^6. Fixed in 08_merge_master_panel.py.
- (2.3) Figure 2 blank: real defect, root cause was the donor codelist
  parser (4-panel Donor.csv; float codes) dropping 100% of donor names.
  Parser rewritten; Fig 2 regenerated as annotated heatmap.
- (2.4) Donor decomposition: full-R² claim replaced by incremental-R²
  (donor FE over recipient+year baseline): TC 0.28, budget support 0.17,
  recipient-govt channel 0.13, project 0.23 (recipient contributes comparably
  there). No more "donor dominance" framing.
- (2.5) Compositional interpretation: omitted share specified; coefficients
  framed as fixed-total reallocation contrasts (10-pp example given).
- (2.6) References: 18 entries corrected to journal DOIs verified via
  Crossref; grey literature correctly labeled; wrong Kyklos DOI for Galiani
  et al replaced with JoEG 10.1007/s10887-016-9137-4.

## 2. Was ODA/GDP a true error or display?
True data error (transformation), not display-only: downstream ln_oda_pc
clipping bound different rows, so estimates moved slightly.

## 3. Did estimates change?
Yes, modestly: β_TC w3_5 log-gdppc −0.190→−0.203; manf −4.11→−4.34;
shuffle extremeness share 0.03→0.02; lead placebo β −0.230 (p=0.166).
Direction and conclusions unchanged.

## 4. Donor-decomposition interpretation
"Substantial but not unilateral": donor FE add 13–28pp of R²; for
project-type shares the recipient dimension contributes as much or more.

## 5. TC coefficient + interpretable contrast
β_TC (w3_5, set B): log GDP pc −0.203 (SE 0.177, p 0.252, n 3538);
manufacturing −4.34pp (SE 2.84, p 0.126, n 3215). 10-pp reallocation toward
modality-D TC vs omitted composition ≈ −0.020 log points, −0.43pp manf.

## 6. Falsification interpretation
Lead placebo null (p=0.166); pseudo-outcome null; within-year shuffle: only
2% of permuted compositions as extreme (one-sided extremeness share over
200 draws — reported as such, not as p=0.02). Falsification table in
results/tables/falsification_table.csv.

## 7. Reference corrections
See REFERENCE_VERIFICATION.md; 13 journal-version DOIs + 5 relabeled
non-DOI items.

## 8. Figure corrections
Fig 2 was blank → heatmap now renders (donor names fixed). Fig 3 axis in
percent post unit-fix. Fig 4 reordered chronologically with readable labels.

## 9. Claim ceiling
Level B throughout; abstract states imprecision explicitly.

## 10. Dashboard compatibility
results/dashboard exports identical to frozen model (max |Δ|≤5e-15);
metadata.json consistent. No UI changes.

## 11. Files produced
- manuscript/manuscript_inline_revised.docx, manuscript_blinded_revised.docx,
  supplement_revised.docx; manuscript_draft.md (27 Vancouver refs)
- results/tables/{model_coefficients_all,donor_decomposition,
  falsification_results,falsification_table,adjustment_stability,
  canonical_numbers,table_donor_architecture}.csv
- results/audits/{TARGETED_REVISION_AUDIT,REFERENCE_VERIFICATION,
  FINAL_CONSISTENCY_CHECK,SUBMISSION_INTEGRITY_CHECK,
  PHASE_26_HOSTILE_REVIEW_REVISED}.md
- submission/ package refreshed (revised docx + figures + tables)

## 12. Additional defect discovered
Donor codelist parser (item 2.3 root cause); TC-share definitional
narrowness (modality D ≈2% of disbursements) now disclosed in text.

## 13. Unresolved issues
- Selection into TC-heavy portfolios remains the main rival explanation
  (declared, not resolved — Level B ceiling).
- Procurement panel remains partial/recent-biased; tying under-reported.
- Target journal not frozen; package generic (WD still the prior pick).
