# Tool builder playbook

## Your job-to-be-done
Turn DCAS artifacts into automation: validation, reporting, dashboards, and integration.

## What to build first (highest ROI)
1. A join pipeline that links:
   - risks (`the referenced artifact (not included in this repo)`)
   - risk→CO (`the referenced artifact (not included in this repo)`)
   - CO→controls/evidence/tests (`controls/*.csv`)
2. A report generator that renders `the referenced artifact (not included in this repo)` from structured inputs.
3. CSV validators and diff tooling for catalogs.

## Design constraints
- Keep IDs stable and diff-friendly.
- Prefer CSV/JSON outputs and deterministic ordering.
