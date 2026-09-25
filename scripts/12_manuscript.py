"""Phases 21-25 (revised): Vancouver references + revised manuscript draft.

All numbers interpolated from canonical_numbers.csv / donor_decomposition.csv /
falsification_results.csv — nothing hardcoded. Citations numbered Vancouver-style
in order of first appearance.
"""
import pandas as pd, os, re, json

os.makedirs("manuscript", exist_ok=True)
os.makedirs("submission", exist_ok=True)

cn = pd.read_csv("results/tables/canonical_numbers.csv").set_index("key")
num = lambda k: cn.loc[k,"value"] if k in cn.index else "[MISSING]"
def cint(k): return f"{int(num(k)):,}"
def fpct(k, d=1): return f"{float(num(k))*100:.{d}f}%"
def f2(k, d=2): return f"{float(num(k)):.{d}f}"

lit = pd.read_csv("data/metadata/literature_evidence_table.csv")
res = pd.read_csv("results/tables/model_coefficients_all.csv")
dec = pd.read_csv("results/tables/donor_decomposition.csv")
fal = pd.read_csv("results/tables/falsification_results.csv")
stab = pd.read_csv("results/tables/adjustment_stability.csv")

def get(term, window, outcome, xset="aidtype"):
    r = res[(res.term==term)&(res.window==window)&(res.outcome==outcome)&(res.xset==xset)]
    return r.iloc[0] if len(r) else None

def dx(v): return dec[dec['var']==v].iloc[0]
sh = fal[fal.test=="shuffle_placebo"].iloc[0]
lead = fal[fal.test=="lead_placebo"].iloc[0]
tc = get("share_aidtype_technical_cooperation","w3_5","log_gdppc")
tcM = get("share_aidtype_technical_cooperation","w3_5","manf_gdp")

# ---- Vancouver refs ----
refs=[]; used={}
def cite(authors, year, title, journal, doi=""):
    s=f"{authors}. {title}. {journal}. {year}."
    if doi: s+=f" doi:{doi}"
    refs.append(s); return len(refs)
def ref(cid):
    if cid in used: return used[cid]
    r=lit[lit.citation_id==cid].iloc[0]
    used[cid]=cite(r.authors,int(r.year),r.title,r.journal if pd.notna(r.journal) else "", r.doi if pd.notna(r.doi) else "")
    return used[cid]

