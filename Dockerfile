FROM ghcr.io/astral-sh/uv:python3.13-bookworm-slim

WORKDIR /app

# Copy only the dependency manifests first, so this (slow) layer is cached
# and only re-runs when dependencies actually change, not on every code edit.
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-dev

# Now copy the actual application code, preserving the same src/Backend
# path depth as in the repo, since core/config.py locates the project
# root (and .env) by walking a fixed number of parent directories.
COPY src/Backend ./src/Backend

ENV PATH="/app/.venv/bin:$PATH"

WORKDIR /app/src/Backend

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
