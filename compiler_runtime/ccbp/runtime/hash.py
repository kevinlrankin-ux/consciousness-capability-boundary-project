import hashlib
import json


def invocation_hash(invocation: dict) -> str:
    """
    Produces a deterministic hash for a CCBP invocation.
    Used for auditability, refusal anchoring, and replay safety.
    """

    canonical = json.dumps(invocation, sort_keys=True).encode("utf-8")
    return hashlib.sha256(canonical).hexdigest()
