# Roadmap

This roadmap is organized as capability increments. Dates are intentionally omitted; delivery is tracked via releases.

## v0.1.x — Adopter + developer readiness (DELIVERED)

**Outcome:** repo is executable for adopters and contributors.

- CSV-first starter bundle templates (`templates/starter-bundle/`)
- Control objectives registry in CSV (`controls/control_objectives.csv`)
- Reproducible validation (`make validate`) and CI workflow
- Updated “front door” docs (start-here, repo-map, FAQ)
- Removal of maintainer-only broken reference inventory (replaced by automated checks)

## v0.2.0 — Coverage reporting + stronger schemas (DELIVERED)
- Generate a coverage report from bundle + mappings (CSV + Markdown output)
- Add explicit CSV schema descriptors for each template (machine-readable)
- Add machine-readable CSV schema descriptors (drives `make validate`)
- Add deterministic coverage reporting (`make coverage`)
- Add a verifier-first workflow doc (`docs/verifier-workflow.md`)
- Tighten CI to regenerate deterministic reports and fail on diffs



## v0.2.1 — Adoption polish + GitHub Pages documentation (DELIVERED)

**Outcome:** a casual visitor can understand the project in 5 minutes, and adopters can self-serve via a published docs site.

- GitHub Pages-ready documentation landing page (`docs/index.md`) + publishing guide (`docs/github-pages.md`)
- Explicit methodology explainer (`docs/methodology.md`)
- Standards & policy reference map (`docs/standards-and-policies.md`)
- Remove references to any specific working group governance; adopt repo-neutral governance language
- Lightweight doc hygiene improvements (navigation, cross-links)



## v0.3.0 — Domain baseline composition pack (DELIVERED)

**Outcome:** downstream baselines can be evaluated by DCAS without losing their own control namespaces.

- Added `docs/domain-baseline-composition.md`
- Added `conformance/examples/anab_evaluation_claim.example.yaml`
- Refreshed README so cross-repo composition is visible from the front door


## Unreleased follow-on — ANAB-over-A2A evaluation alignment

**Outcome:** DCAS can evaluate ANAB A2A-bound trust descriptions without flattening their control identifiers or treating the extension as mere descriptive prose.

- Add evaluator guidance for ANAB-over-A2A trust metadata
- Add a worked evaluation example preserving `ANAGB-A2A-07` through `ANAGB-A2A-10`
- Refresh compatibility and composition docs to recognize the ANAB description extension


## Unreleased follow-on — AIS-1 experimental evaluation lane

**Outcome:** DCAS can evaluate AIS-1 as a bounded, experimental accountability substrate while preserving the correct maturity signal.

- Add an experimental AIS-1 profile for bonded agent identity and accountability
- Add a worked evaluation claim example
- Refresh README and docs navigation so the profile is discoverable
- Keep delegation, provenance, and production-readiness explicitly out of scope for the profile

## v0.8.0 — TIS v0.9 runtime trust artifact evaluation alignment (DELIVERED)

**Outcome:** DCAS can evaluate TIS v0.9 DTG/OpenVTC/VTI runtime trust artifacts without copying TIS schemas or collapsing downstream domain-baseline semantics.

- Added evaluator guidance for TIS v0.9 runtime artifacts.
- Added a drift review process and compatibility review manifest.
- Added a worked TIS-backed evaluation claim.
- Added known-good stack and cross-repo alignment documentation.
- Updated validation to keep the new artifacts CI-safe.

## v0.9.0 — TSMM/TIS v0.10 runtime assurance alignment (DELIVERED)

**Outcome:** DCAS evaluates TSMM runtime governance semantics and TIS v0.10 runtime assurance artifacts as an assurance chain rather than as isolated runtime evidence objects.

- Added TSMM runtime governance evaluator guidance.
- Added TIS v0.10 runtime assurance evaluator guidance.
- Added a worked v0.10 runtime assurance evaluation claim.
- Added portfolio drift review and release impact records.
- Added runtime assurance controls for authority boundary preservation, evidence bundle integrity, decision receipt completeness, and status freshness enforcement.
- Updated validation to check v0.10 compatibility metadata and runtime assurance examples.
- Regenerated deterministic coverage outputs.

## Future follow-on — automated cross-repo drift reporting

**Outcome:** DCAS can generate a local drift report from the TIS compatibility matrix and local manifest.

- Compare tracked TIS release and schema references against local review manifest.
- Emit machine-readable drift status for CI or release readiness checks.
- Keep this as a release-readiness gate rather than a hard dependency on network access.
