# Tool builder playbook

## Your job-to-be-done
Turn DCAS artifacts into automation: validation, reporting, dashboards, and integration.

## What to build first (highest ROI)
1. A join pipeline that links:
   - risks (`risk/exports/risk_assessment.csv`)
   - risk→CO (`risk/mapping/risk_to_control_objectives.csv`)
   - CO→controls/evidence/tests (`controls/*.csv`)
2. A report generator that renders `docs/dcas-evaluate/report-template.md` from structured inputs.
3. CSV validators and diff tooling for catalogs.

## Design constraints
- Keep IDs stable and diff-friendly.
- Prefer CSV/JSON outputs and deterministic ordering.
