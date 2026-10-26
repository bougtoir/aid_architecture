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
— has largely treated aid as a single quantity. Meta-analytic
assessments reach similarly fragile conclusions: pooled across decades of
specifications, the average aid–growth association is small and highly
sensitive to model choice [10,8], and even
quasi-experimental designs exploiting concessional-lending thresholds
find effects concentrated in particular subsamples rather than a general
volume effect [11].

Nominal volume, however, aggregates a heterogeneous delivery structure.
Two recipients receiving identical aid totals in a given year may
experience that aid through entirely different portfolios: one may
receive mostly grants delivered through its own ministries, another
mostly concessional loans implemented by donor executing agencies; one
may procure goods and services domestically, another under tied
procurement from the donor's suppliers; one may host a large
technical-cooperation program while another relies on direct budget
support. The bilateral total is silent on every one of these margins —
on aid type, on delivery channel, on financial instrument, on tying
status, and on the implementation arrangements that follow from them.

The problem is not hypothetical. Aggregate aid totals are the headline
statistic of development cooperation — the number reported in donor
communiqués, monitored against international targets, and fed into
cross-country regressions — yet two identical totals can describe
transfers with almost nothing in common operationally. A recipient whose
aid arrives mostly as tied project contracts implemented by foreign
firms experiences a different inflow than one receiving the same dollars
as untied budget support credited to its treasury: the first may leave
little fiscal trace beyond the projects themselves, while the second is
a budgeted public resource. Comparing their outcomes per dollar of "aid"
treats these as the same exposure.

These margins are not merely administrative detail; each is a plausible
channel through which the same nominal transfer could be experienced
differently. The literature has proposed several such pathways, which we
flag as hypotheses rather than mechanisms this paper tests: aid delivered
through recipient-government systems may build public-sector
implementation capacity, while aid implemented by donors or contractors
may substitute for it; budget support integrates with the recipient's
fiscal planning and may improve predictability, whereas project aid
arrives earmarked to specific activities; procurement structure
determines how much of the nominal transfer is actually spent inside the
recipient economy; the modality mix shapes the administrative burden
placed on scarce civil-service capacity; and the timing at which benefits
accrue differs across modalities. Whether and when any of these pathways
operates is an empirical question this paper does not resolve — but each
implies that the content of a constant-USD dollar of aid depends on the
architecture through which it is delivered.

The analytical stakes are therefore twofold. If architecture matters,
then the average association between volume and outcomes masks
composition effects that could differ in sign and magnitude across
margins — a plausible contributor to the fragility of the aggregate
literature. If architecture does not matter, then documenting that fact
cleanly still requires measuring it: the null question cannot be asked
of data that aggregate the margins away. Either way, an empirical
description of aid architecture — how much it varies, whose identity
predicts it, how it covaries with later outcomes — is a precondition for
evaluating aid on anything other than a volume basis.

Several literatures study these margins separately. The aggregate
aid-effectiveness literature supplies the motivation but treats aid
almost exclusively as a volume. Donor-allocation research shows that
bilateral aid responds to donor motives — strategic, commercial, and
historical — as much as to recipient need
[12,13,14,15], that transparency
and governance shape allocations [16], and that donor
heterogeneity extends beyond the traditional DAC membership
[17,18]; this work establishes that donors are not
interchangeable, though it explains where money goes more than how it is
delivered. Fungibility studies show that the use to which aid is put
depends on its form and on the recipient's budgetary response
[19,20,21,22], and sector-level
analyses reach similar conclusions for earmarked flows [23].
Evaluations of tying and delivery practice document large, persistent
cross-donor differences in procurement conditionality and channel use
[24,25,26,27]. Macroeconomic
side-condition literatures show that the instrument mix matters for
tradable-sector outcomes through real-exchange-rate and absorption
channels [28,29]. Aid volatility complicates planning
on the recipient side [30]. Institutional and capacity-building
analyses link aid structure to governance quality and state capacity
[31,32,33,34], and the
conditionality literature examines how the terms attached to aid shape
its political economy [35]. Bourguignon and Sundberg called for
opening the "black box" between disbursement and outcome [36].

What remains fragmented is integration. The gap is not a shortage of
studies of aid heterogeneity — each margin above has its own literature —
but the absence of an empirical framework that (a) measures the major
architecture dimensions together on a common, comprehensive data
foundation; (b) quantifies how much of the architecture a recipient faces
is attributable to donor identity rather than recipient characteristics;
(c) relates architecture to medium-run outcomes at comparable total aid
volume; (d) preserves the compositional interpretation that share-based
measures require; and (e) produces outputs that subsequent causal or
scenario work can build on directly.

Positioning matters as much as novelty. This is primarily a measurement
and decomposition paper with an associational panel analysis attached —
not a causal evaluation of any modality, not a donor ranking, and not
another generic aid–growth regression. The most policy-sensitive number
we report, a technical-cooperation-share association, is deliberately
framed as illustrative: its purpose is to demonstrate what the
architecture variables can and cannot support inferentially, not to
adjudicate whether technical cooperation helps or harms.

