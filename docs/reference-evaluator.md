# DCAS reference evaluator

`tools/dcas_evaluate.py` is a deliberately thin implementation of the portable DCAS v0.1 evaluator contract. It exists to make the contract executable before a larger evaluator architecture is justified.

## Scope

The current implementation supports the bounded rules needed by the first ANAB experiment:

- current available evidence can support `PASS`;
- revoked or stale evidence produces `FAIL` unless an explicit declared policy says otherwise;
- missing or unverifiable evidence produces `INDETERMINATE` by default;
- explicit assurance overclaim produces `FAIL` by default;
- identity/name assurance does not satisfy a separately required action-authority input.

These are evaluation rules, not ownership of ANAB requirements. Source requirement identifiers are supplied in the input claim and retained in result findings.

## Run

```bash
python tools/dcas_evaluate.py \
  conformance/examples/anab_dcas_evaluation_input.example.json \
  --expect PASS
```

The result conforms to `spec/schemas/dcas-evaluation-result.schema.json`.

## Assurance boundary

This implementation is a reference surface, not certification infrastructure. It does not retrieve live evidence, perform cryptographic validation, choose the relying-party's policy, or redefine a source baseline. An independent implementation should be able to consume the same normalized input and produce a materially equivalent decision; disagreement is evidence of contract or method ambiguity rather than something to hide with evaluator-specific defaults.
