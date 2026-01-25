\# CCBP Compiler Runtime — Architecture



\## Non-bypass invariant (structural)

Every interface funnels through the same compiler core.



Human or System

&nbsp; → CLI (strict ingress) OR API (strict ingress)

&nbsp; → Shared Engine (canonical entrypoint)

&nbsp; → Verifier (framework-compliant)

&nbsp; → Deterministic output:

&nbsp;      - ccbp.invocation

&nbsp;      - ccbp.refusal



\## What this proves

\- No interpretive logic at the edges

\- No fallback “helpfulness”

\- No environment-specific bypass paths

\- Deterministic refusal is a valid, first-class outcome

\- API ingress does not weaken invariants (it only forwards input)



\## Modules

\- compiler\_runtime/ccbp/engine/  — Shared Engine (canonical compiler entrypoint)

\- compiler\_runtime/ccbp/runtime/ — Verifier + enforcement

\- compiler\_runtime/ccbp/cli/     — Strict CLI ingress (no parsing/interpretation)

\- compiler\_runtime/ccbp/api/     — Minimal FastAPI ingress (no parsing/interpretation)



