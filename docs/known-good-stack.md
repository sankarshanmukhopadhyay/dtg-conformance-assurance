# Known-good stack

**Last reviewed:** 2026-07-03

| Component | Version | Role |
| --- | --- | --- |
| trust-systems-meta-model | v0.21.0 | Semantic governance model for authority, delegation, evidence, lifecycle state, trust decisions, runtime governance, and effects |
| trust-infrastructure-schemas | v0.10.0 | Canonical runtime assurance artifact contracts and compatibility matrix |
| dtg-conformance-assurance | v0.10.0 | Evaluation method for TSMM/TIS-backed runtime assurance evidence and AIS-1 v0.2 experimental evidence |
| agent-name-assurance-baseline | v0.10.0 | Domain baseline for named agents and public trust surfaces |
| AIS-1 | v0.2 draft | Experimental bonded identity and accountability substrate for ALA/SOA agents |

## Compatibility statement

This is an additive, non-breaking alignment set. DCAS v0.10.0 consumes TSMM runtime governance semantics and TIS v0.10.0 artifacts as evaluator evidence. ANAB v0.10.0 can publish references to TIS artifacts and AIS-1 v0.2 extension evidence as part of agent-name assurance declarations. DCAS does not copy or replace TIS schemas and does not redefine TSMM semantics.

AIS-1 v0.2 is evaluated as a bounded identity and accountability input. It does not prove delegated authority, runtime authorization, or message provenance.

## Operational note

If TSMM changes runtime governance semantics, or TIS changes runtime governance projection, authority boundary, Trust Task, status-list, decision receipt, evidence bundle, or registry publication artifacts, maintainers SHOULD open a drift review before issuing a new DCAS or ANAB minor release.

If AIS-1 changes ALA/SOA classification, `parentDid`, DID resolution, registry status, timestamp service references, Assurance Container semantics, or SOA cascade revocation rules, maintainers SHOULD open a standards drift review before issuing a new DCAS minor release.
