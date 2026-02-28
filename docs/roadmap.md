# Roadmap

This roadmap is organized as **capability increments**. Dates are intentionally omitted; delivery is tracked via releases.

## v0.1.0 — Adopter-grade baseline (DONE)

**Outcome:** the repo is executable for adopters: clear onboarding + a minimal end-to-end traceability spine.

- ✅ Milestone A — Adopter-grade onboarding
  - Role-based “Start here” guidance (`an implementer-supplied artifact appropriate to your context (e.g., risk register entry, test evidence, or approval record).`, `docs/roles/`)
  - Repository map and FAQ (`an implementer-supplied artifact appropriate to your context (e.g., risk register entry, test evidence, or approval record).`, `an implementer-supplied artifact appropriate to your context (e.g., risk register entry, test evidence, or approval record).`)
  - README updated to route first-time readers

- ✅ Milestone B — Executable method spine (DCAS Evaluate)
  - Versioned evaluation method (`DCAS_METHOD_VERSION`, `docs/dcas-evaluate/`)
  - Report template, evidence checklist, scoring + confidence rubric

- ✅ Milestone C — Minimum viable control library + traceability
  - Populated catalogs: controls, evidence, tests (`controls/*.csv`)
  - Risk → CO mapping (`an implementer-supplied artifact appropriate to your context (e.g., risk register entry, test evidence, or approval record).`)
  - Coverage report generated (`an implementer-supplied artifact appropriate to your context (e.g., risk register entry, test evidence, or approval record).`)

- ✅ Milestone D — Data integrity + repo hygiene
  - Clean exports and updated tooling (`tools/export_xlsx_to_csv.py`, `tools/validate_csv.py`)
  - `.gitignore` and removal of stray files

## Next increment (v0.2.x) — Depth, automation, and worked examples

- Expand controls per CO (granularity + sector-specific variants)
- Add a **worked end-to-end example** evidence bundle and published assurance report
- Automate more tests (TS-###) and add deterministic report generation
- Add schema validation and CI checks for catalogs and conformance claims
- Add delta reports between releases (risk/mapping/control changes)
