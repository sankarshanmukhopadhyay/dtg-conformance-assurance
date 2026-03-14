# CP-7 A2A Agent / Service Endpoint

**Purpose:** evaluate an A2A-exposed agent or multi-agent service that publishes an Agent Card, accepts delegated work, and returns task, message, or artifact outputs over polling, streaming, or webhooks.

## Mandatory control objectives

- **CO2.1** Access control
- **CO2.3** Separation of duties
- **CO3.1** Identity binding
- **CO3.2** Delegation constraints
- **CO3.5** Agent card integrity
- **CO3.6** Task and context authorization scoping
- **CO4.1** Evidence completeness
- **CO4.2** Traceability
- **CO4.3** Testability
- **CO4.4** Repeatability
- **CO5.1** Disclosure baseline
- **CO5.2** Change disclosure
- **CO6.3** Monitoring & response
- **CO6.4** Streaming and webhook reliability

## Minimum assurance level

- **AL2** for internal or bounded deployments
- **AL3** when the agent crosses organizational boundaries, performs delegated actions, or exposes push notifications/webhooks

## Typical evidence

- Signed Agent Card and publication path
- Endpoint inventory showing supported interfaces and auth schemes
- Task authorization tests for create, continue, get, list, cancel, and subscribe flows
- SSE and push notification replay-resistance tests
- Tenant isolation tests for multi-tenant endpoints
- Logging schema showing task ID, context ID, principal, action, result, and timestamp
- Incident and revocation procedure for compromised keys, endpoints, or Agent Card metadata

## Notes

This profile is intentionally protocol-adjacent rather than protocol-prescriptive. A2A defines how agents talk. DCAS evaluates whether the implementation is trustworthy enough to rely on.
