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

Control objectives define the outcomes and constraints an actor (or ecosystem function) SHALL achieve to mitigate one or more identified risks. Control objectives are the primary unit of requirement in DCAS.

### 6.1 Purpose and intent

Control objectives exist to ensure that conformance requirements are:
- **risk-anchored** (derived from identified risks),
- **outcome-focused** (stated as intent, not implementation),
- **role-aware** (applicable to specific actor classes), and
- **assessable** (supported by evidence and/or tests appropriate to the assurance level).

Control objectives SHALL not be used as a substitute for risk assessment. The purpose of control objectives is to express what must be true for an ecosystem to operate within acceptable risk bounds.

### 6.2 Required properties of a control objective

Each control objective SHALL include, at minimum:
- **Control Objective ID** — a stable identifier (e.g., `CO3.2`) unique within a DCAS release.
- **Name** — a short descriptive title.
- **Description** — a clear statement of the intended outcome and constraint.
- **Applicability** — one or more applicable actor classes and/or ecosystem roles.
- **Risk linkage** — a reference to the risks the objective mitigates (directly or indirectly).

Each control objective SHOULD also include:
- **Control nature** — preventive, detective, corrective (or combinations).
- **Layer** — governance, technical, operational, socio-technical, or systemic.
- **Assurance considerations** — typical evidence types and test expectations at various ALs.
- **External alignment** — references to relevant control families in other frameworks (informative).

### 6.3 Control objective semantics

Control objectives SHALL be expressed in a manner that is:
- **testable:** the objective can be evaluated as satisfied or not satisfied, given evidence and defined tests,
- **implementation-neutral:** the objective does not mandate a specific protocol, product, or technology,
- **scope-bounded:** applicability and boundaries are explicit, including what is out of scope,
- **non-contradictory:** objectives do not introduce requirements that cannot be jointly satisfied.

When a control objective is intentionally broad (e.g., “maintain incident response capability”), it SHALL define the minimum required properties of that capability so that assessment is meaningful.

### 6.4 Control objective lifecycle and change management

To preserve auditability and ecosystem stability:

- Control objective identifiers (IDs) SHALL NOT be reused for different semantics.  
- If a control objective’s meaning changes materially, a new identifier SHOULD be issued or the DCAS minor/major version SHALL be incremented (per Section 11).
- Deprecations SHOULD be explicit and SHALL include migration guidance where feasible.
- An ecosystem claiming DCAS alignment SHALL disclose the control objective set (and versions) against which it is evaluated.

### 6.5 Canonical catalogue and normative reference

The canonical catalogue of control objectives is maintained as a versioned artefact referenced by DCAS releases.

For DCAS v0.1, the control objective catalogue:
- SHALL be the authoritative source for control objective text and identifiers.
- SHALL be consistent with the risk inventory and risk-to-control mapping used in the same release.

**TODO (Normative):**
- Insert the normative reference path(s) for the control objective catalogue (repo file paths and/or spreadsheet sheet names).
- Finalize the control objective ID format and allowed namespaces for extensions (e.g., ecosystem-specific `ECO-CO*`).

---

## 7. Conformance Profiles

A conformance profile defines the set of requirements applicable to a specific actor class in a DTG ecosystem. Profiles are the unit by which ecosystems express differentiated obligations, and the unit by which actors claim conformance.

### 7.1 Purpose and intent

Conformance profiles exist to:
- prevent one-size-fits-all requirements across heterogeneous actors,
- ensure obligations align with actor-specific risk exposure and authority,
- enable portable and comparable conformance claims across ecosystems, and
- create a stable basis for assurance and certification pathways without mandating a single governance regime.

Conformance profiles group control objectives into coherent role-based requirements and declare minimum assurance expectations.

### 7.2 Required properties of a conformance profile

Each conformance profile SHALL include, at minimum:
- **Profile ID** — a stable identifier (e.g., `CP-1`) unique within a DCAS release.
- **Actor class** — the actor class to which the profile applies.
- **Profile name and description** — a clear statement of role scope and intent.
- **Mandatory control objectives** — a list of control objectives REQUIRED for conformance.
- **Minimum assurance level** — the minimum AL at which conformance claims SHALL be evaluated.
- **Profile version** — either explicitly stated or implied by DCAS release version.

Each profile SHOULD also include:
- **Optional control objectives** — additional objectives that strengthen assurance or cover expanded scope.
- **Required evidence and tests** — evidence artefacts and tests expected at the stated assurance level.
- **Scope boundaries and exclusions** — what the profile does not cover.
- **Assessor expectations** — who may evaluate the profile at the required AL (informative, unless the ecosystem defines it normatively).

### 7.3 Mandatory vs optional requirements

A profile MAY contain:
- **Mandatory requirements** (SHALL): required for conformance claims.
- **Optional requirements** (MAY/SHOULD): strengthen posture but are not required for baseline conformance.

An ecosystem SHALL NOT label requirements as optional if they mitigate material risks without documenting compensating controls or explicit residual risk acceptance.

### 7.4 Multiple profiles per actor class

An ecosystem MAY define more than one profile for the same actor class when risk exposure differs materially, for example:
- high-impact issuer vs low-impact issuer,
- public verifier vs constrained verifier,
- registry operator with curation authority vs registry operator with mirror-only function.

Where multiple profiles exist:
- each profile SHALL be uniquely identified and versioned,
- the differentiation criteria SHALL be explicit (e.g., claim criticality, blast radius, privilege level),
- mapping from profile selection to risk treatment SHALL be documented.

### 7.5 Profile portability and ecosystem extensions

Profiles are intended to support comparability across ecosystems. However, ecosystems may extend profiles to reflect local governance.

To maintain clarity:
- Ecosystem-specific extensions SHOULD be namespaced and SHALL NOT reuse canonical profile IDs.
- Extensions SHALL disclose deviations from baseline requirements and SHALL preserve core DCAS semantics.

**TODO (Normative):**
- Define the extension mechanism (naming and versioning) for ecosystem-specific profiles.
- Confirm whether v0.1 targets profile portability explicitly, or treats it as aspirational and informative.

### 7.6 Relationship to assurance levels, evidence, and testing

A conformance profile defines **what** must be satisfied.  
An assurance level defines **how strongly** conformance is substantiated.

Therefore:
- A profile SHALL declare a minimum AL.
- Evidence and tests SHALL be proportionate to the AL and the profile’s risk exposure.
- Conformance claims SHOULD include references to evidence and tests used in evaluation, where feasible.

### 7.7 Canonical profile set and normative reference

For DCAS v0.1, the canonical set of profiles:
- SHALL be maintained as versioned artefacts referenced by DCAS releases.
- SHALL be consistent with the control objective catalogue and the risk-to-control mapping of the same release.

**TODO (Normative):**
- Insert the normative reference path(s) for conformance profiles (repo files and/or spreadsheet sheet names).
- Confirm the v0.1 baseline profile set (e.g., Issuer, Verifier, Holder/Agent, Trust Registry Operator, Network/Community Manager, Governance Authority).

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
