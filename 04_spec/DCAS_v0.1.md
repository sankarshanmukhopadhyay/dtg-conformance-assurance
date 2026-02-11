# DCAS v0.1 — Decentralized Conformance and Assurance Standard  
**Draft for DTG Working Group Review**

## Status of This Document

This document is a **working draft** produced for the Decentralized Trust Graph (DTG) Working Group.  
It is **not** a final standard and **must not** be treated as a certification requirement, procurement mandate, or regulatory instrument.

DCAS v0.1 establishes a **shared conceptual and structural foundation** for risk-based conformance and assurance in DTG ecosystems. It is intentionally scoped to enable precise working group review and iterative refinement.

---

## 1. Introduction

Decentralized Trust Graph (DTG) ecosystems enable multiple independent actors to issue, present, and verify claims
about identity, authority, attributes, and behavior across organizational and jurisdictional boundaries. As these ecosystems
scale, reliance shifts from direct bilateral trust to **ecosystem-mediated trust**, where participants must evaluate whether
other actors are operating within acceptable bounds.

In practice, many trust claims are currently expressed as **implicit assurances**—for example, that an issuer follows
appropriate onboarding, that a registry is curated and current, or that an agent acts only under delegated authority.
When such assurances are not explicitly defined, evidenced, and reviewable, ecosystems accumulate **epistemic fog**:
participants cannot reliably distinguish credible claims from weak or adversarial ones. This drives mispricing of trust,
weakens interoperability, and increases systemic risk.

DCAS (Decentralized Conformance and Assurance Standard) defines a structured approach to:
- identify and assess ecosystem risks,
- translate risks into control objectives,
- group control objectives into actor-specific conformance profiles,
- evaluate conformance through assurance levels supported by evidence and tests, and
- enable machine-readable representations of conformance and assurance.

DCAS is designed to be **risk-driven rather than checklist-driven**. It does not prescribe a single governance regime or
technical architecture. Instead, it provides a consistent way for DTG ecosystems to express, compare, and evaluate conformance
requirements—both within a community and across communities.

**Normative intent:** DCAS v0.1 defines the minimum structural requirements for expressing and evaluating conformance in a DTG
ecosystem. Ecosystems may extend DCAS, but SHALL NOT weaken its core semantics without explicitly defining a derivative profile.

**TODO (Editorial):**
- Confirm the preferred DTG WG framing for “DTG ecosystem” and “trust graph” terminology.
- Confirm whether references to “epistemic fog” are acceptable in the core spec, or should move to informative text.

---

## 2. Scope and Non-Goals

### 2.1 In Scope

DCAS v0.1 defines:
1. A **risk-based conformance model** applicable to DTG ecosystems.
2. A conceptual relationship between:
   - risks,
   - control objectives,
   - conformance profiles,
   - assurance levels,
   - evidence and tests, and
   - machine-readable conformance declarations.
3. Normative expectations for:
   - how conformance requirements are derived and structured, and
   - how assurance depth scales with risk.
4. The role of annexes and artefacts (e.g., worksheets, mappings, schemas) as normative and/or informative references.

### 2.2 Non-Goals

DCAS v0.1 explicitly does **not**:
- define legal compliance requirements or interpret laws/regulations,
- mandate specific technologies, protocols, cryptographic suites, or data models,
- prescribe organizational governance forms, institutional arrangements, or market designs,
- define certification schemes, accreditation regimes, or enforcement mechanisms,
- define liability, remedies, or dispute resolution procedures beyond what is needed to express assurance requirements.

Where ecosystems require such elements, they MAY define additional documents and governance artefacts that reference DCAS.

**TODO (Normative):**
- Confirm whether the WG wants an explicit statement that DCAS is compatible with multiple assurance frameworks (e.g., internal audit,
  third-party audit, continuous assurance), without naming them.

---

## 3. Terminology and Normative Language

The key words **MUST**, **MUST NOT**, **REQUIRED**, **SHALL**, **SHALL NOT**, **SHOULD**, **SHOULD NOT**, **RECOMMENDED**,
**MAY**, and **OPTIONAL** are to be interpreted as described in RFC 2119.

### 3.1 Core Terms

**Actor**  
An entity participating in a DTG ecosystem. Actor classes include (but are not limited to) issuer, verifier, holder/agent,
trust registry operator, network/community manager, governance authority, and assurance provider.

**Risk**  
A condition, event, or action that may result in harm to an ecosystem, an actor, a relying party, or affected individuals.
Risks may arise from technical failures, governance failures, adversarial activity, operational weaknesses, or socio-technical dynamics.

**Control Objective (CO)**  
A statement of intent that defines what SHALL be achieved to mitigate a class of risk. Control objectives describe outcomes and constraints,
not implementation details.

**Conformance Profile (CP)**  
A role-specific set of required control objectives, along with associated assurance expectations. A conformance profile defines what an actor
class SHALL implement and what evidence/tests SHALL be available to substantiate conformance.

