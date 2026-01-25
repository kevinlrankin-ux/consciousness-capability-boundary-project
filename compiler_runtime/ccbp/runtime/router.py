from ccbp.runtime.verifier import verify_invocation
from ccbp.runtime.errors import InvocationRejected


def route(raw_input: dict) -> dict:
    """
    HARD ROUTER

    All human and AI input MUST pass through this function.
    There is no alternate execution path.

    If the input cannot be verified against the CCBP invocation grammar,
    the system refuses structurally.
    """

    if not isinstance(raw_input, dict):
        raise InvocationRejected(
            reason="Input is not a structured invocation object"
        )

    verified = verify_invocation(raw_input)

    if not verified["valid"]:
        raise InvocationRejected(
            reason=verified["reason"]
        )

    # At this point, the invocation is framework-compliant
    return verified["invocation"]
