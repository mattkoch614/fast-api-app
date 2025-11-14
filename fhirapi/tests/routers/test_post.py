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


@pytest.mark.anyio
async def test_create_post_missing_body(async_client: AsyncClient):
    response = await async_client.post("/post", json={})
    assert response.status_code == 422


# uses the created_post fixture. Creates a post and then gets all posts.
@pytest.mark.anyio
async def test_get_all_posts(async_client: AsyncClient, created_post: dict):
    response = await async_client.get("/post")
    assert response.status_code == 200
    assert [created_post] == response.json()