**Assurance Level (AL)**  
A graded indication of the rigor, independence, and depth of evaluation applied to determine whether an actor conforms to a conformance profile.
Assurance levels scale with risk and may incorporate periodic or continuous evaluation.

**Evidence**  
Verifiable artefacts used to substantiate a conformance claim. Evidence includes, for example, signed logs, attestations, reports, registries,
configuration snapshots, and test results. Evidence MUST be attributable and time-bound.

**Test**  
A defined procedure used to evaluate evidence against a control objective or profile requirement. Tests may be automated or manual and may include
sampling, behavioral verification, integrity checks, and audit review.

### 3.2 Interpretive notes

- DCAS distinguishes **requirements** (controls and profiles) from **verification** (assurance, evidence, and tests).  
- DCAS uses actor classes to avoid applying the same requirements to actors with meaningfully different risk exposure.

**TODO (Normative):**
- Align actor class names with the DTG WG’s preferred taxonomy and the Risk Assessment Worksheet columns.
- Confirm whether “holder/agent” should be treated as one class or two classes for v0.1.

---

## 4. DCAS Conceptual Model

DCAS is based on a traceable, risk-first chain:

1. **Risks** are identified and assessed for the ecosystem and its actor classes.  
2. **Control objectives** are defined to mitigate those risks.  
3. **Conformance profiles** group control objectives by actor class and define minimum assurance expectations.  
4. **Assurance levels** define the rigor and independence with which conformance is evaluated.  
5. **Evidence and tests** provide substantiation for conformance claims.  
6. **Machine-readable representations** enable automated validation and portability across ecosystems.

### 4.1 Separation of concerns

DCAS separates three distinct concerns:

- **Governance intent:** what outcomes and constraints are required (controls and profiles).  
- **Operational substantiation:** what artefacts and checks support claims (evidence and tests).  
- **Assurance rigor:** how confidence is produced and maintained over time (assurance levels).

This separation enables ecosystems to evolve implementation approaches without changing core conformance semantics.

### 4.2 Traceability requirement

A DCAS-aligned ecosystem SHALL maintain traceability such that:
- each identified risk maps to one or more control objectives,
- each control objective is included in one or more conformance profiles (or explicitly excluded with rationale),
- each conformance profile is associated with required evidence and/or tests appropriate to its assurance level.

**TODO (Informative):**
- Add a simple conceptual diagram showing the flow: Risk → CO → CP → AL → Evidence/Tests → Claim.
- Confirm which traceability artefacts will be treated as normative references for v0.1 (e.g., mapping spreadsheets vs annex tables).

---

## 5. Risk-Based Conformance Model

DCAS adopts a **risk-first** approach to conformance and assurance. Conformance SHALL not be treated as a checklist disconnected from threat models,
operational realities, or ecosystem governance.

### 5.1 Risk identification and assessment

A DTG ecosystem applying DCAS SHALL:
- maintain an inventory of risks relevant to the ecosystem and its actor classes,
- describe each risk in terms of threat source/cause and consequence/harm,
- identify affected actors and assets,
- record ownership and treatment intent (e.g., mitigate, accept, transfer, avoid), and
- support repeatable review and revision as the ecosystem evolves.

The **Risk Assessment Worksheet** is the authoritative structure for risk inventory in DCAS v0.1.  
Risk categorizations and taxonomies MAY be used to support review and coverage analysis but SHALL NOT replace the underlying risk statements.

### 5.2 Proportionality and scaling

DCAS requires proportionality:

- The rigor of conformance requirements SHALL be proportionate to risk severity and likelihood.
- The rigor of assurance (assurance level, evidence depth, and testing) SHALL scale with:
  - criticality of claims being relied upon,
  - blast radius of failure (local vs ecosystem-wide),
  - adversarial incentives and feasibility,
  - operational complexity and change frequency.

Where an ecosystem adopts low assurance for high-impact risks, it SHALL explicitly document the rationale and residual risk acceptance.

### 5.3 From risk to controls

For each material risk, the ecosystem SHALL define one or more control objectives that:
- clearly state the intended mitigation outcome,
- specify applicable actor classes,
- and are assessable through evidence and/or tests.

A control objective MAY mitigate multiple risks. Conversely, a risk MAY require multiple control objectives.

### 5.4 From controls to profiles

Control objectives SHALL be grouped into conformance profiles such that:
- each actor class has a clearly defined profile (or a documented reason for exclusion),
- profile requirements are stable enough to support review and assurance,
- profile evolution is versioned and traceable.

### 5.5 Normative references to artefacts

DCAS v0.1 uses external artefacts as normative references. At minimum, an ecosystem claiming alignment with DCAS v0.1 SHALL provide:
- a Risk Assessment Worksheet (risk inventory),
- a Risk → Control Objective mapping,
- defined conformance profiles for relevant actor classes.

**TODO (Normative):**
- Confirm which artefacts are required vs recommended for v0.1 (e.g., evidence catalogue, test suites).
- Confirm whether the Risk Assessment Worksheet template is normative, or whether any structurally equivalent form is acceptable.

