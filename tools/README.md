# Tools

This repo is **CSV-first**. Tooling exists to keep artifacts consistent and mechanically verifiable.

## Quickstart

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
make validate
```

## Commands

- `make coverage` — generate a deterministic control coverage report (CSV + Markdown) from the starter bundle

- `make validate` — run all repo checks (CSV schema validation + referential integrity + deterministic reports + markdown links)
- `make export-risk` — optional: export `risk/source/Risk Register.xlsx` to `risk/exports/risk_assessment.csv`

## Notes

- The XLSX exporter is optional. Prefer maintaining artifacts directly as CSV where possible.
- Templates live under `templates/` (start with `templates/starter-bundle/`).

## CSV schema descriptors

Machine-readable CSV schemas live under `schemas/csv/` and drive the validation checks.
