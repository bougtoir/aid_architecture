# FINAL_ADVERSARIAL_REVIEW — WD resubmission (word-count expansion)

Adversarial read of the expanded manuscript (Introduction–Conclusion,
6,918 words) performed as if by a hostile referee. Findings and
dispositions:

1. Overclaiming risk — MITIGATED. The central claim remains
   measurement/decomposition ("aid has an empirically measurable
   architecture"), not causal evaluation. TC-share result presented as
   imprecise, with confounding-by-indication confronted as the leading
   rival. Claim-calibration scan (effect/impact/cause/reduce/improve/
   harm/drive/determine/robust/significant): every residual hit is either
   a literature title ("The Aid Effectiveness Literature"), a mechanical
   term ("fixed effects"), an explicitly negated causal reading
   ("we do not interpret this as TC causing growth"), or statistical
   significance language. No causal verb survives in a claim position.

2. Fabricated-direction risk — CORRECTED during expansion:
   - "recipient-government systems carry the largest channel share" was
     wrong in the dyad-weighted frame (multilateral 28.1% > public-recipient
     19.1%); text now states the correct ordering.
   - "precision narrows at longer windows" reversed the actual pattern
     (estimation samples thin; intervals widen); corrected.
   - Procurement subsection claimed a supportive sign; the mergeable
     sample is n=32 with corr=-0.161 — rewritten to the actual values,
     interpolated from PHASE_14_PROCUREMENT.md rather than hardcoded.
   - "strongest point association in the grid" was false (admin_refugee is
     larger); replaced by "the grid's only positive association reaching
     conventional significance at this window".
   - "sector shares reported in the Supplement" was untrue; corrected to
     "dashboard and stack exports".
   - "1995 reflects a reporting-completeness break" was unverifiable;
     softened to "the period of fuller CRS reporting coverage".

3. Frame-consistency bug — CORRECTED: the disbursement-weighted
   composition shares were initially interpolated from the recipient-year
   panel (project 54.5%), but the architecture shares are dyad-level;
   the helper now reads the dyad panel (project 40.5% etc.), matching the
   frozen canonical values.

4. Hardcoded empirical number — CORRECTED: "13–28 percentage points" of
   incremental donor R² now interpolates as the min–max of incr_r2_donor
   over the five share margins (13–28pp reproduced from
   donor_decomposition.csv).

5. Remaining vulnerabilities (acknowledged, not hidden):
   - TC-share associations are imprecise and likely confounded; the text
     says so explicitly (5.3, 6.3, 6.7).
   - Incremental R² is a variance-decomposition statement, not
     out-of-sample prediction; stated as such.
   - Procurement merge (n=32) is presented as suggestive only.
   - The 320-coefficient grid invites multiple-comparison criticism;
     the falsification suite and within-year permutation (2% extremeness)
     are reported, and secondary outcomes are flagged exploratory.
   - Compositionality (shares sum to one) is stated; coefficients are
     interpreted as reallocations against the omitted categories.

Verdict: PASS for resubmission. No claim in the manuscript exceeds the
associational, measurement-first design; all numerals trace to canonical
tables or labelled audits.
