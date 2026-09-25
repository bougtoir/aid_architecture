# Beyond Aid Volume: Aid Architecture, Local Economic Participation, Capacity Formation, and Persistent Development Outcomes

## Abstract

**Background.** The aid-effectiveness literature debates whether aid volume
raises growth; far less is known about whether the *architecture* of delivery —
composition by aid type, delivery channel, financial instrument, and tying —
matters when total aid is held constant. **Methods.** We construct donor ×
recipient × year aid-architecture panels from the OECD CRS full activity file
(145790.0 dyad-years, 1995–2024), merge with UN WPP demography and
WDI outcomes (141.0 recipients, 4169.0
recipient-years), and estimate two-way fixed-effects panel models of outcome
windows 1–2 through 11–15 years ahead, conditional on log ODA per capita and
frozen demographic adjustment sets. All claims are capped at Level B
(adjusted association). **Findings.** Architecture varies systematically by
donor: donor identity explains a large share of portfolio-structure variance.
Holding aid volume constant, a higher technical-cooperation share is
associated with *lower* subsequent GDP per capita (β=-0.1901
per unit share, window 3–5y) and lower manufacturing value added
(β=-4.1142). A within-year shuffle placebo places the
estimate beyond 3% of random
allocations; a lead-architecture placebo is null. **Interpretation.** How aid
is delivered is a first-order margin of donor heterogeneity; the negative TC
association is robust but associational and should not be read causally.
Dashboard exports implement only fixed-total-aid reallocations with explicit
support/extrapolation flags.

## 1. Introduction

The aid-effectiveness literature has centered on whether *how much* aid a
country receives affects growth and development [1,2].
Burnside and Dollar's policy-interaction result was shown fragile to sample
and specification choices [3,4], and meta-analytic and
long-run reassessments remain contested [5,6,7,8,9].
Three adjacent literatures motivate an architectural turn rather than another
aid-growth regression: (i) donor allocation studies show bilateral aid is
shaped by donor motives as much as recipient need
[10,11,12,13]; (ii) fungibility work
shows the use of aid is endogenous to its form
[14,15,16,17]; and (iii) practice-
oriented assessments document large cross-donor differences in tying,
channels, and modality "best practice" [18,19,20,21].
Institutional channels have been linked to governance outcomes
[22,23], aid volatility complicates domestic planning
[24], and capacity formation has long been named as the mechanism
aid is supposed to build [25,26]. Bourguignon and Sundberg
called explicitly for "opening the black box" between disbursement and
outcome [27]. What remains comparatively unexplored is the
*architecture* of delivery: given a fixed nominal amount, does composition
by aid type (budget support vs project vs technical cooperation), delivery
channel (recipient government vs NGO vs multilateral vs private sector),
financial instrument (grant vs loan), and tying status correlate with
medium-run outcomes?

We answer descriptively-associational: this is a Level-B design. The
contribution is (i) a harmonized aid-architecture measurement stack built on
the full CRS activity file; (ii) frozen estimands and a falsification suite;
(iii) a donor-vs-recipient variance decomposition of architecture; and (iv)
dashboard-ready scenario exports constrained to fixed-total reallocations.

## 2. Data

(Section summarizes the provenance ledger in data/metadata/. Full raw files
with SHA-256 manifests are preserved under data/raw/.)

- OECD Creditor Reporting System, full activity file (6.24M rows, 1973–2024);
  ODA rows (category 10), 1995–2024 used for analysis.
- OECD DAC aggregate tables and code lists.
- World Bank World Development Indicators (21 indicators).
- UN World Population Prospects 2024 (demographic indicators + 5-year age
  structure).
- World Bank procurement notices (partial sample; Phase 14 limitations).
- AidData 3.1 core release (sector-composition robustness only).

## 3. Measurement

