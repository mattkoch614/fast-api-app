from contextlib import asynccontextmanager

from fastapi import FastAPI

from fhirapi.database import database
from fhirapi.routers.post import router as post_router


# Lifespan handler for database connection
@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()


app = FastAPI(lifespan=lifespan)
app.include_router(post_router)
