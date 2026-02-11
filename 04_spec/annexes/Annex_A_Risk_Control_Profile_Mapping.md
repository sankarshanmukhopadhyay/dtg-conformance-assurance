# Annex A — Risk / Control Objective / Conformance Profile Mapping  
**Normative**

## A.1 Purpose

This annex defines the **normative mapping** between:

- risks identified in the DTG Risk Assessment Worksheet,
- control objectives that mitigate those risks, and
- conformance profiles that apply those control objectives by actor class.

This mapping is the primary traceability mechanism for DCAS v0.1.

## A.2 Normative artefacts

The normative mapping for DCAS v0.1 SHALL be maintained in:

- Risk inventory (authoritative):  
  `01_risk/source/DTG_WG_Risk_Assessment_Worksheet_Populated_From_WIP.xlsx`

- Risk → Control mapping (authoritative):  
  `01_risk/mapping/risk_to_control.xlsx`

- CSV mirror for GitHub review:  
  `01_risk/mapping/risk_to_control.csv`

If XLSX and CSV disagree, the XLSX source SHALL be treated as canonical and the CSV SHALL be regenerated.

## A.3 Mapping rules

1. Every material risk SHALL map to at least one control objective unless explicitly accepted as residual risk.
2. A control objective MAY mitigate multiple risks.
3. A risk MAY require multiple control objectives.
4. Controls included in profiles SHOULD map to risks unless explicitly marked as baseline hygiene.

## A.4 Relationship to conformance profiles

Conformance profiles (CPs) determine which actor classes are obligated to implement which control objectives.  
Profile artefacts live under `03_conformance/profiles/`.

## A.5 Mapping table (excerpt)

The complete mapping table is maintained in `01_risk/mapping/`. An excerpt is included below.

_(Mapping table not found in repo. See `01_risk/mapping/`.)_

## A.6 Required reporting

An ecosystem claiming alignment with DCAS v0.1 SHOULD be able to produce:
- unmapped risks with rationale,
- controls not linked to any risks with rationale,
- coverage summaries by category and actor class.

## A.7 Change control

Changes that alter risk/control/profile semantics SHALL be recorded per DCAS governance and the repository decision log.
