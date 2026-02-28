# Tool builder playbook

## Your job-to-be-done
Turn DCAS artifacts into automation: validation, reporting, dashboards, and integration.

## What to build first (highest ROI)

1. **Bundle validator**
   - Treat `templates/starter-bundle/` as the canonical contract.
   - Enforce required columns + referential integrity.

2. **Coverage views**
   - Join: risks → control objectives → evidence → results
   - Output CSV and a human-readable report (Markdown/PDF)

3. **Profile-driven checks**
   - For each profile + AL, compute required control objectives.
   - Flag missing evidence and “partial” results.

## Repo utilities

- Validation entrypoint: `tools/validate.py`
- Make targets: `Makefile` (`make validate`)
- Paths contract: `repo-contract/paths.json`