This paper's contribution is a harmonized measurement and decomposition
exercise that supplies that framework, in four parts: (i) a
disbursement-weighted aid-architecture stack built on the full OECD
Creditor Reporting System (CRS) activity file — 145,790
donor–recipient–year observations over
1995–2024, the population of reported ODA
activities rather than a sample; (ii) a donor-versus-recipient
decomposition that quantifies, margin by margin, how much of the
architecture a recipient faces is predictable from which donor supplies
it versus which recipient absorbs it; (iii) a frozen set of
lagged-outcome regressions linking composition to medium-run outcomes at
comparable total aid, accompanied by a pre-registered falsification
suite; and (iv) dashboard-ready scenario exports that let readers explore
fixed-total-aid portfolio reallocations under the model's coefficients.
Each element maps onto one of the gaps (a)–(e) above: the stack supplies
the common data foundation, the decomposition the attribution, the
frozen regressions the outcome link at fixed volume, the compositional
definitions the interpretability, and the exports the reusability. All
outcome associations are reported as adjusted associations, not causal
effects. Section 2
describes the data, Section 3 the measurement approach, Section 4 the
empirical design, Section 5 the results, and Section 6 their
interpretation and limits.

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

### 2.1 Creditor Reporting System

The primary exposure source is the OECD Creditor Reporting System (CRS),
the donor community's activity-level reporting standard. Each CRS record
describes one aid activity — a commitment or disbursement by a reporting
donor to a recipient, in a sector, through a channel, under a financial
instrument and an aid-type modality, with tying status where reported —
rather than an annual aggregate. We retain official development
assistance (category 10) records for 1995–2024 and use
gross disbursements converted to constant US dollars with the DAC
deflator. Disbursements rather than commitments are used because they
measure resources actually transferred; commitments are retained as a
secondary field. Records are then aggregated to the
donor–recipient–year level, yielding 145,790 dyad-years in
the architecture panel. The activity-level design matters for the
measurement concept: composition shares are computed from the same
activity population for every dyad-year, so differences in shares reflect
differences in the underlying portfolio of transfers rather than
differences in reporting conventions at the aggregate level. Sector,
channel, finance-type, aid-type, and tying codes are taken from the
official OECD code lists; where a parent channel is reported it is used
in preference to the sub-channel, and CRS records carry dedicated fields
for the technical-cooperation value component of project aid and for
tied, partially tied, and untied amounts. The 1995 start restricts the
panel to the period of fuller CRS reporting coverage and more consistent
code use; earlier records (the file begins in 1973) remain in the raw
archive but are not used.

### 2.2 Outcomes and demographic covariates

Outcomes come from the World Bank World Development Indicators. The
primary outcomes — log real GDP per capita, gross fixed capital
formation relative to GDP, and manufacturing value added relative to
GDP — are chosen to capture complementary development dimensions: the
income level, investment effort, and structural change respectively. Two
secondary outcomes, tax revenue relative to GDP and electricity access,
capture fiscal capacity and basic-service reach. Macroeconomic covariates
used in the widest adjustment set (foreign direct investment and exports
relative to GDP) come from the same source.

Demographic adjustment uses the UN World Population Prospects 2024.
Population totals supply denominators, but the adjustment set also
exploits the WPP's internal structure: population growth, urbanization,
the shares aged 0–14 and 65 and above, median age, and total fertility
enter because demographic composition — not population size alone — is a
plausible joint correlate of aid allocation and medium-run outcomes. Two
countries with identical population growth can face very different
dependency burdens, and the WPP separates these dimensions rather than
reducing demography to a single trend.

### 2.3 Secondary sources with limited roles

AidData 3.1 extends coverage to non-DAC reporters, including major
non-traditional donors, but ends in 2013 [37]; it is used only
as a coverage cross-check on the CRS-based panel. World Bank procurement
notices name the winning supplier's country for a partial, recent-biased
subset of contracts; they support an exploratory linkage to local
participation only. A supplier's country is not domestic value added,
subcontracting is unobserved, and coverage is partial, so this layer is
never used to claim local-retention effects.

### 2.4 Harmonization

Country identifiers are reconciled through the OECD recipient and donor
code lists: CRS recipient codes map to ISO3 codes together with region,
income-group, landlocked, SIDS, and fragile-state flags, and donor codes
map to ISO3 where a country donor exists, with multilateral and
institutional reporters retained as separate donor entities. Architecture
shares are computed only where a dyad-year's disbursed total is positive,
so missing amounts are distinguished from true zeros: a dyad-year absent
from the CRS means no reported ODA flow, which is different from a flow
whose composition fields are blank. Tying shares are defined only where
tying amounts are reported; dyad-years with unreported tying are flagged
rather than coded as untied — a distinction that matters because
unreported tying is itself unevenly distributed across donors and years.
Recipient-year aggregates pool all donor flows received in a year and
therefore describe the architecture of the total portfolio the recipient
faced, not the portfolio of any single donor.

## 3. Measuring aid architecture

Architecture is measured as disbursement-weighted shares of constant-USD
ODA along four margins, each built from the corresponding CRS code list.
*Aid type* (the CRS aid-type modality) separates technical cooperation,
budget support, project-type interventions, pooled and earmarked
contributions, NGO core support, scholarships and student costs, debt
relief, and administrative plus in-donor refugee and awareness costs.
*Delivery channel* separates recipient government, donor government,
third-country government, NGOs, multilateral bodies, public-private
partnerships and networks, private-sector entities, and universities;
where a parent channel is reported it takes precedence over the executing
sub-channel, so shares describe the channel structure the donor selected
rather than the last implementing agent in the chain. *Financial
instrument* separates grants, concessional loans, equity, debt relief,
guarantees, and residual instruments. *Tying status* separates untied,
partially tied, and tied amounts where donors report them. Variables
follow a frozen level ontology — raw disbursement amount, architecture
shares, downstream outcomes — so no derived quantity ever feeds back into
a lower level, and supplier country is never treated as domestic value
added.

