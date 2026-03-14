# A2A assurance profile

A2A solves inter-agent communication. It does **not** by itself answer whether an agent is safe to trust, whether its metadata is authentic, or whether its task flows preserve policy boundaries. This document closes that gap for DCAS adopters.

## Why this matters

In an A2A deployment, the relying party is rarely evaluating a single API call. It is evaluating an evolving relationship:

- discovery via an Agent Card
- capability and media-type negotiation
- delegated task execution
- task continuation, streaming, or webhook callbacks
- artifact retrieval and downstream action

That stack needs assurance, not just protocol compliance.

## Minimum DCAS questions for A2A

### 1. Can I trust the Agent Card?
The published Agent Card SHOULD be signed or otherwise cryptographically integrity protected. The operator identity, supported interfaces, endpoints, and auth requirements SHOULD be consistent across the Agent Card, the public documentation, and the assurance declaration.

### 2. Can I trust task scoping?
Implementations SHOULD prove that task identifiers, context identifiers, tenant identifiers, and webhook subscriptions cannot be enumerated or replayed across principals. Continuation of a task after `AUTH_REQUIRED` or `INPUT_REQUIRED` MUST preserve the original authorization boundary.

### 3. Can I trust the delivery mode?
Streaming and push notifications introduce a second-order assurance problem: a task can be correct while the delivery channel is misleading, duplicated, stale, or replayed. Evidence SHOULD therefore cover polling, SSE, and webhook behavior together.

### 4. Can I trust the artifacts?
Where artifacts trigger operational or financial consequences, the implementation SHOULD declare supported media types, validate unsupported content safely, and log the provenance of returned outputs.

## Recommended profile

Use **CP-7 A2A Agent / Service Endpoint** when an implementation publishes an Agent Card or exposes A2A task lifecycle operations across a trust boundary.

## Evidence starter pack

- signed Agent Card plus rotation/change process
- auth scheme declaration and endpoint inventory
- task authorization matrix (`send`, `get`, `list`, `cancel`, `subscribe`)
- tenant isolation test report
- streaming and webhook replay-resistance test evidence
- artifact/media-type handling policy
- incident procedure for compromised cards, endpoints, subscriptions, or keys

## Relationship to domain baselines

DCAS is the portable assurance layer. Domain baselines such as **ANAB** define the domain-specific controls that should sit inside that assurance envelope. For named agents in A2A ecosystems, the normal deployment model is:

1. **ANAB** for the name, page, and operator binding
2. **DCAS CP-7** for the operational assurance of the A2A endpoint
3. ecosystem-specific overlays for sector rules, procurement rules, or higher-risk actions
