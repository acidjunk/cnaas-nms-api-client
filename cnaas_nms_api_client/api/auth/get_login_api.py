from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...types import Response


def _get_kwargs() -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/auth/login",
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
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any]:
    """Function to initiate a login of the user

     The user will be sent to the page to login.
    Our client info will also be checked.

    Note:
        We also discussed adding state to this function.
        That way you could be sent to the same page once you logged in.
        We would put the relevant information in a dictionary,
        base64 encode it and sent it around as a parameter.
        For now the application is small and it didn't seem needed.

    Returns:
        A HTTP redirect response to OIDC_CONF_WELL_KNOWN_URL we have defined.
        We give the auth call as a parameter to redirect after login is successfull.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[Any]:
    """Function to initiate a login of the user

     The user will be sent to the page to login.
    Our client info will also be checked.

    Note:
        We also discussed adding state to this function.
        That way you could be sent to the same page once you logged in.
        We would put the relevant information in a dictionary,
        base64 encode it and sent it around as a parameter.
        For now the application is small and it didn't seem needed.

    Returns:
        A HTTP redirect response to OIDC_CONF_WELL_KNOWN_URL we have defined.
        We give the auth call as a parameter to redirect after login is successfull.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)
