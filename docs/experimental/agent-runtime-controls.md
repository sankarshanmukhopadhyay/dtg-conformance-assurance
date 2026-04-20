# Agent runtime controls overlay *(experimental)*

This document introduces a lightweight DCAS overlay for runtime-governed agent systems without changing the stable core method.

## Scope

The overlay focuses on three portable concerns drawn from the Microsoft Agent Governance Toolkit as an upstream reference:

1. **pre-effect policy admission** before a runtime action is allowed
2. **tamper-evident runtime evidence** for what happened at decision time
3. **fail-safe behavior** when policy, status, or delegation context is missing or stale

## Experimental control families

The current incremental adoption uses three DCAS control objectives:

- `CO3.7` Runtime admission control
- `CO4.5` Runtime decision traceability
- `CO6.4` Fail-safe runtime behavior

These controls are intended for ecosystems evaluating agent-to-agent, agent-to-tool, or delegated runtime effects.

## Boundary

This overlay does **not** redefine DCAS as a runtime middleware. It remains an assurance packaging and evaluation method. The overlay simply gives assessors a repeatable way to ask for runtime governance evidence.
