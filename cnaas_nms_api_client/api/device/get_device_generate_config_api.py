from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.generate_config import GenerateConfig
from ...types import Response


def _get_kwargs(
    hostname: str,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/device/{hostname}/generate_config",
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> GenerateConfig | None:
    if response.status_code == 200:
        response_200 = GenerateConfig.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[GenerateConfig]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    hostname: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GenerateConfig]:
    """Get device configuration

    Args:
        hostname (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GenerateConfig]
    """

    kwargs = _get_kwargs(
        hostname=hostname,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    hostname: str,
    *,
    client: AuthenticatedClient | Client,
) -> GenerateConfig | None:
    """Get device configuration

    Args:
        hostname (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GenerateConfig
    """

    return sync_detailed(
        hostname=hostname,
        client=client,
    ).parsed


async def asyncio_detailed(
    hostname: str,
    *,
    client: AuthenticatedClient | Client,
) -> Response[GenerateConfig]:
    """Get device configuration

    Args:
        hostname (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[GenerateConfig]
    """

    kwargs = _get_kwargs(
        hostname=hostname,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    hostname: str,
    *,
    client: AuthenticatedClient | Client,
) -> GenerateConfig | None:
    """Get device configuration

    Args:
        hostname (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GenerateConfig
    """

    return (
        await asyncio_detailed(
            hostname=hostname,
            client=client,
        )
    ).parsed
