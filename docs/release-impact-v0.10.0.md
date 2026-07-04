# Portfolio Release Impact: DCAS v0.10.0

## Release Summary

| Field | Value |
|---|---|
| Repository | dtg-conformance-assurance |
| Release version | v0.10.0 |
| Method version | v0.5.0 |
| Release date | 2026-07-03 |
| Primary change type | AIS-1 v0.2 experimental evaluator profile |
| Portfolio impact classification | Artifact / Assurance / Standards |

## Changed Surfaces

- [x] Terminology or conceptual model
- [x] Schema or runtime artifact
- [x] Evidence bundle or decision receipt
- [x] Conformance verdict or test fixture
- [x] Assurance level or control mapping
- [x] Registry publication or status/revocation semantics
- [x] Standards binding or crosswalk
- [x] README, onboarding, or adoption workflow

## Relationship Review

| Source repo | Target repo | Relationship | Impact | Evidence |
|---|---|---|---|---|
| trust-systems-meta-model | dtg-conformance-assurance | informs | AIS-1 v0.2 remains bounded identity/accountability evidence | `docs/ais1-experimental-assurance-profile.md` |
| trust-infrastructure-schemas | dtg-conformance-assurance | drift_sensitive_to | TIS remains canonical artifact layer for runtime assurance evidence | `docs/compatibility-matrix.md` |
| agent-name-assurance-baseline | dtg-conformance-assurance | produces_evidence_for | ANAB v0.10 declarations can be evaluated under DCAS CP-8 | `conformance/examples/ais1_experimental_evaluation_claim.example.yaml` |

## Validation Evidence

```text
make validate
make coverage
```

## Release Note Language

DCAS v0.10.0 upgrades the experimental AIS-1 evaluator profile for AIS-1 v0.2. Evaluators can now assess ALA/SOA classification, parent DID evidence, DID resolution, registry status, bond integrity, timestamp service references, Assurance Container references, and SOA cascade revocation behavior. The release keeps the assurance boundary explicit: AIS-1 bonded identity is evidence of identity and accountability, not delegated authority, runtime authorization, or message provenance.

## Decision

- [ ] Release has no cross-repo impact.
- [ ] Release has documentation impact only.
- [x] Release requires downstream artifact/profile/test updates.
- [ ] Release should be held until downstream compatibility is updated.
