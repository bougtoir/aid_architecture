"""Verify every cited reference against Crossref by DOI; flag mismatches."""
import pandas as pd, urllib.request, urllib.parse, json, time, re

lit = pd.read_csv("data/metadata/literature_evidence_table.csv")
# extract cited refs from manuscript (numbered list)
md = open("manuscript/manuscript_draft.md").read()
refs_sec = md.split("## References")[1].split("## Figures")[0]
entries = re.findall(r"^\d+\.\s(.+?)\.\s(.+?)\.\s(\d{4})\.\s*(?:doi:(\S+))?", refs_sec, re.M)
print("parsed refs:", len(entries))

def crossref(doi):
    u = "https://api.crossref.org/works/" + urllib.parse.quote(doi)
    try:
        d = json.load(urllib.request.urlopen(u, timeout=20))["message"]
        return {"title": (d.get("title") or [""])[0],
                "journal": (d.get("container-title") or [""])[0],
                "year": (d.get("published-print") or d.get("issued",{})).get("date-parts",[[None]])[0][0],
                "type": d.get("type"),
                "authors": "; ".join(f"{a.get('family','')}, {a.get('given','')[:1]}" for a in d.get("author",[]))}
    except Exception as e:
        return {"error": str(e)}

rows=[]
for auth,title,year,doi in entries:
    r = crossref(doi) if doi else {"error":"no DOI"}
    rows.append({"ms_authors":auth,"ms_title":title,"ms_journal":"","ms_year":year,"doi":doi,**r})
    time.sleep(0.3)
out=pd.DataFrame(rows)

def norm(s): return re.sub(r"[^a-z0-9]","",str(s).lower())
out["title_match"]=out.apply(lambda r: norm(r.ms_title)[:60] in norm(r.get("title","")) or norm(r.get("title",""))[:60] in norm(r.ms_title), axis=1)
out["year_match"]=out.apply(lambda r: str(r.ms_year)==str(r.get("year")), axis=1)
out.to_csv("results/audits/reference_verification.csv", index=False)
print(out[["ms_title","title","journal","year","type","title_match","year_match","error"]].to_string(max_colwidth=40))
