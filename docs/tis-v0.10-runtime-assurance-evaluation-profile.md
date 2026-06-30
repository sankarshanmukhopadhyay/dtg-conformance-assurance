# TIS v0.10 runtime assurance evaluation profile

**Status:** Active evaluator guidance for DCAS v0.9.0  
**Aligned TIS release:** v0.10.0  
**Last reviewed:** 2026-06-29

## Purpose

This profile defines how DCAS evaluators consume `trust-infrastructure-schemas` v0.10.0 runtime assurance artifacts. It supersedes the v0.9 runtime artifact profile for new evaluations because TIS v0.10.0 adds TSMM runtime governance projection, Trust Task execution evidence, integrity-bound evidence bundles, status and revocation references, registry publication profiles, and a stronger runtime decision receipt chain.

The profile is intentionally evaluator-facing. TIS owns canonical schema contracts. DCAS evaluates whether those artifacts are authentic, current, scoped, complete, policy-relevant, and sufficient for the target assurance level.

## Runtime assurance chain

The expected v0.10 evidence chain is:

```text
TSMM runtime governance projection
  -> authority boundary
  -> policy and evidence references
  -> status or revocation check
  -> Trust Task lifecycle and execution evidence
  -> integrity-bound evidence bundle
  -> decision receipt
  -> registry publication profile
  -> DCAS assurance outcome
```

Registry publication, task completion, and schema validity are not authorization by themselves. Runtime reliance still requires current authority, policy, evidence, status/revocation checks, and a decision receipt for the requested effect where the profile requires one.

## Artifact families in scope

| TIS v0.10 family | Runtime evidence surface | DCAS evaluation use |
|---|---|---|
| TSMM runtime governance projection | Projection of actor, effect, boundary, authority, policy, evidence, and audit expectation | Semantic bridge from TSMM governance model to machine-validatable evidence |
| Authority boundary | Bounded authority, scope, delegation, lifecycle state, and revocation obligations | Authority and delegation sufficiency |
| VTI authorization evidence | ACL entry, authorization credential, capability grants, allowed contexts, consumer kind, lifecycle state, step-up metadata, and status references | Enforcement and capability evidence |
| OpenVTC task evidence | Relationship state, normalized workflow state, task evidence, VRC or relationship workflow references | Runtime workflow replayability |
| Trust Task artifacts | Task reference, manifest reference, lifecycle event, and execution receipt | Separation of lifecycle state, decision outcome, and effect admission |
| Evidence bundle manifest | Artifact inventory, hashes, canonicalization, bundle digest, detached proof, signature reference | Evidence completeness and tamper-evidence |
| Status-list reference | Revocation, suspension, expiry, activation, or other lifecycle status evidence | Freshness and fail-safe evaluation |
| Decision receipt | Policy, facts, authority, evidence, status posture, decision, effect, and review path | Audit pivot for runtime trust decisions |
| Registry publication profile | Discoverable publication of artifacts and assurance posture | Publication evidence, not runtime authorization |

## Evaluator intake rules

A DCAS evaluator SHOULD collect the following at intake:

1. canonical TIS schema `$id` or stable in-repo profile path;
2. artifact instance URI, bundle path, or immutable reference;
3. artifact hash, bundle digest, or detached proof reference where available;
4. issuer, operator, registry publisher, or governance authority responsible for the artifact;
5. validation status against the relevant TIS schema;
6. authority source, delegation scope, and permitted effect context;
7. policy reference and policy version, digest, or publication reference;
8. status/revocation source, check time, value, and freshness window;
9. Trust Task lifecycle state, decision outcome, and effect admission where runtime execution is in scope;
10. decision receipt reference and review path;
11. control objectives and assurance level for which the artifact is being used;
12. limitations, stale evidence, unresolved drift findings, or compensating controls.

## Evaluation semantics

DCAS evaluates six questions:

1. **Authority:** does the evidence identify who was authorized to assert, delegate, route, provision, execute, or enforce the trust operation?
2. **Scope:** does the evidence constrain what the authority may do, for whom, in which context, for which effect, and for how long?
3. **Policy:** does the decision bind to an identifiable policy reference rather than an implicit local rule?
4. **Enforcement and revocation:** can expiry, suspension, revocation, missing status, or failed step-up change the operational outcome?
5. **Evidence integrity:** can the exact evidence set used for the decision be replayed or verified?
6. **Auditability:** can an independent reviewer inspect the path from authority and evidence to decision and effect?

## Assurance-level interpretation

| Assurance level | TIS v0.10 artifact treatment |
|---|---|
| AL1 | Artifact existence and basic schema conformance may be sufficient for discovery or self-asserted review. |
| AL2 | Artifacts must be bound to identifiable authorities, operators, policies, and control objectives. |
| AL3 | Artifacts must be independently reviewable, freshness-bound, and sufficient to replay the authority, evidence, status, and decision path. |
| AL4 | Runtime monitoring, integrity-bound evidence bundles, revocation/status checks, incident/change history, and decision receipt retention should support continuous or periodic revalidation. |

## Fail-safe rules

For AL3 and AL4 evaluations, DCAS SHOULD treat the following as material negative findings unless explicitly justified:

- effect admitted with missing policy reference;
- effect admitted with revoked, suspended, expired, unknown, unavailable, or stale authority status;
- effect admitted outside delegated scope or allowed context;
- decision receipt missing for a high-risk effect;
- evidence bundle digest missing or unverifiable where integrity-bound evidence is required;
- registry publication treated as sufficient authorization;
- task completion treated as a successful trust decision without separate decision outcome and effect admission.

## Required evaluator output

A TIS v0.10-backed DCAS evaluation SHOULD produce or reference:

- evaluation claim ID;
- covered control objectives;
- target assurance level;
- TIS artifact family and schema references;
- validation status;
- evaluated coverage and freshness window;
- authority, delegation, and scope findings;
- policy and evidence binding findings;
- status and revocation findings;
- Trust Task lifecycle and execution findings where applicable;
- evidence bundle integrity findings;
- decision receipt and review path;
- final outcome and limitations.

See `../conformance/examples/tis_v0_10_runtime_assurance_evaluation_claim.example.yaml` for a worked example.
