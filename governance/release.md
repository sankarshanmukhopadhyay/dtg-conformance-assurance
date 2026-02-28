# Release checklist

Use this checklist before cutting a tagged release.

## Required checks

- [ ] `make validate` passes locally
- [ ] CI `validate` workflow is green
- [ ] Repo “front door” docs updated as needed (`README.md`, `docs/start-here.md`, `docs/repo-map.md`, `docs/FAQ.md`)

## Artifact hygiene

- [ ] Templates updated if bundle structure changed (`templates/`)
- [ ] Control objectives updated if new IDs are introduced (`controls/control_objectives.csv`)
- [ ] Risk exports updated if applicable (`risk/exports/`)
- [ ] Remove accidental OS/editor artifacts (e.g., `.DS_Store`)

## Release notes

- [ ] Add/refresh a release note under `docs/releases/`
- [ ] Include breaking changes (if any) + migration notes
