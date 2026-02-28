# Coverage summary

This report summarizes coverage across:

**Risks → Control Objectives → Controls → Evidence → Tests**

Generated from:
- `risk/exports/risk_assessment.csv`
- `risk/mapping/risk_to_control_objectives.csv`
- `controls/control_catalog.csv`
- `controls/evidence_catalog.csv`
- `controls/test_suites.csv`

## Snapshot

- Risks (total): **50**
- Mapped risks (Risk → CO): **50**
- Control objectives referenced: **22**
- Controls in catalog: **22**
- Evidence items in catalog: **15**
- Tests in catalog: **15**

## Risk coverage

All risks have at least one mapped control objective.

- Unmapped risks: **0**

## Control objective coverage

All mapped control objectives have:
- a definition in `controls/control_objectives.md`
- at least one mapped control in `controls/control_catalog.csv`

- COs without controls: **0**
- COs without definitions: **0**

## Risks by category

| Category | Count |
|---|---:|
| AI Agents | 5 |
| Credentials | 5 |
| Cryptography | 5 |
| External | 5 |
| Governance | 5 |
| Human Experience | 5 |
| Identity | 5 |
| Network Managers | 5 |
| Schemas | 5 |
| Systemic | 5 |

## Top control objectives by mapped risks

| Control Objective ID | Risk count |
|---|---:|
| CO3.3 | 5 |
| CO1.1 | 4 |
| CO4.2 | 4 |
| CO2.1 | 4 |
| CO2.3 | 4 |
| CO3.1 | 3 |
| CO5.2 | 3 |
| CO1.4 | 2 |
| CO1.3 | 2 |
| CO3.2 | 2 |

## Notes

This is a **minimum viable** control/evidence/test spine intended to make the repository executable for adopters.
Future releases should expand:
- control granularity (more controls per CO)
- automated test coverage
- richer evidence bundle examples and sample data
