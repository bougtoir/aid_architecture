# PHASE 1 — Literature review and novelty audit

Evidence table: `data/metadata/literature_evidence_table.csv` (50 entries).
45/50 have Crossref-verified DOIs; 5 are grey literature / reports flagged
`grey_lit` or `unverified` — these are cited only where a peer-reviewed
equivalent does not exist, and never for load-bearing claims.

## What is already known
- The aggregate aid–growth relation is contested and near-zero on average
  (Burnside & Dollar 2000; Easterly 2003; Rajan & Subramanian 2008; Doucouliagos
  & Paldam 2009, 2011; meta-updates Mekasha & Tarp 2013 report a small positive
  mean with publication bias).
- Timing matters: "early-impact" aid shows more positive associations
  (Clemens et al. 2012).
- Donor allocation is systematically non-altruistic and heterogeneous
  (Alesina & Dollar 2000; Berthelemy & Tichit 2004; Feeny & McGillivray 2008;
  Dreher & Fuchs 2015; Fuchs & Vadlamannati 2013; Easterly & Pfutze 2008).
- Fungibility undermines earmarked composition as a pure intent measure
  (Boone 1996; Feyzioglu et al. 1998; Devarajan & Swaroop 1998).
- Tying inflates effective cost and favors donor suppliers
  (Jepma 1991; Morrissey & White 1996; Clay et al. 2009;
  Nowak-Lehmann et al. on aid→donor exports).
- Channels/mechanisms flagged: Dutch disease (Rajan & Subramanian 2011;
  Wagner 2014), governance/aid dependence (Knack 2001; Brautigam & Knack 2004),
  volatility (Bulir & Hamann 2008), fragmentation (Annen & Kosek 2016),
  sectoral composition (Dreher et al. 2008; Pettersson 2007).
- Identification: quasi-experimental thresholds exist (Galiani et al. 2017)
  but apply only locally; generic IVs are discredited (Rajan & Subramanian 2008
  critique).

## What remains unresolved
- Aid **architecture** (composition × modality × tying × procurement) as the
  object of analysis rather than aggregate aid: studied piecemeal, not jointly.
- Donor heterogeneity decomposed into architecture vs residual: no canonical
  decomposition exists.
- Local procurement / local economic participation measured at scale:
  OECD untied-award data exist but are thin and rarely linked to outcomes.
- Demographic structure treated as a first-class pre-specified
  confounder/moderator in aid analysis: largely absent.
- Dashboard-ready counterfactual portfolio tools with support diagnostics:
  essentially novel as a transparent, estimand-labeled instrument.

## What this study can genuinely add
- A multi-layer empirical architecture (L0 volume → L1 composition → L2
  procurement → L3 local participation → L4 capacity → L5 persistent outcomes)
  estimated on a common donor–recipient–year panel.
- Decomposition of donor-associated heterogeneity into portfolio vs delivery/
  procurement vs residual components, with claim-level calibration.
- Lag-window estimation by aid type rather than a single horizon.
- Frozen-estimand dashboard exports with explicit support/extrapolation flags.

## What would NOT be novel enough
- Another aggregate aid–growth regression (saturated).
- Donor ranking or "which donor is best" (excluded by design and ethics).
- Composition-only models without procurement/participation layers.
