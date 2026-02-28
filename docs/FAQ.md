# FAQ

## Is DCAS a certification program?
No. DCAS provides **structures and artifacts** that ecosystems can use for risk-based conformance and assurance.
Certification, procurement, or regulation is out of scope for this repository.

## What is an Assurance Level (AL)?
AL1–AL4 describe increasing rigor for evidence and testing. See `an implementer-supplied evidence artifact (e.g., audit report excerpt, test output, or signed attestation).`.

## What should I publish to be “DCAS-aligned”?
At minimum:
- a conformance claim (example formats in `conformance/examples/`)
- a minimal evidence bundle mapped to controls (`controls/`)
- an assurance report produced via `docs/dcas-evaluate/`

## How do I map a risk to what I should do?
Use:
1. `an implementer-supplied artifact appropriate to your context (e.g., risk register entry, test evidence, or approval record).`
2. `an implementer-supplied artifact appropriate to your context (e.g., risk register entry, test evidence, or approval record).`
3. `an implementer-supplied evidence artifact (e.g., audit report excerpt, test output, or signed attestation).` (CO → controls → evidence/tests)

## Is DCAS tied to a specific DID method, ledger, or product?
No. DCAS is explicitly implementation-neutral.
