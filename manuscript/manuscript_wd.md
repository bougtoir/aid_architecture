# Beyond Aid Volume: Donor Heterogeneity, Aid Architecture, and Medium-Run Development Outcomes

## Abstract

Aid-effectiveness research has focused largely on how much aid countries receive, yet recipients experience aid through a structured delivery architecture — its composition by aid type, delivery channel, financial instrument, and tying status. This paper constructs a harmonized, disbursement-weighted aid-architecture panel from the full OECD Creditor Reporting System (145,790 donor–recipient–year observations, 1995–2024), merged with UN World Population Prospects demography and World Development Indicators outcomes (141 countries, 4,169 recipient-years), and asks how architecture varies across donors and how exposure to different architectures is associated with medium-run outcomes at comparable total aid. Adding donor fixed effects to a recipient-and-year baseline raises explained variance by roughly 13–28 percentage points across major architecture shares, although for some dimensions recipient characteristics contribute comparably. Illustratively, at fixed ODA per capita, reallocating the aid-type portfolio toward technical cooperation is associated with lower subsequent GDP per capita and manufacturing share (a 10-point reallocation ≈ -0.020 log points); estimates are imprecise and selection remains plausible. Evaluating assistance by volume alone conceals systematic differences in how aid is delivered.

**Keywords:** foreign aid; aid architecture; donor heterogeneity; technical cooperation; aid effectiveness; development assistance

## 1. Introduction

Aid effectiveness has traditionally been evaluated in terms of amounts: how
much aid a country receives, and whether that volume raises growth or
development outcomes [1,2,3]. The resulting
debate — over policy interactions, timing, and fragility of the
aid–growth correlation [4,5,6,7,8,9]
— has largely treated aid as a single quantity.

Nominal volume, however, aggregates a heterogeneous delivery structure.
Recipients experience aid as a portfolio: grants versus loans, budget
support versus project interventions, delivery through government versus
non-state channels, tied versus untied procurement, and a large technical-
cooperation component embedded in project aid.

Several literatures study these margins separately. Donor-allocation work
shows bilateral aid responds to donor motives as much as recipient need
[10,11,12,13]; fungibility studies
show the use of aid depends on its form
[14,15,16,17]; evaluations of tying
and delivery practice document large cross-donor differences
[18,19,20,21]; and institutional and
capacity-building analyses link aid structure to governance and state
capacity [22,23,24,25]. Aid
volatility complicates planning on the recipient side [26].
Bourguignon and Sundberg called for opening the "black box" between
disbursement and outcome [27].

What remains unresolved is integration: how much of the variation in the
architecture a recipient faces is attributable to donor identity rather
than to recipient characteristics, and whether exposure to different
architectures at comparable total aid is associated with different
medium-run outcomes.

This paper's contribution is a harmonized measurement and decomposition
exercise: (i) a disbursement-weighted aid-architecture stack built on the
full OECD Creditor Reporting System (CRS) activity file; (ii) a
donor-versus-recipient decomposition of architecture variation; (iii) a
frozen set of lagged-outcome regressions with a falsification suite; and
(iv) dashboard-ready scenario exports for fixed-total-aid portfolio
reallocations. All outcome associations are reported as adjusted
associations, not causal effects.

## 2. Data

The analysis combines four public sources (full provenance, checksums and
machine-readable manifests are maintained in the project repository):

- OECD Creditor Reporting System, full activity file (about 6.2 million
  activity rows, 1973–2024); ODA rows, 1995–2024 used here.
  CRS amounts are reported in millions of constant USD (DAC deflator base).
- OECD DAC aggregate tables and official code lists.
- World Bank World Development Indicators (21 indicators).
- UN World Population Prospects 2024.
- World Bank procurement notices (partial, recent-biased; exploratory
  linkage only) and the AidData 3.1 core release (robustness cross-check;
  coverage ends 2013).

## 3. Measuring aid architecture

Architecture is measured as disbursement-weighted shares of constant-USD
ODA along four margins: aid type (technical cooperation, budget support,
project-type interventions, pooled/earmarked contributions, NGO core
support, scholarships, debt relief, administrative and in-donor refugee
costs), delivery channel (recipient government, donor government,
third-country government, NGO, multilateral, PPP/network, private sector),
financial instrument (grant, loan, other), and tying status where reported.
Variables follow a frozen level ontology (raw amount → architecture shares
→ downstream outcomes); no composite index is constructed, and supplier
country is never treated as domestic value added.

One definitional caveat matters for interpretation. The CRS aid-type
variable distinguishes technical cooperation (type D) as a modality; a
substantial share of technical-cooperation activity is delivered inside
project-type interventions. The TC share used here (disbursement-weighted
mean 1.8%) is therefore a narrow modality
measure; the TC *value component* embedded in projects is measured
separately and shows no consistent association pattern.

