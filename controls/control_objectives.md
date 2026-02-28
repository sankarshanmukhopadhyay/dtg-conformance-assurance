# Control Objectives (DCAS)

Control objectives (COs) define *what must be true* for a DTG ecosystem to operate within acceptable risk bounds.
They are **testable**, **implementation-neutral**, and **scope-bounded**.

- Canonical spec context: `an implementer-supplied artifact appropriate to your context (e.g., risk register entry, test evidence, or approval record).` (Section 6).
- Control catalog mapping: `an implementer-supplied artifact appropriate to your context (e.g., risk register entry, test evidence, or approval record).`

## Control objectives

| CO ID | Name | Applicability | Layer | Nature | Risk linkage (examples) | External alignment (informative) |
|---|---|---|---|---|---|---|
| CO1.1 | Governance coherence & role clarity | Governance Authority; Network Manager; Registry Operator | Governance | Preventive/Corrective | EX3, G1, G4, NM5 | ISO/IEC 38500; ToIP Governance Metamodel |
| CO1.2 | Anti-capture & multi-stakeholder checks | Governance Authority | Governance | Preventive/Detective | G2 | ToIP Governance Metamodel; OECD AI principles (informative) |
| CO1.3 | Transparent adjudication & auditability | Governance Authority; Registry Operator | Governance/Operational | Detective | EX4, G5 | ISO 27001 logging controls; NIST SP 800-53 AU (informative) |
| CO1.4 | Change control & versioning | Governance Authority; Registry Operator; Network Manager | Governance/Technical | Preventive/Corrective | G3, S4 | SemVer; ToIP change management patterns |
| CO2.1 | Registry integrity & authenticity | Registry Operator | Technical | Preventive/Detective | CR3, S1, S3, S5 | NIST SP 800-63 (informative); ISO 27001 A.8 |
| CO2.2 | Registry transparency & publication | Registry Operator; Network Manager | Operational | Preventive/Detective | CR5, EX5 | W3C data integrity (informative) |
| CO2.3 | Registry dispute & redress process | Registry Operator; Governance Authority | Governance/Operational | Corrective | CR1, CR2, CR4, NM4 | ISO 10002 complaints handling (informative) |
| CO2.4 | Registry availability & continuity | Registry Operator | Operational | Preventive/Corrective | S2 | ISO 22301 BCM; NIST CP (informative) |
| CO3.1 | Issuer onboarding & authorization | Issuer; Governance Authority; Registry Operator | Operational/Governance | Preventive | ID1, ID2, NM2 | ToIP onboarding patterns; ISO 27001 supplier controls |
| CO3.2 | Credential issuance controls | Issuer | Operational/Technical | Preventive/Detective | C1, C2 | W3C VC (informative); NIST 800-53 AC/AU |
| CO3.3 | Revocation, status & lifecycle management | Issuer; Network Manager; Registry Operator | Technical/Operational | Preventive/Corrective | C3, ID4, NM3, SYS3, SYS5 | Status lists (informative); ISO 27001 A.5 |
| CO3.4 | Verifier validation & decisioning | Verifier | Technical | Detective | C4, C5 | OWASP ASVS concepts (informative); NIST 800-53 IA |
| CO4.1 | Holder/agent consent & control | Holder/Agent | Socio-technical | Preventive | ID3 | GDPR principles (informative); UX safety patterns |
| CO4.2 | Delegation & agent boundary safety | Holder/Agent; Network Manager | Socio-technical/Operational | Preventive/Detective | AI1, AI4, ID5, NM1 | Least privilege; ToIP governance delegation |
| CO4.3 | Network operations monitoring | Network Manager | Operational | Detective/Corrective | AI2, EX1 | SRE practices; NIST IR (informative) |
| CO4.4 | User-facing transparency & recourse | Holder/Agent; Verifier; Registry Operator | Human Experience | Corrective | AI3, AI5 | ISO 9241 (informative) |
| CO5.1 | Key management & compromise handling | Issuer; Registry Operator; Governance Authority | Technical | Preventive/Corrective | HX4 | NIST SP 800-57; ISO 27001 A.10 |
| CO5.2 | Signature verification & algorithm agility | Verifier; Registry Operator | Technical | Preventive/Detective | HX1, HX2, HX3 | NIST FIPS (informative) |
| CO5.3 | Cryptographic auditability | Issuer; Registry Operator | Technical/Operational | Detective | HX5 | NIST AU controls; ISO 27001 logging |
| CO6.1 | External dependency governance | All roles | Systemic | Preventive | EX2, SYS4 | ISO 27036; NIST SR (informative) |
| CO6.2 | Interoperability & schema governance | Issuer; Verifier; Registry Operator; Governance Authority | Technical/Governance | Preventive | SYS1 | SemVer; W3C best practices (informative) |
| CO6.3 | Systemic risk review & continuous improvement | Governance Authority; Network Manager | Systemic | Corrective | SYS2 | NIST CSF continuous improvement |


## Notes

- “Risk linkage” is the **traceability anchor** to `an implementer-supplied artifact appropriate to your context (e.g., risk register entry, test evidence, or approval record).` via `an implementer-supplied artifact appropriate to your context (e.g., risk register entry, test evidence, or approval record).`.
- External alignment is informative: DCAS does not import external frameworks as normative requirements.
