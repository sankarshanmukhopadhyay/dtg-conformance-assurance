# Changelog

## [Unreleased]

## [0.10.0] - 2026-07-03

### Added
- Added AIS-1 v0.2 evaluator coverage for ALA/SOA classification, `parentDid`, DID resolution, registry status, bond integrity, timestamp service references, Assurance Container references, and SOA cascade revocation.
- Added new control objectives for AIS-1 SOA parent-chain validation, AIS-1 v0.2 evidence sufficiency, and AIS-1 cascade revocation handling.
- Added evidence catalog and test suite entries for AIS-1 v0.2 bond verification packages, Assurance Container references, and SOA cascade revocation checks.
- Added AIS-1 v0.2 risk mappings and starter-bundle evidence mappings.
- Added a refreshed AIS-1 v0.2 worked evaluation claim.
- Added portfolio drift review and release impact records for AIS-1 v0.2.

### Changed
- Updated DCAS release version to v0.10.0 and method version to v0.5.0.
- Expanded CP-8 from a generic AIS-1 experimental profile into an AIS-1 v0.2 evaluator profile.
- Refreshed README, docs index, compatibility matrix, known-good stack, and roadmap.
- Updated validation tooling to check the AIS-1 v0.2 worked example.

### Quality
- Preserved the boundary that AIS-1 v0.2 is identity and accountability evidence only.
- Kept delegation, runtime authorization, and provenance evidence separate from AIS-1 bond state.
- Regenerated deterministic coverage outputs after adding AIS-1 v0.2 control mappings.

## [0.9.0] - 2026-06-29

### Added
- Added a TSMM runtime governance evaluation profile for authority, delegation, policy, evidence, status, decision, effect, and review-path evaluation.
- Added a TIS v0.10 runtime assurance evaluation profile covering runtime governance projection, authority boundaries, VTI authorization evidence, OpenVTC task evidence, Trust Task receipts, integrity-bound evidence bundles, status-list references, decision receipts, and registry publication profiles.
- Added a worked TIS v0.10 runtime assurance evaluation claim example.
- Added portfolio drift review and release impact records for the TIS v0.10 to DCAS v0.9.0 alignment.
- Added control, evidence, and test catalog entries for runtime authority preservation, evidence integrity, decision receipt completeness, and status freshness enforcement.

### Changed
- Updated the compatibility posture from TIS v0.9 runtime artifact evaluation to TIS v0.10 runtime assurance evaluation.
- Updated README, documentation index, start-here guide, repo map, interoperability docs, known-good stack, compatibility matrix, drift process, roadmap, and release documentation.
- Updated validation tooling to check the TIS v0.10 compatibility manifest and runtime assurance example.
- Regenerated deterministic coverage outputs after extending runtime assurance control mappings.

### Quality
- Preserved the v0.9 runtime artifact profile as legacy guidance while making v0.10 the active path for new runtime assurance evaluations.
- Kept schema ownership in TIS, semantic ownership in TSMM, and assurance interpretation in DCAS.

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
