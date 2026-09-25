"""Phase 3: reproducible raw-data acquisition.
Every file lands under data/raw/<source>/ and is registered in
data/metadata/<source>_manifest.csv with sha256 + retrieval metadata.
Raw files are never edited or overwritten (existing sha256 is kept).
"""
import csv, hashlib, json, os, sys, time, urllib.request, urllib.parse, zipfile, io

RAW = "data/raw"
META = "data/metadata"
UA = {'User-Agent': 'Mozilla/5.0 (academic reproducibility; contact via GitHub)'}

os.makedirs(META, exist_ok=True)

def sha256(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(1 << 20), b''):
            h.update(chunk)
    return h.hexdigest()

def manifest(source):
    p = os.path.join(META, f"{source}_manifest.csv")
    if not os.path.exists(p):
        with open(p, 'w', newline='') as f:
            csv.writer(f).writerow(["file","url","retrieved_utc","bytes","sha256","license_note","notes"])
    return p

def record(source, path, url, license_note, notes=""):
    row = [os.path.basename(path), url, time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
           os.path.getsize(path), sha256(path), license_note, notes]
    with open(manifest(source), 'a', newline='') as f:
        csv.writer(f).writerow(row)
    print("  saved", path, row[3], "bytes")

def fetch(url, dest, source, license_note, notes="", skip_existing=True):
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    if skip_existing and os.path.exists(dest) and os.path.getsize(dest) > 0:
        print("  exists, keeping:", dest)
        return dest
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=600) as r:
        with open(dest, 'wb') as f:
            while True:
                b = r.read(1 << 20)
                if not b: break
                f.write(b)
    record(source, dest, url, license_note, notes)
    return dest

OECD_LIC = "OECD terms of use (oecd.org/termsandconditions)"
WDI_LIC = "CC-BY-4.0 (World Bank)"
UN_LIC = "UN terms of use"
AIDDATA_LIC = "AidData terms (aiddata.org)"
WB_LIC = "World Bank terms of use"

# ---------- OECD DAC tables + CRS bulk ----------
oecd = [
 ("DSD_DAC2/Table2a_Data.zip",   "oecd_dac", "DAC2a bilateral ODA disbursements donor x recipient"),
 ("DSD_DAC2/Table3a_Data.zip",   "oecd_dac", "DAC3a ODA commitments donor x recipient"),
 ("DSD_DAC2/TotalOfficial_Data.zip","oecd_dac", "DAC2 total official flows donor x recipient"),
 ("DSD_DAC2/TotalODF_Data.zip",  "oecd_dac", "Total ODF donor x recipient"),
 ("DSD_DAC2/TotalReceipts_Data.zip","oecd_dac","Recipient receipts donor x recipient"),
 ("DSD_DAC1/Table1_Data.zip",    "oecd_dac", "DAC1 flows by provider"),
 ("DSD_DAC1/Table5_Data.zip",    "oecd_dac", "DAC5 ODA by sector and provider"),
]
for rel, src, note in oecd:
    url = "https://webfs-dcd.oecd.org/files/dotStat/" + urllib.parse.quote(rel)
    dest = f"{RAW}/{src}/{os.path.basename(url)}"
    try:
        fetch(url, dest, src, OECD_LIC, note)
    except Exception as e:
        print("FAIL", url, e)

# CRS reduced parquet (all years, code columns only)
try:
    fetch("https://webfs-dcd.oecd.org/files/dotStat/DSD_CRS/CRS-reduced.parquet",
          f"{RAW}/oecd_crs/CRS-reduced.parquet", "oecd_crs", OECD_LIC,
          "Full CRS activity-level, all years, code columns")
except Exception as e:
    print("FAIL CRS parquet", e)

# CRS codebook + codelists + deflators
try:
    fetch("https://webfs.oecd.org/oda/DataCollection/Resources/DAC-CRS-CODES.xlsx",
          f"{RAW}/oecd_crs/DAC-CRS-CODES.xlsx", "oecd_crs", OECD_LIC, "CRS codelists")
    fetch("https://webfs.oecd.org/oda/DataCollection/Resources/Deflators-base-2024.xlsx",
          f"{RAW}/oecd_dac/Deflators-base-2024.xlsx", "oecd_dac", OECD_LIC, "DAC deflators base 2024")
    fetch("https://webfs-dcd.oecd.org/files/dotStat/DSD_CRS/crs readme_en.txt",
          f"{RAW}/oecd_crs/crs_readme_en.txt", "oecd_crs", OECD_LIC, "CRS readme")
except Exception as e:
    print("FAIL resource", e)

