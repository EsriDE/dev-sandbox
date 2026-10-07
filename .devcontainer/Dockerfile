FROM mcr.microsoft.com/devcontainers/python:3.12

# Lean REST-based toolchain only (no heavy ArcGIS SDK) to keep container
# builds fast and the "clone to running app < 5 minutes" goal realistic.
RUN pip install --no-cache-dir \
    fastapi \
    uvicorn \
    requests \
    python-dotenv