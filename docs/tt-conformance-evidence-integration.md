# Trust Tasks conformance evidence integration

**Status:** experimental, unreleased. This path evaluates a bounded set of assessor-mapped test propositions, not an implementation's overall trustworthiness.

## Who should use this

An assessor or tool builder who has obtained a Trust Tasks suite run and needs an independently inspectable DCAS decision. Start with the synthetic example below; do not treat it as measured evidence.

## Authority and compatibility

The [draft Trust Tasks conformance suite](https://github.com/bmiller59/dtgwg-conformance/tree/864687a5bc072b12c952e16539b42e738c4a7dd5) owns its test definitions and outcome semantics. Its working-group adoption is not asserted. DCAS owns the local evaluation contract. The relying party owns the selected scope, evidence acceptance and reliance decision. Specification owners retain normative authority.

The importer accepts suite commit `864687a5bc072b12c952e16539b42e738c4a7dd5`, suite version `0.1.0-draft`, run format `tt-conformance-run/0.2`, and a matching implementation/tier record from the results array. A new suite revision requires explicit review. No live fetching or test execution takes place. Registry, PR, proposed and candidate channel declarations are recognized, but only registry results can support a requirement. Upstream separates advisory rows from its main results file; do not combine them into gating evidence.

## Run the example

From the repository root:

```bash
pip install -r requirements.txt
python conformance/examples/tt_conformance/generate_fixture.py /tmp/dcas-tt
python tools/import_tt_conformance.py /tmp/dcas-tt/run.json /tmp/dcas-tt/results.json /tmp/dcas-tt/manifest.json --output /tmp/dcas-tt/input.json
python tools/dcas_evaluate.py /tmp/dcas-tt/input.json --expect PASS --output /tmp/dcas-tt/decision.json
python -m unittest discover -s tests -p 'test_*.py'
```

The generated fixture is synthetic. Its PASS demonstrates the pipeline only. Inspect the normalized input's source_context and the decision's requirement findings. Retain source files, assessor manifest, normalized input and decision together. No upstream vectors are copied.

## Evaluate an actual run

1. Obtain original run.json and results.json through a trusted channel. Independently review the run provenance, implementation checkout, exact specification revision, vector files, exceptions, scope, applicable mandatory requirements, and positive anchors. Confirm that the review identifies a complete requirement set for the declared target.
2. Create a separately controlled assessor manifest using the generated example as a structural guide and `spec/schemas/dcas-tt-assessor-manifest.schema.json` as the contract. Set the actual implementation/version/revision, specification revision, tier, implementation revision reference, review reference, artifact SHA-256 digests, vector inventory digest, observation time, validity interval and evaluation time. Map each requirement to every required vector and at least one reviewed positive anchor. Never generate an approval manifest solely from the producer's assertions.
3. Run the importer and evaluate the normalized input using the commands above with the actual paths. A validation error means no decision was issued; do not substitute PASS.
4. Review all requirement findings, the source outcome records and remaining scope exclusions before using the assessment. The assessor must separately establish relevance, completeness, authentication, and reliance authority.

The importer compares exact artifact hashes and the vector inventory digest with the manifest, but cannot authenticate the manifest, prove the implementation checkout, retrieve specification contents, or prove that the reported vector inventory is complete. The source records and manifest are trusted assessment inputs, not signatures. The upstream maintainer checklist requires explicit platform attribution: do not describe a measured checkout as unmodified upstream without evidence of ancestry and local modifications. Assess evidence of a patched checkout only for that checkout. Keep them protected from modification. Source records can contain sensitive identifiers or operational details; restrict access and review before publication. Re-import when evidence or assessment time changes; do not simply edit normalized statuses or timestamps.

## Outcome interpretation

| Source condition | Evidence state |
| --- | --- |
| Applicable registry PASS, positive anchor verified where required | available |
| Applicable FAIL or KNOWN-FAIL | contradicted |
| SKIP, CLARIFY, QUARANTINED, SPEC-CHANGED, SKIPPED-SAFETY | unverifiable |
| Required vector absent or excluded | missing |
| Advisory, synthetic, authorization-gate-only, non-profile window, drift or governance mismatch | unverifiable (applicable recorded failures remain contradictions) |
| Expired review interval | stale |

The original source result and recorded exclusion reasons are retained, even when they do not support reliance. No automatic non-applicability is inferred. Missing and unverifiable evidence yield INDETERMINATE; stale evidence is INDETERMINATE under this import policy. A contradicted mapped proposition yields FAIL. Each requirement needs all mapped evidence and its declared positive anchors. FAIL dominates INDETERMINATE, which dominates PASS.

## Boundaries

No certification, assurance-level assignment, independent third-party verification, live revocation check, or demonstrated cross-platform interoperability follows from this result. The importer does not establish that a claimed implementation revision matches the running binary: that is a separate assessor obligation. See [evaluator contract](evaluator-contract.md) for the normalized contract and [reference evaluator](reference-evaluator.md) for migration.
