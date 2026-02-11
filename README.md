# DTG Conformance & Assurance

DTG Conformance & Assurance provides the **risk, control, conformance, and assurance foundations**
for Decentralized Trust Graph (DTG) ecosystems.

This repository consolidates:
- Risk assessment worksheets and taxonomies
- Control objectives aligned with governance and assurance needs
- Conformance profiles and assurance levels
- Evidence and test requirements
- Draft specification material for DCAS (Decentralized Conformance and Assurance Standard)
- Machine-readable schemas to enable automation and auditability

## Purpose

The goal of this project is to move DTG governance from *conceptual trust* to
**operational, reviewable, and auditable trust infrastructure**.

It is designed to support:
- Working Group review and consensus building
- Future certification and assurance programs
- Regulator- and enterprise-facing governance artefacts
- Tooling and automation built on top of DTG specifications

## Repository structure (high level)

- `01_risk/` — risk assessment source artefacts, mappings, and exports  
- `02_controls/` — control objectives, evidence catalogues, and test suites  
- `03_conformance/` — conformance profiles (CPs) and assurance levels (ALs)  
- `04_spec/` — DCAS v0.1 draft, annexes, and schemas  
- `05_governance/` — decision log, release checklist, and review cadence  
- `tools/` — helper scripts for export and validation  

## Working conventions

- **XLSX is the canonical authoring format**
- **CSV is the GitHub review surface**
- All changes land via Pull Requests
- Decisions that change meaning or requirements are recorded explicitly

## Status

This repository is a **working-group draft**. Nothing here should be treated as a
final standard without explicit WG approval and release tagging.
