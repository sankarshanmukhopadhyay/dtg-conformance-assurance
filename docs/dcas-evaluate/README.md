# DCAS Evaluate (method)

DCAS Evaluate is a lightweight, repeatable method for producing an assurance outcome from DCAS artifacts.

It packages DCAS into a **doable workflow**:

**Select profile → choose AL → map COs → run tests → review evidence → publish report**

## Inputs

- Target actor class profile: `conformance/profiles/`
- Assurance levels: `conformance/assurance_levels.md`
- Risk register export: `risk/exports/risk_assessment.csv`
- Risk→CO mapping: `risk/mapping/risk_to_control_objectives.csv`
- Catalogs:
  - controls: `controls/control_catalog.csv`
  - evidence: `controls/evidence_catalog.csv`
  - tests: `controls/test_suites.csv`

## Outputs

- An **assurance report** (template): `docs/dcas-evaluate/report-template.md`
- A **score + confidence** rationale (rubric): `docs/dcas-evaluate/scoring.md`
- An **evidence checklist** snapshot: `docs/dcas-evaluate/evidence-checklist.md`

## Minimal workflow

1. Identify actor class (e.g., Issuer) and select the profile.
2. Choose target AL (AL1–AL4).
3. List mandatory COs for the profile.
4. For each CO, pull required controls from `control_catalog.csv`.
5. Collect evidence (EV-###) and execute tests (TS-###).
6. Score results and document confidence.
7. Publish the assurance report.

## Versioning

- Method version: `DCAS_METHOD_VERSION`
- Catalog IDs are stable within a release; do not renumber casually.
