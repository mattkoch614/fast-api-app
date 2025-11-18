import logging

from fastapi import APIRouter, HTTPException, status

from fhirapi.database import database, user_table
from fhirapi.models.user import UserIn
from fhirapi.security import get_user

logger = logging.getLogger(__name__)
router = APIRouter()


@router.post("/register", status_code=201)
async def register(user: UserIn):
    if await get_user(user.email):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="A user with this email already exists",
        )

    # This is a very bad idea! We should use a hashing library like bcrypt.
    query = user_table.insert().values(email=user.email, password=user.password)
    logger.debug(query)
    await database.execute(query)
    return {"detail": "User registered successfully"}
