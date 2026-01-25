FROM python:3.12-slim

WORKDIR /app

# Critical: expose compiler_runtime as import root
ENV PYTHONPATH=/app/compiler_runtime

COPY compiler_runtime ./compiler_runtime

RUN pip install --no-cache-dir fastapi uvicorn

CMD ["python", "-c", "from compiler_runtime.ccbp.cli.main import main; import sys; sys.argv=['ccbp','compile','hello']; print(main())"]
