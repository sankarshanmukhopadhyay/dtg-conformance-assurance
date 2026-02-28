# Tools

This folder contains lightweight utilities to keep the repo **diff-friendly** and **machine-readable**.

## 1) Export the risk register (XLSX → CSV)

Source: `risk/source/Risk an implementer-supplied artifact appropriate to your context (e.g., risk register entry, test evidence, or approval record).`  
Output: `an implementer-supplied artifact appropriate to your context (e.g., risk register entry, test evidence, or approval record).`

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

- `an implementer-supplied artifact appropriate to your context (e.g., risk register entry, test evidence, or approval record).`
- `an implementer-supplied artifact appropriate to your context (e.g., risk register entry, test evidence, or approval record).`
- `an implementer-supplied artifact appropriate to your context (e.g., risk register entry, test evidence, or approval record).`

Suggested validation pattern:
- ensure stable headers (do not rename casually)
- keep IDs stable (`DCAS-CTRL-###`, `EV-###`, `TS-###`)