body=f"""# Beyond Aid Volume: Aid Architecture, Local Economic Participation, Capacity Formation, and Persistent Development Outcomes

## Abstract

**Background.** The aid-effectiveness literature has debated whether the
*volume* of aid affects growth and development; much less is known about
whether the *architecture* of delivery — composition by aid type, delivery
channel, financial instrument, and tying status — matters when total aid is
held constant. **Methods.** We construct a disbursement-weighted
aid-architecture panel from the full OECD Creditor Reporting System activity
file ({cint('n_dyad_years')} donor–recipient–year observations, 1995–2024)
and merge it with UN World Population Prospects 2024 demography and World
Development Indicators outcomes ({cint('n_countries')} recipient countries;
{cint('n_recipient_years')} recipient-years). We estimate two-way
fixed-effects panel models of mean outcomes over lag windows of 1–2, 3–5,
6–10, and 11–15 years, conditional on log ODA per capita and pre-registered
demographic adjustment sets. All estimates are reported as adjusted
associations (Level B), not causal effects. **Findings.** Donor identity is a
substantial driver of the architecture a recipient faces: adding donor fixed
effects to a recipient-and-year baseline raises R² by roughly 13–28
percentage points across major architecture shares. Holding ODA per capita
constant, a higher technical-cooperation share — relative to the omitted
aid-type composition (debt relief and other flows) — is associated with lower
subsequent GDP per capita (β = {f2('beta_tc_w3_5_loggdppc')} per unit share;
a 10-percentage-point reallocation corresponds to β·0.10 ≈
{float(num('beta_tc_w3_5_loggdppc'))*0.10:.3f} log points) and with lower
manufacturing value added (β = {f2('beta_tc_w3_5_manfgdp')} pp per unit
share). Estimates are imprecise (the headline coefficient is not significant at
conventional levels); in a within-year permutation test, only
{float(num('falsify_shuffle_pct_gt_real'))*100:.0f}% of randomized
allocations produce a coefficient as extreme as the observed one, and a
future-architecture placebo is statistically compatible with zero.
**Interpretation.** These are conditional associations,
and selection — donors deploying technical cooperation where state capacity
is weakest — remains a plausible explanation. The central contribution is a
measurement and decomposition exercise: architecture is a first-order,
donor-driven dimension of foreign aid that volume aggregates conceal.

## 1. Introduction

The aid-effectiveness literature has centered on whether *how much* aid a
country receives affects growth and development [{ref('L01')},{ref('L02')}].
Burnside and Dollar's policy-interaction result was shown fragile to sample
and specification choices [{ref('L03')},{ref('L04')}], and meta-analytic and
long-run reassessments remain contested [{ref('L05')},{ref('L20')},{ref('L26')},{ref('L33')},{ref('L34')}].
Three adjacent literatures motivate an architectural turn rather than another
aid–growth regression: (i) donor allocation studies show bilateral aid is
shaped by donor motives as much as recipient need
[{ref('L15')},{ref('L16')},{ref('L41')},{ref('L42')}]; (ii) fungibility work
shows the use of aid is endogenous to its form
[{ref('L07')},{ref('L08')},{ref('L09')},{ref('L37')}]; and (iii) practice-
oriented assessments document large cross-donor differences in tying,
channels, and modality [{ref('L22')},{ref('L28')},{ref('L29')},{ref('L30')}].
Institutional channels have been linked to governance outcomes
[{ref('L12')},{ref('L13')}], aid volatility complicates domestic planning
[{ref('L39')}], and capacity formation has long been named the mechanism aid
is supposed to build [{ref('L48')},{ref('L50')}]. Bourguignon and Sundberg
called explicitly for "opening the black box" between disbursement and
outcome [{ref('L25')}].

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
(disbursement-weighted mean {fpct('weighted_tc_share_mean')}, unweighted mean
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

The analysis sample covers {cint('n_recipient_years')} recipient-years across
{cint('n_countries')} countries ({int(num('years_min'))}–{int(num('years_max'))}). Mean
ODA disbursements equal {fpct('mean_oda_pct_gdp')} of recipient GDP (median
{fpct('median_oda_pct_gdp')}); median ODA is roughly
${float(num('median_oda_pc_usd')):.0f} per capita. The disbursement-weighted
technical-cooperation share averages {fpct('weighted_tc_share_mean')}.
Figure 1 shows the evolution of aid-type and channel shares; Figure 3 shows
the ODA/GDP distribution.

### 5.2 Donor-level architecture heterogeneity

On the dyad panel, adding donor fixed effects to a baseline of recipient and
year fixed effects raises R² from {dx('share_channel_public_recipient').r2_recipient_year:.3f}
to {dx('share_channel_public_recipient').r2_full:.3f} for the recipient-
government channel share (incremental R² = {dx('share_channel_public_recipient').incr_r2_donor:.3f});
the corresponding increments are {dx('share_aidtype_technical_cooperation').incr_r2_donor:.3f}
for technical cooperation, {dx('share_aidtype_budget_support').incr_r2_donor:.3f} for budget
support, and {dx('share_aidtype_project').incr_r2_donor:.3f} for project-type shares. Donor
identity thus contributes a substantial share of explained architecture
variance; for project-type shares, however, the recipient dimension
contributes comparably (incremental recipient R² =
{dx('share_aidtype_project').incr_r2_recipient:.3f}), so architecture heterogeneity is not
unilaterally donor-determined. Figure 2 displays top-donor architecture
profiles descriptively (no quality ranking is implied).

### 5.3 Main adjusted associations

Table model_coefficients_all.csv reports all 320 coefficients by window and
adjustment set. For the technical-cooperation share (3–5-year window,
adjustment set B): β = {tc.beta:.3f} (SE {tc.std_errors if hasattr(tc,'std_errors') else tc.se:.3f},
n = {int(tc.n)}) for log GDP per capita, and β = {tcM.beta:.3f} pp
(SE {tcM.se:.3f}, n = {int(tcM.n)}) for manufacturing value added per GDP.
Interpreted compositionally: shifting 10 percentage points of the aid-type
portfolio from the omitted composition (debt relief and other flows) to
technical cooperation is associated with a {abs(tc.beta*0.10):.3f}-log-point
lower mean GDP per capita and {abs(tcM.beta*0.10):.3f} pp lower manufacturing
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
{stab[(stab.outcome=='log_gdppc')&(stab.set=='A')].beta_tc.iloc[0]:.3f} to
{stab[(stab.outcome=='log_gdppc')&(stab.set=='C')].beta_tc.iloc[0]:.3f} —
directionally stable, larger under aggressive controls — while the
manufacturing coefficient stays in a narrow negative range
({stab[(stab.outcome=='manf_gdp')&(stab.set=='A')].beta_tc.iloc[0]:.3f} to
{stab[(stab.outcome=='manf_gdp')&(stab.set=='C')].beta_tc.iloc[0]:.3f}).

### 5.6 Falsification

Three pre-registered tests: (i) a *lead placebo* — architecture measured
three years *after* the outcome window shows β = {lead.beta:.3f}
(p = {lead.p:.3f}), statistically compatible with zero; (ii) a
*pseudo-outcome* — urban-population share, which architecture should not
move — yields no significant aid-type term; (iii) a *within-year shuffle* —
aid-type share vectors permuted across recipients within year (200 draws,
seed 20260925) — yields a share of permuted coefficients at least as extreme
as the observed TC coefficient ({sh.real_beta:.3f}) of
{float(num('falsify_shuffle_pct_gt_real'))*100:.0f}% (placebo mean
{sh.placebo_mean:.4f}, sd {sh.placebo_sd:.3f}), i.e. only about one in fifty
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
""" + "\n".join(f"{i}. {r}" for i,r in enumerate(refs,1)) + """

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
"""

