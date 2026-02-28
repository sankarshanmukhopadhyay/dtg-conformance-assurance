# Coverage summary

This document defines the intended coverage view across the DCAS spine:

**Risks → Control Objectives → Evidence → Evaluation results**

## Inputs (CSV-first)

- Risk export: `risk/exports/risk_assessment.csv`
- Risk → control mapping: `risk/mapping/risk_to_control_objectives.csv`
- Control objectives: `controls/control_objectives.csv`
- Bundle outputs (issuer submissions): `templates/starter-bundle/` structure

## Recommended reporting outputs

A minimal coverage report should answer:

1. Which risks are in-scope?
2. Which control objectives mitigate each risk?
3. Which control objectives have evidence attached?
4. Which checks passed/failed/partial?

## Automation

This repo currently validates *structure and link integrity* via `make validate`.
Coverage report generation can be added as a future tooling increment once adopters converge on bundle conventions.
