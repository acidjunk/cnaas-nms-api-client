from http import HTTPStatus
from typing import Any, Optional, Union, cast

import httpx

from ...client import AuthenticatedClient, Client
from ...types import Response, UNSET
from ... import errors

from ...models.generate_config import GenerateConfig
from typing import cast



def _get_kwargs(
    hostname: str,

) -> dict[str, Any]:
    

    

    

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/device/{hostname}/generate_config".format(hostname=hostname,),
    }


    return _kwargs



def _parse_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Optional[GenerateConfig]:
    if response.status_code == 200:
        response_200 = GenerateConfig.from_dict(response.json())



        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(*, client: Union[AuthenticatedClient, Client], response: httpx.Response) -> Response[GenerateConfig]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    hostname: str,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Response[GenerateConfig]:
    """ Get device configuration

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
    client: Union[AuthenticatedClient, Client],

) -> Optional[GenerateConfig]:
    """ Get device configuration

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
    client: Union[AuthenticatedClient, Client],

) -> Response[GenerateConfig]:
    """ Get device configuration

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

    response = await client.get_async_httpx_client().request(
        **kwargs
    )

    return _build_response(client=client, response=response)

async def asyncio(
    hostname: str,
    *,
    client: Union[AuthenticatedClient, Client],

) -> Optional[GenerateConfig]:
    """ Get device configuration

    Args:
        hostname (str):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        GenerateConfig
     """


    return (await asyncio_detailed(
        hostname=hostname,
client=client,

    )).parsed
