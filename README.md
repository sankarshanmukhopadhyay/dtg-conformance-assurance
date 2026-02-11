# DTG Conformance & Assurance

DTG Conformance & Assurance provides the **risk, control, conformance, and assurance foundations**
for Decentralized Trust Graph (DTG) ecosystems.

This repository consolidates artefacts and specifications that enable **explicit, reviewable,
and risk-proportionate trust claims** across decentralized systems.

---

## Start here

If you are new to this repository, begin with:

- 📄 **[DCAS Positioning Note](04_spec/DCAS_Positioning.md)**  
  A one-page overview explaining *why* DCAS exists, what problems it addresses, and what it does
  (and does not) attempt to standardize.

- 📘 **[DCAS v0.1 Draft Specification](04_spec/DCAS_v0.1.md)**  
  The working-group draft defining the conceptual model, terminology, and structure for
  risk-based conformance and assurance in DTG ecosystems.

---

## What this repository contains

This repository brings together the artefacts required to move from **implicit governance**
to **operational, auditable assurance**:

- **Risk assessment**
  - Risk taxonomy and risk assessment worksheets
  - Structured risk → control mappings

- **Control objectives**
  - Outcome-focused control objectives derived from risk
  - Alignment across governance, technical, and operational layers

- **Conformance profiles**
  - Role-specific groupings of control objectives
  - Minimum assurance expectations per actor class

- **Assurance**
  - Assurance levels that scale rigor with risk
  - Evidence and testing expectations

- **Specification and schemas**
  - DCAS draft specification and annexes
  - Machine-readable schemas for conformance declarations

- **Governance**
  - Decision logs, release checklists, and review cadence
  - GitHub-native workflows for review and change control

---

## Repository structure (high level)

- `01_risk/` — risk assessment source artefacts, mappings, and exports  
- `02_controls/` — control objectives, evidence catalogues, and test definitions  
- `03_conformance/` — conformance profiles and assurance levels  
- `04_spec/` — DCAS draft specification, positioning note, annexes, and schemas  
- `05_governance/` — decision log, release checklist, and review cadence  
- `tools/` — helper scripts for export, validation, and CI integration  

---

## Working conventions

- **XLSX is the canonical authoring format** for structured artefacts  
- **CSV is the GitHub review surface** for diffs and pull requests  
- All changes land via **pull requests to `main`**  
- Decisions that change meaning or requirements are **explicitly recorded**

---

## Status

This repository contains **working-group drafts**.  
Nothing here should be treated as a final standard, certification scheme, or compliance mandate
without explicit WG approval and versioned release.

---

## Contributing

Contributions are welcome via issues and pull requests.  
Please follow the governance and review processes defined in `05_governance/`.

