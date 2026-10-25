# DATA_TEXT_FIGURE_CONSISTENCY — WD resubmission

Spot verification that rendered docx text equals table/figure sources:

- Main-text word count (Intro–Conclusion): 6,918 (method: whitespace
  tokens of manuscript_wd.md between "## 1. Introduction" and
  "## Data availability statement").
- Abstract: 169 words (within WD limits).
- All {num()}/{get()}/{dx()}/{wshare()}/{IR2_RANGE}/{PROC_*} tokens
  resolve; no literal "{" or "}" remains in rendered docx.
- Table 1 n-values match canonical_numbers (4,169 / 141 / 145,790).
- Table 3 TC coefficients match model_coefficients_all.csv rows
  (w3_5 log_gdppc β=-0.2031 se=0.1773 verified by re-fit).
- Figure 1 composition shares in text (41/22/7/2; 28/19) equal dyad-panel
  weighted means; figure itself generated from the same panel.
- Figure 2 donor profiles derive from table_donor_architecture.csv.
- Figure 3 coefficient path matches the same stored grid.
- Figure S1 (ODA/GDP histogram), Figure S2 (secondary outcomes), Table S1
  (320-coefficient grid) cited in text; supplement file regenerated.
- Citation numbering: 38 works, order == first-appearance order; every
  bibliography entry cited; no dangling citation.
- docx internals: no w:docGrid, no OMML equations (manuscript contains
  none — N/A), single asterisk is the verified Morrissey & White title.
