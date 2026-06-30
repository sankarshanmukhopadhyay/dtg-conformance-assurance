# TSMM runtime governance evaluation profile

**Status:** Active evaluator guidance for DCAS v0.9.0  
**Aligned TSMM release:** v0.21.0  
**Last reviewed:** 2026-06-29

## Purpose

This profile tells DCAS evaluators how to assess runtime governance evidence that is modeled with the Trust Systems Meta Model (TSMM). TSMM owns the semantic governance model for actors, authority, delegation, policy, evidence, lifecycle state, trust decisions, and operational effects. DCAS owns the evaluation method used to decide whether the evidence is sufficient for a declared assurance level.

The profile applies when an actor, agent, service, tool, registry client, or delegated automation requests an operational effect and the relying party needs a reviewable assurance outcome before or after the effect is admitted.

## Boundary rule

DCAS MUST NOT redefine TSMM runtime governance semantics. A TSMM runtime governance envelope, authority graph, evidence artifact, or decision receipt is an input to the DCAS evaluation process. It is not an automatic assurance pass.

The evaluator decision remains separate:

```text
TSMM models the governance meaning.
TIS packages the meaning into machine-validatable artifact contracts.
DCAS evaluates evidence sufficiency, assurance posture, limitations, and outcome.
```

## Required evaluation surfaces

| Evaluation surface | DCAS evaluator question | Minimum evidence |
|---|---|---|
| Actor identity | Who requested the effect? | Actor or agent reference with stable identifier |
| Effect definition | What operational effect was requested? | Action, target, effect class, and requested admission state |
| Trust boundary | What boundary was crossed? | Boundary reference and relying-party context |
| Authority basis | What authority was relied on? | Authority source, scope, state, and issuer or governance source |
| Delegation chain | Was authority delegated, narrowed, or constrained? | Delegation references, scope limits, expiry, and permitted contexts |
| Policy binding | Which policy governed the decision? | Policy references and policy version or digest |
| Evidence binding | What evidence was evaluated? | Evidence references, hashes, bundle manifest, or equivalent evidence index |
| Status and revocation | Was authority current at decision time? | Status source, status value, check time, and freshness window |
| Decision outcome | What decision was made? | Outcome such as allow, deny, warn, review, downgrade, or suspend |
| Effect admission | What happened to the requested effect? | Admission value such as permitted, blocked, queued-for-review, or restricted |
| Review path | Can the decision be challenged or audited? | Assessor contact, issue path, appeal route, or governance review reference |

## Assurance-level interpretation

| Assurance level | Runtime governance expectation |
|---|---|
| AL1 | Runtime governance artifacts may be self-asserted, but actor, effect, boundary, and decision outcome must be identifiable. |
| AL2 | Authority, policy, evidence, and status references must be present and attributable to an identifiable operator, issuer, or governance authority. |
| AL3 | Evidence must be independently reviewable, freshness-bound, and sufficient for replay of the decision path by an assessor. |
| AL4 | Runtime monitoring, revocation/status checks, integrity-bound evidence bundles, decision receipts, and change/incident history should be available for continuous or periodic assurance. |

## Negative-path obligations

For high-risk delegated or side-effecting operations, a DCAS evaluation SHOULD include negative-path evidence. At minimum, evaluators should test or review behavior for:

- missing policy reference;
- revoked, suspended, expired, unknown, or stale authority state;
- requested effect outside authority scope;
- missing evidence bundle or unverifiable evidence digest;
- absent decision receipt where the profile requires one;
- downgrade or fail-open behavior when status freshness cannot be established.

A system that admits a high-risk effect when authority, policy, evidence, or status cannot be established SHOULD NOT receive an AL3 or AL4 runtime governance outcome for that effect.

## Required evaluator output

A TSMM-backed DCAS evaluation SHOULD produce or reference:

- evaluation claim ID;
- target actor or agent;
- requested effect and trust boundary;
- authority and delegation findings;
- policy and evidence references;
- status or revocation freshness findings;
- decision receipt or decision trace reference;
- target assurance level;
- final outcome and limitations;
- review or escalation path.

## Relationship to TIS v0.10.0

For machine-validatable artifact contracts, use the TIS v0.10.0 runtime assurance profile in `tis-v0.10-runtime-assurance-evaluation-profile.md`. The TSMM profile defines what must be understood. The TIS profile defines what can be validated and packaged.
