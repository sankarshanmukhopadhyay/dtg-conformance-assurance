# Transport alignment: ToIP Trust Spanning Protocol (TSP)

DCAS is transport-agnostic: it defines **how** assurance and conformance are evaluated, not **how** messages are carried between endpoints.

TSP matters because most conformance workflows eventually require secure exchange of:
- conformance results
- evidence bundles
- signed declarations
- remediation and closure records

Spec reference: https://trustoverip.github.io/tswg-tsp-specification/

## Integration model

DCAS can be applied in deployments where exchanges occur over TSP. In that context:

- DCAS defines the **artifact types** and **evidence expectations**
- TSP provides a **secure and privacy-preserving transport substrate**
- Implementations define endpoint policy, routing, and operational controls

## Assurance implications when using TSP

When deployments use TSP, DCAS assessments SHOULD evaluate:

- **Integrity**: messages and referenced artifacts are tamper-evident and verifiable.
- **Authenticity**: endpoints and senders are verifiably bound to identifiers used in the assurance context.
- **Confidentiality** (when required): sensitive evidence is protected in transit and at rest.
- **Correlation resistance** (where applicable): metadata leakage is minimized to reduce cross-context linkability.
- **Replay and downgrade resistance**: exchanges enforce freshness and avoid protocol downgrade paths.

## Evidence patterns (non-exhaustive)

- Signed conformance declaration transported or referenced via TSP exchange.
- Evidence bundle hash commitments shared over transport, with artifacts retrieved through controlled channels.
- Endpoint-to-endpoint challenge/response logs retained as verifiable evidence (subject to privacy policy).

## Non-goals

DCAS does not define:
- TSP message formats beyond referencing the TSP specification
- network policy, routing constraints, or key management procedures
