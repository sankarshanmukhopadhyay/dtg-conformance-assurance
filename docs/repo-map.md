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
- TSMM runtime governance evaluation: `docs/tsmm-runtime-governance-evaluation-profile.md`
- TIS v0.10 runtime assurance evaluation: `docs/tis-v0.10-runtime-assurance-evaluation-profile.md`
- Runtime assurance worked example: `conformance/examples/tis_v0_10_runtime_assurance_evaluation_claim.example.yaml`
- Portfolio drift review: `docs/portfolio-drift-review-tis-v0.10.md`
- Release impact record: `docs/release-impact-v0.9.0.md`

## Reports

- Control coverage (deterministic): `risk/reports/coverage/` (generated via `make coverage`)

## Executable evaluation (unreleased)

- `tools/dcas_evaluate.py`: strict normalized evaluation.
- `tools/import_tt_conformance.py`: pinned Trust Tasks run importer.
- `spec/schemas/dcas-evaluation-*-v0.2.schema.json`: normalized input/output contracts.
- `spec/schemas/dcas-tt-assessor-manifest.schema.json`: assessor intake contract.
- `conformance/examples/tt_conformance/generate_fixture.py`: reproducible synthetic example.
- `tests/`: evaluator and importer regression tests.

See [Trust Tasks evidence integration](tt-conformance-evidence-integration.md).
