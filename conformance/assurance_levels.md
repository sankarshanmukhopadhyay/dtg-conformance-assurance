# Assurance Levels (AL1–AL4) in DCAS

**Normative source:** The canonical AL model is defined in the `schemas` repository at `assurance/assurance-levels.md`.

This document explains how DCAS uses Assurance Levels to parameterize **evidence strength** and **evaluation rigor**. Assurance Levels do **not** change which requirements apply. They change how rigorously conformance is substantiated.

## How DCAS uses AL

DCAS treats AL as an “auditability dial”:

- At lower ALs, evidence can be **self-attested** and structurally complete.
- At higher ALs, evidence MUST become **verifiable**, then **independently reviewed**, and finally **continuously monitored**.

## Evidence expectations (operational guidance)

| Assurance Level | Evidence posture | Typical evaluation stance |
| --- | --- | --- |
| AL1 | Structured, internally produced evidence. Basic completeness and internal consistency. | Lightweight validation, clear gaps called out. |
| AL2 | Verifiable evidence (cryptographic integrity, provenance, issuer binding where applicable). | Validation includes verification checks and artifact integrity. |
| AL3 | Independent review and documented remediation closure. | Evaluation includes assessor review and challenge-response. |
| AL4 | Continuous monitoring, audit-grade logging, and strong governance controls with periodic external assessment. | Evaluation assumes ongoing assurance, not point-in-time claims. |

## Where AL appears in DCAS artifacts

- Conformance declarations include an explicit `assurance_level` claim.
- Evidence bundles are expected to justify the declared AL via artifacts and references.
- Evaluation reports SHOULD state the achieved AL and the limiting factors (what prevented a higher AL).

## Drift prevention

DCAS intentionally avoids re-defining AL semantics. If you believe the canonical AL model needs adjustment, propose changes upstream in `schemas` and then update DCAS operational guidance accordingly.