# ---------- WDI ----------
wdi_ind = {
 "NY.GDP.PCAP.KD":"real_gdppc","NY.GDP.PCAP.KD.ZG":"gdppc_growth",
 "NE.GDI.FTOT.ZS":"gfcf_share_gdp","NV.IND.MANF.ZS":"manufacturing_va_share_gdp",
 "NE.GDI.TOTL.ZS":"gross_capital_formation_share","GC.TAX.TOTL.GD.ZS":"tax_revenue_share_gdp",
 "EG.ELC.ACCS.ZS":"electricity_access","SL.EMP.TOTL.SP.ZS":"employment_to_population",
 "NY.GDP.MKTP.KD":"real_gdp","NY.GNI.MKTP.CD":"gni_usd","NY.GNI.PCAP.CD":"gni_pc_usd",
 "SP.POP.TOTL":"pop_total","SP.URB.TOTL.IN.ZS":"urbanization_share",
 "DT.ODA.ODAT.GN.ZS":"oda_gni_received","DT.ODA.ODAT.PC.ZS":"oda_per_capita_usd",
 "NE.EXP.GNFS.ZS":"exports_share_gdp","BX.KLT.DINV.WD.GD.ZS":"fdi_share_gdp",
 "SP.POP.GROW":"pop_growth","SP.DYN.TFRT.IN":"fertility_wdi",
 "SP.POP.DPND":"dependency_ratio_wdi",
}
os.makedirs(f"{RAW}/wdi", exist_ok=True)
for ind, name in wdi_ind.items():
    url = (f"https://api.worldbank.org/v2/country/all/indicator/{ind}"
           "?format=json&per_page=20000&date=1960:2025")
    dest = f"{RAW}/wdi/{ind}.json"
    try:
        fetch(url, dest, "wdi", WDI_LIC, name)
        time.sleep(0.3)
    except Exception as e:
        print("FAIL WDI", ind, e)

# WDI country metadata (income, region)
try:
    fetch("https://api.worldbank.org/v2/country?format=json&per_page=400",
          f"{RAW}/wdi/country_metadata.json", "wdi", WDI_LIC, "country metadata")
except Exception as e:
    print("FAIL WDI meta", e)

# ---------- UN WPP ----------
wpp = [
 ("WPP2024_Demographic_Indicators_Medium.csv.gz","demographic indicators (pop, growth, TFR, dep ratios, urban)"),
 ("WPP2024_TotalPopulationBySex.csv.gz","total population by sex"),
]
for f, note in wpp:
    url = ("https://population.un.org/wpp/assets/Excel%20Files/1_Indicator%20(Standard)/CSV_FILES/" + f)
    try:
        fetch(url, f"{RAW}/un_wpp/{f}", "un_wpp", UN_LIC, note)
    except Exception as e:
        print("FAIL WPP", f, e)

# ---------- AidData ----------
try:
    fetch("https://github.com/AidData-WM/public_datasets/releases/download/v3.1/AidDataCore_ResearchRelease_Level1_v3.1.zip",
          f"{RAW}/aiddata/AidDataCore_ResearchRelease_Level1_v3.1.zip", "aiddata", AIDDATA_LIC,
          "AidData Core Research Release v3.1 (1947-2013, project level)")
except Exception as e:
    print("FAIL AidData", e)

# ---------- WB procurement notices (partial, documented) ----------
os.makedirs(f"{RAW}/wb_procurement", exist_ok=True)
try:
    page, got, total = 1, 0, None
    while page <= 60:
        url = (f"https://search.worldbank.org/api/v2/procnotices?format=json&rows=500&os={got}"
               "&qterm=&proct=Contract%20Awards&submission_date_exact=&proc_no=&notice_type="
               "&srt=submission_date%20desc")
        req = urllib.request.Request(url, headers=UA)
        with urllib.request.urlopen(req, timeout=120) as r:
            d = json.load(r)
        total = d.get('total', total)
        recs = d.get('procnotices', [])
        if not recs: break
        p = f"{RAW}/wb_procurement/procnotices_os{got}.json"
        with open(p, 'w') as f:
            json.dump(d, f)
        got += len(recs); page += 1
        time.sleep(0.4)
    record("wb_procurement", f"{RAW}/wb_procurement/procnotices_os0.json",
           "https://search.worldbank.org/api/v2/procnotices", WB_LIC,
           f"PARTIAL: {got} of {total} contract-award notices fetched (latest-first); ledger notes partial acquisition")
except Exception as e:
    print("FAIL WB proc", e)

print("Phase 3 download pass complete")