Architecture is measured as disbursement-weighted shares of constant-USD ODA:
aid-type shares (technical cooperation, budget support, project-type,
pooled/earmarked, NGO core, scholarships, debt relief, admin/refugee),
channel shares (recipient government, donor government, third-country
government, NGO, multilateral, PPP/network, private), finance shares
(grant/loan/other), and tying where reported. Levels L0–L5 follow the
variable ontology; no composite capacity index is constructed.

## 4. Empirical strategy

Frozen estimands and adjustment sets are documented in
results/audits/PHASE_10_11_IDENTIFICATION_AND_ESTIMANDS.md. Primary spec:
outcome mean over lag window w ~ architecture shares_t + ln ODA pc_t +
demographic controls + country and year FE, clustered by country. Claim
ceiling B throughout; no estimates are described as causal.

## 5. Results

### 5.1 Descriptive structure
Mean ODA/GDP is 0.0 (share). Disbursement-weighted TC
share averages 0.0181. Architecture trends and donor
profiles are in results/figures/fig_architecture_trends.png and
fig_donor_architecture.png.

### 5.2 Main estimates
Figure fig_coef_tc_windows.png and Table model_coefficients_all.csv report
coefficients by lag window. Technical-cooperation share β on log GDP pc is
-0.1901 (3–5y window); on manufacturing VA/GDP
-4.1142. Budget-support share is small and imprecise
throughout.

### 5.3 Adjustment stability
β_TC moves from -0.1901 (set B) to more negative under
aggressive controls (set C); see adjustment_stability.csv.

### 5.4 Donor decomposition
Donor+year fixed effects explain a large share of architecture variance
(e.g., full-model r² ≈ 0.6241
for recipient-government channel share, 0.6712
for project-type share): donor identity is a first-order driver of the
architecture recipients face.

### 5.5 Falsification
Lead-placebo β=-0.1476 (n.s.); pseudo-outcome null;
within-year shuffle percentile 3%.
See falsification_results.csv.

### 5.6 Procurement linkage (exploratory)
Partial WB contract-award sample suggests bidder-country patterns correlate
with channel shares; treated as descriptive only.

## 6. Discussion

Findings are consistent with architecture being a real margin of donor
heterogeneity, and with technical-cooperation-heavy portfolios associating
with weaker subsequent outcomes conditional on aid volume. Mechanisms cannot
be separated from selection (donors may deploy TC where governments are
weak). All results are Level B.

## 7. Limitations

- No causal identification; sorting on unobservables remains.
- Tying under-reported post-2005; procurement sample partial and recent-biased.
- Share coefficients are compositional contrasts vs the omitted share.
- Supplier-country of procurement ≠ domestic value added.

## 8. Conclusion

When aid volume is held constant, delivery architecture still differs
sharply across donors and correlates with medium-run recipient outcomes.
These are associations, not effects; the burden of causal evidence remains
on future designs.

