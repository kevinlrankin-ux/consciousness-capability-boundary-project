from __future__ import annotations
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional


@dataclass(frozen=True)
class RefusalObject:
    """
    Minimal refusal object that will be serialized to match the repo's refusal schema contract.

    NOTE: We keep this intentionally small + deterministic.
    Downstream layers can add *metadata* only if the schema allows it.
    """
    type: str
    schema_version: str
    timestamp_utc: str
    refusal_code: str
    refusal_title: str
    refusal_message: str
    required_next_step: str
    evidence: Optional[Dict[str, Any]] = None
    allowed_outputs: Optional[List[str]] = None

    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        # Drop None fields to keep output clean/deterministic
        return {k: v for k, v in d.items() if v is not None}


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def make_refusal(
    refusal_code: str,
    refusal_title: str,
    refusal_message: str,
    required_next_step: str,
    *,
    schema_version: str = "1.0.0",
    evidence: Optional[Dict[str, Any]] = None,
    allowed_outputs: Optional[List[str]] = None,
) -> Dict[str, Any]:
    obj = RefusalObject(
        type="ccbp.refusal",
        schema_version=schema_version,
        timestamp_utc=utc_now_iso(),
        refusal_code=refusal_code,
        refusal_title=refusal_title,
        refusal_message=refusal_message,
        required_next_step=required_next_step,
        evidence=evidence,
        allowed_outputs=allowed_outputs or [
            "ccbp.refusal",
            "ccbp.invocation"
        ],
    )
    return obj.to_dict()
