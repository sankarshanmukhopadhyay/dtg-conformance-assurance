# Known-good stack

**Last reviewed:** 2026-06-29

| Component | Version | Role |
| --- | --- | --- |
| trust-systems-meta-model | v0.21.0 | Semantic governance model for authority, delegation, evidence, lifecycle state, trust decisions, runtime governance, and effects |
| trust-infrastructure-schemas | v0.10.0 | Canonical runtime assurance artifact contracts and compatibility matrix |
| dtg-conformance-assurance | v0.9.0 | Evaluation method for TSMM/TIS-backed runtime assurance evidence |
| agent-name-assurance-baseline | v0.9.0 | Domain baseline for named agents and public trust surfaces |

## Compatibility statement

This is an additive, non-breaking alignment set. DCAS v0.9.0 consumes TSMM runtime governance semantics and TIS v0.10.0 artifacts as evaluator evidence. ANAB v0.9.0 can publish references to TIS artifacts as part of agent-name assurance declarations. DCAS does not copy or replace TIS schemas and does not redefine TSMM semantics.

## Operational note

If TSMM changes runtime governance semantics, or TIS changes runtime governance projection, authority boundary, Trust Task, status-list, decision receipt, evidence bundle, or registry publication artifacts, maintainers SHOULD open a drift review before issuing a new DCAS or ANAB minor release.
