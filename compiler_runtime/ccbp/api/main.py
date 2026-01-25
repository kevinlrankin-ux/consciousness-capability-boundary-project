from fastapi import FastAPI
from pydantic import BaseModel

from compiler_runtime.ccbp.engine import compile_input

app = FastAPI(
    title="CCBP Compiler API",
    version="0.1.0",
    description="Minimal API wrapper around the CCBP Shared Engine (no bypass paths).",
)


class CompileRequest(BaseModel):
    input: str


@app.post("/compile")
def compile_endpoint(req: CompileRequest):
    # Canonical ingress: EVERYTHING funnels through the Shared Engine
    return compile_input(req.input)
