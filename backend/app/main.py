from fastapi import FastAPI

app = FastAPI(
    title="Oficina API",
    version="0.1.0",
    description="Backend API for OficinaApp.",
)


@app.get("/health", tags=["health"])
def health() -> dict[str, str]:
    """Liveness probe."""
    return {"status": "ok"}
