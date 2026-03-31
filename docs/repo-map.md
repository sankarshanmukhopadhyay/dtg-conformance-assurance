# Repository map

This repo is organized around an end-to-end traceability spine:

**Risks → Control Objectives → Evidence → Evaluation outcome**

## Top-level folders

- `context/` — glossary, assumptions, and project scope (`context/project-scope.md`)
- `controls/` — DCAS control objectives (CSV + narrative)
- `risk/` — risk register exports and mappings
- `templates/` — CSV-first evidence bundle templates
- `conformance/` — assurance levels + conformance profiles + examples, including experimental profiles such as AIS-1
- `docs/` — adoption guidance and evaluation method
- `spec/` — draft specification and annexes
- `schemas/` — machine-readable CSV schema descriptors used by tooling
- `tools/` — validation + report tooling (runs in CI)

## Where to begin

- New adopters: `docs/start-here.md`
- Templates: `templates/starter-bundle/`
- Validation: `tools/validate.py` (or `make validate`)

## Reports

- Control coverage (deterministic): `risk/reports/coverage/` (generated via `make coverage`)
