from io import BytesIO
from base64 import b64decode
import wave
import pytest
from respeecher import Respeecher
from respeecher.tts import ContextfulGenerationRequest


transcript = "A quick brown fox jumps over the lazy dog."
voice = dict(id="samantha")
context_id = "abc"


@pytest.fixture(scope="module")
def respeecher():
    # Reads the API key from the environment (RESPEECHER_API_KEY)
    return Respeecher()

def test_voices(respeecher):
    assert respeecher.voices.list()

def test_tts_bytes(respeecher):
    response = b''

    for chunk in respeecher.tts.bytes(transcript=transcript, voice=voice):
        response += chunk

    with BytesIO(response) as buffer:
        with wave.open(buffer, "rb") as audio:
            assert audio.getnchannels() == 1
            assert audio.getframerate() == 22050
            assert audio.getnframes() > 22050

def test_tts_sse(respeecher):
    audio = b''

    for event in respeecher.tts.sse(transcript=transcript, voice=voice):
        assert event.type == "chunk"
        audio += b64decode(event.data)

    assert len(audio) > 22050


def test_tts_websocket(respeecher):
    with respeecher.tts.connect() as socket:
        socket.send_generate(ContextfulGenerationRequest(
            transcript=transcript,
            voice=voice,
            context_id=context_id
        ))

        audio = b''

        for message in socket:
            if message.type == "done":
                break

            assert message.type == "chunk"
            assert message.context_id == context_id

            audio += b64decode(message.data)

        assert len(audio) > 22050
