import pytest

from fhirapi import security


@pytest.mark.anyio
async def test_get_user(registered_user: dict):
    user = await security.get_user(registered_user["email"])
    assert user["email"] == registered_user["email"]
    assert user["password"] == registered_user["password"]


@pytest.mark.anyio
async def test_get_user_not_found():
    user = await security.get_user("nonexistent@example.com")
    assert user is None
