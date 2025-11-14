import pytest
from httpx import AsyncClient


async def create_post(body: str, async_client: AsyncClient) -> dict:
    response = await async_client.post("/post", json={"body": body})
    return response.json()


# Fixture to create a post, no autouse=True because it's used in other tests
@pytest.fixture()
async def created_post(async_client: AsyncClient):
    return await create_post("Test post", async_client)


# Tell pytest to use anyio backend for async tests
@pytest.mark.anyio
async def test_create_post(async_client: AsyncClient):
    body = "Test post"

    response = await async_client.post(
        "/post",
        json={"body": body},
    )

    assert response.status_code == 201
    assert {"id": 0, "body": body}.items() <= response.json().items()
