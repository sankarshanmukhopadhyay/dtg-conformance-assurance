# DCAS methodology

DCAS is a pragmatic methodology for producing reviewable, risk-proportionate conformance and assurance claims.

At a high level, DCAS uses a traceability spine:

**Risks → Control Objectives → Evidence → Evaluation outcome**

## Key roles

- **Issuer:** produces an evidence bundle and a claim (what is asserted, at what assurance level, under which profile).
- **Verifier / assessor:** evaluates the evidence and reproduces checks to reach an outcome.
- **Relying party:** consumes outcomes and decides whether the residual risk is acceptable.

## Building blocks

### Conformance profiles
A profile defines what is in scope for a claim (issuer responsibilities, verifier expectations, required artifacts).

### Assurance levels (AL1–AL4)
Assurance levels define the strength of evidence and evaluation rigor required. See `conformance/assurance_levels.md`.

### Control objectives
Control objectives are the “what must be true” statements that connect risk to evidence and are designed to be testable (CSV-first).

### Evidence bundles
Evidence is packaged as bundles with machine-readable rows (CSV) and optional narrative context (Markdown). Templates live under `templates/`.

### Evaluation outcomes
Evaluation is a structured process that results in an outcome such as pass, conditional pass, fail, or needs-more-evidence.

## Interop with other repositories

DCAS is designed to interoperate with a broader trust infrastructure ecosystem (e.g., trust registries, conformance test suites, assurance hubs).

This repository focuses on the portable artifact layer: profiles, assurance levels, control objectives, evidence templates, and evaluation guidance.
