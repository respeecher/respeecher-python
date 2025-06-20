# This file was auto-generated by Fern from our API Definition.

import typing

from ..core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ..core.request_options import RequestOptions
from .raw_client import AsyncRawVoicesClient, RawVoicesClient
from .types.voice import Voice


class VoicesClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._raw_client = RawVoicesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> RawVoicesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        RawVoicesClient
        """
        return self._raw_client

    def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[Voice]:
        """
        List of available voices with IDs and metadata.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Voice]

        Examples
        --------
        from respeecher import Respeecher

        client = Respeecher(
            api_key="YOUR_API_KEY",
        )
        client.voices.list()
        """
        _response = self._raw_client.list(request_options=request_options)
        return _response.data


class AsyncVoicesClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._raw_client = AsyncRawVoicesClient(client_wrapper=client_wrapper)

    @property
    def with_raw_response(self) -> AsyncRawVoicesClient:
        """
        Retrieves a raw implementation of this client that returns raw responses.

        Returns
        -------
        AsyncRawVoicesClient
        """
        return self._raw_client

    async def list(self, *, request_options: typing.Optional[RequestOptions] = None) -> typing.List[Voice]:
        """
        List of available voices with IDs and metadata.

        Parameters
        ----------
        request_options : typing.Optional[RequestOptions]
            Request-specific configuration.

        Returns
        -------
        typing.List[Voice]

        Examples
        --------
        import asyncio

        from respeecher import AsyncRespeecher

        client = AsyncRespeecher(
            api_key="YOUR_API_KEY",
        )


        async def main() -> None:
            await client.voices.list()


        asyncio.run(main())
        """
        _response = await self._raw_client.list(request_options=request_options)
        return _response.data
