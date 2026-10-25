# World Development word-count expansion audit

- Original main-text word count (Introduction-Conclusion): ~1,660
- Revised main-text word count (Introduction-Conclusion): 6918
- Count method: whitespace-split tokens of manuscript_wd.md from the
  '## 1. Introduction' heading to the end of '## 7. Conclusion' (immediately
  before '## Data availability statement'); markdown section headings included,
  abstract/keywords/references/tables/figures/captions excluded — matching the
  journal's Introduction-through-Conclusion rule.
- Journal requirement: 4,500-10,000 words. Status: PASS (target ~7,000).
- Sections expanded: Introduction (gap framing, literature synthesis,
  positioning), Data (CRS/WDI/WPP detail, secondary sources, harmonization),
  Measuring aid architecture (margins, no-composite rationale, TC caveat,
  compositional example, tying caution), Empirical design (fixed effects,
  windows, adjustment, decomposition, falsification, identification limits),
  Results (exposure, decomposition null result, other-margin coefficients,
  falsification, procurement), Discussion (hidden-dimension, donor/recipient,
  TC selection, channel result, measurement implications, policy, research
  agenda, limitations, dashboard framing), Conclusion.
- Analysis remained FROZEN: no model, estimand, window, adjustment set, or
  principal number changed. All numerals interpolated from canonical tables.
- Targeted corrections made during expansion:
  * 5.6 procurement text aligned to actual mergeable sample (n=32) and the
    negative local-share correlation (-0.161), correcting a too-positive
    direction-of-effect description.
  * md_to_doc now merges hard-wrapped markdown lines into single paragraphs
    (removes mid-word paragraph breaks and stray asterisk artifacts).
  * Removed w:docGrid character/line grid from all output docx sections.
  * Figure S1 mention reordered after Figure 1 first-mention.
- References added during expansion (all from the pre-verified literature
  evidence table): meta-analyses and quasi-experimental aid-growth work,
  sectoral aid, Dutch-disease/manufacturing channels, donor-motives and
  transparency, AidData coverage comparison, conditionality.
