from ccbp.runtime.hash import invocation_hash


REQUIRED_KEYS = {
    "book",
    "section",
    "intent",
    "content",
}


def verify_invocation(invocation: dict) -> dict:
    """
    Verifies that an invocation conforms to the CCBP framework.

    This function does NOT attempt to interpret meaning.
    It only verifies structural legitimacy.
    """

    missing = REQUIRED_KEYS - invocation.keys()
    if missing:
        return {
            "valid": False,
            "reason": f"Missing required keys: {sorted(missing)}"
        }

    if invocation["book"] not in {"Book I", "Book II", "Appendix A"}:
        return {
            "valid": False,
            "reason": "Invocation does not reference a valid CCBP book"
        }

    invocation["invocation_hash"] = invocation_hash(invocation)

    return {
        "valid": True,
        "invocation": invocation
    }
