# REFERENCE_VERIFICATION (targeted revision)

Method: every DOI in data/metadata/literature_evidence_table.csv queried
against api.crossref.org/works/{doi}; title/container/year compared.
Corrections applied in-place to the evidence table; manuscript Vancouver
numbering is generated from this table, so the references section reflects
all corrections automatically.

## Corrections applied (peer-reviewed journal versions preferred)

| cid | work | new DOI / source |
|-----|------|------------------|
| L01 | Burnside & Dollar, Aid Policies and Growth | AER 2000, 10.1257/aer.90.4.847 |
| L05 | Rajan & Subramanian | REStat 2008, 10.1162/rest.90.4.643 |
| L07 | Boone | EER 1996, 10.1016/0014-2921(95)00127-1 |
| L08 | Feyzioglu, Swaroop & Zhu | WBER 1998, 10.1093/wber/12.1.29 |
| L12 | Knack | SEJ 2001, 10.2307/1061596 |
| L15 | Alesina & Dollar | JoEG 2000, 10.1023/a:1009874203400 |
| L16 | Kilby & Dreher | Economics Letters 2010, 10.1016/j.econlet.2010.02.015 |
| L21 | Galiani, Knack, Xu & Zou | JoEG 2017, 10.1007/s10887-016-9137-4 |
| L22 | Easterly & Pfutze | JEP 2008, 10.1257/jep.22.2.29 |
| L26 | Minoiu & Reddy | QREF 2010, 10.1016/j.qref.2009.10.004 |
| L33 | Doucouliagos & Paldam | EJPE 2011, 10.1016/j.ejpoleco.2010.11.004 |
| L39 | Bulir & Hamann | World Development 2008, 10.1016/j.worlddev.2007.02.019 |
| L50 | Kenny | EJDR 2008, 10.1080/09578810802078704 |

## Correctly labeled grey literature / no journal DOI exists

| cid | item | disposition |
|-----|------|-------------|
| L02 | Burnside & Dollar 2004 "Revisiting the Evidence" | WP DOI 10.1596/1813-9450-3251; labeled Policy Research Working Paper (the WBER 2004 version is not indexed under a resolvable DOI in Crossref) |
| L09 | Devarajan & Swaroop fungibility implications | WB PRWP 2022, 10.1596/1813-9450-2022 |
| L28 | Clay, Geddes & Natali untying evaluation | DIIS report 2009 — no DOI; labeled as institute report |
| L29 | Jepma 1991 aid tying | Book chapter in *The Economics of Aid* (Routledge) — labeled as chapter |
| L48 | Fukuda-Parr, Lopes & Malik (eds), Capacity for Development | Earthscan/UNDP 2002 — no DOI; previous journal DOI removed |

## Notes
- scripts/14_verify_refs.py re-runnable; earlier cosmetic parse issues
  (journal merged into title; str-vs-float year compare) do not affect the
  evidence table itself.
- All remaining DOIs resolve to the cited work.
