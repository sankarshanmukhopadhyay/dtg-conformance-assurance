# Start here: adopting DCAS for DTG ecosystems

This repository publishes **DCAS (Decentralized Conformance and Assurance Standard)** artifacts for DTG ecosystems.

DCAS is not a certification scheme. It is a **shared, testable vocabulary** for:
- expressing ecosystem risks,
- defining control objectives and controls,
- producing evidence,
- running assurance checks (AL0–AL3),
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
1. a **conformance claim** for your actor class (`03_conformance/examples/`)
2. an **evidence bundle** aligned to controls (`02_controls/`)
3. an **assurance report** using the evaluation method (`docs/dcas-evaluate/`)

## Core artifacts

- **Risk register export**: `01_risk/exports/risk_assessment.csv`
- **Risk → CO mapping**: `01_risk/mapping/risk_to_control_objectives.csv`
- **Control objectives**: `02_controls/control_objectives.md`
- **Control catalog**: `02_controls/control_catalog.csv`
- **Evidence catalog**: `02_controls/evidence_catalog.csv`
- **Test suite catalog**: `02_controls/test_suites.csv`
- **Assurance levels**: `03_conformance/assurance_levels.md`
- **DCAS spec**: `04_spec/DCAS_v0.1.md`

## Next

Run the DCAS evaluation workflow: `docs/dcas-evaluate/README.md`
