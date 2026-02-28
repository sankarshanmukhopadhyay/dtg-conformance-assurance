# Auditor / assessor playbook

## Your job-to-be-done
Produce an assessment outcome that is **repeatable**, **explainable**, and **evidence-grounded**.

## Recommended workflow

1. Identify the target profile + assurance level
   - Profiles: `conformance/profiles/`
   - AL definitions: `conformance/assurance_levels.md`

2. Require a bundle submission (CSV-first)
   - Use the bundle structure under `templates/starter-bundle/` as your intake contract.

3. Sample and test
   - For each required control objective, pick evidence entries from `evidence.csv`
   - Record sampling decisions and results in `evaluation_results.csv`

4. Produce an outcome
   - Outcome should be reproducible from the bundle + your recorded checks.
   - Where you disagree with issuer self-evaluation, record rationale and point to evidence.

## What “good” looks like

- Stable IDs for controls/evidence/results
- Clear trace links (control objective → evidence → result)
- A minimal audit trail: who checked what, when, and why
