# Portfolio drift review: TIS v0.10.0 to DCAS v0.9.0

**Review ID:** `portfolio-drift-20260629-01`  
**Source repository:** `trust-infrastructure-schemas`  
**Source release:** `v0.10.0`  
**Target repository:** `dtg-conformance-assurance`  
**Target release:** `v0.9.0`  
**Review status:** Completed

## Drift classification

| Classification | Applies? | Rationale |
|---|---:|---|
| Documentation drift | Yes | DCAS needed updated evaluator guidance and onboarding paths for TIS v0.10.0. |
| Artifact drift | Yes | TIS added runtime governance projection, Trust Task artifacts, integrity-bound evidence bundles, status-list references, and registry publication profiles. |
| Assurance drift | Yes | DCAS assurance interpretation needed stronger AL3/AL4 expectations for freshness, evidence integrity, decision receipts, and fail-safe behavior. |
| Standards drift | No | No new external standards binding was introduced by this DCAS update. |

## Relationship reviewed

| Source repo | Target repo | Relationship | Impact | Evidence |
|---|---|---|---|---|
| `trust-infrastructure-schemas` | `dtg-conformance-assurance` | `drift_sensitive_to` | Runtime artifact, evidence, revocation/status, and assurance interpretation updates required | `docs/tis-v0.10-runtime-assurance-evaluation-profile.md`; `model/tis-compatibility-review.json`; `conformance/examples/tis_v0_10_runtime_assurance_evaluation_claim.example.yaml` |
| `trust-systems-meta-model` | `dtg-conformance-assurance` | `informs` | TSMM runtime governance semantics made explicit in DCAS evaluator profile | `docs/tsmm-runtime-governance-evaluation-profile.md` |

## Changed surfaces

- TSMM runtime governance projection.
- Authority boundary and delegation scope evidence.
- VTI authorization and status evidence.
- OpenVTC relationship and task evidence.
- Trust Task lifecycle and execution receipts.
- Integrity-bound evidence bundle manifest.
- Decision receipt as runtime audit pivot.
- Registry publication profile and discovery-versus-authorization boundary.

## Downstream DCAS updates completed

| Area | Evidence |
|---|---|
| Evaluator guidance | `docs/tsmm-runtime-governance-evaluation-profile.md`; `docs/tis-v0.10-runtime-assurance-evaluation-profile.md` |
| Worked example | `conformance/examples/tis_v0_10_runtime_assurance_evaluation_claim.example.yaml` |
| Compatibility tracking | `docs/compatibility-matrix.md`; `model/tis-compatibility-review.json` |
| Control/evidence/test mapping | `controls/control_objectives.csv`; `controls/evidence_catalog.csv`; `controls/test_suites.csv`; `risk/mapping/risk_to_control_objectives.csv` |
| Release documentation | `CHANGELOG.md`; `docs/releases/v0.9.0.md`; `docs/release-impact-v0.9.0.md` |
| Validation | `tools/validate.py`; `make validate`; `make coverage` |

## Decision

DCAS v0.9.0 is required because the upstream TIS v0.10.0 release changes artifact and assurance expectations in ways that affect evaluator behavior. The release remains additive and preserves historical TIS v0.9 guidance for legacy evaluations.
