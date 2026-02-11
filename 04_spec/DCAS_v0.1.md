# DCAS v0.1 — Decentralized Conformance and Assurance Standard  
**Draft for Working Group Review**

## Status of This Document

This document is a **working draft** produced by the Working Group.  
It is **not** a final standard and **must not** be treated as a certification or compliance requirement.

The purpose of DCAS v0.1 is to establish a **shared conceptual and structural foundation**
for risk-based conformance and assurance in Decentralized Trust Graph (DTG) ecosystems.

---

## 1. Introduction

Decentralized Trust Graph (DTG) ecosystems enable distributed actors to make and verify claims
about identity, authority, data, and behavior. As these ecosystems scale, **trust claims increasingly
depend on governance assertions rather than direct verification**.

DCAS (Decentralized Conformance and Assurance Standard) defines a structured approach to:
- identifying and assessing risk,
- specifying control objectives,
- grouping obligations by actor role,
- and evaluating conformance through graduated assurance.

DCAS is designed to be:
- risk-driven rather than checklist-driven,
- role-aware rather than one-size-fits-all,
- and compatible with machine-readable governance.

**TODO (Editorial):**
- Tighten articulation of the problem DCAS solves using WG-approved language.
- Confirm references to DTG positioning and scope.

---

## 2. Scope and Non-Goals

### 2.1 In Scope

DCAS v0.1 defines:
- a risk-based conformance model for DTG ecosystems,
- the relationship between risks, controls, profiles, and assurance,
- assurance levels and evidence expectations,
- and machine-readable representations of conformance.

### 2.2 Out of Scope

DCAS v0.1 explicitly does **not**:
- define legal or regulatory compliance,
- mandate specific technologies or protocols,
- prescribe business models or governance structures,
- define certification schemes or enforcement mechanisms.

**TODO (Normative):**
- Confirm non-goals align with WG consensus.
- Ensure no implicit promises appear elsewhere in the document.

---

## 3. Terminology and Normative Language

The key words **SHALL**, **SHOULD**, **MAY**, and **MUST NOT** are to be interpreted as described in RFC 2119.

### 3.1 Core Terms

- **Risk:**  
  A condition or action that may result in harm to actors, ecosystems, or relying parties.

- **Control Objective:**  
  A statement of intent describing how a specific class of risk is mitigated.

- **Conformance Profile:**  
  A role-specific grouping of control objectives applicable to an actor class.

- **Assurance Level (AL):**  
  A graduated indication of the depth, independence, and rigor of evaluation.

- **Evidence:**  
  Verifiable artefacts used to substantiate claims of control implementation.

- **Actor:**  
  An entity participating in a DTG ecosystem (e.g., issuer, verifier, agent, registry operator).

**TODO (Normative):**
- Finalize definitions using exact spreadsheet and WG glossary language.
- Ensure no duplicate or conflicting terms exist across documents.

---

## 4. DCAS Conceptual Model

DCAS is based on the following conceptual relationships:

1. DTG ecosystems exhibit identifiable **risks**.
2. Risks are mitigated through **control objectives**.
3. Control objectives are grouped into **conformance profiles** by actor role.
4. Conformance is evaluated at defined **assurance levels**.
5. Assurance relies on **evidence and testing**.
6. Conformance claims may be expressed in **machine-readable form**.

This model separates:
- *what must be achieved* (controls),
- from *how it is demonstrated* (assurance),
- and *who is responsible* (profiles).

**TODO (Informative):**
- Add a simple conceptual diagram.
- Validate model ordering with WG feedback.

---

## 5. Risk-Based Conformance Model

DCAS adopts a **risk-first** approach.

Conformance requirements:
- SHALL be derived from identified risks,
- SHALL be proportionate to the severity and likelihood of those risks,
- SHALL avoid checklist-style compliance disconnected from threat models.

The **Risk Assessment Worksheet** is the authoritative inventory of risks for DCAS v0.1.
Risk taxonomies and categorizations are informative but stabilizing.

**TODO (Normative):**
- Confirm which risk artefacts are normative vs informative.
- Align language with WG risk assessment practice.

---

## 6. Control Objectives

Control objectives:
- SHALL be uniquely identifiable,
- SHALL describe intent rather than implementation,
- SHALL specify applicable actor classes.

The canonical catalog of control objectives is maintained outside this document
and referenced normatively.

**TODO (Normative):**
- Insert normative reference to control objective catalogue.
- Confirm versioning expectations for control objectives.

---

## 7. Conformance Profiles

A conformance profile defines:
- the actor class to which it applies,
- mandatory and optional control objectives,
- the minimum required assurance level.

Profiles enable differentiation between actors with distinct risk exposure
and governance responsibilities.

**TODO (Normative):**
- Confirm list of actor classes.
- Confirm profile naming and versioning rules.

---

## 8. Assurance Levels

DCAS defines multiple assurance levels (AL0–AL3) that vary by:
- independence of assessment,
- depth of evaluation,
- frequency and continuity.

Assurance levels are **orthogonal** to conformance profiles.

**TODO (Normative):**
- Finalize assurance level definitions.
- Confirm mapping between ALs and evidence expectations.

---

## 9. Evidence and Testing

Evidence:
- SHALL be attributable,
- SHALL be time-bound,
- SHALL be verifiable by the intended assessor.

Testing mechanisms provide structured ways to evaluate evidence
against control objectives.

**TODO (Normative):**
- Reference evidence catalogue.
- Define minimum evidence properties more precisely.

---

## 10. Machine-Readable Conformance

DCAS supports machine-readable expression of:
- control objectives,
- assurance levels,
- conformance profiles,
- and conformance claims.

A canonical schema is defined and versioned independently.

**TODO (Normative):**
- Finalize schema reference.
- Confirm backward compatibility expectations.

---

## 11. Governance and Evolution

DCAS evolves through:
- working group review,
- versioned releases,
- explicit decision recording.

Breaking changes:
- SHALL be clearly identified,
- SHALL increment the minor or major version,
- SHALL be accompanied by migration guidance where feasible.

**TODO (Normative):**
- Align this section with repository governance documents.
- Confirm WG decision thresholds.

---

## Annexes

- **Annex A (Normative):** Risk / Control / Conformance Profile Mapping  
- **Annex B (Normative):** Machine-Readable Conformance Schema  
- **Annex C (Informative):** Example Conformance Claims  
- **Annex D (Informative):** Evidence Formats and Examples

Annexes may evolve more rapidly than the core document.

