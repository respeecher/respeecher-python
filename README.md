# Respeecher Python Library

[![fern shield](https://img.shields.io/badge/%F0%9F%8C%BF-Built%20with%20Fern-brightgreen)](https://buildwithfern.com?utm_source=github&utm_medium=github&utm_campaign=readme&utm_source=https%3A%2F%2Fgithub.com%2Frespeecher%2Frespeecher-python)
[![pypi](https://img.shields.io/pypi/v/respeecher)](https://pypi.python.org/pypi/respeecher)

The Respeecher Python library provides convenient access to the Respeecher API from Python.

## Installation

```sh
pip install respeecher
```

## Reference

A full reference for this library is available [here](https://github.com/respeecher/respeecher-python/blob/HEAD/./reference.md).

## Usage

Instantiate and use the client with the following:

```python
from respeecher import Respeecher

client = Respeecher(
    api_key="YOUR_API_KEY",
)
client.tts.bytes(
    transcript="Hello, World!",
    voice={"id": "samantha"},
)
```

## Async Client

The SDK also exports an `async` client so that you can make non-blocking calls to our API.

```python
import asyncio

from respeecher import AsyncRespeecher

client = AsyncRespeecher(
    api_key="YOUR_API_KEY",
)


async def main() -> None:
    await client.tts.bytes(
        transcript="Hello, World!",
        voice={"id": "samantha"},
    )


asyncio.run(main())
```

## Exception Handling

When the API returns a non-success status code (4xx or 5xx response), a subclass of the following error
will be thrown.

```python
from respeecher.core.api_error import ApiError

try:
    client.tts.bytes(...)
except ApiError as e:
    print(e.status_code)
    print(e.body)
```

## Streaming

The SDK supports streaming responses, as well, the response will be a generator that you can loop over.

```python
from respeecher import Respeecher

client = Respeecher(
    api_key="YOUR_API_KEY",
)
response = client.tts.sse(
    transcript="Hello, World!",
    voice={"id": "samantha"},
)
for chunk in response.data:
    yield chunk
```

## Websockets

The SDK supports both sync and async websocket connections for real-time, low-latency communication. Sockets can be created using the `connect` method, which returns a context manager. 
You can either iterate through the returned `SocketClient` to process messages as they arrive, or attach handlers to respond to specific events.

```python

# Connect to the websocket (Sync)
import threading

from respeecher import Respeecher

client = Respeecher(...)

with client.tts.connect() as socket:
    # Iterate over the messages as they arrive
    for message in socket
        print(message)

    # Or, attach handlers to specific events
    socket.on(EventType.OPEN, lambda _: print("open"))
    socket.on(EventType.MESSAGE, lambda message: print("received message", message))
    socket.on(EventType.CLOSE, lambda _: print("close"))
    socket.on(EventType.ERROR, lambda error: print("error", error))


    # Start the listening loop in a background thread
    listener_thread = threading.Thread(target=socket.start_listening, daemon=True)
    listener_thread.start()
```

```python

# Connect to the websocket (Async)
import asyncio

from respeecher import AsyncRespeecher

client = AsyncRespeecher(...)

async with client.tts.connect() as socket:
    # Iterate over the messages as they arrive
    async for message in socket
        print(message)

    # Or, attach handlers to specific events
    socket.on(EventType.OPEN, lambda _: print("open"))
    socket.on(EventType.MESSAGE, lambda message: print("received message", message))
    socket.on(EventType.CLOSE, lambda _: print("close"))
    socket.on(EventType.ERROR, lambda error: print("error", error))


    # Start listening for events in an asyncio task
    listen_task = asyncio.create_task(socket.start_listening())
```

## Advanced

### Access Raw Response Data

The SDK provides access to raw response data, including headers, through the `.with_raw_response` property.
The `.with_raw_response` property returns a "raw" client that can be used to access the `.headers` and `.data` attributes.

```python
from respeecher import Respeecher

client = Respeecher(
    ...,
)
response = client.tts.with_raw_response.bytes(...)
print(response.headers)  # access the response headers
print(response.data)  # access the underlying object
with client.tts.with_raw_response.sse(...) as response:
    print(response.headers)  # access the response headers
    for chunk in response.data:
        print(chunk)  # access the underlying object(s)
```

### Retries

The SDK is instrumented with automatic retries with exponential backoff. A request will be retried as long
as the request is deemed retryable and the number of retry attempts has not grown larger than the configured
retry limit (default: 2).

A request is deemed retryable when any of the following HTTP status codes is returned:

- [408](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/408) (Timeout)
- [429](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/429) (Too Many Requests)
- [5XX](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status/500) (Internal Server Errors)

Use the `max_retries` request option to configure this behavior.

```python
client.tts.bytes(..., request_options={
    "max_retries": 1
})
```

### Timeouts

The SDK defaults to a 60 second timeout. You can configure this with a timeout option at the client or request level.

```python

from respeecher import Respeecher

client = Respeecher(
    ...,
    timeout=20.0,
)


# Override timeout for a specific method
client.tts.bytes(..., request_options={
    "timeout_in_seconds": 1
})
```

### Custom Client

You can override the `httpx` client to customize it for your use-case. Some common use-cases include support for proxies
and transports.

```python
import httpx
from respeecher import Respeecher

client = Respeecher(
    ...,
    httpx_client=httpx.Client(
        proxies="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)
```

## Contributing

While we value open-source contributions to this SDK, this library is generated programmatically.
Additions made directly to this library would have to be moved over to our generation code,
otherwise they would be overwritten upon the next generated release. Feel free to open a PR as
a proof of concept, but know that we will not be able to merge it as-is. We suggest opening
an issue first to discuss with us!

On the other hand, contributions to the README are always very welcome!
