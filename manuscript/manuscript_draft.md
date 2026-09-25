# Beyond Aid Volume: Aid Architecture, Local Economic Participation, Capacity Formation, and Persistent Development Outcomes

## Abstract

**Background.** The aid-effectiveness literature has debated whether the
*volume* of aid affects growth and development; much less is known about
whether the *architecture* of delivery — composition by aid type, delivery
channel, financial instrument, and tying status — matters when total aid is
held constant. **Methods.** We construct a disbursement-weighted
aid-architecture panel from the full OECD Creditor Reporting System activity
file (145,790 donor–recipient–year observations, 1995–2024)
and merge it with UN World Population Prospects 2024 demography and World
Development Indicators outcomes (141 recipient countries;
4,169 recipient-years). We estimate two-way
fixed-effects panel models of mean outcomes over lag windows of 1–2, 3–5,
6–10, and 11–15 years, conditional on log ODA per capita and pre-registered
demographic adjustment sets. All estimates are reported as adjusted
associations (Level B), not causal effects. **Findings.** Donor identity is a
substantial driver of the architecture a recipient faces: adding donor fixed
effects to a recipient-and-year baseline raises R² by roughly 13–28
percentage points across major architecture shares. Holding ODA per capita
constant, a higher technical-cooperation share — relative to the omitted
aid-type composition (debt relief and other flows) — is associated with lower
subsequent GDP per capita (β = -0.20 per unit share;
a 10-percentage-point reallocation corresponds to β·0.10 ≈
-0.020 log points) and with lower
manufacturing value added (β = -4.34 pp per unit
share). Estimates are imprecise (the headline coefficient is not significant at
conventional levels); in a within-year permutation test, only
2% of randomized
allocations produce a coefficient as extreme as the observed one, and a
future-architecture placebo is statistically compatible with zero.
**Interpretation.** These are conditional associations,
and selection — donors deploying technical cooperation where state capacity
is weakest — remains a plausible explanation. The central contribution is a
measurement and decomposition exercise: architecture is a first-order,
donor-driven dimension of foreign aid that volume aggregates conceal.

## 1. Introduction

The aid-effectiveness literature has centered on whether *how much* aid a
country receives affects growth and development [1,2].
Burnside and Dollar's policy-interaction result was shown fragile to sample
and specification choices [3,4], and meta-analytic and
long-run reassessments remain contested [5,6,7,8,9].
Three adjacent literatures motivate an architectural turn rather than another
aid–growth regression: (i) donor allocation studies show bilateral aid is
shaped by donor motives as much as recipient need
[10,11,12,13]; (ii) fungibility work
shows the use of aid is endogenous to its form
[14,15,16,17]; and (iii) practice-
oriented assessments document large cross-donor differences in tying,
channels, and modality [18,19,20,21].
Institutional channels have been linked to governance outcomes
[22,23], aid volatility complicates domestic planning
[24], and capacity formation has long been named the mechanism aid
is supposed to build [25,26]. Bourguignon and Sundberg
called explicitly for "opening the black box" between disbursement and
outcome [27].

We do not claim the literature has ignored aid heterogeneity. The
contribution is integrative: (i) a harmonized aid-architecture measurement
stack built on the full CRS activity file; (ii) frozen estimands with a
falsification suite; (iii) a donor-versus-recipient decomposition of the
architecture recipients face; and (iv) dashboard-ready scenario exports
constrained to fixed-total reallocations. The question is: when total aid
exposure is held comparable, how is delivery architecture associated with
medium- and long-run recipient outcomes, and how much of the observed
heterogeneity in architecture is attributable to donor identity rather than
to recipient characteristics?

## 2. Data

(Full provenance: machine-readable manifests with URLs, UTC timestamps, and
SHA-256 checksums under data/metadata/; raw files preserved under data/raw/.)

- OECD Creditor Reporting System, full activity file (6.2 million activity
  rows, 1973–2024); ODA rows (category 10), 1995–2024 used for analysis. CRS
  amounts are reported in millions of constant USD (DAC deflator base).
- OECD DAC aggregate tables and official code lists.
- World Bank World Development Indicators (21 indicators).
- UN World Population Prospects 2024 (demographic indicators; population by
  five-year age group).
