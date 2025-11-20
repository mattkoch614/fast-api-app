import httpx
import pytest

from fhirapi.tasks import (
    APIResponseError,
    _generate_cute_creature_api,
    send_simple_email,
)


@pytest.mark.anyio
async def test_send_simple_email(mock_httpx_client):
    await send_simple_email("test@example.com", "Test Subject", "Test Body")
    mock_httpx_client.post.assert_called()


@pytest.mark.anyio
async def test_send_simple_email_error(mock_httpx_client):
    mock_httpx_client.post.return_value = httpx.Response(
        status_code=500, content="", request=httpx.Request("POST", "//")
    )

    with pytest.raises(APIResponseError):
        await send_simple_email("test@example.com", "Test Subject", "Test Body")


@pytest.mark.anyio
async def test_generate_cute_creature_api_success(mock_httpx_client):
    json_data = {"output_url": "https://fakeurl.cm/image.jpg"}
    mock_httpx_client.post.return_value = httpx.Response(
        status_code=200, json=json_data, request=httpx.Request("POST", "//")
    )

    result = await _generate_cute_creature_api(
        "A cute newfoundland puppy with a pink bow on its head"
    )
    assert result == json_data
