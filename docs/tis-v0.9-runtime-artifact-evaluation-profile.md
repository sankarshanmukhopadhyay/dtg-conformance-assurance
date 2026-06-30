# TIS v0.9 runtime trust artifact evaluation profile

**Status:** Legacy evaluator guidance for DCAS v0.8.0; superseded for new runtime assurance evaluations by `tis-v0.10-runtime-assurance-evaluation-profile.md`
**Aligned TIS release:** v0.9.0
**Last reviewed:** 2026-05-06

## Purpose

This profile defines how DCAS evaluators consume runtime trust artifacts produced under `trust-infrastructure-schemas` v0.9.0, especially the DTG, OpenVTC, and VTI compatibility profiles.

The profile exists to prevent semantic drift. TIS owns the canonical artifact schemas. DCAS owns the evaluation method that determines whether those artifacts are sufficient evidence for a declared assurance level, relying-party context, and control objective.

## Boundary rule

DCAS MUST preserve canonical TIS schema identifiers and MUST NOT rename TIS artifact semantics into opaque local labels.

A valid TIS artifact is an evidence input. It is not, by itself, a DCAS assurance pass. The evaluator still has to determine whether the artifact is authentic, current, scoped, complete, policy-relevant, and sufficient for the target assurance level.

## Artifact families in scope

| TIS family | Runtime evidence surface | DCAS evaluation use |
| --- | --- | --- |
| DTG credential profiles | VC envelope, credential subject, proof, issuer DID, validity window | Credential shape and issuer-binding evidence |
| OpenVTC runtime profiles | relationship state, VRC issuance receipt, configuration evidence, DIDComm routing evidence | Replayable relationship and issuance workflow evidence |
| VTI runtime assurance profiles | VTA context, ACL entry, authorization credential, sealed transfer, DID template reference, TEE attestation reference, provision integration receipt | Authority, delegation, enforcement, revocation, and provision evidence |
| TIS decision receipts | rule set, facts evaluated, authority exercised, outcome | Runtime decision audit evidence |
| TIS evidence bundle manifest | artifact inventory, hashes, references, validation metadata | Evidence completeness and chain-of-custody surface |

## Evaluator intake rules

A DCAS evaluator SHOULD collect the following at intake:

1. canonical TIS schema `$id` or stable in-repo profile path;
2. artifact instance URI or bundled local path;
3. artifact hash or immutable reference;
4. issuer, operator, or authority responsible for the artifact;
5. validation status against the TIS schema;
6. freshness, expiry, and revocation status;
7. control objectives and assurance level for which the artifact is being used;
8. known limitations or unresolved drift review findings.

For AL3 and AL4 reviews, evaluators SHOULD require either a signed evidence bundle manifest or an equivalent tamper-evident evidence index. For AL4, runtime monitoring, revocation checks, and incident/change history SHOULD also be present.

## Evaluation semantics

DCAS evaluates four questions:

1. **Authority:** does the artifact identify who is authorized to assert, delegate, route, provision, or enforce the trust operation?
2. **Scope:** does the artifact constrain what the authority may do, for whom, in which context, and for how long?
3. **Enforcement and revocation:** is there evidence that runtime policy, expiry, suspension, or revocation can change operational outcomes?
4. **Auditability:** can an independent reviewer replay or inspect the evidence path that produced the assurance decision?

## Minimum evidence interpretation

| Assurance level | TIS artifact treatment |
| --- | --- |
| AL1 | Artifact existence and basic schema conformance may be enough for discovery or self-asserted review. |
| AL2 | Artifact must be bound to an identifiable issuer or operator and linked to documented controls. |
| AL3 | Artifact must be independently reviewable, freshness-bound, and connected to evaluator findings. |
| AL4 | Artifact must be continuously monitored or periodically revalidated, with revocation, incident, and change evidence available. |

## Non-substitution rule

TIS schemas do not replace DCAS controls. DCAS controls do not replace TIS schemas. The relationship is intentionally layered:

- TIS defines canonical trust artifact shape.
- DCAS evaluates evidence sufficiency and assurance posture.
- Domain baselines such as ANAB define domain-specific obligations.

## Required evaluator output

A TIS-backed DCAS evaluation SHOULD produce or reference:

- evaluation claim ID;
- covered control objectives;
- target assurance level;
- TIS artifact family and schema references;
- validation status;
- evaluated freshness window;
- authority and scope findings;
- revocation and enforcement findings;
- final outcome and limitations.

See `../conformance/examples/tis_v0_9_runtime_artifact_evaluation_claim.example.yaml` for a worked example.
