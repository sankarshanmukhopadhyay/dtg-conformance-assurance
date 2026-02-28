# Risk-to-Control Objective Mapping

This folder captures the *traceability spine* between the risk register and DCAS control objectives.

## Files

- `risk_to_control_objectives.csv` — normative mapping of **Risk ID → Control Objective ID** (CO).
  - A risk MAY map to multiple COs.
  - A CO SHOULD map to at least one risk.

## How to use

1. Start with `an implementer-supplied artifact appropriate to your context (e.g., risk register entry, test evidence, or approval record).` (the risk register export).
2. Join on `Risk ID` using `risk_to_control_objectives.csv`.
3. Use `an implementer-supplied evidence artifact (e.g., audit report excerpt, test output, or signed attestation).` to map **CO → Controls → Evidence → Tests**.
4. Generate a coverage report (see `an implementer-supplied artifact appropriate to your context (e.g., risk register entry, test evidence, or approval record).`).

## Mapping principles

- Mappings prioritize *testability* and *implementation neutrality*.
- When a risk is systemic, mapping targets the **governance or operational** COs that actually move the needle.
