# PHASES 12–16 — Estimation results and falsification

All outputs are Level B (adjusted association, two-way FE panel, country-clustered SEs).
Coefficients on architecture shares are compositional: reallocation of the
aid-type/channel/finance share holding total ODA constant, relative to the
omitted share (aid-type: debt-relief + other; channel: other; finance:
other-finance/equity/debt-relief).

## Files
- results/tables/model_coefficients_all.csv — 320 term estimates over
  4 lag windows × 5 outcomes × 4 exposure sets.
- results/tables/donor_decomposition.csv — dyad-level variance decomposition.
- results/tables/adjustment_stability.csv — β_TC and β_budget-support across
  adjustment sets A/B/C.
- results/tables/falsification_results.csv — 3 falsification tests.

## Headline findings (to be verified in canonical numbers phase)

1. **Technical cooperation share ↔ GDP per capita (w3–5, set B)**: β ≈ −0.19
   (SE 0.18, n=3,538). Negative sign persists and strengthens (−0.38) under
   the aggressive set C. Interpretation: reallocating the full aid-type mix
   to TC is *associated with* lower subsequent GDPpc vs the omitted share —
   a conditional association, not a causal claim.
2. **Manufacturing VA/GDP**: TC share β ≈ −4.1 to −5.1 pp-equivalent across
   sets (SE ≈ 2.9) — the strongest and most adjustment-robust association.
3. **GFCF/GDP**: β_TC ≈ −1.0 to −1.9, SE ≈ 7.6 — imprecise.
4. **Donor decomposition (dyad panel, disbursement-weighted)**: donor+year
   FE explain a substantial share of architecture variance — e.g. recipient-
   government channel share r²_full ≈ 0.62, budget support ≈ 0.50 — donor
   identity is a first-order determinant of architecture, i.e. much
   "recipient-side" variation is donor-driven sorting.
5. **Falsification**: (a) lead placebo TC β = −0.148, p=0.42 — passes;
   (b) pseudo-outcome (urban share): no significant terms; (c) shuffle
   placebo: real TC β (−0.19) exceeds |β| of 97% of 200 within-year shuffles
   (placebo mean −0.002, sd 0.083) — the negative TC association is not an
   artifact of the share-composition design.

## Caveats recorded
- Tying shares estimable only where reported (tying_reported flag);
  "extra" set results must be read as reported-subsample estimates.
- usd_irtc decomposition r² near zero: within-recipient TC-intensity is
  donor-year specific, consistent with donor sorting.
- Procurement panel is a partial, recent-biased sample — descriptive only
  (Phase 14 audit).

## Decision
Results are consistent enough to proceed to dashboard exports and drafting;
all headline numbers will be re-derived programmatically (no hardcoding).
