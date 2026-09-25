# SUBMISSION_INTEGRITY_CHECK (revision)

## Package contents (submission/)
- manuscript_inline_revised.docx — inline-figure reading copy
- manuscript_blinded_revised.docx — same content, no author identifiers
- supplement_revised.docx — Tables S1–S5
- results/figures/fig_*.png — figures as separate files (journal rule)
- cover_letter.md / README retained from prior package

## Rules verified
- Vancouver citations numbered in order of first appearance; DOIs verified
  (see REFERENCE_VERIFICATION.md).
- Figures exist as separate PNGs AND embedded inline in the reading copy.
- All figures and tables cited in the text.
- Times New Roman; citations are font-superscript runs, not Unicode.
- No fabricated data; all panels derive from persisted raw files with
  sha256 manifests; raw data retained locally under data/raw/ (gitignored,
  reproducible via scripts/02_download.py + manifests).
- No composite capacity index; supplier-country ≠ domestic value added.
- Abstract states claim level; nothing submitted as causal.

## Not verified (external)
- Target journal not frozen; package kept generic (prior audit favored
  World Development). Journal-specific formatting left to submission time.
