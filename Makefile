SHELL := /bin/bash

.PHONY: run test stop

# Start the FastAPI application locally
run:
	source .venv/bin/activate && uvicorn fhirapi.main:app --reload

# Run tests
test:
	source .venv/bin/activate && pytest

# Stop the running FastAPI application
stop:
	pkill -f "uvicorn fhirapi.main:app" || true

