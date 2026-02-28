# Repository map

This repo is organized around an end-to-end traceability spine:

**Risks → Control Objectives → Evidence → Evaluation outcome**

## Top-level folders

- `context/` — glossary, assumptions, and DTG working group scope
- `controls/` — DCAS control objectives (CSV + narrative)
- `risk/` — risk register exports and mappings
- `templates/` — CSV-first evidence bundle templates
- `conformance/` — assurance levels + conformance profiles + examples
- `docs/` — adoption guidance and evaluation method
- `spec/` — draft specification and annexes
- `tools/` — validation tooling (runs in CI)

## Where to begin

- New adopters: `docs/start-here.md`
- Templates: `templates/starter-bundle/`
- Validation: `tools/validate.py` (or `make validate`)
