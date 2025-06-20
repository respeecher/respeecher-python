# Reference
## Tts
<details><summary><code>client.tts.<a href="src/respeecher/tts/client.py">bytes</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

The easiest way to generate text-to-speech audio. Not suitable for latency-sensitive applications.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

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
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**transcript:** `str` — Text for narration.
    
</dd>
</dl>

<dl>
<dd>

**voice:** `VoiceParams` — Voice for narration.
    
</dd>
</dl>

<dl>
<dd>

**output_format:** `typing.Optional[OutputFormatParams]` — Audio format specification.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration. You can pass in configuration such as `chunk_size`, and more to customize the request and response.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.tts.<a href="src/respeecher/tts/client.py">sse</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Stream text-to-speech audio as JSONL (JSON lines) objects over HTTP. A less performant alternative to WebSockets, without text input streaming.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

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
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**transcript:** `str` — Text for narration.
    
</dd>
</dl>

<dl>
<dd>

**voice:** `VoiceParams` — Voice for narration.
    
</dd>
</dl>

<dl>
<dd>

**output_format:** `typing.Optional[StreamingOutputFormatParams]` — Audio format specification.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Voices
<details><summary><code>client.voices.<a href="src/respeecher/voices/client.py">list</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List of available voices with IDs and metadata.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from respeecher import Respeecher

client = Respeecher(
    api_key="YOUR_API_KEY",
)
client.voices.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

