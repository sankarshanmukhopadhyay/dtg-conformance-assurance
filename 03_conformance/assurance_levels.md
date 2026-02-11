# Assurance Levels (AL0–AL3)  
**Normative for DCAS v0.1**

This document defines the normative Assurance Level (AL) model for DCAS v0.1.

Assurance Levels indicate the **degree of confidence** that a conformance profile has been satisfied.  
Assurance Levels do **not** change which requirements apply. They change how rigorously conformance is substantiated.

Assurance Levels are **orthogonal** to Conformance Profiles.

---

## 1. Assurance Dimensions

Assurance Levels scale across four dimensions:

1. **Independence** — separation between the subject being evaluated and the evaluator.
2. **Evidence depth** — completeness, integrity, and coverage of evidence.
3. **Test rigor** — clarity of pass/fail criteria and repeatability of evaluation.
4. **Continuity** — point-in-time vs periodic vs continuous assurance.

Each successive AL increases one or more dimensions.

---

## 2. AL0 — Declared Conformance

AL0 represents self-declared conformance without required independent review.

### 2.1 Required characteristics
At AL0:
- The actor **SHALL** declare a profile claim and scope.
- Evidence **MAY** exist but **SHALL NOT** be represented as independently assessed.
- Tests **MAY** exist but are not required to be repeatable or externally reviewable.

### 2.2 Constraints
AL0 **SHALL NOT** be used for profiles that mitigate material ecosystem-wide risk unless the ecosystem explicitly records risk acceptance and residual risk rationale.

---

## 3. AL1 — Documented & Reviewable

AL1 introduces structured evaluation with reviewable artefacts.

### 3.1 Required characteristics
At AL1:
- The actor **SHALL** maintain documented evidence sufficient to substantiate the claimed controls.
- Evidence **SHALL** be attributable (actor identity), time-bound (coverage window), and retrievable for review.
- Tests or evaluation procedures **SHALL** exist and **SHALL** be repeatable.
- Findings **SHALL** be recorded in a reviewable form.

### 3.2 Independence
Independence is **not required** at AL1. However:
- Evidence and procedures **SHALL** be structured so that an external reviewer could evaluate them.

---

## 4. AL2 — Independent Assessment

AL2 introduces independent evaluation and stronger substantiation.

### 4.1 Required characteristics
At AL2:
- Evaluation **SHALL** be performed by an assessor independent of operational implementation.
- Evidence depth **SHALL** include verification beyond documentation review, such as sampling, behavioral verification, or inspection.
- Tests **SHALL** specify pass/fail criteria for the evaluated scope.
- Findings **SHALL** include scope, coverage window, and outcome summary.

### 4.2 Independence requirements
For AL2, independence **SHALL** satisfy all of the following:
- The assessor **SHALL NOT** be the same operational team responsible for implementing the controls.
- Conflicts of interest **SHALL** be disclosed.
- The ecosystem **SHALL** document the independence model (organizational, contractual, or structural).

If independence cannot be established, the claim **SHALL NOT** be represented as AL2.

### 4.3 Periodicity
AL2 claims **SHALL** declare a coverage window and **SHALL** define reassessment cadence appropriate to risk.

---

## 5. AL3 — Continuous & High-Assurance

AL3 represents the highest rigor level in DCAS v0.1, emphasizing continuous substantiation for critical controls.

### 5.1 Required characteristics
At AL3:
- The evaluation model **SHALL** include independent assessment (as per AL2).
- Evidence for critical controls **SHALL** be integrity-protected and tamper-evident where feasible.
- Monitoring for critical controls **SHALL** be continuous or near-real-time.
- Tests **SHALL** include deep inspection and MAY include adversarial testing where appropriate to threat models.
- Remediation expectations **SHALL** be defined for non-conformance (e.g., response windows and escalation paths).

### 5.2 Constraints
AL3 does not require public disclosure of sensitive evidence.  
However, AL3 claims **SHALL** include integrity anchors and defined audit access mechanisms where evidence is restricted.

---

## 6. Minimum Requirements Matrix (Normative)

The following matrix defines minimum normative requirements per AL.

| Requirement | AL0 | AL1 | AL2 | AL3 |
|---|---|---|---|---|
| Declared profile claim and scope | SHALL | SHALL | SHALL | SHALL |
| Evidence attributable and time-bound | MAY | SHALL | SHALL | SHALL |
| Evidence retrievable for review | MAY | SHALL | SHALL | SHALL |
| Repeatable evaluation procedure | MAY | SHALL | SHALL | SHALL |
| Defined pass/fail criteria | MAY | SHOULD | SHALL | SHALL |
| Independent assessor | NO | NO | SHALL | SHALL |
| Independence model documented | NO | NO | SHALL | SHALL |
| Verified evidence beyond document review | NO | SHOULD | SHALL | SHALL |
| Continuous/near-real-time monitoring for critical controls | NO | NO | NO | SHALL |
| Integrity protection for critical evidence | NO | SHOULD | SHALL | SHALL |

Notes:
- “Critical controls” are controls whose failure has high blast radius or high-impact harm as defined by the ecosystem risk model.

---

## 7. Assurance Claim Requirements (Normative)

An assurance claim SHALL include:
- Actor identifier
- Actor class
- Profile identifier
- Claimed assurance level
- Coverage window (from/to timestamps)

Additionally:
- AL1+ claims **SHALL** include references to evidence and/or tests used.
- AL2+ claims **SHALL** identify the assessor and disclose the independence model.
- AL3 claims **SHALL** include monitoring description for critical controls and integrity anchors where evidence is restricted.

---

## 8. Use with Profiles and Risk

- Conformance profiles **SHALL** declare a minimum AL.
- Ecosystems **SHOULD** require AL2 or AL3 where failures create systemic risk, high-value fraud exposure, or high blast radius harms.
- Where a profile requires AL2/AL3 but actors only meet AL1/AL0, the ecosystem **SHALL** treat the actor as non-conforming for that profile.

---

## 9. Versioning and evolution

- Changes that modify AL semantics SHALL be treated as breaking or semantic changes and recorded via the Decision Log.
- Ecosystems claiming alignment with DCAS v0.1 SHALL disclose the version of this AL definition they apply.
