SHELL := /bin/bash

.PHONY: run test stop install install-dev

# Start the FastAPI application locally
run:
	source .venv/bin/activate && uvicorn fhirapi.main:app --reload

# Run tests
test:
	source .venv/bin/activate && pytest

# Stop the running FastAPI application
stop:
	pkill -f "uvicorn fhirapi.main:app" || true

# Install production dependencies
install:
	uv pip install --requirements requirements.txt

# Install development dependencies
install-dev:
	uv pip install --requirements requirements-dev.txt