All share variables are compositional: within each margin they sum to one.
Coefficients are contrasts against the omitted share (aid type: debt
relief plus residual "other"; channel: "other"; finance: residual
category). A coefficient on the technical-cooperation share reads as:
reallocating the aid-type portfolio toward technical cooperation — and away
from the omitted composition — at fixed total aid is associated with a
β-sized change in the outcome-window mean.

## 4. Empirical design

The primary specification regresses the mean of outcome Y over lag window
w (1–2, 3–5, 6–10, or 11–15 years after exposure year t) on the year-t
architecture shares, log ODA per capita at t, a pre-registered demographic
adjustment set, and country and year fixed effects, with country-clustered
standard errors. Estimands, windows, and adjustment sets were frozen before
inference; the claim ceiling is adjusted association throughout. Primary
outcomes: log real GDP per capita, gross fixed capital formation per GDP,
and manufacturing value added per GDP; secondary outcomes: tax revenue per
GDP and electricity access.

## 5. Results

### 5.1 Sample and architecture exposure

Table 1 summarizes the sample: 4,169 recipient-years
across 141 countries (1995–2024). Mean ODA
disbursements equal 6.8% of recipient GDP (median
2.6%); median ODA is about
$53 per capita. Figure 1 shows the
evolution of disbursement-weighted aid-type and channel shares; project-
type interventions dominate throughout. The ODA/GDP histogram is relegated
to the Supplement (Figure S1).

### 5.2 Donor heterogeneity and the decomposition of architecture

Figure 2 — the paper's central exhibit — shows architecture profiles of the
top-20 donors by ODA volume: recipient-government channel shares, technical-
cooperation shares, and reported untied shares differ sharply across donors
(descriptive; no quality ranking implied).

Table 2 decomposes the variance of each architecture share. Adding donor
fixed effects to a recipient-and-year baseline raises R² from
0.401 to
0.624 for the
recipient-government channel share (incremental R² =
0.223); donor increments are
0.249 for technical cooperation and
0.268 for budget support. Donor identity
thus contributes substantially to explained architecture variation — but
not unilaterally: for project-type shares, the recipient dimension
contributes comparably (incremental recipient R² =
0.225 vs donor
0.131), indicating architecture also reflects
what recipients receive and demand.

### 5.3 Architecture and medium-run outcomes

Table 3 reports the technical-cooperation-share coefficients across lag
windows for the primary outcomes; the full 320-coefficient grid is in the
Supplement (Table S1). At the 3–5-year window, β = -0.203
(SE 0.177) for log GDP per
capita and β = -4.345 pp
(SE 2.840) for manufacturing
share. Compositionally, a 10-percentage-point reallocation toward technical
cooperation (from the omitted composition, at fixed total aid) corresponds
to about 0.020
log points lower mean GDP per capita and 0.43
pp lower manufacturing share over the window. These estimates are
imprecise: conventional intervals include zero at most windows.

### 5.4 Lag structure and sensitivity

Figure 3 shows TC-share coefficients by window in chronological order; the
negative point estimates for GDP per capita do not attenuate monotonically,
and precision narrows at longer windows. Across adjustment sets A–C the
TC coefficient on GDP per capita moves from
-0.134 to
-0.369 —
directionally stable, larger under aggressive controls — while the
manufacturing coefficient stays in a narrow negative range
(-5.379 to
-3.861).

### 5.5 Falsification

Table 4 summarizes the pre-registered suite. A lead placebo (architecture
measured three years after the outcome window) yields β = -0.230
(p = 0.166), compatible with zero. A pseudo-outcome (urban-
population share) shows no significant aid-type term. A within-year
permutation of aid-type share vectors (200 draws, fixed seed) places the
observed TC coefficient (-0.203) beyond |β| of all but
2% of randomized
allocations (permutation mean -0.0026, sd 0.083);
this is an extremeness share, not a conventional p-value, and it rules out
parameterization artifacts only — not selection on recipient
characteristics.

### 5.6 Procurement linkage (exploratory)

In the partial, recent-biased World Bank contract-award sample, the share
of contract value awarded to in-country bidders correlates modestly with
the recipient-government channel share. Supplier country is not domestic
value added, subcontracting is unobserved, and coverage is partial; this
layer is presented strictly as a measurement extension motivating better
local-participation reporting.

## 6. Discussion

### 6.1 Aid architecture as a hidden dimension of aid exposure

At equal nominal ODA per capita, recipients face materially different
portfolios — different aid types, channels, instruments, and tying. Volume-
only evaluation aggregates this structure away; the architecture stack
shows it is measurable, persistent, and partially donor-driven.

### 6.2 Donor heterogeneity versus recipient context

Donor fixed effects contribute meaningfully to explained architecture
variance, consistent with allocation research showing donor motives shape
aid. But the decomposition is not one-sided: for project-type shares the
recipient dimension contributes comparably, meaning architecture also
reflects recipient demand, absorptive choices, and project pipelines.

