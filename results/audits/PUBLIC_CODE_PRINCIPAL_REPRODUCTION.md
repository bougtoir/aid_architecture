# PUBLIC_CODE_PRINCIPAL_REPRODUCTION — WD resubmission

Question: can the principal published results be regenerated from the
code that ships in the public repository (bougtoir/aid_architecture)
against the persisted inputs?

Method: re-executed the primary specification from scripts/10_models.py
verbatim (X_AIDTYPE 7-share set, ADJ_B covariates, forward 3–5-year mean
of log GDP per capita, PanelOLS with entity+time fixed effects, clustered
by recipient country, drop_absorbed, check_rank=False) against
data/processed/master_panel.parquet.

Result:
  reproduced: beta=-0.2031  se=0.1773  n=3538
  stored:     beta=-0.2031  se=0.1773  n=3538   → MATCH (exact)

Panel-derived counts independently recomputed:
  dyad rows 145,790; recipient-years 4,169; countries 141 — all equal
  canonical_numbers.csv.

Disbursement-weighted composition recomputed from the dyad panel
(aid_architecture_donor_recipient_year.parquet): project 40.5%,
pooled/earmarked 21.8%, budget support 7.2%, TC 2.1%, multilateral
channel 28.1%, recipient-government channel 19.1% — matching the
manuscript text after the frame-consistency fix recorded in
FINAL_ADVERSARIAL_REVIEW.md item 3.

Full-grid re-run note: a complete re-execution of scripts/10_models.py
(4 windows × outcomes × 4 regressor sets plus falsification draws) was
terminated by the VM OOM killer mid-grid; donor_decomposition.csv and
other phase outputs were verified byte-identical to the stored canonical
files afterward, and the regression table was restored from git. The
targeted rerun above covers the principal result quoted in abstract,
results, and discussion. This is the principal-output reproduction the
resubmission requires; it is not a full software-release-grade rerun.
