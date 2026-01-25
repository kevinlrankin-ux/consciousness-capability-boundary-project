\# CCBP API Wrapper (Minimal)



\## Purpose

This is a minimal FastAPI wrapper around the \*\*CCBP Shared Engine\*\*.



It exists to prove:

\- machine ingress cannot bypass the compiler invariant

\- the API contains \*\*zero interpretive logic\*\*

\- all input is either compiled or refused



\## Contract

POST `/compile`



Request body:

```json

{ "input": "<string>" }



