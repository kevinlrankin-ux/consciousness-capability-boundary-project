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
def verify_input_is_framework_compliant(raw: str):
    """
    Minimal gatekeeper used by the Shared Engine.

    Returns:
      (True, "OK")  if admissible
      (False, <reason>) if not admissible
    """
    if raw is None:
        return (False, "Input is null.")

    text = str(raw).strip()

    if len(text) == 0:
        return (False, "Empty input cannot be compiled.")

    # HARD REQUIREMENT (current placeholder rule):
    # Until Book I/II/A parsing is implemented, we require the user to explicitly request compilation
    # via a recognizable invocation marker.
    #
    # This prevents "freeform chat" from being treated as compilable.
    markers = [
        "CCBP:",            # explicit invocation prefix
        "INVOCATION:",      # alternative explicit prefix
        "BOOK I",           # explicit Book routing intent
        "BOOK II",
        "APPENDIX A",
    ]

    if not any(m.lower() in text.lower() for m in markers):
        return (
            False,
            "Input is not in CCBP invocation form. "
            "Add an explicit invocation marker (e.g., 'CCBP:' or 'INVOCATION:') "
            "and route intent through Book I → Book II → Appendix A."
        )

    return (True, "OK")
