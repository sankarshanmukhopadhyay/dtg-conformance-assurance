# Portfolio Drift Review: AIS-1 v0.2 to DCAS v0.10.0

| Field | Value |
|---|---|
| Source standard | AIS-1 Agent Identity Standard |
| Source version | v0.2 draft for comment |
| Reviewed repo | dtg-conformance-assurance |
| Target release | v0.10.0 |
| Review date | 2026-07-03 |
| Drift classification | Standards drift, artifact drift, assurance drift |

## Changed Surfaces

- `agentClass` introduces ALA and SOA distinction.
- `parentDid` introduces machine-readable SOA accountability chains.
- DID resolution and registry publication become explicit verifier inputs.
- `timestampServiceRef` replaces the earlier service-specific timestamp field.
- SOA revocation cascades from parent ALA revocation.
- Assurance Container introduces versioned attestations alongside the immutable bond.

## DCAS Impact

DCAS v0.10.0 must evaluate AIS-1 v0.2 as bounded identity and accountability evidence. It must not convert bond existence, tier, DID resolution, registry status, timestamp evidence, or assurance-container presence into delegated authority, runtime authorization, or message provenance.

## Relationship Review

| Source | Target | Relationship | Impact | Evidence |
|---|---|---|---|---|
| trust-systems-meta-model | DCAS | informs | Preserve identity, delegation, authority, evidence, decision, and effect boundaries | `docs/ais1-experimental-assurance-profile.md` |
| trust-infrastructure-schemas | DCAS | drift_sensitive_to | Consume AIS-1 and runtime assurance artifacts as evidence inputs only | `docs/compatibility-matrix.md` |
| agent-name-assurance-baseline | DCAS | produces_evidence_for | ANAB declarations and AIS-1 extension evidence can be evaluated under CP-8 | `conformance/examples/ais1_experimental_evaluation_claim.example.yaml` |

## Required Evidence

- Updated CP-8 AIS-1 v0.2 evaluation profile.
- Updated control, evidence, and test catalogs for SOA parent-chain validation and cascade revocation.
- Updated worked evaluation claim.
- Validation coverage for the AIS-1 v0.2 claim.
- Release impact documentation.
