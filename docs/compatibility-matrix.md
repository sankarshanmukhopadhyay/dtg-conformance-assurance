# Compatibility matrix

This matrix is a lightweight coordination tool to prevent cross-repo drift. It documents the current interoperability posture across the ecosystem.

| Repository | Repo version (declared) | Canonical AL model | Control ID namespace | Conformance declaration schema | Evidence bundle expectations |
| --- | --- | --- | --- | --- | --- |
| `trust-infrastructure-schemas` | See upstream repo | `AL-Model-Version: 1.0` (canonical OTAM artifact) | N/A | Canonical trust artifact schemas | N/A |
| `dtg-conformance-assurance` (DCAS) | See `DCAS_METHOD_VERSION` | References `trust-infrastructure-schemas` AL model | `DCAS-*` (method-level) | DCAS declaration templates | DCAS evidence bundle structure |
| `agent-name-assurance-baseline` (ANAB) | See README / badges | References `trust-infrastructure-schemas` AL model | `ANAGB-*` | ANAB conformance declarations and A2A description extension artifacts | ANAB evidence bundles, evaluable via DCAS |

## Notes

- Repositories MUST not redefine AL semantics. If AL changes are needed, update the canonical document in `trust-infrastructure-schemas`.
- If declaration schemas are extended, prefer extension schemas that reference canonical `$id` values instead of copying schema bodies.



### ANAB-over-A2A binding note

- DCAS SHOULD expect ANAB A2A deployments to carry the extension URI `https://trustoverip.github.io/dtgwg-agent-names-tf/extensions/anab-description/v1`.
- DCAS SHOULD treat `conformance/anab-over-a2a-description-extension.schema.json` in ANAB as a domain-specific extension contract, not as a replacement for canonical OTAM schemas.
- Compatibility requires preserving `ANAGB-A2A-07` through `ANAGB-A2A-10` during evaluation rather than flattening them into opaque local labels.


## Experimental additions

| Surface | Current treatment in DCAS | Status |
|---|---|---|
| AIS-1 bonded identity/accountability | Evaluated via `CP-8_AIS1Experimental.md` as a bounded identity-and-accountability input | Experimental |

## TIS v0.9 runtime trust artifact profile alignment

| Surface | Expected DCAS treatment | Drift signal |
| --- | --- | --- |
| TIS v0.9 DTG credential profiles | Credential evidence substrate for issuer, subject, proof, and validity review | credential context, type, proof, or subject shape changes |
| TIS v0.9 OpenVTC profiles | Runtime relationship, routing, configuration, and VRC issuance evidence | state machine, routing, or issuance receipt changes |
| TIS v0.9 VTI profiles | Authority, ACL, authorization, sealed transfer, attestation, DID template, and provision evidence | VTA context, ACL, authorization, attestation, or provision schema changes |
| TIS decision receipts | Runtime decision evidence pattern for rule set, facts, authority, and outcome | receipt structure or authority semantics changes |
| TIS evidence bundle manifest | Evidence inventory, hash, and chain-of-custody surface | bundle shape, hash semantics, or validation metadata changes |
| TIS cross-repo compatibility matrix | Source artifact for DCAS drift review | new mapping, changed upstream role, or changed validation status |

DCAS MUST treat this table as an evaluation compatibility map, not as a schema copy. Canonical schema ownership remains with TIS.

