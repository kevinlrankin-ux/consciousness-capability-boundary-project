from __future__ import annotations
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from typing import Any, Dict, Optional


@dataclass(frozen=True)
class InvocationEnvelope:
    """
    A minimal envelope that proves the input has been admitted into the CCBP pipeline.

    NOTE: This is not yet "Book I/II/A compilation".
    It is the normalized 'accepted' state that downstream compilation will expand.
    """
    type: str
    schema_version: str
    timestamp_utc: str
    source: str
    raw_input: str
    normalized: Dict[str, Any]
    notes: Optional[str] = None

    def to_dict(self) -> Dict[str, Any]:
        d = asdict(self)
        return {k: v for k, v in d.items() if v is not None}


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def make_invocation(raw_input: str, source: str, *, schema_version: str = "0.1.0") -> Dict[str, Any]:
    # Normalization is intentionally conservative for now.
    normalized = {
        "text": raw_input.strip(),
        "length": len(raw_input),
    }

    env = InvocationEnvelope(
        type="ccbp.invocation",
        schema_version=schema_version,
        timestamp_utc=utc_now_iso(),
        source=source,
        raw_input=raw_input,
        normalized=normalized,
        notes="Accepted into CCBP pipeline (Book I/II/A compilation not yet wired).",
    )
    return env.to_dict()