A fifth margin, purpose sector, is tracked in the stack for completeness —
education, health, water and sanitation, governance and other social,
infrastructure, energy, finance and business, productive, environment,
multisector, program support, debt, humanitarian, and
administrative/refugee/other groups — but is not carried into the frozen
outcome regressions, whose estimands use aid type, channel, finance, and
tying. Sector shares enter the dashboard and stack exports but are not
analyzed further here, to keep the inferential layer focused.

Shares, not activity counts or levels, are the unit of measurement
because the object of interest is the composition of the portfolio a
recipient faces. A dyad-year in which 60% of disbursed aid runs through
recipient-government systems is architecturally different from one at
20%, independently of whether the totals differ. Weighting by
disbursement ensures shares reflect resource composition rather than the
number of activities — a single large loan counts by its value, not as
one line item equal to a small grant.

We deliberately do not collapse the four margins into a composite
"architecture quality" index. Any scalar index would require weights
that are not identifiable from the data — nothing determines whether a
point of government-channel share should count more or less than a point
of untied share — would destroy the interpretability of the component
dimensions, whose coefficients carry direct compositional meanings, and
would manufacture an ordinal ranking of donors or recipients that the
measurement does not support. The temptation is understandable — a
single number is easier to report and to rank on — but the cost is
deciding in advance, without evidence, that margins trade off at fixed
rates. Retaining separate dimensions preserves exactly what can be
defended: each share is measured identically for every dyad-year, and
each coefficient reads as a reallocation contrast within its own
margin.

One definitional caveat matters for interpretation. The CRS aid-type
variable distinguishes technical cooperation (type D) as a modality; a
substantial share of technical-cooperation activity is delivered inside
project-type interventions. The TC share used here (disbursement-weighted
mean 1.8%) is therefore a narrow modality
measure — the standalone TC modality — not total technical-cooperation
intensity; the TC *value component* embedded in projects is measured
separately through the CRS TC-amount field and shows no consistent
association pattern. A reader comparing our headline TC share with the
higher TC intensities sometimes quoted in the literature should keep this
distinction in view: the modality share understates total TC activity
wherever TC is delivered inside projects, and the two measures answer
different questions — one about delivery modality, the other about
resource content.

All share variables are compositional: within each margin they sum to
one, so increasing one share mechanically implies decreasing another.
Coefficients are therefore contrasts against the omitted share (aid type:
debt relief plus residual "other"; channel: "other"; finance: residual
category), and the omitted composition matters for interpretation.
Concretely, a coefficient β on the technical-cooperation share means
that moving 10 percentage points of the aid-type portfolio into technical
cooperation — and therefore 10 points out of the omitted composition — is
associated with a β/10 change in the outcome-window mean at fixed total
aid per capita. It is not a statement about raising the TC share while
holding every other share fixed, which the summation constraint makes
impossible.

Tying merits separate caution. Tied and untied amounts are self-reported,
and coverage is incomplete and uneven across donors and over time; early
CRS years in particular carry sparse tying fields. We therefore compute
tying shares only on the reported subset, flag unreported dyad-years
rather than coding them as untied, and treat all tying-related quantities
as descriptive context rather than inferential inputs.

## 4. Empirical design

### 4.1 Specification and fixed effects

The primary specification regresses the mean of outcome Y over lag window
w (1–2, 3–5, 6–10, or 11–15 years after exposure year t) on the year-t
architecture shares, log ODA per capita at t, a pre-registered adjustment
set, and country and year fixed effects, with country-clustered standard
errors.

Country fixed effects absorb all time-invariant recipient
characteristics — geography, institutional history, persistent level of
development — so coefficients are identified from within-country changes
in architecture exposure rather than from cross-sectional comparisons
between chronically different recipients. Year fixed effects absorb
global shocks and common trends in aid practice and outcomes — the
post-2001 scaling-up of aid, the 2008–09 financial crisis, the COVID-19
period — that would otherwise load onto any architecture–outcome
association. Standard errors are clustered by recipient because both
exposures and outcomes are serially correlated within countries: donors
maintain multi-year engagement strategies, so a recipient's portfolio in
year t strongly predicts its portfolio in year t+1, and unclustered
errors would overstate precision.

The outcome regressions run at the recipient-year level — the level at
which development outcomes are defined — using the architecture of the
total aid portfolio the recipient faced that year, pooled across donors.
The dyadic donor–recipient–year panel is reserved for the decomposition
exercise (Section 4.4), where donor identity is the object of interest.
Keeping the two units separate avoids attributing a single donor's
architecture to an outcome that responds, if anything, to the combined
portfolio.

### 4.2 Window means and multiple windows

Outcomes are averaged across each window rather than taken at a single
lag for two reasons: annual outcomes are noisy, so averaging reduces the
sensitivity of each coefficient to which particular post-exposure year is
examined; and the conceptual question concerns medium-run consequences of
exposure, not event-study dynamics. Multiple windows are retained because
candidate pathways operate on different clocks: a delivery-structure
margin could plausibly appear within one to two years if it works through
implementation mechanics, a capacity or procurement channel would operate
over the medium run, and structural outcomes such as manufacturing share
adjust on still slower horizons. Reporting all four windows descriptively
avoids selecting the lag that produces a preferred sign, and we impose
and claim no monotonic temporal mechanism.

### 4.3 Demographic and macroeconomic adjustment

