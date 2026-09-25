# PHASES 27–28 — Consistency and integrity audit

## Consistency
- manuscript/manuscript_draft.md contains zero `[MISSING]` placeholders —
  every interpolated number resolved from results/tables/canonical_numbers.csv.
- All figures/tables named in the manuscript exist in results/figures|tables
  and are copied to submission/.
- Claim language: manuscript uses "associated with" throughout; the word
  "causal" appears only in disclaimers/limitations.
- Falsification suite executed post-freeze with seed 20260925.

## Integrity
- integrity_check.csv: 38/38 manifest files exist on disk; all sha256 match.
- Raw files never edited post-acquisition; all transforms in scripts/.
- Partial acquisitions flagged: wb_procurement (~30k/420k notices),
  OECD SDMX CRS dataflow failure → bulk parquet substitute documented.
- No fabricated values anywhere; unverifiable grey-literature entries carry
  verified=grey_lit/unverified flags in literature_evidence_table.csv.
