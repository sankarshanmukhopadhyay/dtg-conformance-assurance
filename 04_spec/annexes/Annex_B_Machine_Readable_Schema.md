# Annex B — Machine-Readable Conformance Schema  
**Normative**

## B.1 Purpose

This annex defines the normative machine-readable schema used to represent DCAS artefacts and claims.

## B.2 Normative schema artefacts

- Normative JSON Schema: `04_spec/schemas/dcas-conformance-schema-v0.1.json`

Supporting examples (informative):
- `03_conformance/examples/ecosystem_schema.example.yaml`
- `03_conformance/examples/actor_conformance_claim.example.yaml`

## B.3 Requirements

Machine-readable DCAS artefacts SHALL:
1. Declare `dtg_conformance_schema_version`.
2. Provide complete referenced objects (no dangling identifiers).
3. Use stable identifiers for AL/CO/EV/T/CP.
4. Validate against the normative schema.

## B.4 Extensions

Ecosystems MAY extend objects with namespaced properties provided core semantics remain intact.  
Material deviations MUST be disclosed and MUST NOT be represented as baseline DCAS alignment.

## B.5 Compatibility and evolution

- Minor revisions MAY add optional fields.
- Breaking changes SHALL increment schema version and include migration guidance.
