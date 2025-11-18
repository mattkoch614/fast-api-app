import logging
from contextlib import asynccontextmanager

from asgi_correlation_id import CorrelationIdMiddleware
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

from fhirapi.database import database
from fhirapi.logging_conf import configure_logging
from fhirapi.routers.post import router as post_router

logger = logging.getLogger(__name__)


# Lifespan handler for database connection
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Configure logging before app responds to requests
    configure_logging()
    logger.info("Starting application")
    await database.connect()
    yield
    await database.disconnect()


app = FastAPI(lifespan=lifespan)
app.add_middleware(CorrelationIdMiddleware)
app.include_router(post_router)


@app.exception_handler(HTTPException)
async def http_exception_handle_logging(request: Request, exc: HTTPException):
    """
    Custom exception handler for HTTPException that logs the error
    and returns a JSON response with the exception details.

    Args:
        request: The incoming request that triggered the exception
        exc: The HTTPException that was raised

    Returns:
        JSONResponse with the status code and detail from the exception
    """
    logger.error(f"HTTPException: {exc.status_code} - {exc.detail}")
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.detail})
