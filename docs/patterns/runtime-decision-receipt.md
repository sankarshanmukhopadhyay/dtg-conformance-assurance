# Runtime decision receipt pattern *(experimental)*

This pattern captures a verifier-friendly, machine-reviewable record of a runtime governance decision.

## Why this exists

DCAS already structures assurance as **Risks → Control Objectives → Evidence → Evaluation outcome**. For agentic and delegated systems, one evidence gap remains common: the system often proves what policy exists, but not what happened **at the moment of execution**.

The Microsoft Agent Governance Toolkit is a useful upstream reference here because it emphasizes deterministic policy evaluation before execution and tamper-evident audit trails for agent actions. DCAS adopts that insight in an experimental way by defining a portable evidence pattern rather than importing the upstream implementation.

## Minimum receipt fields

A runtime decision receipt SHOULD include:

- receipt identifier
- timestamp
- subject / actor identifier
- requested action
- target resource or tool
- authority basis or delegation reference
- policy reference
- evidence or status inputs consulted
- verdict (`allow`, `deny`, `review`, `degrade`, `suspend`)
- resulting effect or blocked effect
- receipt integrity metadata (hash, signature, log inclusion proof, or equivalent)

## Example usage

See `conformance/examples/runtime_decision_receipt.example.yaml`.

## Assurance value

This pattern improves:

- runtime reproducibility
- delegation auditability
- verifier visibility into stale-status failures and fail-open risks
- cross-repo composition with TSMM pre-effect governance and ANAB runtime identity lifecycle guidance
