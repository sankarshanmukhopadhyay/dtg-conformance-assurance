# Start here: adopting DCAS for DTG ecosystems

This repository publishes **DCAS (Decentralized Conformance and Assurance Standard)** artifacts for DTG ecosystems.

DCAS is not a certification scheme. It is a **shared, testable vocabulary** for:
- expressing ecosystem risks,
- defining control objectives and controls,
- producing evidence,
- running assurance checks (AL1–AL4),
- publishing conformance claims.

## Quick paths (choose your role)

- **Ecosystem operator / Governance authority** → `docs/roles/governance-authority.md`
- **Registry / trust list operator** → `docs/roles/registry-operator.md`
- **Network manager** → `docs/roles/network-manager.md`
- **Issuer** → `docs/roles/issuer.md`
- **Verifier** → `docs/roles/verifier.md`
- **Holder / agent implementer** → `docs/roles/holder-agent.md`
- **Auditor / assessor** → `docs/roles/auditor-assessor.md`
- **Tool builder** → `docs/roles/tool-builder.md`

## What is “done” when you adopt DCAS?

At minimum, you should be able to produce:
1. a **conformance claim** for your actor class (`conformance/examples/`)
2. an **evidence bundle** aligned to controls (`controls/`)
3. an **assurance report** using the evaluation method (`docs/dcas-evaluate/`)

## Core artifacts

- **Risk register export**: `risk/exports/risk_assessment.csv`
- **Risk → CO mapping**: `risk/mapping/risk_to_control_objectives.csv`
- **Control objectives**: `controls/control_objectives.md`
- **Control catalog**: `controls/control_catalog.csv`
- **Evidence catalog**: `controls/evidence_catalog.csv`
- **Test suite catalog**: `controls/test_suites.csv`
- **Assurance levels**: `conformance/assurance_levels.md`
- **DCAS spec**: `spec/DCAS_v0.1.md`

## Next

Run the DCAS evaluation workflow: `docs/dcas-evaluate/README.md`
