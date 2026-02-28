# FAQ

## Is DCAS a certification program?
No. DCAS provides **structures and artifacts** that ecosystems can use for risk-based conformance and assurance.
Certification, procurement, or regulation is out of scope for this repository.

## What is an Assurance Level (AL)?
AL0–AL3 describe increasing rigor for evidence and testing. See `03_conformance/assurance_levels.md`.

## What should I publish to be “DCAS-aligned”?
At minimum:
- a conformance claim (example formats in `03_conformance/examples/`)
- a minimal evidence bundle mapped to controls (`02_controls/`)
- an assurance report produced via `docs/dcas-evaluate/`

## How do I map a risk to what I should do?
Use:
1. `01_risk/exports/risk_assessment.csv`
2. `01_risk/mapping/risk_to_control_objectives.csv`
3. `02_controls/control_catalog.csv` (CO → controls → evidence/tests)

## Is DCAS tied to a specific DID method, ledger, or product?
No. DCAS is explicitly implementation-neutral.
