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
