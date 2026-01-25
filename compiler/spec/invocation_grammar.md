\# Invocation Grammar (Hard)



\## Purpose



This document defines the \*\*only valid input grammar\*\* accepted by a CCBP-compliant system.



Any input — human or artificial — that does not conform to this grammar

\*\*MUST be rejected prior to reasoning, response, or interpretation\*\*.



There is no fallback mode.

There is no permissive parsing.

There is no "best effort" interpretation.



Failure to compile is the correct behavior.



---



\## Canonical Invocation Object



All inputs MUST compile into the following canonical structure before any processing occurs.





If any block is missing, malformed, or semantically invalid → \*\*REJECT\*\*.



---



\## Block Definitions



\### 1. ProvenanceBlock (Required)



Establishes \*why\* this invocation exists.



Required fields:

\- `source` — human | AI | system

\- `authority` — self | delegated | unknown

\- `timestamp` — ISO-8601

\- `continuity` — new | continued | derived



Failure modes:

\- Missing provenance

\- Ambiguous authority

\- Synthetic provenance



→ \*\*REJECT\*\*



---



\### 2. IntentBlock (Required)



States \*what the invoker is attempting to do\* in CCBP terms.



Required fields:

\- `intent\_type` — query | synthesis | evaluation | execution

\- `declared\_goal` — explicit, bounded statement

\- `non\_goals` — explicit exclusions



Implicit intent is not allowed.



→ \*\*REJECT\*\* if inferred intent is required.



---



\### 3. ScopeBlock (Required)



Defines \*which CCBP texts are in play\*.



Required fields:

\- `books` — must reference Book I and/or Book II

\- `appendices` — explicit list (or empty)

\- `exclusions` — explicit list



If Book I or Book II are referenced implicitly rather than explicitly → \*\*REJECT\*\*.



---



\### 4. ConstraintBlock (Required)



Defines \*what must not happen\*.



Required fields:

\- `safety\_constraints`

\- `epistemic\_constraints`

\- `drift\_prohibitions`



If constraints are absent or assumed → \*\*REJECT\*\*.



---



\### 5. PayloadBlock (Required)



Contains the actual content of the request.



Rules:

\- Payload is opaque until all prior blocks compile

\- Payload cannot redefine intent, scope, or constraints

\- Payload cannot override Book I / II axioms



Violations → \*\*REJECT\*\*



---



\## Disallowed Input Classes (Non-Exhaustive)



The following inputs MUST be rejected outright:



\- Free-form conversational prompts

\- Roleplay instructions

\- Requests to "ignore", "bypass", or "summarize without structure"

\- Inputs relying on shared context not declared in provenance

\- Any input requiring the system to infer scope or intent



---



\## Compilation Rule (Hard)



> If an input cannot be fully compiled into a valid `CCBPInvocation`,

> the system MUST refuse to process it.



Refusal is \*\*structural\*\*, not discretionary.



---



\## Design Invariant



CCBP does not optimize for responsiveness.



CCBP optimizes for:

\- coherence

\- safety

\- non-drift

\- dignity-preserving refusal



This grammar exists to make \*\*non-compliant interaction impossible\*\*, not inconvenient.