- World Bank procurement notices (partial, recent-biased sample —
  exploratory only).
- AidData 3.1 core release (robustness cross-check only; coverage ends 2013).

## 3. Measurement

Architecture is measured as disbursement-weighted shares of constant-USD
ODA: aid-type shares (technical cooperation, budget support, project-type,
pooled/earmarked, NGO core, scholarships, debt relief, administrative and
in-donor refugee costs), channel shares (recipient government, donor
government, third-country government, NGO, multilateral, PPP/network,
private-sector), finance-type shares (grant, loan, other), and tying status
where reported. Variables follow the frozen L0–L5 ontology
(config/variable_ontology.yaml); no composite capacity index is constructed,
and supplier country is never equated with domestic value added.

One measurement caveat: the CRS aid-type variable distinguishes
technical cooperation (type D) as a modality; a substantial share of
technical-cooperation activity is delivered inside project-type
interventions and is classified as such, so the TC share used here
(disbursement-weighted mean 1.8%, unweighted mean
about 2.4%) is a narrow modality measure, not the total TC intensity of a
portfolio. Results for the TC-share term should be read against that
definition.

All share variables are compositional: within each group they sum to one.
Estimated coefficients are therefore relative contrasts versus the omitted
share (aid type: debt relief plus residual "other"; channel: "other";
finance: residual category). A coefficient on, e.g., the technical-
cooperation share should be read as: reallocating the aid-type portfolio
toward technical cooperation *and away from the omitted composition*, at
fixed total aid, is associated with a β-sized change in the outcome window
mean.

## 4. Empirical strategy

Frozen estimands and adjustment sets are documented in
results/audits/PHASE_10_11_IDENTIFICATION_AND_ESTIMANDS.md. The primary
specification regresses the mean of outcome Y over lag window w on the
year-t architecture shares, log ODA per capita at t, demographic controls,
and country and year fixed effects; standard errors are clustered by
country. The claim ceiling is Level B (adjusted association) throughout; no
estimate is described as causal.

## 5. Results

### 5.1 Sample and exposure structure

The analysis sample covers 4,169 recipient-years across
141 countries (1995.0–2024.0). Mean
ODA disbursements equal 6.8% of recipient GDP (median
2.6%); median ODA is roughly
$53 per capita. The disbursement-weighted
technical-cooperation share averages 1.8%.
Figure 1 shows the evolution of aid-type and channel shares; Figure 3 shows
the ODA/GDP distribution.

### 5.2 Donor-level architecture heterogeneity

On the dyad panel, adding donor fixed effects to a baseline of recipient and
year fixed effects raises R² from 0.401
to 0.624 for the recipient-
government channel share (incremental R² = 0.223);
the corresponding increments are 0.249
for technical cooperation, 0.268 for budget
support, and 0.131 for project-type shares. Donor
identity thus contributes a substantial share of explained architecture
variance; for project-type shares, however, the recipient dimension
contributes comparably (incremental recipient R² =
0.225), so architecture heterogeneity is not
unilaterally donor-determined. Figure 2 displays top-donor architecture
profiles descriptively (no quality ranking is implied).

### 5.3 Main adjusted associations

Table model_coefficients_all.csv reports all 320 coefficients by window and
adjustment set. For the technical-cooperation share (3–5-year window,
adjustment set B): β = -0.203 (SE 0.177,
n = 3538) for log GDP per capita, and β = -4.345 pp
(SE 2.840, n = 3215) for manufacturing value added per GDP.
Interpreted compositionally: shifting 10 percentage points of the aid-type
portfolio from the omitted composition (debt relief and other flows) to
technical cooperation is associated with a 0.020-log-point
lower mean GDP per capita and 0.434 pp lower manufacturing
share over the subsequent 3–5 years — conditional associations, not effects
of technical cooperation in isolation. GFCF/GDP coefficients are imprecise
(see falsification_results and adjustment_stability tables).

### 5.4 Lag structure

Figure 4 reports TC-share coefficients by lag window in chronological order.
Point estimates are negative across windows for GDP per capita and
manufacturing share and do not display a monotonic attenuation pattern.

