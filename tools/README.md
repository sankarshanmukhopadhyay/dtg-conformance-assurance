# Tools

This folder contains lightweight utilities to keep the repo **diff-friendly** and **machine-readable**.

## 1) Export the risk register (XLSX → CSV)

Source: `risk/source/Risk Register.xlsx`  
Output: `risk/exports/risk_assessment.csv`

```bash
python tools/export_xlsx_to_csv.py
```

## 2) Validate the risk register export

```bash
python tools/validate_csv.py
```

This checks:
- required columns exist
- `Risk ID` values are present and unique

## 3) Validate other CSV artifacts (optional)

The control and evidence catalogs are intended to be simple CSVs that are easy to diff and integrate.

- `controls/control_catalog.csv`
- `controls/evidence_catalog.csv`
- `controls/test_suites.csv`

Suggested validation pattern:
- ensure stable headers (do not rename casually)
- keep IDs stable (`DCAS-CTRL-###`, `EV-###`, `TS-###`)
