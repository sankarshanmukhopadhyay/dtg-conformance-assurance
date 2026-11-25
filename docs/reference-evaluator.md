# DCAS reference evaluator

The reference evaluator implements the bounded [evaluator contract](evaluator-contract.md). Install dependencies using `pip install -r requirements.txt`.

## Run

For a complete synthetic 0.2 PASS path, follow [Trust Tasks evidence integration](tt-conformance-evidence-integration.md). For legacy input:

```bash
python tools/dcas_evaluate.py conformance/examples/anab_dcas_evaluation_input.example.json --expect INDETERMINATE
python -m unittest discover -s tests -p 'test_*.py'
```

The historical ANAB input/result pair is preserved unchanged. The current evaluator deliberately does not reproduce its former PASS without explicit reviewed requirement bindings. To migrate, retain the original receipt, independently review the evidence required by each ANAB requirement, add the claim.requirement_evidence map, change contract_version to 0.2 and re-evaluate. Do not copy all evidence to every requirement without establishing relevance.

Use --output to retain a decision JSON and --expect to make a decision assertion executable in CI. Invalid JSON, schema violations or unsupported policy produce a nonzero exit rather than a decision. A successful process without --expect indicates evaluation completed, not that the assurance decision is PASS.

## Scope

This is not certification infrastructure. It does not retrieve or cryptographically validate live evidence, independently establish applicability, or redefine external baselines. The relying party is responsible for trusting the normalized input and its assessor. Contract 0.2 distinguishes contradiction, missing evidence and per-requirement sufficiency.
