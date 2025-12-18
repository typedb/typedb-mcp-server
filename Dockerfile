FROM python:3.11-slim

WORKDIR /app

COPY pyproject.toml uv.lock ./
COPY *.py ./

RUN pip install --no-cache-dir uv && \
    uv sync --frozen

EXPOSE 8001

ENTRYPOINT ["uv", "run", "python", "server.py"]
