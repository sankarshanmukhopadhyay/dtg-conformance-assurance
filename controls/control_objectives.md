# Control Objectives (DCAS)

Control objectives (COs) define *what must be true* for a DTG ecosystem to operate within acceptable risk bounds.

They are:

- **Testable** (you can check them)
- **Implementation-neutral** (no specific tech mandated)
- **Traceable** (they map to risks and evidence)

## Canonical registry (CSV)

The primary registry is:

- `controls/control_objectives.csv`

Each control objective has a stable `control_objective_id` (e.g., `CO1.4`) that is referenced by:
- risk → control mappings (`risk/mapping/risk_to_control_objectives.csv`)
- evidence bundles (`templates/starter-bundle/`)

## v0.10.0 AIS-1 v0.2 additions

DCAS v0.10.0 adds three AIS-1 v0.2 evaluator objectives:

| Control objective | Purpose |
|---|---|
| `CO3.9` | Validate SOA parent-chain state before relying on an AIS-1 subordinate operating agent |
| `CO4.8` | Check AIS-1 v0.2 evidence sufficiency, including DID resolution, registry status, bond hash, tier, issuer, timestamp, and assurance-container evidence |
| `CO6.6` | Test cascade revocation and fail-safe behavior when AIS-1 bond, parent ALA, registry, or timestamp evidence is stale or unavailable |

## How to extend

If you add new control objectives:
1. Add a new row to `controls/control_objectives.csv`
2. Update mappings under `risk/mapping/` as needed
3. Run `make validate` to ensure references remain consistent
