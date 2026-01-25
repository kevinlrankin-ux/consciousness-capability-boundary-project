\# Shared Engine Module (NEW invention)



\## What this is

This module is a deliberately strict “center of gravity” for CCBP compilation.



It is an explicit design invention for this repo:



> Every interface (CLI, API, agent, tests) must funnel input through a single canonical engine

> that enforces the compiler invariant before any “response” is possible.



There is no supported bypass path.



\## The invariant

The system does not “process” non-framework input.



Instead, it deterministically returns a \*\*Refusal Object\*\* (schema-locked) whenever input

cannot be represented as a CCBP Invocation.



\## Public surface

All callers must use:



\- `compile\_input(raw\_input: str, source: str) -> dict`



This function returns exactly one of:



\- an \*\*Invocation Result\*\* (compiled envelope; placeholder until Book I/II/A compilation logic is wired)

\- a \*\*Refusal Object\*\* (schema-locked contract for audit + downstream systems)



\## Boundary

This module is:

\- enforcement + canonical routing only

\- not a chat persona

\- not an “AI response generator”

\- not a UI



Downstream layers may \*present\* results differently, but cannot change what results are possible.



