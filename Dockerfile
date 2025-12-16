# Stage 1: Builder
FROM python:3.11-slim as builder

WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY backend/pyproject.toml backend/setup.py* ./
RUN pip install --user --no-cache-dir --upgrade pip setuptools wheel && \
    pip install --user --no-cache-dir ".[dev]" 2>&1 | tail -20

# Stage 2: Runtime
FROM python:3.11-slim

LABEL maintainer="Colab AI Coder Team"
LABEL description="Assistant IA complet pour développement basé sur Qwen-2.5-Coder"

# Security: Create non-root user
RUN groupadd -r aiapp && useradd -r -g aiapp aiapp

WORKDIR /app

# Install runtime dependencies only
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgomp1 \
    libopenblas-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy Python dependencies from builder
COPY --from=builder /root/.local /home/aiapp/.local

# Copy application
COPY backend/src ./src
COPY backend/tests ./tests
COPY README.md .

# Set environment variables
ENV PATH=/home/aiapp/.local/bin:$PATH \
    PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    FASTAPI_ENV=production

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import requests; requests.get('http://localhost:8000/health')" || exit 1

# Switch to non-root user
USER aiapp

# Expose API port
EXPOSE 8000

# Run application
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
