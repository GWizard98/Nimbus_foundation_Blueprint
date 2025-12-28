"""Main application module for the FastAPI server."""

from fastapi import FastAPI
from app.database import engine

app = FastAPI()

@app.on_event("startup")
def startup_event():
    """Verify database connectivity on startup."""
    with engine.connect():
        pass


@app.get("/health")
def health():
    """Health check endpoint."""
    return {"status": "ok"}
