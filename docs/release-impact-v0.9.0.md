# Release impact: DCAS v0.9.0

## Release summary

| Field | Value |
|---|---|
| Repository | `dtg-conformance-assurance` |
| Release version | `v0.9.0` |
| Release date | 2026-06-29 |
| Release owner | Maintainers |
| Primary change type | Runtime assurance alignment |
| Portfolio impact classification | Artifact + Assurance |

## Changed surfaces

- [x] Terminology or conceptual model
- [x] Schema or runtime artifact
- [x] Evidence bundle or decision receipt
- [ ] Conformance verdict or test fixture
- [x] Assurance level or control mapping
- [x] Registry publication or status/revocation semantics
- [ ] Standards binding or crosswalk
- [x] README, onboarding, or adoption workflow

## Relationship review

| Source repo | Target repo | Relationship | Impact | Evidence |
|---|---|---|---|---|
| `trust-systems-meta-model` | `dtg-conformance-assurance` | `informs` | DCAS now includes an explicit TSMM runtime governance evaluation profile | `docs/tsmm-runtime-governance-evaluation-profile.md` |
| `trust-infrastructure-schemas` | `dtg-conformance-assurance` | `drift_sensitive_to` | DCAS now tracks TIS v0.10.0 runtime assurance artifacts | `docs/tis-v0.10-runtime-assurance-evaluation-profile.md`; `model/tis-compatibility-review.json` |

## Downstream review requirements

| Downstream repo | Required review | Owner | Status |
|---|---|---|---|
| `agent-name-assurance-baseline` | Review whether ANAB-over-A2A examples should reference the v0.10 runtime assurance chain | ANAB maintainers | Recommended |
| `trust-infrastructure-schemas` | No schema change required; DCAS consumes existing v0.10 contracts | TIS maintainers | No action |
| `trust-systems-meta-model` | No model change required; DCAS consumes existing TSMM runtime governance semantics | TSMM maintainers | No action |

## Validation evidence

```text
make validate
make coverage
```

## Release note language

```text
DCAS v0.9.0 aligns the assurance method with TSMM runtime governance and TIS v0.10.0 runtime assurance artifacts. The release adds evaluator guidance, a worked evaluation claim, portfolio drift records, control/evidence/test catalog updates, and validation checks for authority-bound, policy-bound, status-aware, receipt-backed runtime assurance.
```

## Decision

- [ ] Release has no cross-repo impact.
- [ ] Release has documentation impact only.
- [x] Release requires downstream artifact/profile/test updates.
- [ ] Release should be held until downstream compatibility is updated.
