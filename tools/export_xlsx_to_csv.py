import csv
from pathlib import Path
from openpyxl import load_workbook

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "01_risk" / "source" / "DTG_WG_Risk_Assessment_Worksheet_Populated_From_WIP.xlsx"
OUT = ROOT / "01_risk" / "exports" / "risk_assessment.csv"

def main():
    wb = load_workbook(SRC)
    ws = wb["Risk Assessment Worksheet"] if "Risk Assessment Worksheet" in wb.sheetnames else wb.active
    header_row = 4 if ws.max_row >= 4 else 1
    headers = [c.value for c in ws[header_row]]
    while headers and (headers[-1] is None or str(headers[-1]).strip()==""):
        headers.pop()

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with OUT.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(headers)
        for r in ws.iter_rows(min_row=header_row+1, values_only=True):
            if not any(v is not None and str(v).strip() != "" for v in r):
                continue
            w.writerow(list(r[:len(headers)]))
    print(f"Wrote {OUT}")

if __name__ == "__main__":
    main()
