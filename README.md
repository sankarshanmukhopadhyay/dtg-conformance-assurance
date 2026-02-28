# DTG Conformance & Assurance (DCAS)

This repository publishes **DCAS (Decentralized Conformance and Assurance Standard)** artifacts for Decentralized Trust Graph (DTG) ecosystems.

DCAS is a practical, implementation-neutral way to move from **implicit trust** to **explicit, reviewable, risk-proportionate trust claims**.

---

## Start here (new to the repo)

- **Adoption guide (role-based):** `docs/start-here.md`
- **Repository map:** `docs/repo-map.md`
- **FAQ:** `docs/FAQ.md`

## Read the DCAS documents

- **DCAS Positioning Note:** `04_spec/DCAS_Positioning.md`
- **DCAS v0.1 Draft Specification:** `04_spec/DCAS_v0.1.md`
- **Assurance levels (AL1–AL4):** `03_conformance/assurance_levels.md` (aligned to canonical model in the `schemas` repository)

---

## How to use this repo (end-to-end)

DCAS is organized as a traceability chain:

**Risks → Control Objectives → Controls → Evidence → Tests → Assurance output**

1. Start with the risk register export: `01_risk/exports/risk_assessment.csv`
2. Map risks to control objectives (COs): `01_risk/mapping/risk_to_control_objectives.csv`
3. Use catalogs to enumerate what to implement and prove:
   - control objectives: `02_controls/control_objectives.md`
   - controls: `02_controls/control_catalog.csv`
   - evidence: `02_controls/evidence_catalog.csv`
   - tests: `02_controls/test_suites.csv`
4. Select your conformance profile: `03_conformance/profiles/`
5. Produce an assurance outcome using the evaluation method: `docs/dcas-evaluate/`

---

## DCAS Evaluate (method)

DCAS Evaluate turns the repo into a **repeatable assessment workflow**:

- method entry: `docs/dcas-evaluate/README.md`
- report template: `docs/dcas-evaluate/report-template.md`
- evidence checklist: `docs/dcas-evaluate/evidence-checklist.md`
- scoring + confidence rubric: `docs/dcas-evaluate/scoring.md`
- method version: `DCAS_METHOD_VERSION`

---

## Roadmap

- `docs/roadmap.md`

---

## Tooling

- Export risk register XLSX → CSV: `python tools/export_xlsx_to_csv.py`
- Validate risk export: `python tools/validate_csv.py`

See `tools/README.md` for details.

---

## License

See `LICENSE`.
