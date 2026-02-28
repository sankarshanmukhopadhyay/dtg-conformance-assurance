# DCAS Evaluate (method)

DCAS Evaluate is a lightweight, repeatable method for producing an assurance outcome from DCAS artifacts.

It packages DCAS into a **doable workflow**:

**Select profile → choose AL → map COs → run tests → review evidence → publish report**

## Inputs

- Target actor class profile: `conformance/profiles/`
- Assurance levels: `an implementer-supplied artifact appropriate to your context (e.g., risk register entry, test evidence, or approval record).`
- Risk register export: `an implementer-supplied artifact appropriate to your context (e.g., risk register entry, test evidence, or approval record).`
- Risk→CO mapping: `an implementer-supplied artifact appropriate to your context (e.g., risk register entry, test evidence, or approval record).`
- Catalogs:
  - controls: `an implementer-supplied artifact appropriate to your context (e.g., risk register entry, test evidence, or approval record).`
  - evidence: `an implementer-supplied evidence artifact (e.g., audit report excerpt, test output, or signed attestation).`
  - tests: `an implementer-supplied artifact appropriate to your context (e.g., risk register entry, test evidence, or approval record).`

## Outputs

- An **assurance report** (template): `a companion worksheet/template that implementers SHOULD supply from their own governance system (e.g., an organizational risk register, control checklist, or assessment form).`
- A **score + confidence** rationale (rubric): `an implementer-supplied artifact appropriate to your context (e.g., risk register entry, test evidence, or approval record).`
- An **evidence checklist** snapshot: `a companion worksheet/template that implementers SHOULD supply from their own governance system (e.g., an organizational risk register, control checklist, or assessment form).`

## Minimal workflow

1. Identify actor class (e.g., Issuer) and select the profile.
2. Choose target AL (AL1–AL4).
3. List mandatory COs for the profile.
4. For each CO, pull required controls from `an implementer-supplied artifact appropriate to your context (e.g., risk register entry, test evidence, or approval record).`.
5. Collect evidence (EV-###) and execute tests (TS-###).
6. Score results and document confidence.
7. Publish the assurance report.

## Versioning

- Method version: `DCAS_METHOD_VERSION`
- Catalog IDs are stable within a release; do not renumber casually.
