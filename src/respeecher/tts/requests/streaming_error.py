# This file was auto-generated by Fern from our API Definition.

import typing_extensions


class StreamingErrorParams(typing_extensions.TypedDict):
    error: str
    """
    Error message.
    """

    status_code: int
    """
    HTTP status code most appropriate for this error.
    """

    context_id: typing_extensions.NotRequired[str]
