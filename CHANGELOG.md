# Changelog

## [Unreleased]


## [0.8.0] - 2026-05-06

### Added
- Added a TIS v0.9 runtime trust artifact evaluation profile for DTG/OpenVTC/VTI evidence consumption.
- Added a worked TIS v0.9 evaluation claim example that preserves canonical TIS artifact references.
- Added a machine-readable TIS compatibility review manifest and drift review process.
- Added a known-good stack statement and cross-repo DCAS/ANAB/TIS alignment matrix.

### Changed
- Refreshed README, docs index, interoperability, compatibility matrix, and roadmap for TIS v0.9 synchronization.
- Clarified that TIS artifact validity is evidence input, not an automatic DCAS assurance outcome.
- Updated validation tooling to parse the new YAML example and verify the compatibility review manifest.

### Quality
- Confirmed `make validate` and `make coverage` remain compatible with the existing CI workflow.
- Preserved additive, non-breaking control semantics and existing DCAS control namespaces.



## [0.7.0] - 2026-04-20

### Added
- Added `docs/patterns/runtime-decision-receipt.md` to define a portable runtime evidence pattern for pre-effect policy decisions.
- Added `docs/experimental/agent-runtime-controls.md` and `conformance/examples/runtime_decision_receipt.example.yaml` as an experimental runtime-governance overlay.
- Extended the control, evidence, and test catalogs with `CO3.7`, `CO4.5`, `CO6.4`, `EV-016` through `EV-018`, and `TS-016` through `TS-018`.

### Changed
- Refreshed README, docs index, methodology, and verifier workflow to make runtime-governance evidence expectations visible without changing the stable DCAS method core.

## [0.6.0] - 2026-03-24

### Added
- Added `docs/domain-baseline-composition.md` to document how DCAS evaluates downstream baselines such as ANAB while preserving their control namespaces.
- Added `conformance/examples/anab_evaluation_claim.example.yaml` as an illustrative cross-repo evaluation artifact.

### Changed
- Refreshed README freshness metadata and navigation for the new composition pack.
- Updated roadmap status to close the GitHub Pages adoption increment and record the domain-baseline composition increment.

## [0.5.1] - 2026-03-14

### Changed
- Updated ecosystem references from `schemas` to `trust-infrastructure-schemas`.
- Clarified OTAM positioning and the dependency on canonical trust artifact schemas.
