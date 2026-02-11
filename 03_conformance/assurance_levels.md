# Assurance Levels (AL0–AL3)

This document defines the normative assurance level model for DCAS v0.1.

Assurance Levels (ALs) indicate the **degree of confidence** that a conformance
profile has been satisfied. They do not change what requirements apply.
They change how rigorously those requirements are substantiated.

Assurance Levels are orthogonal to Conformance Profiles.

---

## 1. Conceptual Model

Assurance Level reflects increasing rigor across four dimensions:

1. **Independence** — Who performs the evaluation?
2. **Depth** — How comprehensive is the evidence and testing?
3. **Formalization** — How structured and repeatable is the evaluation?
4. **Continuity** — Is assurance point-in-time or ongoing?

Each successive AL increases one or more of these dimensions.

---

## 2. AL0 — Declared Conformance

AL0 represents unverified declaration.

### Characteristics

- Conformance is asserted by the actor.
- Evidence MAY exist but is not independently reviewed.
- Tests MAY be internal or informal.
- No independent evaluation is required.
- Assurance is point-in-time.

### Intended Use

- Early-stage ecosystems
- Pilot deployments
- Low-impact or low-risk environments

AL0 SHALL NOT be used where ecosystem-wide systemic risk is material unless explicitly documented as risk acceptance.

---

## 3. AL1 — Documented & Reviewable

AL1 introduces structured internal validation.

### Characteristics

- Conformance is supported by documented evidence.
- Evidence is attributable and time-bound.
- Defined tests exist and are repeatable.
- Evaluation may be performed internally but follows documented procedures.
- Results are reviewable by ecosystem participants.

### Intended Use

- Production environments with moderate impact
- Community-governed ecosystems
- Baseline public trust signaling

AL1 requires that evidence and test procedures be sufficiently structured to enable external review, even if not independently performed.

---

## 4. AL2 — Independent Assessment

AL2 introduces evaluation independence.

### Characteristics

- Conformance is evaluated by a party independent of operational implementation.
- Evidence depth includes sampling, behavioral verification, or inspection beyond documentation review.
- Tests follow defined criteria with pass/fail thresholds.
- Findings are documented.
- Reassessment occurs periodically.

Independence may be organizational, structural, or contractual, provided conflicts of interest are disclosed.

### Intended Use

- High-value issuance
- Cross-ecosystem interoperability
- Situations where failure would have material financial, reputational, or societal impact

AL2 establishes credible external assurance without requiring full certification infrastructure.

---

## 5. AL3 — Continuous & High-Assurance

AL3 represents the highest level of rigor in DCAS v0.1.

### Characteristics

- Independent evaluation with formal methodology.
- Deep evidence inspection and adversarial testing where appropriate.
- Continuous or near-real-time monitoring of critical controls.
- Cryptographic or tamper-evident logging where applicable.
- Defined remediation timelines for non-conformance.

AL3 MAY incorporate automated verification pipelines and continuous attestation.

### Intended Use

- Systemically critical ecosystems
- High-blast-radius actors
- Regulatory or public infrastructure contexts
- Delegated authority models where compromise has cascading effects

AL3 SHOULD be used where governance failures could materially undermine ecosystem legitimacy.

---

## 6. Comparative Summary

| Dimension      | AL0 | AL1 | AL2 | AL3 |
|---------------|------|------|------|------|
| Declaration   | Self | Structured | Structured | Structured |
| Independence  | None | Internal | Independent | Independent |
| Evidence Depth| Minimal | Documented | Verified | Deep + Monitored |
| Testing       | Informal | Repeatable | Formal | Formal + Adversarial |
| Continuity    | Point-in-time | Periodic | Periodic | Continuous |

---

## 7. Normative Requirements

- A conformance profile SHALL declare a minimum required AL.
- An actor SHALL NOT claim a higher AL without meeting the defined characteristics.
- Ecosystems SHALL document how independence is achieved at AL2 and AL3.
- Assurance level claims SHOULD reference evidence and tests used in evaluation.

---

## 8. Future Work

Future versions of DCAS MAY:
- Subdivide ALs
- Define sector-specific AL mappings
- Formalize accreditation expectations

No such extensions are implied by v0.1.
