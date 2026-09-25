"""Phase 5: procurement structure panel from World Bank procurement notices.

Input : data/raw/wb_procurement/procnotices_*.json (PARTIAL ~30k of ~420k notices)
Output: data/processed/procurement_contract_level.csv
        data/processed/procurement_recipient_year.csv
        results/audits/PHASE_5_PROCUREMENT_PANEL.md

Contract Award notices are parsed for awarded-bidder country and signed
contract price. Local share = signed price where bidder country == project
country / total signed price, aggregated to recipient x award year.
Only usable as a recent-period, illustrative panel (see audit).
"""
import json, glob, re, os, pandas as pd, numpy as np

os.makedirs("data/processed", exist_ok=True)
files = sorted(glob.glob("data/raw/wb_procurement/*.json"))

COUNTRY_RE = re.compile(r"Country:\s*([^<]+)<")
PRICE_RE = re.compile(r"Signed Contract price\s*<br/>\s*USD\s*([\d,.]+)")
BIDDER_RE = re.compile(r"<b>([^<]+)\s*\(\d+\)</b>")

rows = []
for f in files:
    d = json.load(open(f))
    for n in d.get("procnotices", []):
        if n.get("notice_type") != "Contract Award":
            continue
        t = n.get("notice_text") or ""
        # award date: noticedate fallback award year from submission_date
        year = None
        m = re.search(r"(\d{4})/(\d{2})/(\d{2})", t)
        if m: year = int(m.group(1))
        if year is None:
            sd = n.get("submission_date") or ""
            if sd[:4].isdigit(): year = int(sd[:4])
        bidders = COUNTRY_RE.findall(t)
        prices = PRICE_RE.findall(t)
        bnames = BIDDER_RE.findall(t)
        # pairwise assign: take signed price block(s)
        for i, bc in enumerate(bidders):
            rows.append({
                "notice_id": n.get("id"),
                "project_id": n.get("project_id"),
                "project_ctry_name": n.get("project_ctry_name"),
                "award_year": year,
                "bidder": bnames[i].strip() if i < len(bnames) else None,
                "bidder_country": bc.strip(),
                "signed_price_usd": float(prices[i].replace(",", "")) if i < len(prices) else np.nan,
                "procurement_group": n.get("procurement_group"),
                "procurement_method": n.get("procurement_method_name"),
                "loan_info": (re.search(r"Loan/Credit/TF Info:</b>([^<]+)<", t) or [None, None])[1] if re.search(r"Loan/Credit/TF Info:</b>([^<]+)<", t) else None,
            })

cl = pd.DataFrame(rows)
print("contract-awards with bidder:", len(cl))
cl.to_csv("data/processed/procurement_contract_level.csv", index=False)

cl["local"] = (cl.bidder_country.str.upper() == cl.project_ctry_name.str.upper()).astype(float)
ry = (cl.dropna(subset=["award_year","signed_price_usd"])
        .groupby(["project_ctry_name","award_year"])
        .apply(lambda g: pd.Series({
            "local_procurement_share": np.average(g.local, weights=g.signed_price_usd),
            "local_procurement_share_count": g.local.mean(),
            "n_awards": len(g),
            "total_award_usd": g.signed_price_usd.sum()}), include_groups=False)
        .reset_index().rename(columns={"project_ctry_name":"recipient_name","award_year":"year"}))
ry.to_csv("data/processed/procurement_recipient_year.csv", index=False)
print("recipient-year:", ry.shape)

lines = ["# PHASE 5 — Procurement panel","",
 f"- Source files: {len(files)} pages of notices (~{len(files)*500:,} notices; total available 420,382 — PARTIAL, recent-biased)",
 f"- Contract Award notices parsed: {len(cl):,}",
 f"- With signed price: {cl.signed_price_usd.notna().sum():,}",
 f"- Recipient-year rows: {len(ry):,}, years {int(ry.year.min())}-{int(ry.year.max())}",
 f"- Mean local share (value-weighted): {ry.local_procurement_share.mean():.3f}","",
 "LIMITATION: page download stopped early; coverage skews to the most recent notices. Used for descriptive/robustness only."]
open("results/audits/PHASE_5_PROCUREMENT_PANEL.md","w").write("\n".join(lines))
print("done")
