from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import UNSET, Response, Unset


def _get_kwargs(
    hostname: str,
    *,
    include_uplinks: Unset | bool = UNSET,
    include_downlinks: Unset | bool = UNSET,
    include_descriptions: Unset | bool = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["include_uplinks"] = include_uplinks

    params["include_downlinks"] = include_downlinks

    params["include_descriptions"] = include_descriptions

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": f"/device/{hostname}/interfaces_export",
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Any | None:
    if response.status_code == 200:
        return None

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Any]:
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
    include_uplinks: Unset | bool = UNSET,
    include_downlinks: Unset | bool = UNSET,
    include_descriptions: Unset | bool = UNSET,
) -> Response[Any]:
    """Export all interfaces for local download

    Args:
        hostname (str):
        include_uplinks (Union[Unset, bool]):
        include_downlinks (Union[Unset, bool]):
        include_descriptions (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        hostname=hostname,
        include_uplinks=include_uplinks,
        include_downlinks=include_downlinks,
        include_descriptions=include_descriptions,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    hostname: str,
    *,
    client: AuthenticatedClient | Client,
    include_uplinks: Unset | bool = UNSET,
    include_downlinks: Unset | bool = UNSET,
    include_descriptions: Unset | bool = UNSET,
) -> Response[Any]:
    """Export all interfaces for local download

    Args:
        hostname (str):
        include_uplinks (Union[Unset, bool]):
        include_downlinks (Union[Unset, bool]):
        include_descriptions (Union[Unset, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs(
        hostname=hostname,
        include_uplinks=include_uplinks,
        include_downlinks=include_downlinks,
        include_descriptions=include_descriptions,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