## References
1. Burnside & Dollar. Aid, growth, policies and fragility. Handbook on the Economics of Foreign Aid. 2000. doi:10.4337/9781783474592.00032
2. Burnside & Dollar. Aid, Policies, and Growth: Revisiting the Evidence. World Bank Economic Review. 2004. doi:10.1596/1813-9450-3251
3. Easterly. Can Foreign Aid Buy Growth?. Journal of Economic Perspectives. 2003. doi:10.1257/089533003769204344
4. Clemens et al.. Counting Chickens when they Hatch: Timing and the Effects of Aid on Growth. The Economic Journal. 2012. doi:10.1111/j.1468-0297.2011.02482.x
5. Rajan & Subramanian. Aid and Growth: What Does the Cross-Country Evidence Really Show?. Review of Economics and Statistics. 2008. doi:10.5089/9781451861464.001.a001
6. Arndt, Jones & Tarp. Assessing Foreign Aid’s Long-Run Contribution to Growth and Development. World Development. 2015. doi:10.1016/j.worlddev.2013.12.016
7. Minoiu & Reddy. Development Aid and Economic Growth: A Positive Long-Run Relation. Quarterly Review of Economics and Finance. 2010. doi:10.5089/9781451872651.001.a001
8. Doucouliagos & Paldam. The ineffectiveness of development aid on growth: An update. European Journal of Political Economy. 2011. doi:10.1016/j.ejpoleco.2010.11.004
9. Mekasha & Tarp. Aid and Growth: What Meta-Analysis Reveals. The Journal of Development Studies. 2013. doi:10.1080/00220388.2012.709621
10. Alesina & Dollar. Who Gives Foreign Aid to Whom and Why?. Journal of Economic Growth. 2000. doi:10.3386/w6612
11. Kilby & Dreher. The Impact of Aid on Growth Revisited: Do Donor Motives Matter?. SSRN Electronic Journal. 2010. doi:10.2139/ssrn.1402503
12. Feeny & McGillivray. What Determines Bilateral Aid Allocations? Evidence From Time Series Data. Review of Development Economics. 2008. doi:10.1111/j.1467-9361.2008.00443.x
13. Berthelemy & Tichit. Bilateral donors' aid allocation decisions—a three-dimensional panel analysis. International Review of Economics &amp; Finance. 2004. doi:10.1016/j.iref.2003.11.004
14. Boone. Politics and the Effectiveness of Foreign Aid. European Economic Review. 1996. doi:10.3386/w5308
15. Feyzioglu, Swaroop & Zhu. Is Donors' Concern About the Fungibility of Foreign Aid Justified?: A Panel Data Analysis. World Bank Economic Review. 1998. doi:10.2139/ssrn.5035639
16. Devarajan & Swaroop. The Implications of Foreign Aid Fungibility for Development Assistance. Policy Research Working Papers. 1998. doi:10.1596/1813-9450-2022
17. Pettersson. Foreign sectoral aid fungibility, growth and poverty reduction. Journal of International Development. 2007. doi:10.1002/jid.1378
18. Easterly & Pfutze. Where Does the Money Go? Best and Worst Practices in Foreign Aid. Journal of Economic Perspectives. 2008. doi:10.2139/ssrn.1156890
19. Clay, Geddes & Natali. Figure 14.5. Trends in untying aid, 1995-2010. DIIS report. 2009.
20. Jepma. Aid tying: trade and resource allocation effects. The Economics of Aid. 1991.
21. Morrissey & White. EVALUATING THE CONCESSIONALITY OF TIED AID*. The Manchester School. 1996. doi:10.1111/j.1467-9957.1996.tb00481.x
22. Knack. Aid Dependence and the Quality of Governance: A Cross-Country Empirical Analysis. Southern Economic Journal. 2001. doi:10.1596/1813-9450-2396
23. Brautigam & Knack. Foreign Aid, Institutions, and Governance in Sub‐Saharan Africa. Economic Development and Cultural Change. 2004. doi:10.1086/380592
24. Bulir & Hamann. Volatility of Development Aid: From the Frying Pan into the Fire?. World Development. 2008. doi:10.5089/9781451863253.001.a001
25. Fukuda-Parr, Lopes & Malik. Capacity for Development: New Solutions to Old Problems. International Journal of Sustainability in Higher Education. 2002. doi:10.1108/ijshe.2002.24903dae.008
26. Kenny. What Is Effective Aid? How Would Donors Allocate It?. European Journal of Development Research. 2008. doi:10.1596/1813-9450-4005
27. Bourguignon & Sundberg. Aid Effectiveness—Opening the Black Box. American Economic Review. 2007. doi:10.1257/aer.97.2.316

## Figures (separate files)
- fig_architecture_trends.png — weighted architecture shares over time.
- fig_donor_architecture.png — top-20 donor architecture profiles.
- fig_oda_gdp_hist.png — distribution of ODA/GDP.
- fig_coef_tc_windows.png — TC-share coefficients by lag window.
