# This file was auto-generated by Fern from our API Definition.

import typing_extensions
from .generation_request import GenerationRequestParams
from .output_format import OutputFormatParams


class BytesGenerationRequestParams(GenerationRequestParams):
    output_format: typing_extensions.NotRequired[OutputFormatParams]
    """
    Audio format specification.
    """
