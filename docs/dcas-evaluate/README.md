# DCAS Evaluate (method)

DCAS Evaluate is a lightweight, repeatable method for producing an assurance outcome from DCAS artifacts.

It operationalizes DCAS as:

**Select profile → choose AL → map control objectives → review evidence → record results → publish outcome**

## Inputs

- Target profile: `conformance/profiles/`
- Assurance level definitions: `conformance/assurance_levels.md`
- Control objectives: `controls/control_objectives.csv`
- Risk and mappings: `risk/exports/` and `risk/mapping/`

## The bundle

Use `templates/starter-bundle/` as the canonical structure:
- `claims.csv`
- `risks.csv`
- `evidence.csv`
- `mappings_control_evidence.csv`
- `evaluation_results.csv`

## Output

A defensible outcome is a combination of:
- a structured result set (`evaluation_results.csv`)
- evidence pointers (`evidence.csv`)
- trace links to control objectives (`mappings_control_evidence.csv`)

## Mechanical validation

Run:
```bash
make validate
```

CI runs the same checks on every PR/push.

## Coverage report (automated)

Use `make coverage` to generate a deterministic control coverage report (CSV + Markdown). This is intended to be a first-pass verifier lens before deeper evidence checks.
