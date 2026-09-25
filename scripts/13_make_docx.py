"""Build inline-figures manuscript docx from manuscript_draft.md.

Citations [n] rendered as font-superscript runs (per house rule, no unicode
superscripts). Figures embedded inline with captions.
"""
import re, os
from docx import Document
from docx.shared import Inches, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH

MD = "manuscript/manuscript_draft.md"
OUT = "manuscript/manuscript_inline_revised.docx"
OUT_BLIND = "manuscript/manuscript_blinded_revised.docx"

FIGS = {
 "fig_architecture_trends.png": ("results/figures/fig_architecture_trends.png",
    "Figure 1. Disbursement-weighted aid-type and delivery-channel shares over time."),
 "fig_donor_architecture.png": ("results/figures/fig_donor_architecture.png",
    "Figure 2. Aid-architecture profiles of the top-20 donors by ODA volume."),
 "fig_oda_gdp_hist.png": ("results/figures/fig_oda_gdp_hist.png",
    "Figure 3. Distribution of ODA disbursements as a share of recipient GDP."),
 "fig_coef_tc_windows.png": ("results/figures/fig_coef_tc_windows.png",
    "Figure 4. Technical-cooperation-share coefficients by lag window."),
}

doc = Document()
st = doc.styles["Normal"]; st.font.name="Times New Roman"; st.font.size=Pt(11)

def add_rich(par, text):
    # [n,n,...] -> superscript
    for seg in re.split(r"(\[\d+(?:,\d+)*\])", text):
        m = re.match(r"\[(\d+(?:,\d+)*)\]", seg)
        if m:
            r = par.add_run(m.group(1)); r.font.superscript = True
        elif seg:
            # **bold** handling
            for b in re.split(r"(\*\*[^*]+\*\*)", seg):
                if b.startswith("**"):
                    r=par.add_run(b[2:-2]); r.bold=True
                elif b:
                    # *italic*
                    for it in re.split(r"(\*[^*]+\*)", b):
                        if it.startswith("*"):
                            r=par.add_run(it[1:-1]); r.italic=True
                        elif it:
                            par.add_run(it)

lines = open(MD).read().split("\n")
in_refs = False
for ln in lines:
    s = ln.strip()
    if not s: continue
    if s.startswith("## References"):
        doc.add_heading("References", level=1); in_refs=True; continue
    if s.startswith("# "):
        doc.add_heading(s[2:], level=0); continue
    if s.startswith("## "):
        doc.add_heading(s[3:], level=1); continue
    if s.startswith("### "):
        doc.add_heading(s[4:], level=2); continue
    if s.startswith("- fig_"):
        fname = s.split(" ")[1].rstrip("—").strip().rstrip("—")
        continue
    if s.startswith("- ") and not in_refs:
        p=doc.add_paragraph(style="List Bullet"); add_rich(p, s[2:]); continue
    if in_refs and re.match(r"^\d+\.", s):
        doc.add_paragraph(s); continue
    p=doc.add_paragraph(); add_rich(p, s)

# inline figures at end with captions
doc.add_heading("Figures", level=1)
for f,(path,cap) in FIGS.items():
    if os.path.exists(path):
        doc.add_picture(path, width=Inches(5.8))
        doc.paragraphs[-1].alignment = WD_ALIGN_PARAGRAPH.CENTER
        doc.add_paragraph(cap)

doc.save(OUT)
print(OUT, os.path.getsize(OUT))
doc.save(OUT_BLIND)  # no author-identifying content present in draft
print(OUT_BLIND, os.path.getsize(OUT_BLIND))

# ---- supplement: key tables ----
import pandas as pd
sup = Document()
st = sup.styles["Normal"]; st.font.name="Times New Roman"; st.font.size=Pt(10)
sup.add_heading("Supplementary Materials — Beyond Aid Volume (revised)", level=0)

def add_table(title, df, cols=None, maxrows=None):
    sup.add_heading(title, level=2)
    if cols: df = df[cols]
    if maxrows: df = df.head(maxrows)
    df = df.round(4)
    t = sup.add_table(rows=1, cols=len(df.columns)); t.style="Table Grid"
    for j,c in enumerate(df.columns): t.rows[0].cells[j].text=str(c)
    for _,row in df.iterrows():
        cells=t.add_row().cells
        for j,v in enumerate(row): cells[j].text=str(v)

res = pd.read_csv("results/tables/model_coefficients_all.csv")
add_table("S1. Technical-cooperation share coefficients, all windows and outcomes",
    res[res.term=="share_aidtype_technical_cooperation"].sort_values(["xset","outcome","window"]),
    ["xset","term","outcome","window","beta","se","p","n"])
add_table("S2. Donor/recipient decomposition of architecture shares (incremental R²)",
    pd.read_csv("results/tables/donor_decomposition.csv"))
add_table("S3. Falsification suite",
    pd.read_csv("results/tables/falsification_results.csv"))
add_table("S4. Adjustment-set sensitivity (TC share)",
    pd.read_csv("results/tables/adjustment_stability.csv"))
add_table("S5. Canonical numbers",
    pd.read_csv("results/tables/canonical_numbers.csv"))
sup.save("manuscript/supplement_revised.docx")
print("manuscript/supplement_revised.docx", os.path.getsize("manuscript/supplement_revised.docx"))
