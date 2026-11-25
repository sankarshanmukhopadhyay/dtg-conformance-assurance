# FAQ

## Is DCAS a certification program?
No. DCAS provides **structures and artifacts** that ecosystems can use for risk-based conformance and assurance.
Certification and regulation are out of scope.

## What is an Assurance Level (AL)?
AL1–AL4 describe increasing expectations for what must be true and what evidence must be available.
See `conformance/assurance_levels.md`.

## What formats does this repo prefer?
**CSV-first.** CSV is the default interchange format for templates and mappings.
XLSX exists only as an optional convenience for teams maintaining a spreadsheet source.

## What should I adopt first?
Start with the issuer bundle:
- `templates/starter-bundle/`
- validate with `make validate`

## How do extensions work?
Add optional columns prefixed with `x_` (e.g., `x_ticket_url`). Core columns remain stable for interoperability.


## Does DCAS support AIS-1?

DCAS includes an **experimental** AIS-1 profile. It allows verifiers to assess whether an AIS-1 surface is coherent enough to use as an identity-and-accountability input. It does not treat AIS-1 as a complete delegation or provenance layer.

## Does a passing test run establish assurance?

No. A test outcome supports a bounded proposition under recorded conditions. The experimental [Trust Tasks integration](tt-conformance-evidence-integration.md) preserves that scope and requires reviewed mappings and positive anchors. A normalized PASS is conditional on the assessor's evidence and is not certification or runtime authorization.

## Why does a legacy evaluator example no longer pass?

The unreleased 0.2 evaluator requires explicit requirement-to-evidence bindings. Historical 0.1 results remain auditable, but current reliance needs reassessment. See [migration guidance](reference-evaluator.md).
