# Roadmap

This roadmap is organized as capability increments. Dates are intentionally omitted; delivery is tracked via releases.

## v0.1.x — Adopter + developer readiness (DELIVERED)

**Outcome:** repo is executable for adopters and contributors.

- CSV-first starter bundle templates (`templates/starter-bundle/`)
- Control objectives registry in CSV (`controls/control_objectives.csv`)
- Reproducible validation (`make validate`) and CI workflow
- Updated “front door” docs (start-here, repo-map, FAQ)
- Removal of maintainer-only broken reference inventory (replaced by automated checks)

## Next increment (proposed)

### v0.2.0 — Coverage reporting + stronger schemas
- Generate a coverage report from bundle + mappings (CSV + Markdown output)
- Add explicit CSV schema descriptors for each template (machine-readable)
- Expand control objectives catalog and align with profiles/ALs
- Add a “verifier-first” workflow doc (independent checks + decision logging)
