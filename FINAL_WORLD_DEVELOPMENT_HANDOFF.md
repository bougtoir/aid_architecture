# FINAL_WORLD_DEVELOPMENT_HANDOFF

## 1. Final title
"Beyond Aid Volume: Donor Heterogeneity, Aid Architecture, and Medium-Run
Development Outcomes" — dropped "Local Economic Participation" and
"Capacity Formation" (evidence base is thinner than the old title implied).

## 2. Final abstract
169 words (≤300 WD cap); leads with problem → data/design → decomposition
contribution → illustrative TC illustration with imprecision and selection
caveat; no "Level B" jargon; no causal wording.

## 3. Final positioning
Integrative measurement + decomposition paper, not an aid–growth
regression, not "TC is bad", not a donor ranking.

## 4. What changed for World Development
- New title; WD-style abstract; 6 keywords; 5 highlights (≤125 chars
  sans spaces); cover letter; data availability statement; title page with
  author placeholders.
- Result hierarchy reordered: measurement/decomposition primary, outcome
  associations secondary, TC + procurement illustrative/exploratory.
- Discussion expanded to six conceptual subsections (architecture as hidden
  dimension; donor vs recipient; rival TC explanations; procurement as
  partial layer; evaluation implications; future causal designs).
- Figure hierarchy: Fig 1 trends, Fig 2 donor heatmap (central exhibit),
  Fig 3 TC windows; ODA/GDP histogram demoted to Supplement (Fig S1).
- Tables: 4 compact main tables; full coefficient grid in supplement S1–S4.
- Internal/repo/audit language and "Level B" phrasing removed from prose.

## 5. Whether any analysis changed
No new analysis. The frozen model is unchanged; only presentation,
framing, and packaging. (Earlier targeted fixes — USD-millions unit error,
donor-codelist parser, incremental-R² decomposition — were made in the
preceding revision and are carried forward.)

## 6. Principal architecture findings
- 145,790 dyad-years, 141 countries, 4,169 recipient-years, 1995–2024.
- Donor FE incremental R²: TC 0.28, budget support 0.17, recipient-govt
  channel 0.13, project 0.23 (recipient increment 0.28 there — non-unilateral).

## 7. TC finding and uncertainty
β_TC w3_5 log-gdppc = −0.203 (SE 0.177, p=0.252); manf −4.34pp (p=0.126);
10-pp reallocation ≈ −0.02 log points; permutation extremeness share 2%
(one-sided, not a p-value); lead placebo β=−0.230, p=0.166 compatible with
zero. Framed as imprecise, directionally stable, unusually extreme vs
randomized compositions, and vulnerable to residual selection.

## 8. Donor-decomposition interpretation
"Donor identity contributes substantially to explained architecture
variation" — never "determines"; recipient-side comparability on
project-type shares preserved.

## 9. Figure hierarchy
Main: Figs 1–3 (trends, donor heatmap, TC windows). Supplement: ODA/GDP
histogram (Fig S1). Captions state the omitted/reference composition.

## 10. Dashboard status
Supplementary "interactive model-based scenario explorer for
fixed-total-aid reallocations"; exports match frozen model (≤5e-15 diff);
metadata carries no-causal/no-ranking disclaimers; no UI work performed.

## 11. References
27 Vancouver-numbered; journal-version DOIs verified against Crossref in
prior pass; no new references added; none inflated.

## 12. Files generated
- manuscript/world_development_manuscript.docx / _blinded.docx /
  _title_page.docx / _supplement.docx
- manuscript/cover_letter_world_development.{docx,txt},
  highlights.txt, data_availability_statement.txt
- manuscript/manuscript_wd.md (canonical source)
- submission/world_development_submission_package.zip (12 files)
- results/audits/WORLD_DEVELOPMENT_FIT_AUDIT.md

## 13. Unresolved author-side placeholders
Author name, affiliation, email, ORCID, funding, acknowledgments,
declaration of interests — clearly marked [TO COMPLETE] on the title page
and cover letter signature. Nothing fabricated.

## 14. Submission ZIP
submission/world_development_submission_package.zip — blinded + unblinded
manuscripts, title page, supplement, cover letter, highlights, data
statement, figures/ ×4. No audits, scratch files, or raw restricted data.

## 15. Exact git commit
Recorded below in commit history (wip branch
devin/1790338560-aid-architecture-clean; public bougtoir/aid_architecture
main synced via subtree).

## ANALYSIS STATUS
- frozen; targeted reruns only (none this pass — presentation only);
- no broad re-analysis performed.
