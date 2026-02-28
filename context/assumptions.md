# Assumptions and boundaries

This repository defines **DTG Conformance & Assurance** artifacts: schemas, example claims, and guidance for how to produce verifiable conformance statements.

## Operating assumptions
- Implementers operate an internal governance system (policies, change control, risk register, audit trail) that is authoritative for their organization.
- Evidence artifacts may contain sensitive information; published examples MUST be sanitized or synthetic.
- Assurance Levels (AL1–AL4) define *rigor of evidence and review*, not an absolute measure of “trust”.

## Boundaries
- This repo defines *what must be true* and *what evidence must exist* for a claim at each AL.
- This repo does not mandate a single risk methodology; it is compatible with multiple approaches (risk registers, threat models, controls frameworks).

## How to use this
When a document refers to an “implementer-supplied artifact”, provide the equivalent record from your governance system (e.g., a risk register entry, test run output, or approval record).
