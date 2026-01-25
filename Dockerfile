# CCBP — Deterministic Compiler Invariant Container
# This container proves:
# - Single canonical entrypoint
# - No bypass paths
# - Engine + verifier enforced structurally

FROM python:3.12-slim

# Prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install only runtime requirements
RUN pip install --no-cache-dir fastapi uvicorn

# Copy source
COPY compiler_runtime/ compiler_runtime/

# Default command: CLI invariant proof
CMD ["python", "-c", "from compiler_runtime.ccbp.cli.main import main; import sys; sys.argv=['ccbp','compile','hello']; print(main())"]
