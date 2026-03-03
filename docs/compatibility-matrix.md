# Compatibility matrix

This matrix is a lightweight coordination tool to prevent cross-repo drift. It documents the current interoperability posture across the ecosystem.

| Repository | Repo version (declared) | Canonical AL model | Control ID namespace | Conformance declaration schema | Evidence bundle expectations |
| --- | --- | --- | --- | --- | --- |
| `schemas` | N/A (schema repo) | `AL-Model-Version: 1.0` (canonical) | N/A | N/A | N/A |
| `dtg-conformance-assurance` (DCAS) | See `DCAS_METHOD_VERSION` | References `schemas` AL model | `DCAS-*` (method-level) | DCAS declaration templates | DCAS evidence bundle structure |
| `agent-name-assurance-baseline` (ANAB) | See README / badges | References `schemas` AL model | `ANAB-*` | ANAB conformance declarations | ANAB evidence bundles, evaluable via DCAS |

## Notes

- Repositories MUST not redefine AL semantics. If AL changes are needed, update the canonical document in `schemas`.
- If declaration schemas are extended, prefer extension schemas that reference canonical `$id` values instead of copying schema bodies.

