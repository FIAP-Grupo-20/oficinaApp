# Oficina Backend

Python 3.14 + FastAPI, managed with [uv](https://docs.astral.sh/uv/).

## Setup

```bash
uv sync
```

## Commands

| Task       | Command                         |
| ---------- | ------------------------------- |
| Run (dev)  | `uv run fastapi dev app/main.py` |
| Tests      | `uv run pytest` (coverage ≥ 80%) |
| Lint       | `uv run ruff check .`           |
| Format     | `uv run ruff format .`          |
| Type check | `uv run mypy .`                 |

API docs: http://localhost:8000/docs (Swagger) · http://localhost:8000/redoc
