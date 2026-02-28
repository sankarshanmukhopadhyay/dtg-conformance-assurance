# DCAS Evaluate (method)

DCAS Evaluate is a lightweight, repeatable method for producing an assurance outcome from DCAS artifacts.

It packages DCAS into a **doable workflow**:

**Select profile → choose AL → map COs → run tests → review evidence → publish report**

## Inputs

- Target actor class profile: `conformance/profiles/`
- Assurance levels: `the referenced artifact (not included in this repo)`
- Risk register export: `the referenced artifact (not included in this repo)`
- Risk→CO mapping: `the referenced artifact (not included in this repo)`
- Catalogs:
  - controls: `the referenced artifact (not included in this repo)`
  - evidence: `the referenced artifact (not included in this repo)`
  - tests: `the referenced artifact (not included in this repo)`

## Outputs

- An **assurance report** (template): `the referenced artifact (not included in this repo)`
- A **score + confidence** rationale (rubric): `the referenced artifact (not included in this repo)`
- An **evidence checklist** snapshot: `the referenced artifact (not included in this repo)`

## Minimal workflow

1. Identify actor class (e.g., Issuer) and select the profile.
2. Choose target AL (AL1–AL4).
3. List mandatory COs for the profile.
4. For each CO, pull required controls from `the referenced artifact (not included in this repo)`.
5. Collect evidence (EV-###) and execute tests (TS-###).
6. Score results and document confidence.
7. Publish the assurance report.

## Versioning

- Method version: `DCAS_METHOD_VERSION`
- Catalog IDs are stable within a release; do not renumber casually.
