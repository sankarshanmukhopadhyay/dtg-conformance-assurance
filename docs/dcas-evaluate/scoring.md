# Scoring and confidence rubric

DCAS uses **score + confidence**, because ecosystems are messy and evidence is rarely perfect.

## Score

Score is a 0–4 scale per control:

- **0 — Not implemented**: control absent, no credible evidence.
- **1 — Partial**: some implementation, inconsistent, weak evidence.
- **2 — Implemented**: implemented with basic evidence; gaps exist.
- **3 — Verified**: implemented and verified via tests; gaps are minor and tracked.
- **4 — Robust**: verified and continuously monitored; incident learnings feed improvements.

## Confidence

Confidence reflects the quality of evaluation:

- **Low**: limited evidence, limited testability, significant reliance on assertions.
- **Medium**: evidence is present; some tests executed; sampling is reasonable.
- **High**: evidence is strong; tests executed; sampling is justified; traceability is complete.

## How AL influences expectations

- **AL0** favors *declarations* and basic documentation.
- **AL1** expects consistent evidence and basic test checks.
- **AL2** expects audit trails, versioning, and repeatability.
- **AL3** expects stronger independence, immutability, and higher assurance on critical controls.

## Reporting

Every score MUST include:
- evidence references (EV-###)
- tests executed (TS-###)
- rationale for confidence
