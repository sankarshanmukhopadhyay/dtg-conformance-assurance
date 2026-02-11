# Annex D — Evidence Formats and Examples  
**Informative**

## D.1 Purpose

Guidance on evidence properties and example formats that support DCAS assurance evaluations.

## D.2 Recommended evidence properties

Evidence SHOULD be:
- attributable (actor identity + role),
- time-bound (timestamps + coverage window),
- integrity-protected (signatures/hashes/append-only),
- queryable (supports sampling/review),
- retainable (policy-defined retention),
- explainable (interpretable without private context).

## D.3 Common evidence types

- Signed event logs (issuance, verification, registry updates)
- Attestations (assessor assertions over scope + validity)
- Configuration snapshots (policy/config state)
- Test results and reports (pass/fail + artefact references)

## D.4 Example snippets (JSON)

### Issuance event log entry
```json
{
  "event_id": "evt-2026-02-11-0001",
  "timestamp": "2026-02-11T06:10:00+05:30",
  "actor_id": "did:example:issuer:bank-001",
  "event_type": "credential_issued",
  "object_ref": "urn:vc:hash:abcd1234",
  "outcome": "success",
  "signature": "base64url(signature)"
}
```

### Attestation envelope
```json
{
  "attestation_id": "att-2026-02-11-0007",
  "attester_id": "did:example:assessor:firm-01",
  "subject_id": "did:example:issuer:bank-001",
  "claim": "Conforms to CP-1 at AL2 for period 2026-Q1",
  "scope": ["CO3.1", "CO3.2", "CO3.3"],
  "validity_period": { "from": "2026-01-01", "to": "2026-03-31" },
  "signature": "base64url(signature)"
}
```

## D.5 Evidence publication patterns

Ecosystems MAY publish evidence via immutable releases, append-only logs, or controlled audit channels.  
Where evidence cannot be public, integrity anchors and access governance SHOULD be provided.
