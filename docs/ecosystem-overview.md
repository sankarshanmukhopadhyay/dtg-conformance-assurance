# Ecosystem overview: schemas ↔ DCAS ↔ domain baselines

This repository (DCAS) is designed to work as part of a small ecosystem of repositories that, together, enable **reviewable, machine-checkable assurance**.

## The stack

1. **`schemas`**: the shared data contracts  
   - Canonical JSON Schemas and registries for credentials, controls, and machine-checkable declarations.
   - Canonical definition of **Assurance Levels (AL1–AL4)**.

2. **`dtg-conformance-assurance` (this repo / DCAS)**: the assurance method and evaluation kit  
   - Control objectives, evidence expectations, verifier workflow, scoring, and evaluation report templates.

3. **Domain baselines (example: `agent-name-assurance-baseline`)**: domain-specific normative requirements  
   - A concrete baseline for a specific domain that produces conformance declarations and evidence bundles that can be evaluated using DCAS.

## Data flow (end to end)

Baseline (domain)  
→ Conformance declaration (machine-checkable)  
→ Evidence bundle (artifacts + references)  
→ Evaluation (DCAS verifier workflow)  
→ Evaluation report (reviewable result)

## Actor model

- **Issuer**: claims conformance and provides evidence.
- **Verifier / Assessor**: validates claims and evaluates evidence.
- **Ecosystem operator**: defines policies, publishes registries, and sets acceptance thresholds.
- **Procurement / Governance stakeholders**: consume evaluation reports as decision instruments.

## Why this split exists

- The ecosystem needs **stable contracts** (`schemas`).
- It needs a **repeatable assurance method** (DCAS).
- It needs **domain baselines** that can evolve independently without breaking the shared contract.

## Links

- Canonical AL model: `schemas/assurance/assurance-levels.md`
- DCAS AL usage: `conformance/assurance_levels.md`
- Example baseline: Agent Name Assurance Baseline (`agent-name-assurance-baseline`)

