.PHONY: run test stop install install-dev

# Detect OS and set Python/pytest paths
ifeq ($(OS),Windows_NT)
    PYTHON := .venv\Scripts\python.exe
    PYTEST := .venv\Scripts\pytest.exe
    UVICORN := .venv\Scripts\uvicorn.exe
    KILL := taskkill //F //IM
else
    PYTHON := .venv/bin/python
    PYTEST := .venv/bin/pytest
    UVICORN := .venv/bin/uvicorn
    KILL := pkill -f
endif

# Start the FastAPI application locally
run:
	$(UVICORN) fhirapi.main:app --reload

# Run tests
# Usage: make test ARGS="-k test_get_all_posts"
test:
	$(PYTEST) $(ARGS)

# Stop the running FastAPI application
stop:
	$(KILL) "uvicorn fhirapi.main:app" || true

# Install production dependencies
install:
	uv pip install --requirements requirements.txt

# Install development dependencies
install-dev:
	uv pip install --requirements requirements-dev.txt
