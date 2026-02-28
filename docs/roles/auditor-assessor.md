# Auditor / assessor playbook

## Your job-to-be-done
Produce an assessment outcome that is **repeatable**, **explainable**, and **evidence-grounded**.

## Recommended workflow
1. Identify actor class + target assurance level (AL1–AL4).
2. Pull required COs from the conformance profile (`03_conformance/profiles/`).
3. Use `02_controls/control_catalog.csv` to enumerate required controls, evidence, and tests.
4. Execute tests (manual or automatable).
5. Produce an assurance report using `docs/dcas-evaluate/report-template.md`.

## Outputs you should be able to produce
- Evidence review notes mapped to controls
- Test results (per TS-###)
- Final assurance report + score/confidence rationale
