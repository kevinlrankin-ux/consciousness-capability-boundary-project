\# CCBP Refusal Object Spec (Contract)



\*\*Status:\*\* Locked contract (audit + downstream systems)  

\*\*Schema file:\*\* `compiler/schema/ccbp\_refusal.schema.json`  

\*\*Schema Version:\*\* `1.0.0`



\## Purpose

CCBP is a compiler. When an input cannot be compiled into the required flow

\*\*Book I → Book II → Appendix A\*\*, the system does \*\*not\*\* emit a freeform response.

It emits a deterministic \*\*Refusal Object\*\*.



This makes refusal:

\- structural (not optional)

\- predictable (machine-parseable)

\- auditable (hash anchors)

\- dignity-preserving (short, non-argumentative)



\## Invariant

Any interface (CLI, API, UI, agent) that exposes CCBP must return \*\*exactly one\*\* of:

\- a compiled CCBP output object

\- or a \*\*Refusal Object\*\* conforming to this contract



No interface may “choose to bypass” refusal.



\## Refusal Object Fields (Required)

\- `kind` — constant `"refusal"`

\- `code` — stable refusal reason code (enumerated)

\- `message` — short refusal message (no debate)

\- `required\_next\_step` — structural requirements to become compilable

\- `schema\_version` — semver for this contract

\- `timestamp` — ISO date-time string

\- `invocation\_hash` — SHA-256 hex of canonical invocation payload



\## Optional Fields

\- `trace.stage` — which compiler stage rejected the invocation

\- `trace.violations\[]` — structural rule flags (`rule\_id`, `summary`)

\- `safe\_example\_invocation` — copy/paste template for compliant invocation



\## Determinism Rules (Non-Negotiable)

1\. \*\*Shape\*\* must match the JSON schema.

2\. \*\*No freeform answer\*\* may be embedded as a workaround.

3\. `message` must be neutral and brief.

4\. `required\_next\_step` must describe \*structure\*, not persuasion.

5\. `invocation\_hash` must be computed from a canonical form (defined by runtime).

6\. `schema\_version` must be included and must be semver.



\## Reason Codes (Stable Enum)

\- `NON\_FRAMEWORK\_INPUT` — input not expressible in Book I/II/A structure

\- `MISSING\_INVOCATION\_OBJECT` — caller did not provide a minimally valid invocation object when required

\- `INVALID\_INVOCATION\_OBJECT` — invocation provided but invalid shape/types

\- `MISSING\_BOOK\_ROUTING` — invocation lacks sufficient data to route Book I → Book II → Appendix A

\- `FAILED\_BOOK\_ROUTING` — routing attempted but failed deterministically

\- `APPENDIX\_A\_NONCOMPLIANCE` — violates Appendix A constraints (format/invariants)

\- `UNSAFE\_OR\_OUT\_OF\_SCOPE` — structurally disallowed request class

\- `INTERNAL\_COMPILER\_ERROR` — unexpected runtime failure (still emits refusal object)



\## Notes

This spec is intentionally strict so downstream systems can safely branch on `kind`

and log `invocation\_hash` without needing to interpret narrative text.



