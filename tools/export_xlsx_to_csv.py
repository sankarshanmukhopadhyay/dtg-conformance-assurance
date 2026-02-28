import csv
from pathlib import Path
from openpyxl import load_workbook

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "01_risk" / "source" / "Risk Register.xlsx"
OUT = ROOT / "01_risk" / "exports" / "risk_assessment.csv"

CATEGORY_SHEETS_EXCLUDE = {"Explanation (using Gemini)", "Risk to Control Mapping"}

COLUMNS = [
    "Risk ID",
    "Category",
    "Risk Statement",
    "Cause",
    "Consequence",
    "Owner",
    "Likelihood",
    "Impact",
    "Inherent Risk",
    "Controls",
    "Residual Risk",
]

def main():
    wb = load_workbook(SRC, data_only=True)

    rows = []
    for name in wb.sheetnames:
        if name in CATEGORY_SHEETS_EXCLUDE:
            continue
        ws = wb[name]
        header = [c.value for c in ws[1]]
        idx = {h: i for i, h in enumerate(header) if h}

        for r in ws.iter_rows(min_row=2, values_only=True):
            if not any(v is not None and str(v).strip() != "" for v in r):
                continue
            row = {h: (r[i] if i < len(r) else None) for h, i in idx.items()}
            row["Category"] = name
            rows.append(row)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS)
        w.writeheader()
        for row in rows:
            out = {k: (row.get(k) if row.get(k) is not None else "") for k in COLUMNS}
            w.writerow(out)

    print(f"Wrote {OUT} ({len(rows)} risks).")

if __name__ == "__main__":
    main()
