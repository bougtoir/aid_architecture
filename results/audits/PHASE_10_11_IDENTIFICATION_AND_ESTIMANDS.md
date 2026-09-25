# PHASES 10–11 — Identification strategy and frozen estimands

## Claim ceiling: Level B (adjusted association)

The design cannot credibly identify causal effects of aid *architecture* on
development outcomes: donors choose architectures, and recipients differ on
unobservables correlated with both. We therefore freeze all confirmatory
claims at Level B — associations conditional on aid volume, recipient and
year fixed effects, and a demographic/economic adjustment set.

## Estimands (frozen before model fitting)

Unit of analysis: **recipient country × year** (portfolio-level architecture).

Primary estimand (per outcome Y and lag window w):

    E[mean(Y) over t+w | X_t] − E[mean(Y) over t+w | X'_t]

estimated as β in

    Ȳ_{c,t→t+w} = α_c + λ_t + β' A_{c,t} + γ ln(ODA_pc)_{c,t} + δ' Z_{c,t} + ε_{c,t}

where:
- Ȳ_{c,t→t+w} = country mean of Y over the lag window w after year t,
- A_{c,t} = vector of aid-architecture shares in year t (composition of a
  *fixed total* — the coefficient reads "reallocating 10 pp of the aid
  portfolio from the omitted share to share j, holding total aid constant"),
- ln(ODA_pc)_{c,t} holds nominal aid volume comparable (the paper's core
  conditioning), with oda_pct_gdp variant as robustness,
- α_c, λ_t = country and year fixed effects (within-transformation; absorbs
  time-invariant recipient heterogeneity and common shocks),
- Z_{c,t} = adjustment set (see Phase 15),
- ε clustered by country.

Lag windows w (frozen): **1–2, 3–5, 6–10, 11–15** years.

Primary outcomes (frozen): real GDP per capita (log), GFCF/GDP,
manufacturing VA/GDP. Secondary: tax/GDP, electricity access.

Exposure set (frozen, compositional — omit "other" as reference):
- aid type: technical_cooperation, budget_support, project,
  pooled_earmarked, ngo_core, scholarships_students, debt_relief_aidtype,
  admin_refugee_awareness
- channel: public_recipient, public_donor, public_third, ngo, multilateral,
  ppp_network, private_recipient, private_donor, private_third, university
- finance: grant, loan, equity, debt_relief, guarantee
- tying: untied, partially_tied, tied (reported-years subsample)
- share_tc_usd_irtc as continuous TC-intensity check.

Adjustment sets (frozen):
- A (parsimonious): ln(ODA_pc), population growth, urban share.
- B (age structure): A + share_0_14, share_65plus, median_age, TFR.
- C (sensitivity): B + FDI/GDP, exports/GDP, GDPpc level lag.

## Demographic adjustment rationale

Demography is a confounder (aid targets young, fast-growing populations and
age structure drives growth/investment mechanically). Sets A→C move from
minimal to aggressive; stability of β across sets is the diagnostic, not
significance under one set.

## Donor decomposition (Phase 13)

Dyad-year panel: A_{d,c,t} = μ_d + ν_c + τ_t + u. Variance shares attributed
to donor FE vs recipient FE + residual show how much "recipient architecture"
is donor-driven sorting — the paper's second question.

## Falsification suite (Phase 16, frozen)

1. **Lead placebo**: same model with A_{c,t+3} predicting outcomes over
   window ending at t (future architecture should not predict past outcomes).
2. **Pseudo-outcome**: urban-population share (slow-moving, aid-architecture-
   insensitive) as outcome.
3. **Share shuffle**: randomly permute architecture vectors across
   recipient-years within year (500 draws, seed 20260925); distribution of
   placebo β vs. real β.
4. **Exclusion check**: drop humanitarian+debt+admin shares (non-projective
   flows), re-estimate.

## Known threats (declared, not resolved)

- Reverse selection: donors shift architecture in response to recipient
  performance (mitigated partially by leads placebo).
- Portfolio shares are compositional: coefficients are relative to the
  omitted share; we interpret magnitudes as share-reallocation contrasts.
- Measurement: tying is under-reported post-2005 (only flagged years used
  in tying spec); TC share relies on aid_t coding quality.
- We never label Level-B output causal anywhere in manuscript or dashboard.
