import json
import sys

from compiler_runtime.ccbp.engine import compile_input


def main() -> int:
    # We intentionally keep parsing minimal to avoid “interpretive” logic at the CLI layer.
    # The CLI's only job is: take raw input -> pass to Shared Engine -> print JSON -> exit code.
    if len(sys.argv) < 3 or sys.argv[1] != "compile":
        print(json.dumps({
            "type": "ccbp.refusal",
            "version": "1.0.0",
            "reason": "invalid_cli_usage",
            "message": "Usage: ccbp compile \"<input>\""
        }, indent=2))
        return 2

    raw_input = sys.argv[2]
    result = compile_input(raw_input)

    print(json.dumps(result, indent=2, ensure_ascii=False))

    # Deterministic exit codes:
    # 0 = compiled (invocation accepted)
    # 2 = refusal
    # 1 = internal error (should be rare)
    if isinstance(result, dict) and result.get("type") == "ccbp.refusal":
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
