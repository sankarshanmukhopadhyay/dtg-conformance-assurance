# DCAS OASF integration

## Why this matters

DCAS already knew how to evaluate declarations, evidence bundles, and profile claims. What it did not yet provide was a crisp handoff for subjects that are **discovered and described through OASF**.

That is now addressed with a small but useful integration layer.

## What is added

- OASF evaluation envelope schema: `../spec/schemas/dcas-oasf-evaluation-envelope.schema.json`
- Example evaluation envelope: `../conformance/examples/oasf_evaluation_envelope.example.json`
- Example OASF-aware ANAB evaluation claim: `../conformance/examples/oasf_anab_evaluation_claim.example.yaml`

## Evaluation pattern

1. Discover the subject through an OASF record.
2. Resolve the ANAB declaration and evidence references attached to the record or its extension surface.
3. Evaluate the published controls and evidence under DCAS.
4. Emit a DCAS claim that preserves the original OASF and ANAB references for replayable review.

## Architectural point

DCAS is still the evaluator. OASF is not an assurance engine. OASF is the publication surface from which a verifier can discover enough structured metadata to decide whether to proceed to deeper evaluation.

This keeps the layers clean:

- TSMM provides the semantics.
- OASF provides the publication surface.
- ANAB provides the domain baseline.
- DCAS provides the evaluation method.
