# DCAS evaluator contract

The portable reference evaluator consumes assessed evidence, not raw claims of trust. DCAS owns the evaluation method and receipt semantics; source baselines own requirements and the relying party owns acceptance policy.

## Current contract: 0.2 (unreleased)

The input identifies baseline, version, profile, evaluation ID/time, nonempty requirement IDs, evidence records, policy, and explicit requirement-to-evidence bindings. Every binding lists all evidence necessary for that requirement. Evidence statuses are available, missing, unverifiable, stale, revoked or contradicted. A binding to an absent record is missing evidence. Duplicate evidence or requirement IDs, unknown bindings and unsafe policies are rejected.

Schemas: `spec/schemas/dcas-evaluation-input-v0.2.schema.json` and `spec/schemas/dcas-evaluation-result-v0.2.schema.json`.

| Decision | Semantics |
| --- | --- |
| PASS | Every declared requirement has nonempty bindings and all bound assessed evidence supports it, with no applicable blocking claim condition. |
| FAIL | A mapped proposition is contradicted or a declared failure policy is triggered. |
| INDETERMINATE | Evidence is insufficient to decide; missing, unbound or unverifiable evidence cannot yield PASS. |

FAIL dominates INDETERMINATE, which dominates PASS. Findings are per requirement; unrelated available evidence cannot fill a missing binding. Stale and revoked evidence default to FAIL, and policy may instead choose INDETERMINATE. Policy may not choose PASS for an adverse state. Identity cannot substitute for required action-authority evidence. If action authority is required, it must be explicitly bound and available.

The result includes evaluator version, overall decision, per-requirement findings, consumed/missing/rejected evidence and an input digest (SHA-256 over compact JSON with sorted keys, Python JSON escaping and no non-finite numbers). This is a reproducibility identifier, not a signature.

## Assessor responsibilities

A PASS is conditional on the trusted normalized input, not proof that the assessor selected all applicable requirements or authenticated the underlying artifacts. The evaluator does not fetch evidence, infer source requirements or choose relying-party policy. Source-specific ingestion must preserve provenance and applicability. See [Trust Tasks integration](tt-conformance-evidence-integration.md).

Independent implementations using identical assessed input and policy should produce equivalent decisions and requirement findings; differing interpretation is an interoperability finding.

## Compatibility and migration

Contract 0.1 input/output schemas and the published ANAB example/result remain historical. The current evaluator accepts legacy input but will not return PASS because 0.1 does not require explicit bindings. Legacy failure conditions remain failures. Consumers must reassess source requirements, add explicit bindings, use contract 0.2 and regenerate results. Do not relabel historical receipts as current results. This is a semantic breaking change for the reference evaluator, not a change to external control identifiers or canonical assurance levels.