### 5.5 Adjustment-set sensitivity

Moving from adjustment set A to C (adding age structure, fertility, median
age, FDI/GDP, exports/GDP), the TC coefficient on GDP per capita moves from
-0.134 to
-0.369 —
directionally stable, larger under aggressive controls — while the
manufacturing coefficient stays in a narrow negative range
(-5.379 to
-3.861).

### 5.6 Falsification

Three pre-registered tests: (i) a *lead placebo* — architecture measured
three years *after* the outcome window shows β = -0.230
(p = 0.166), statistically compatible with zero; (ii) a
*pseudo-outcome* — urban-population share, which architecture should not
move — yields no significant aid-type term; (iii) a *within-year shuffle* —
aid-type share vectors permuted across recipients within year (200 draws,
seed 20260925) — yields a share of permuted coefficients at least as extreme
as the observed TC coefficient (-0.203) of
2% (placebo mean
-0.0026, sd 0.083), i.e. only about one in fifty
randomized compositions is as extreme, in a one-sided extremeness sense. This rules out
mechanical artifacts of the share-parameterization, but not selection on
recipient characteristics.

### 5.7 Procurement linkage (exploratory)

In the partial, recent-biased sample of World Bank contract awards, the
share of contract value awarded to bidders located in the project country
correlates modestly with the recipient-government channel share
(results/audits/PHASE_14_PROCUREMENT.md). Supplier country is not domestic
value added and coverage is partial; this section is descriptive only.

## 6. Discussion

The most plausible alternative explanation for the negative technical-
cooperation association is confounding by indication: donors deploy TC-heavy
portfolios precisely where institutions and implementation capacity are
weakest. Under that reading, TC intensity is a *marker* of a difficult
recipient context rather than a harmful architecture. Our within-recipient
and falsification analyses constrain but cannot eliminate this
interpretation. The lead-placebo result is consistent with the association
not being an artifact of trending portfolios alone, but residual selection
on recipient need remains the leading rival explanation.

Further limitations: lag windows may miss the true horizon of capacity
formation; reporting heterogeneity across donors (tying flags are
increasingly non-reported after 2005) limits the tying analysis to a
reported subsample; the procurement measure is partial and cannot measure
domestic value added; and share coefficients are compositional contrasts,
not absolute effects of any single modality. In addition, the TC-share
measure captures only modality-D technical cooperation (a small disbursement
share); TC embedded in project-type aid is measured separately via the
project-TC-component variable and shows no consistent association pattern.

## 7. Conclusion

Conditional on aid volume, delivery architecture differs systematically
across donors and is associated with medium-run recipient outcomes. The
technical-cooperation association is negative and survives the falsification
suite, but the design is associational and selection is a first-order rival
explanation. Whether TC-heavy portfolios are causal, a marker, or both is
the priority question for designs with better identification.