---

## 6. Control Objectives

Control objectives define what outcomes and constraints SHALL be achieved to mitigate a class of risk.

Control objectives:
- SHALL be uniquely identifiable and stable within a release line,
- SHALL be stated in outcome terms (intent), not implementation terms,
- SHALL specify applicable actor classes,
- SHOULD be assessable through evidence and/or tests.

Control objectives MAY be layered, for example:
- governance-layer objectives (policy, accountability, decision rights),
- technical objectives (protocol behavior, integrity properties),
- operational objectives (monitoring, incident response),
- socio-technical objectives (human experience constraints, redress pathways).

The canonical catalog of control objectives is maintained outside this document and referenced normatively.

**TODO (Normative):**
- Insert the normative reference location for the control objective catalog (sheet/file/path).
- Define control objective versioning rules (e.g., deprecation, renumbering, backward compatibility expectations).

---

## 7. Conformance Profiles

A conformance profile defines requirements for a specific actor class in a DTG ecosystem.

A conformance profile:
- SHALL declare the actor class to which it applies,
- SHALL list mandatory control objectives (and MAY list optional objectives),
- SHALL declare the minimum required assurance level,
- SHOULD specify required evidence and/or tests at that assurance level.

An ecosystem MAY define multiple profiles for the same actor class where risk exposure differs materially (e.g., “issuer-high-value” vs “issuer-low-value”),
provided each profile is uniquely identified and versioned.

**TODO (Normative):**
- Confirm list of actor classes for v0.1.
- Define conformance profile versioning rules and how profiles reference specific control objective versions.
- Decide whether profile portability across ecosystems is an explicit v0.1 goal or deferred.

---

## 8. Assurance Levels

Assurance levels (ALs) define the depth, rigor, and independence of evaluation applied to determine conformance.

DCAS v0.1 defines assurance levels AL0–AL3. Each AL:
- SHALL define the expected evaluation rigor,
- SHALL define the expected evidence depth,
- SHOULD define the expected frequency of evaluation (periodic or continuous).

Assurance levels are **orthogonal** to conformance profiles:
- a profile defines what requirements apply,
- an AL defines how strongly conformance is substantiated.

**TODO (Normative):**
- Finalize AL0–AL3 definitions using WG-approved language.
- Define minimal evidence expectations per AL (or normatively reference the evidence catalog).

---

## 9. Evidence and Testing

Evidence substantiates conformance claims. Evidence:
- SHALL be attributable to a specific actor and time interval,
- SHALL be verifiable by the intended assessor (human or automated),
- SHOULD be integrity-protected (e.g., signatures, hashes, append-only logs) appropriate to risk.

Tests evaluate evidence and behavior against control objectives and profile requirements. Tests:
- MAY be automated, semi-automated, or manual,
- SHOULD specify inputs, expected outcomes, and pass/fail criteria,
- SHOULD produce auditable outputs (reports, logs, attestations).

**TODO (Normative):**
- Insert the normative reference location for the evidence catalog and test suite definitions.
- Define minimum properties for “acceptable evidence” more precisely (formats, retention, availability) or defer to an annex.

---

## 10. Machine-Readable Conformance

DCAS supports machine-readable expression of:
- control objectives,
- conformance profiles,
- assurance levels,
- evidence and tests, and
- actor conformance claims.

A canonical machine-readable schema:
- SHALL be versioned,
- SHALL support validation of conformance claims,
- SHOULD support ecosystem-specific extensions without breaking core semantics.

**TODO (Normative):**
- Finalize schema reference (file path and version) and declare whether it is normative in v0.1.
- Define schema evolution expectations (compatibility rules) for v0.1.

---

## 11. Governance and Evolution

DCAS evolves through working group review, versioned releases, and explicit decision recording.

Changes to DCAS that alter meaning or requirements (e.g., control semantics, profile requirements, assurance definitions, schema breaking changes):
- SHALL be clearly identified as semantic or breaking,
- SHALL be versioned accordingly,
- SHALL be accompanied by rationale and consequences.

Ecosystems claiming alignment with DCAS:
- SHOULD declare the DCAS version they align to,
- SHOULD declare any extensions or deviations,
- MUST NOT claim DCAS alignment if they omit required artefacts or materially alter core semantics without explicit disclosure.

**TODO (Normative):**
- Align this section with repository governance documents (decision log, release checklist, review cadence).
- Define WG decision thresholds for breaking changes (e.g., meeting consensus requirement).

---

## Annexes

- **Annex A (Normative):** Risk / Control / Conformance Profile Mapping  
- **Annex B (Normative):** Machine-Readable Conformance Schema  
- **Annex C (Informative):** Example Conformance Claims  
- **Annex D (Informative):** Evidence Formats and Examples  

Annexes MAY evolve more rapidly than the core document provided they remain consistent with the versioned DCAS release in which they are published.