### 6.3 Why TC-heavy portfolios may correlate with weaker outcomes

The leading rival explanation is confounding by indication: donors deploy
technical cooperation where institutions and implementation capacity are
weakest, and where results are hardest. Under that reading TC intensity is
a marker of a difficult context, not a harmful modality. Alternative
hypotheses (labeled as such): TC may substitute for — rather than build —
local capacity; it may reflect implementation difficulty in post-crisis or
institutionally weak settings. The lead-placebo and permutation results
bound mechanical explanations but cannot eliminate selection; the negative
TC association is directionally stable and unusually extreme relative to
randomized within-year compositions, yet statistically imprecise and
vulnerable to residual selection.

### 6.4 Procurement and local participation remain a partial layer

Supplier-country data cannot measure domestic value added; subcontracting
and reporting gaps are material. The procurement linkage is therefore a
proof of concept for extending the architecture stack toward local economic
participation once reporting harmonizes.

### 6.5 Implications for aid evaluation

Amount alone is an insufficient statistic for aid exposure. Evaluation and
comparison frameworks — including donor scorecards — should track
composition and delivery structure explicitly, and procurement/local-
participation reporting deserves harmonization. No specific reallocation
(toward or away from technical cooperation, budget support, or any channel)
is prescribed by this associational evidence.

### 6.6 Implications for future causal research

Credible identification could come from donor-specific procurement or
tying reforms, policy shocks that shift modality shares, staggered adoption
of Paris/Busan-era commitments, or quasi-experimental variation in
architecture at fixed volume — designs the measurement stack here is built
to support.

## 7. Conclusion

Aid architecture is an empirically measurable dimension of development
assistance that varies substantially across donors and contains information
about recipient exposure that nominal aid volume alone conceals. Donor
identity contributes substantially — though not unilaterally — to the
architecture recipients face, and composition-weighted associations with
medium-run outcomes are detectable but imprecise and non-causal. The
priority for the literature is designs that separate the architecture
donors choose from the recipient contexts that call for it.

## Data availability statement

All data are public: OECD Creditor Reporting System and DAC tables (OECD),
World Development Indicators (World Bank), World Population Prospects 2024
(United Nations), AidData 3.1, and World Bank procurement notices.
Raw-source acquisition scripts, provenance manifests, panel-construction
and analysis code, and dashboard-ready exports are available in the
project repository (link on title page). Source terms of use apply;
proprietary or access-restricted microdata are not redistributed.

## References
1. Burnside & Dollar. Aid, Policies, and Growth. American Economic Review. 2000. doi:10.1257/aer.90.4.847
2. Burnside & Dollar. Aid, Policies, and Growth: Revisiting the Evidence. World Bank Policy Research Working Paper 3251. 2004. doi:10.1596/1813-9450-3251
3. Rajan & Subramanian. Aid and Growth: What Does the Cross-Country Evidence Really Show?. Review of Economics and Statistics. 2008. doi:10.1162/rest.90.4.643
4. Easterly. Can Foreign Aid Buy Growth?. Journal of Economic Perspectives. 2003. doi:10.1257/089533003769204344
5. Clemens et al.. Counting Chickens when they Hatch: Timing and the Effects of Aid on Growth. The Economic Journal. 2012. doi:10.1111/j.1468-0297.2011.02482.x
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
24. Fukuda-Parr, Lopes & Malik. Capacity for Development: New Solutions to Old Problems. Earthscan/UNDP (eds. Fukuda-Parr, Lopes, Malik). 2002.
25. Kenny. What Is Effective Aid? How Would Donors Allocate It?. European Journal of Development Research. 2008. doi:10.1080/09578810802078704
26. Bulir & Hamann. Volatility of Development Aid: From the Frying Pan into the Fire?. World Development. 2008. doi:10.1016/j.worlddev.2007.02.019
27. Bourguignon & Sundberg. Aid Effectiveness—Opening the Black Box. American Economic Review. 2007. doi:10.1257/aer.97.2.316

## Tables

Table 1. Sample and architecture summary (disbursement-weighted shares, pooled).
Table 2. Variance decomposition of architecture shares (incremental R² of donor and recipient fixed effects).
Table 3. Technical-cooperation-share coefficients by lag window (β; country-clustered SE in parentheses; compositional contrast vs omitted aid-type composition).
Table 4. Falsification suite summary.

## Figures

Figure 1. Disbursement-weighted aid-type and channel shares over time.
Figure 2. Aid-architecture shares of the top-20 donors by ODA volume (descriptive; no quality ranking implied).
Figure 3. Technical-cooperation-share coefficients by outcome window after exposure year (compositional contrast vs omitted aid-type composition; whiskers are 95% CI).