The frozen adjustment sets are deliberately modest. The primary set
(adjustment B) adds to log ODA per capita and the fixed effects the WPP
controls population growth and urbanization plus the age-structure
variables — shares aged 0–14 and 65 and above, median age, and total
fertility. Demographic structure is a plausible joint correlate of aid
allocation — donors target need — and of medium-run outcomes — dependency
burdens shape savings, labor supply, and fiscal capacity — so
conditioning on it removes one obvious compositional channel. A narrower
set A drops the age-structure variables; a wider set C adds FDI and
export shares relative to GDP. Adjustment improves comparability across
recipient-years; it does not create causal identification, and nothing in
the design can exclude time-varying confounders we do not observe.

### 4.4 Donor-versus-recipient decomposition

The decomposition asks how much of the variation in each architecture
share is accounted for by donor identity versus recipient identity. Each
disbursement-weighted share is regressed on donor, recipient, and year
indicators by weighted least squares, with dyad disbursements as weights,
and R² is compared across specifications. The incremental donor R² —
the increase in explained variance when donor indicators are added to a
recipient-and-year baseline — measures how much donors contribute to the
architecture recipients face over and above what recipient identity and
year already explain; the incremental recipient R² is defined
symmetrically. These are decomposition statistics, not causal
attributions: they quantify how predictable architecture is from each
identity margin, not which side chooses it.

### 4.5 Falsification suite

Three pre-registered falsification exercises bound what the main
associations could reflect. A lead placebo replaces exposure-year
architecture with architecture measured three years after the outcome
window begins; a nonzero association there would flag reverse timing or
persistent unobserved heterogeneity. A pseudo-outcome substitutes
urban-population share — a variable aid architecture should not plausibly
shift on these horizons — for the development outcomes. A within-year
permutation shuffles aid-type share vectors across recipients within each
year (200 draws, fixed seed) and locates the observed TC coefficient in
the resulting distribution; this tests whether the estimation machinery
produces the sign and magnitude mechanically, but it cannot rule out
confounding by indication — donors may select real, systematically
different recipients into TC-heavy portfolios, which permutation
preserves by construction. The suite is deliberately asymmetric: each
test can only reject a specific mechanical account — reverse timing, a
generic regressor artifact, a parameterization quirk — and no combination
of them delivers causal identification, so a failure to reject is the
informative outcome and we report it as such.

### 4.6 Identification limits

The design's limits are as important as its mechanics. Country and year
fixed effects remove time-invariant heterogeneity and common shocks, and
the adjustment sets remove observed compositional correlates, but no
element of the design addresses time-varying, unobserved selection: if
donors shift portfolios toward technical cooperation in response to a
recipient's deteriorating capacity — a change invisible to our covariates
— the resulting association is a selection correlation, not an effect of
architecture. The falsification suite narrows the space of mechanical
explanations without identifying a causal one. We therefore treat the
outcome layer as a disciplined description of conditional covariation,
useful for bounding what architecture correlates with and for targeting
future designs, rather than as an evaluation of what architecture does.

Estimands, windows, and adjustment sets were frozen before inference;
the claim ceiling is adjusted association throughout. Primary outcomes:
log real GDP per capita, gross fixed capital formation per GDP, and
manufacturing value added per GDP; secondary outcomes: tax revenue per
GDP and electricity access.

## 5. Results

### 5.1 Sample and architecture exposure

Table 1 summarizes the sample: 4,169 recipient-years
across 141 countries (1995–2024). Mean ODA
disbursements equal 6.8% of recipient GDP (median
2.6%); median ODA is about
$53 per capita. The mean–median gap in
the GDP-share distribution reflects a well-known skew: a minority of
recipients — small economies and post-crisis states — receive aid flows
that are very large relative to GDP, while the median recipient receives
a few percent. Beneath these recipient-year statistics sit
145,790 donor–recipient–year rows: the typical recipient
deals with many donors simultaneously, so the architecture of a
recipient-year is a weighted blend of several distinct donor delivery
models rather than a single bilateral style.

Figure 1 shows the evolution of disbursement-weighted aid-type and
channel shares across the panel. Project-type interventions dominate the
aid-type composition throughout the period (disbursement-weighted mean
41%), with pooled and earmarked contributions a substantial second
category (22%); budget support (7%) and standalone
technical cooperation (2%) each remain
single-digit shares of disbursements by value. On the channel margin,
multilateral implementation carries the largest average share
(28%), ahead of recipient-government systems (19%), but the
split between government, NGO, multilateral, and other implementation
differs widely across dyads and years — precisely the variation the
decomposition and the outcome regressions exploit. The ODA/GDP
histogram is shown in Figure A1 (Appendix).

### 5.2 Donor heterogeneity and the decomposition of architecture

Figure 2 — the paper's central exhibit — shows architecture profiles of the
top-20 donors by ODA volume. The differences are stark and systematic:
some donors route the bulk of their portfolio through recipient-government
systems while others work predominantly through multilateral or
non-government channels; standalone technical-cooperation shares range
from near zero to a substantial fraction of the portfolio; and reported
untied shares differ sharply (descriptive variation only; no quality
ranking is implied). These are not noise around a common architecture —
they are persistent, donor-characteristic delivery models.

Table 2 decomposes the variance of each architecture share to quantify
this pattern. Adding donor fixed effects to a recipient-and-year baseline
raises R² from
0.401 to
0.624 for the
recipient-government channel share (incremental R² =
0.223); donor increments are
0.249 for technical cooperation and
0.268 for budget support. Donor identity
thus contributes substantially to explained architecture variation:
knowing which donor is on the other side of the dyad predicts a large
fraction of the channel and modality mix a recipient sees.

