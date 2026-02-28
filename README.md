# DTG Conformance & Assurance (DCAS)

This repository publishes **DCAS (Decentralized Conformance and Assurance Standard)** artifacts for DTG ecosystems.

DCAS is an implementation-neutral way to move from implicit trust to **explicit, reviewable, risk-proportionate claims**.

## Status

- **Primary goal (this repo):** make DCAS *operational* — templates, schemas, and a repeatable evaluation method.
- **Spec:** `spec/DCAS_v0.1.md` is a **draft** (contains TODOs). Templates + validation tooling are treated as the stable “adoption surface”.

## Start here

- **Adoption guide (role-based):** `docs/start-here.md`
- **Repository map:** `docs/repo-map.md`
- **FAQ:** `docs/FAQ.md`
- **Verifier workflow:** `docs/verifier-workflow.md`

## Golden path (issuer-first)

1. Copy the starter bundle: `templates/starter-bundle/`
2. Populate CSVs with your real IDs, risks, evidence, and results
3. Attach real evidence artifacts (or stable URIs)
4. Validate structure:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
make validate
```

Generate a deterministic control coverage report:

```bash
make coverage
```

## Key artifacts

- **Control objectives (CSV):** `controls/control_objectives.csv`
- **Risk register export (CSV):** `risk/exports/risk_assessment.csv`
- **CSV schema descriptors (machine-readable):** `schemas/csv/` (see `schemas/csv/index.json`)
- **Risk → control mapping (CSV):** `risk/mapping/risk_to_control_objectives.csv`
- **Conformance profiles:** `conformance/profiles/`
- **Assurance level definitions:** `conformance/assurance_levels.md`
- **Evaluation method:** `docs/dcas-evaluate/README.md`

## Contributing

See `CONTRIBUTING.md`. CI enforces mechanical correctness (CSV structure + markdown link integrity).
