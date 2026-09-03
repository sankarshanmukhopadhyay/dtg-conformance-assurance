# DCAS evaluator contract

This document defines the smallest portable contract for independently implementing a DCAS evaluator. It is intentionally narrower than the draft DCAS specification.

## Inputs

A normalized evaluation input identifies:

- the source assurance baseline, version and profile;
- the claim under evaluation;
- evidence references and their observable status;
- relying-party policy constraints;
- the evaluation time used for freshness-sensitive decisions.

Schema: `spec/schemas/dcas-evaluation-input.schema.json`.

## Outputs

A normalized result identifies:

- overall `PASS`, `FAIL` or `INDETERMINATE`;
- per-requirement findings;
- consumed, missing and rejected evidence;
- claimed versus supported assurance where relevant;
- evaluator identity/version;
- digest material sufficient to bind a decision receipt to normalized input.

Schema: `spec/schemas/dcas-evaluation-result.schema.json`.

## Outcome semantics

**PASS** means sufficient current evidence demonstrates all requirements needed for the evaluated target under the declared policy.

**FAIL** means evidence demonstrates that at least one required proposition is false or unmet.

**INDETERMINATE** means the available evidence is insufficient to decide, including evidence that is missing, stale, inaccessible or unverifiable where policy does not establish a deterministic failure rule.

Missing evidence MUST NOT silently become PASS.

## Authority boundary

DCAS owns evaluation-method and result/receipt semantics. It does not own or rewrite the requirements of the source baseline. For ANAB evaluations, ANAB remains authoritative for named-agent controls, tier/profile meaning and evidence expectations.

An evaluator MUST therefore reference source requirement identifiers rather than replacing them with DCAS-local control semantics merely for convenience.

## Equivalence expectation

Two conforming evaluator implementations receiving identical normalized input and the same declared policy SHOULD produce materially equivalent overall decisions and source-requirement findings. Differences in formatting, ordering or explanatory prose are not material. Different decisions, different treatment of missing evidence, or different interpretation of source requirements are material and MUST be surfaced as an interoperability finding.

## Scope of the first experiment

The first consumer is `IC-ANAB-DCAS-001` in the Trust Protocol Interop Lab. It will test at least PASS, FAIL and INDETERMINATE vectors from the ANAB implementation-validation pack.