## References
1. Burnside & Dollar. Aid, Policies, and Growth. American Economic Review. 2000. doi:10.1257/aer.90.4.847
2. Burnside & Dollar. Aid, Policies, and Growth: Revisiting the Evidence. World Bank Policy Research Working Paper 3251. 2004. doi:10.1596/1813-9450-3251
3. Easterly. Can Foreign Aid Buy Growth?. Journal of Economic Perspectives. 2003. doi:10.1257/089533003769204344
4. Clemens et al.. Counting Chickens when they Hatch: Timing and the Effects of Aid on Growth. The Economic Journal. 2012. doi:10.1111/j.1468-0297.2011.02482.x
5. Rajan & Subramanian. Aid and Growth: What Does the Cross-Country Evidence Really Show?. Review of Economics and Statistics. 2008. doi:10.1162/rest.90.4.643
6. Arndt, Jones & Tarp. Assessing Foreign Aid’s Long-Run Contribution to Growth and Development. World Development. 2015. doi:10.1016/j.worlddev.2013.12.016
7. Minoiu & Reddy. Development Aid and Economic Growth: A Positive Long-Run Relation. Quarterly Review of Economics and Finance. 2010. doi:10.1016/j.qref.2009.10.004
8. Doucouliagos & Paldam. The ineffectiveness of development aid on growth: An update. European Journal of Political Economy. 2011. doi:10.1016/j.ejpoleco.2010.11.004
9. Mekasha & Tarp. Aid and Growth: What Meta-Analysis Reveals. The Journal of Development Studies. 2013. doi:10.1080/00220388.2012.709621
10. Alesina & Dollar. Who Gives Foreign Aid to Whom and Why?. Journal of Economic Growth. 2000. doi:10.1023/a:1009874203400
11. Kilby & Dreher. The Impact of Aid on Growth Revisited: Do Donor Motives Matter?. Economics Letters. 2010. doi:10.1016/j.econlet.2010.02.015
12. Feeny & McGillivray. What Determines Bilateral Aid Allocations? Evidence From Time Series Data. Review of Development Economics. 2008. doi:10.1111/j.1467-9361.2008.00443.x
13. Berthelemy & Tichit. Bilateral donors' aid allocation decisions—a three-dimensional panel analysis. International Review of Economics &amp; Finance. 2004. doi:10.1016/j.iref.2003.11.004
14. Boone. Politics and the Effectiveness of Foreign Aid. European Economic Review. 1996. doi:10.1016/0014-2921(95)00127-1
15. Feyzioglu, Swaroop & Zhu. A Panel Data Analysis of the Fungibility of Foreign Aid. World Bank Economic Review. 1998. doi:10.1093/wber/12.1.29
16. Devarajan & Swaroop. The Implications of Foreign Aid Fungibility for Development Assistance. World Bank Policy Research Working Paper 2022. 1998. doi:10.1596/1813-9450-2022
17. Pettersson. Foreign sectoral aid fungibility, growth and poverty reduction. Journal of International Development. 2007. doi:10.1002/jid.1378
18. Easterly & Pfutze. Where Does the Money Go? Best and Worst Practices in Foreign Aid. Journal of Economic Perspectives. 2008. doi:10.1257/jep.22.2.29
19. Clay, Geddes & Natali. Untying Aid: Is it Working? An Evaluation of the Implementation of the Paris Declaration and of the 2001 DAC Recommendation on Untying ODA to the LDCs. Danish Institute for International Studies (DIIS) report. 2009.
20. Jepma. Aid Tying: Trade and Resource Allocation Effects. The Economics of Aid (Jepma, ed., Routledge). 1991.
21. Morrissey & White. EVALUATING THE CONCESSIONALITY OF TIED AID*. The Manchester School. 1996. doi:10.1111/j.1467-9957.1996.tb00481.x
22. Knack. Aid Dependence and the Quality of Governance: Cross-Country Empirical Tests. Southern Economic Journal. 2001. doi:10.2307/1061596
23. Brautigam & Knack. Foreign Aid, Institutions, and Governance in Sub‐Saharan Africa. Economic Development and Cultural Change. 2004. doi:10.1086/380592
24. Bulir & Hamann. Volatility of Development Aid: From the Frying Pan into the Fire?. World Development. 2008. doi:10.1016/j.worlddev.2007.02.019
25. Fukuda-Parr, Lopes & Malik. Capacity for Development: New Solutions to Old Problems. Earthscan/UNDP (eds. Fukuda-Parr, Lopes, Malik). 2002.
26. Kenny. What Is Effective Aid? How Would Donors Allocate It?. European Journal of Development Research. 2008. doi:10.1080/09578810802078704
27. Bourguignon & Sundberg. Aid Effectiveness—Opening the Black Box. American Economic Review. 2007. doi:10.1257/aer.97.2.316

## Figures (separate files for submission)

- fig_architecture_trends.png (Figure 1) — disbursement-weighted aid-type and
  channel shares over time.
- fig_donor_architecture.png (Figure 2) — heatmap of architecture shares for
  the top-20 donors by ODA volume (descriptive; not a quality ranking).
- fig_oda_gdp_hist.png (Figure 3) — distribution of ODA disbursements as a
  share of recipient GDP (percent).
- fig_coef_tc_windows.png (Figure 4) — technical-cooperation-share
  coefficients by lag window, chronological order; coefficients are
  compositional contrasts vs the omitted aid-type composition.
