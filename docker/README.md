\# CCBP Docker Invariant Proof



This container provides a \*\*reproducible, reviewer-proof demonstration\*\*

of the Consciousness–Capability Boundary Project (CCBP) compiler invariant.



\## What this proves



\- There is \*\*one canonical compiler entrypoint\*\*

\- All input is either:

&nbsp; - a `ccbp.invocation`, or

&nbsp; - a deterministic `ccbp.refusal`

\- No environment, script, or framework can bypass enforcement



\## Build



From repo root:



```bash

docker build -t ccbp-invariant .



