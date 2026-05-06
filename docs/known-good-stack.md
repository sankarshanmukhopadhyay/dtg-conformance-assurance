# Known-good stack

**Last reviewed:** 2026-05-06

| Component | Version | Role |
| --- | --- | --- |
| trust-infrastructure-schemas | v0.9.0 | Canonical DTG/OpenVTC/VTI runtime trust artifact schemas and compatibility matrix |
| dtg-conformance-assurance | v0.8.0 | Evaluation method for TIS-backed runtime evidence |
| agent-name-assurance-baseline | v0.9.0 | Domain baseline for named agents and public trust surfaces |

## Compatibility statement

This is an additive, non-breaking alignment set. DCAS v0.8.0 consumes TIS v0.9.0 artifacts as evaluator evidence. ANAB v0.9.0 can publish references to TIS v0.9.0 artifacts as part of agent-name assurance declarations. Neither repo copies or replaces TIS schemas.

## Operational note

If TIS changes any DTG, OpenVTC, VTI, decision receipt, or evidence bundle schema, maintainers SHOULD open a drift review before issuing a new DCAS or ANAB minor release.
