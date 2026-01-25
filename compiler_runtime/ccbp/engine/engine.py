from __future__ import annotations
from typing import Dict

from ..runtime.verifier import verify_input_is_framework_compliant
from .invocation import make_invocation
from .refusal import make_refusal


def compile_input(raw_input: str, source: str = "unknown") -> Dict:
    """
    The ONE canonical entrypoint for all compilation.

    Hard rule:
    - If input is not representable within the CCBP framework, return Refusal Object.
    - Otherwise, return Invocation Envelope (accepted state).
    """
    if raw_input is None:
        return make_refusal(
            refusal_code="CCBP_NULL_INPUT",
            refusal_title="Null input cannot be processed",
            refusal_message="No input was provided to the compiler.",
            required_next_step="Provide a non-empty input string that can be compiled through Book I/II/Appendix A.",
            evidence={"source": source},
        )

    text = str(raw_input)

    ok, reason = verify_input_is_framework_compliant(text)

    if not ok:
        return make_refusal(
            refusal_code="CCBP_NON_FRAMEWORK_INPUT",
            refusal_title="Non-framework input rejected",
            refusal_message=reason,
            required_next_step="Rewrite the input as a CCBP Invocation Object aligned to Book I → Book II → Appendix A.",
            evidence={"source": source, "length": len(text)},
        )

    # Accepted: create invocation envelope (later steps will compile it into full CCBP language).
    return make_invocation(text, source)
