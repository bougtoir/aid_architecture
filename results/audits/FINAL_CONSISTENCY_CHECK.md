# FINAL_CONSISTENCY_CHECK (revision)

Checks performed on the revised package.

## Numbers ↔ manuscript
- manuscript_draft.md interpolates every numeric claim from
  canonical_numbers.csv / model_coefficients_all.csv /
  donor_decomposition.csv / falsification_results.csv — no hardcoded
  estimates. Verified keys resolve: n_dyad_years=145,790,
  n_recipient_years=4,169, n_countries=141, mean_oda_pct_gdp=6.8%,
  β_TC w3_5 log-gdppc=−0.2031, β_TC w3_5 manf=−4.34,
  shuffle extremeness share=0.02, lead β=−0.2296 (p=0.166).
- No `.0` residue, no `[MISSING]` placeholders.

## Units
- CRS USD-millions ×1e6 applied once in 08_merge_master_panel.py for both
  per-capita and GDP-share variables; figure axes labeled in percent.

## Decomposition
- Manuscript cites incremental R² (donor FE over recipient+year baseline),
  not full-model R². Project-share caveat stated.

## Compositional reading
- Omitted share stated; all share coefficients framed as reallocation
  contrasts at fixed total aid; 10-pp interpretation given.

## Claim ceiling
- Level B throughout; "causal"/"effect" language absent from claims;
  reverse-causality/selection rival given in Abstract and Discussion.

## Figures
- Fig 1 trends, Fig 2 heatmap (renders; was blank due to donor-name parser
  defect), Fig 3 ODA/GDP %, Fig 4 chronological windows with readable
  outcome labels. All four cited in text.

## Dashboard
- Exports identical to frozen model (max |Δ|≤5e-15); metadata consistent.

## Known residual caveats (documented, not hidden)
- TC-share measure is modality-D only (~2% of disbursements by value).
- Tying non-reporting post-2005; procurement sample partial/recent-biased.
- Headline associations are imprecise (p≈0.25); significance rests on the
  permutation-extremeness evidence, reported honestly as a share, not p.
