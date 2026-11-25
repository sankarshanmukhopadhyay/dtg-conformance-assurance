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

- `make validate` — run all repo checks (evaluator tests + CSV schema validation + referential integrity + deterministic reports + markdown links)
- `make export-risk` — optional: export `risk/source/Risk Register.xlsx` (or the consolidated `risk/source/risk-register.csv`) to `risk/exports/risk_assessment.csv`

## Notes

- The XLSX exporter is optional. Prefer maintaining artifacts directly as CSV where possible. The repo now includes a consolidated CSV export at `risk/source/risk-register.csv` for review and automation.
- Templates live under `templates/` (start with `templates/starter-bundle/`).

## CSV schema descriptors

Machine-readable CSV schemas live under `schemas/csv/` and drive the validation checks.

## Executable evidence assessment (unreleased)

- `make test`: evaluator and importer tests, also run by `make validate`.
- `tools/dcas_evaluate.py`: normalized requirement-level evaluation.
- `tools/import_tt_conformance.py`: pinned external test evidence intake.

Follow the [reference evaluator](../docs/reference-evaluator.md) and [Trust Tasks integration](../docs/tt-conformance-evidence-integration.md) for commands, scope and migration.
