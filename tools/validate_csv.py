import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "01_risk" / "exports" / "risk_assessment.csv"

REQUIRED = {
    "Risk ID",
    "Category",
    "Risk Statement",
    "Likelihood",
    "Impact",
    "Inherent Risk",
    "Controls",
    "Residual Risk",
}

def main():
    with CSV_PATH.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        fields = set(reader.fieldnames or [])
        missing = REQUIRED - fields
        if missing:
            raise SystemExit(f"Missing required columns: {sorted(missing)}")

        seen = set()
        n = 0
        for row in reader:
            n += 1
            rid = (row.get("Risk ID") or "").strip()
            if not rid:
                raise SystemExit(f"Row {n}: missing Risk ID")
            if rid in seen:
                raise SystemExit(f"Duplicate Risk ID: {rid}")
            seen.add(rid)

        print(f"Validated {n} risks with required columns.")

if __name__ == "__main__":
    main()
