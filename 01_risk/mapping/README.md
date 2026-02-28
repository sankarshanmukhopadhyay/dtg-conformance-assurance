# Risk-to-Control Objective Mapping

This folder captures the *traceability spine* between the risk register and DCAS control objectives.

## Files

- `risk_to_control_objectives.csv` — normative mapping of **Risk ID → Control Objective ID** (CO).
  - A risk MAY map to multiple COs.
  - A CO SHOULD map to at least one risk.

## How to use

1. Start with `01_risk/exports/risk_assessment.csv` (the risk register export).
2. Join on `Risk ID` using `risk_to_control_objectives.csv`.
3. Use `02_controls/control_catalog.csv` to map **CO → Controls → Evidence → Tests**.
4. Generate a coverage report (see `01_risk/reports/coverage_summary.md`).

## Mapping principles

- Mappings prioritize *testability* and *implementation neutrality*.
- When a risk is systemic, mapping targets the **governance or operational** COs that actually move the needle.
