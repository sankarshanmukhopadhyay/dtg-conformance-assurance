# Domain baseline composition

DCAS is most useful when it can evaluate a downstream baseline without pretending that the baseline and the evaluator are the same thing.

## Intended pattern

1. A downstream baseline emits a domain-specific declaration and evidence bundle.
2. DCAS maps that declaration to its control objectives and risk posture.
3. DCAS emits an evaluation result that preserves the original baseline identifiers for traceability.

## Why this matters

Without this discipline, evaluators often rename or flatten baseline controls during ingestion. That makes audits harder, weakens traceability, and turns cross-repo composition into manual glue work.

The example in `conformance/examples/anab_evaluation_claim.example.yaml` shows the intended posture for ANAB. The example is illustrative, but the pattern is general: preserve the baseline namespace, add DCAS evaluation semantics on top, and keep Assurance Levels anchored to the canonical OTAM model.
