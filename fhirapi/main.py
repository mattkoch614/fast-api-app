import logging
from contextlib import asynccontextmanager

from fastapi import FastAPI

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
app.include_router(post_router)