The decomposition is not one-sided, however. For the project-type share
the recipient dimension contributes comparably (incremental recipient R²
= 0.225 vs donor
0.131): which recipient a donor serves
independently predicts the modality mix, consistent with recipients
differing in implementation capacity, in the projects they can host, and
in the terms they negotiate. The full donor- and recipient-side
decomposition for every margin is reported in full (Table A1, Appendix).
Architecture is therefore jointly produced —
supplied in systematically different forms by different donors, and
filtered by recipient context — rather than dictated by either side.

One null result inside the decomposition deserves note: the TC value
component embedded within project aid (share_tc_usd_irtc) is barely
predictable from either identity margin (full R² =
0.004). Whether that reflects genuinely
idiosyncratic allocation or simply thin, uneven reporting of the field,
it cautions against reading structure into the embedded-TC layer that
the modality-level TC share does exhibit.

### 5.3 Architecture and medium-run outcomes

Table 3 reports the technical-cooperation-share coefficients across lag
windows for the primary outcomes; the full 320-coefficient grid over all
architecture margins, outcomes, windows, and adjustment sets is
reported in Table A2 (Appendix). We focus on the TC share because it is the
sharpest architectural contrast the data offer: a modality whose stated
purpose is capacity transfer, measured separately from the
capacity-relevant question of who implements the underlying projects.

At the 3–5-year window, β = -0.203
(SE 0.177) for log GDP per
capita and β = -4.345 pp
(SE 2.840) for manufacturing
share. Compositionally, a 10-percentage-point reallocation toward technical
cooperation (from the omitted composition, at fixed total aid) corresponds
to about 0.020
log points lower mean GDP per capita and 0.43
pp lower manufacturing share over the window. These estimates are
imprecise: conventional intervals include zero at most windows, so the
coefficients are best read as negative point associations of uncertain
magnitude rather than as established negative relationships. The
compositional reading also matters: the coefficient contrasts
TC-heavy portfolios against the omitted aid-type composition, not
against project aid specifically.

The other margins carry their own patterns. At the same 3–5-year window,
the recipient-government channel share is positively associated with
subsequent GDP per capita (β = 0.253,
SE 0.071) — the grid's only
positive association reaching conventional significance at this window — while the administrative/refugee/awareness
aid-type share is strongly negative (β =
-2.585, SE
0.557), a category that bundles
in-donor administrative and refugee costs and plausibly marks
diverted-to-domestic rather than transferred resources. The embedded-TC
value share shows no consistent association (β =
-0.103, SE
0.160 at this window), consistent with the
decomposition's near-unpredictable pattern for that field. These
coefficients share the compositional interpretation and the same
selection caveats; we flag the channel association as the most
informative single-margin contrast in the grid and return to it in the
Discussion.

### 5.4 Lag structure and sensitivity

