import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "01_risk" / "exports" / "risk_assessment.csv"

def main():
    with CSV_PATH.open("r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        required = {"No.", "CATEGORY", "RISK STATEMENT"}
        missing = required - set(reader.fieldnames or [])
        if missing:
            raise SystemExit(f"Missing required columns: {sorted(missing)}")
        seen = set()
        for i, row in enumerate(reader, start=1):
            no = (row.get("No.") or "").strip()
            if no and no in seen:
                raise SystemExit(f"Duplicate No. {no}")
            if no:
                seen.add(no)
        print(f"Validated {i} rows.")
if __name__ == "__main__":
    main()