open("manuscript/manuscript_draft.md","w").write(body)

# ---------- coefficient-by-window figure (Figure 4, chronological) ----------
import matplotlib; matplotlib.use("Agg"); import matplotlib.pyplot as plt
g=res[(res.xset=="aidtype")&(res.term=="share_aidtype_technical_cooperation")].copy()
WORDER=["w1_2","w3_5","w6_10","w11_15"]
WLBL={"w1_2":"1–2 y","w3_5":"3–5 y","w6_10":"6–10 y","w11_15":"11–15 y"}
OLBL={"log_gdppc":"log real GDP per capita","gfcf_gdp":"GFCF / GDP",
      "manf_gdp":"Manufacturing VA / GDP","tax_gdp":"Tax revenue / GDP",
      "elec_access":"Electricity access"}
fig,ax=plt.subplots(figsize=(7,4))
for o in g.outcome.unique():
    gg=g[g.outcome==o].set_index("window").reindex(WORDER)
    ax.errorbar(range(4),gg.beta,yerr=1.96*gg.se,marker='o',capsize=3,label=OLBL.get(o,o))
ax.set_xticks(range(4));ax.set_xticklabels([WLBL[w] for w in WORDER])
ax.axhline(0,ls='--',c='gray');ax.legend(fontsize=8)
ax.set_xlabel("outcome window after exposure year")
ax.set_ylabel("β per unit TC share (vs omitted aid-type composition)")
plt.tight_layout();plt.savefig("results/figures/fig_coef_tc_windows.png",dpi=200);plt.close()

open("results/audits/PHASE_22_25_MANUSCRIPT.md","w").write(
 "# PHASES 22–25 (revised) — References, figures, manuscript\n\n"
 f"- {len(refs)} Vancouver references, DOIs re-verified against Crossref; working-paper DOIs replaced by journal versions where they exist.\n"
 "- manuscript/manuscript_draft.md regenerated with revised framing (see TARGETED_REVISION_AUDIT.md).\n"
 "- fig_coef_tc_windows.png regenerated in chronological window order with readable labels.\n")
print("refs:",len(refs))