Figure 3 shows TC-share coefficients by window in chronological order for
the primary outcomes (secondary outcomes — tax/GDP and electricity access —
are shown in Figure A2 (Appendix). Two descriptive features stand out. First,
the negative point estimates for GDP per capita do not attenuate
monotonically with horizon: the 6–10-year point estimate is the most
negative, and we do not read a clean temporal mechanism into the pattern —
imprecision is too large to distinguish attenuation from amplification.
Second, the sample thins at longer windows — fewer exposure years have
11–15 years of observable outcomes — so intervals widen correspondingly
and the far-horizon estimates are the least precise.

Across adjustment sets A–C the
TC coefficient on GDP per capita moves from
-0.134 to
-0.369 —
directionally stable and larger in magnitude under the aggressive
macroeconomic controls — while the
manufacturing coefficient stays in a narrow negative range
(-5.379 to
-3.861). We describe this
as directional stability, not robustness: the intervals remain broad in
every adjustment set, and stability of the point-estimate sign is
consistent both with a weak underlying association and with a stable
selection pattern. The full adjustment-set sensitivity grid is in the
sensitivity grid is reported in Table A3 (Appendix).

### 5.5 Falsification

Table 4 summarizes the pre-registered suite. A lead placebo (architecture
measured three years after the outcome window) yields β = -0.230
(p = 0.166), compatible with zero — future architecture does not
"explain" past outcomes, so the primary specification is not simply
detecting persistent country heterogeneity through reverse timing. A
pseudo-outcome (urban-population share) likewise shows no significant
aid-type term, consistent with the estimates reflecting
development-related covariation rather than a mechanical feature of the
share regressors. A within-year permutation of aid-type share vectors
(200 draws, fixed seed) places the observed TC coefficient (-0.203)
beyond |β| of all but
2% of randomized
allocations (permutation mean -0.0026, sd 0.083).
This last statistic is an extremeness share, not a conventional p-value:
it shows the observed coefficient is unusually negative relative to what
the same machinery produces on randomly reassigned — but real —
architecture portfolios. Crucially it does not rule out confounding by
indication, because the permutation preserves the mapping from
architecture to whatever recipient characteristics originally attracted
it. The complete falsification results are reported in Table A4 (Appendix).

### 5.6 Procurement linkage (exploratory)

In the partial, recent-biased World Bank contract-award sample — only
32 recipient-years are mergeable to the architecture panel — the share of
contract value awarded to in-country bidders correlates weakly and
negatively with the recipient-government channel share (r ≈ -0.161), and
weakly positively with the TC share. Neither pattern supports a simple
local-participation reading, and the caveats are first-order: supplier
country is not domestic value added, subcontracting is unobserved, and
coverage is partial and skewed to recent years. This layer is presented
strictly as a measurement extension motivating better
local-participation reporting, not as evidence on local retention.

## 6. Discussion

### 6.1 Aid architecture as a hidden dimension of aid exposure

At equal nominal ODA per capita, recipients face materially different
portfolios — different aid types, channels, instruments, and tying
arrangements. Volume-only evaluation aggregates this structure away and
implicitly assumes that a dollar of aid is a dollar of aid: that the
treatment delivered by a tied, contractor-implemented loan equals the
treatment delivered by untied budget support through government systems.
The architecture stack shows the assumption is not merely a
simplification but a loss of measurable information — the differences
are large, persistent over time, and partly systematic to the donor. If
any of the delivery margins matter for what aid accomplishes, then
evaluating assistance by volume alone discards exactly the variation
that would reveal it. In that sense architecture is a hidden dimension
of aid exposure: present in the data, consequential in principle, and
invisible to any analysis that conditions only on amounts.

The practical consequence is a change in what "more aid" and "better
aid" can mean. For a fixed total, donors and recipients effectively
choose a point in a multidimensional architecture space, and the
evidence here is that they choose very different points. Two evaluation
errors follow if that space is ignored: attributing to volume
differences what in fact differs in composition, and treating
recipients' outcomes as responses to a treatment that was never
homogeneous in the first place.

### 6.2 Donor heterogeneity versus recipient context

Donor fixed effects contribute meaningfully to explained architecture
variance, consistent with allocation research showing donor motives
shape where aid goes [12,13,38]; the
present result adds that they also shape how it is delivered. Several
institutional sources could generate such systematic differences —
statutory mandates that constrain modality choice, national procurement
rules and untying commitments, historical specialization in particular
sectors or regions, and organizational delivery models built around
implementing agencies versus direct budget operations — but the
decomposition measures predictability, not provenance, and we label
these as possible explanations rather than demonstrated mechanisms.

Equally, the decomposition is not one-sided: for project-type shares the
recipient dimension contributes comparably, meaning architecture also
reflects recipient demand, absorptive choices, and project pipelines. A
recipient that can prepare, appraise, and co-finance discrete investments
presents a different portfolio opportunity than one that cannot;
recipients negotiate, and some negotiating positions produce more
government-channel or budget-support aid than others. The finding that
both margins matter is itself informative: architecture is jointly
produced, so efforts to change it by reforming donor behavior alone will
meet the constraint of recipient capacity and preference — and vice
versa.

### 6.3 Why TC-heavy portfolios may correlate with weaker outcomes

The leading rival explanation for the negative TC-share association is
confounding by indication: donors deploy technical cooperation where
institutions and implementation capacity are weakest, and where results
are hardest to produce on any margin. Under that reading TC intensity is
a marker of a difficult context — fragile institutions, post-crisis
settings, administrations unable to absorb project aid directly — not a
harmful modality. This selection story is consistent with every feature
of the results: the negative sign, the directional stability under
stronger controls (conditioning on observable difficulty does not remove
unobservable difficulty), and the failure of the permutation test to
shrink the estimate (reassigning real portfolios preserves the
indication mapping). We therefore do not interpret the TC coefficient as
evidence that technical cooperation reduces growth.

Alternative hypotheses, explicitly labeled as such, remain open: TC may
substitute for — rather than build — local capacity when external experts
perform functions that would otherwise have to be staffed domestically;
TC-heavy portfolios may reflect implementation difficulty that project
aid would have handled no better; and the modality-D measure itself is a
narrow slice of total technical-cooperation intensity. The lead-placebo
and pseudo-outcome tests bound mechanical explanations but cannot
eliminate selection. The honest summary is that the association is
detectable, directionally stable, unusually extreme relative to
randomized within-year compositions — and imprecise, non-causal, and
vulnerable to residual selection that no test here can close.

The other margins read the same way — informative, but selection-exposed.
The positive recipient-government-channel association is consistent with
the capacity/fiscal-integration hypothesis that channeling aid through
domestic systems accompanies better medium-run outcomes — and equally
consistent with reverse selection, in which donors entrust government
systems only where capacity already exists. The strongly negative
administrative/refugee/awareness share is near-mechanical: that category
substantially records in-donor costs, so a larger share literally means a
smaller fraction of the nominal total ever reaches the recipient
economy. Both results sharpen the measurement point — architecture
shares correlate with outcomes in interpretable directions — without
crossing into causal reading.

### 6.4 What the measurement implies for the aid literature

Three measurement implications follow. First, aid-volume studies
implicitly mask architecture: the same regressor — ODA per capita —
averages across portfolios whose composition varies systematically, so
heterogeneous associations are compressed into a single fragile
coefficient; this may be one source of the well-documented fragility of
the aggregate aid–growth literature. Second, donor comparisons based
only on amounts are incomplete: donors differ in what they deliver, not
just how much, and amount-based scorecards cannot capture that margin.
Third, the gaps in the data themselves are findings: tying fields are
incompletely reported, supplier-country procurement data cannot measure
local economic participation, and TC value embedded in projects is only
partially observed. Future CRS and procurement reporting that closes
these gaps would improve every downstream analysis of this kind — and
the architecture stack makes the value of such closing concrete: each
unmeasured margin is a dimension on which two identical aid totals may
still differ.

### 6.5 Procurement and local participation remain a partial layer

The exploratory procurement linkage illustrates both the promise and the
current limits of extending architecture measurement toward the
recipient economy. Supplier-country data cannot measure domestic value
added; subcontracting and reporting gaps are material; and the mergeable
sample is small. The linkage is therefore a proof of concept — the
architecture stack can be joined to local-participation outcomes once
reporting harmonizes — not evidence about how much aid value is retained
locally.

### 6.6 Implications for aid evaluation

Within these limits the policy implications are restrained but real.
Amount alone is an insufficient statistic for aid exposure, so
evaluation and comparison frameworks — including donor scorecards and
recipient-level aid monitoring — should track composition and delivery
structure explicitly alongside volumes. Reporting standards deserve as
much attention as totals: tying coverage, TC-within-project measurement,
and procurement/local-participation fields are exactly the dimensions
where better data would most change what can be learned. And because
architecture is jointly produced by donor supply and recipient context,
coherence agendas that push only donors or only recipients to change
will predictably under-deliver. For evaluation practice specifically,
the modest steps are the valuable ones: report composition shares
alongside totals in donor and recipient monitoring; treat modality and
channel as descriptors of the exposure, not footnotes to it; and build
portfolio comparisons — "same total, different architecture" — into
assessments that today compare only amounts. We deliberately do not
prescribe any specific reallocation — toward or away from technical
cooperation, budget support, or any channel — on the basis of this
associational evidence.

### 6.7 A research agenda for causal identification

The measurement stack is built to support a concrete causal agenda.
Candidate identification strategies exploit changes in the rules of
delivery rather than changes in volume: donor-specific procurement or
untying reforms that shift the tied share at roughly fixed totals;
modality rule changes — the introduction or reform of budget-support
instruments, or reclassifications of TC activities — that move aid-type
shares discontinuously; staggered adoption of Paris/Busan-era
commitments across donors, which supplies difference-in-differences
variation in channel and modality shares; and donor policy shocks
(agency reorganizations, mandate changes) that alter delivery models
exogenously to recipient conditions. A complementary route runs through
recipients: decentralization, public-finance, or civil-service reforms
that change a recipient's ability to host particular modalities would
shift the recipient side of the decomposition and could instrument the
jointly produced margin from the other direction.

Each of these designs has the same shape: find a shock that moves the
composition at approximately fixed volume, verify the first stage on the
architecture shares themselves, and only then interpret the outcome
equation. What these designs require — and what this paper supplies — is
a consistent, comprehensive measurement of the architecture margin at
the donor–recipient–year level, so that a reform's first-stage effect on
composition can be estimated before any outcome equation is run. The
decomposition also tells researchers where to look: margins with large
donor increments are the margins donor-side reforms can actually move.

### 6.8 Limitations

The limitations are first-order and worth restating compactly. The
outcome associations are conditional correlations exposed to
time-varying unobserved selection; the TC measure is a narrow modality,
not total technical-cooperation intensity; tying fields are incompletely
reported; the procurement layer covers only a small, recent-biased
sample; the architecture margins are correlated with each other, so
single-margin coefficients share interpretation risk; and CRS covers
reported ODA only, so the architecture of non-DAC and non-reporting
flows — a growing share of the landscape — is outside the frame. None of
these undermines the measurement contribution, which stands
independently of the outcome layer; all of them discipline how far the
outcome layer can be read.

### 6.9 Interpretation tools, not policy calculators

The dashboard-ready scenario exports deserve explicit framing. They let
a user compare fixed-total-aid portfolio reallocations — holding total
aid constant and moving share points between architecture categories —
under the model's associational coefficients. They are interpretation
tools for the compositional logic of the estimates: they make concrete
what a reallocation contrast means and where its uncertainty lies. They
are not policy calculators, do not rank donors, and inherit every
caveat of the underlying adjusted associations — including support
limits (scenarios outside the observed support are flagged) and
imprecision.

## 7. Conclusion

This paper set out to measure something the aid literature has long
treated as background noise: the architecture through which assistance
is delivered. Using the full OECD Creditor Reporting System, we
constructed a disbursement-weighted donor–recipient–year panel of aid
architecture — aid type, delivery channel, financial instrument, and
tying status — merged with demographic and outcome data for 141
recipient countries over 1995–2024.

Three findings stand out. First, architecture is measurable and it
varies systematically: the differences across donors in channel,
modality, and tying composition are large and persistent, and donor
identity adds 13–28 percentage points of explained variance over a
recipient-and-year baseline on the major margins. Second, architecture
is jointly produced: for project-type shares the recipient dimension
contributes comparably to the donor dimension, so the portfolio a
recipient faces reflects both who supplies the aid and what the
recipient can absorb and negotiate. Third, at comparable total aid,
composition-weighted associations with medium-run outcomes are
detectable — most visibly the negative technical-cooperation-share
association — but they are imprecise, compositional, and non-causal,
with confounding by indication the leading untested explanation.

The paper does not establish that any modality, channel, or tying
practice causes better or worse development outcomes, and it does not
rank donors or prescribe reallocations. The falsification suite narrows
mechanical explanations without closing selection, and the narrowness
of some measurement fields — tying coverage, TC embedded in projects —
marks where the data, not the design, bind hardest.

What it changes for aid research is the unit of description: evaluation
should distinguish the amount transferred from the structure through
which that amount is delivered. The measurement framework, the
decomposition, and the falsification discipline demonstrated here make
that distinction operational on the largest available evidence base.
Until the field adopts it, the architecture that recipients actually
experience will remain inside the residual of every aid–volume
regression.

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
10. Doucouliagos & Paldam. The Aid Effectiveness Literature - The Sad Result of 40 Years of Research. Journal of Economic Surveys. 2009. doi:10.2139/ssrn.1147611
11. Galiani et al.. The Effect of Aid on Growth: Evidence from a Quasi-Experiment. Journal of Economic Growth. 2017. doi:10.1007/s10887-016-9137-4
12. Alesina & Dollar. Who Gives Foreign Aid to Whom and Why?. Journal of Economic Growth. 2000. doi:10.1023/a:1009874203400
13. Kilby & Dreher. The Impact of Aid on Growth Revisited: Do Donor Motives Matter?. Economics Letters. 2010. doi:10.1016/j.econlet.2010.02.015
14. Feeny & McGillivray. What Determines Bilateral Aid Allocations? Evidence From Time Series Data. Review of Development Economics. 2008. doi:10.1111/j.1467-9361.2008.00443.x
15. Berthelemy & Tichit. Bilateral donors' aid allocation decisions—a three-dimensional panel analysis. International Review of Economics &amp; Finance. 2004. doi:10.1016/j.iref.2003.11.004
16. Greenhill, Priolo & Ward. Donor Transparency and Aid Allocation. Political Studies. 2013. doi:10.2139/ssrn.1644704
17. Dreher & Fuchs. Rogue Aid? The Determinants of China's Aid Allocation. Canadian Journal of Economics. 2015. doi:10.2139/ssrn.1932086
18. Fuchs & Vadlamannati. The Needy Donor: An Empirical Analysis of India’s Aid Motives. World Development. 2013. doi:10.2139/ssrn.2140949
19. Boone. Politics and the Effectiveness of Foreign Aid. European Economic Review. 1996. doi:10.1016/0014-2921(95)00127-1
20. Feyzioglu, Swaroop & Zhu. A Panel Data Analysis of the Fungibility of Foreign Aid. World Bank Economic Review. 1998. doi:10.1093/wber/12.1.29
21. Devarajan & Swaroop. The Implications of Foreign Aid Fungibility for Development Assistance. World Bank Policy Research Working Paper 2022. 1998. doi:10.1596/1813-9450-2022
22. Pettersson. Foreign sectoral aid fungibility, growth and poverty reduction. Journal of International Development. 2007. doi:10.1002/jid.1378
23. Dreher, Nunnenkamp & Thiele. Does Aid for Education Educate Children? Evidence from Panel Data. World Bank Economic Review. 2008. doi:10.1596/4481
24. Easterly & Pfutze. Where Does the Money Go? Best and Worst Practices in Foreign Aid. Journal of Economic Perspectives. 2008. doi:10.1257/jep.22.2.29
25. Clay, Geddes & Natali. Untying Aid: Is it Working? An Evaluation of the Implementation of the Paris Declaration and of the 2001 DAC Recommendation on Untying ODA to the LDCs. Danish Institute for International Studies (DIIS) report. 2009.
26. Jepma. Aid Tying: Trade and Resource Allocation Effects. The Economics of Aid (Jepma, ed., Routledge). 1991.
27. Morrissey & White. EVALUATING THE CONCESSIONALITY OF TIED AID*. The Manchester School. 1996. doi:10.1111/j.1467-9957.1996.tb00481.x
28. Wagner. Aid and the Dutch disease: Macroeconomic management when everybody loves you. World Development. 2014. doi:10.1016/0305-750x(92)90016-o
29. Rajan & Subramanian. Aid, Dutch disease, and manufacturing growth. Journal of Development Economics. 2011. doi:10.1016/j.jdeveco.2009.12.004
30. Bulir & Hamann. Volatility of Development Aid: From the Frying Pan into the Fire?. World Development. 2008. doi:10.1016/j.worlddev.2007.02.019
31. Knack. Aid Dependence and the Quality of Governance: Cross-Country Empirical Tests. Southern Economic Journal. 2001. doi:10.2307/1061596
32. Brautigam & Knack. Foreign Aid, Institutions, and Governance in Sub‐Saharan Africa. Economic Development and Cultural Change. 2004. doi:10.1086/380592
33. Fukuda-Parr, Lopes & Malik. Capacity for Development: New Solutions to Old Problems. Earthscan/UNDP (eds. Fukuda-Parr, Lopes, Malik). 2002.
34. Kenny. What Is Effective Aid? How Would Donors Allocate It?. European Journal of Development Research. 2008. doi:10.1080/09578810802078704
35. Temple. Aid and Conditionality. Handbook of Development Economics. 2010. doi:10.1016/b978-0-444-52944-2.00005-7
36. Bourguignon & Sundberg. Aid Effectiveness—Opening the Black Box. American Economic Review. 2007. doi:10.1257/aer.97.2.316
37. Gehring et al.. China's Global Finance Footprint 2005–2014: Comparing AidData and CGIT. Australian Economic Review. 2017.
38. Nowak-Lehmann et al.. Does Aid Promote Donor Exports? Commercial Interest versus Instrumental Philanthropy. Kyklos. 2014. doi:10.1111/kykl.12068

## Tables

Table 1. Sample and architecture summary (disbursement-weighted shares, pooled).
Table 2. Variance decomposition of architecture shares (incremental R² of donor and recipient fixed effects).
Table 3. Technical-cooperation-share coefficients by lag window (β; country-clustered SE in parentheses; compositional contrast vs omitted aid-type composition).
Table 4. Falsification suite summary.

## Figures

Figure 1. Disbursement-weighted aid-type and channel shares over time.
Figure 2. Aid-architecture shares of the top-20 donors by ODA volume (descriptive; no quality ranking implied).
Figure 3. Technical-cooperation-share coefficients by outcome window after exposure year (compositional contrast vs omitted aid-type composition; whiskers are 95% CI).
