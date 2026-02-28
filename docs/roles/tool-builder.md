# Tool builder playbook

## Your job-to-be-done
Turn DCAS artifacts into automation: validation, reporting, dashboards, and integration.

## What to build first (highest ROI)
1. A join pipeline that links:
   - risks (`an implementer-supplied artifact appropriate to your context (e.g., risk register entry, test evidence, or approval record).`)
   - risk→CO (`an implementer-supplied artifact appropriate to your context (e.g., risk register entry, test evidence, or approval record).`)
   - CO→controls/evidence/tests (`controls/*.csv`)
2. A report generator that renders `an implementer-supplied artifact appropriate to your context (e.g., risk register entry, test evidence, or approval record).` from structured inputs.
3. CSV validators and diff tooling for catalogs.

## Design constraints
- Keep IDs stable and diff-friendly.
- Prefer CSV/JSON outputs and deterministic ordering.
