# Tools

This folder contains lightweight utilities to keep the repo **diff-friendly** and **machine-readable**.

## 1) Export the risk register (XLSX → CSV)

Source: `01_risk/source/Risk Register.xlsx`  
Output: `01_risk/exports/risk_assessment.csv`

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

- `02_controls/control_catalog.csv`
- `02_controls/evidence_catalog.csv`
- `02_controls/test_suites.csv`

Suggested validation pattern:
- ensure stable headers (do not rename casually)
- keep IDs stable (`DCAS-CTRL-###`, `EV-###`, `TS-###`)
