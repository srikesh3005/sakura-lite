from openai import AsyncOpenAI

from app.core.config import settings
from app.llm.base import BaseLLMProvider
from app.llm.models import LLMMessage, LLMResponse, TokenUsage


class OpenRouterProvider(BaseLLMProvider):
    """OPENROUTER LLM Provider."""

    def __init__(self):
        self.client = AsyncOpenAI(
        base_url=settings.OPENROUTER_BASE_URL,
        api_key=settings.OPENROUTER_API_KEY,
        )

    def _to_openai_messages(
        self,
        messages: list[LLMMessage],
    ) -> list[dict[str, str]]:
        """Convert internal message objects to OpenAI/NVIDIA format."""

        return [
            {
                "role": message.role,
                "content": message.content,
            }
            for message in messages
        ]

    async def chat(
        self,
        messages: list[LLMMessage],
    ) -> LLMResponse:
        """Generate a chat completion."""

        response = await self.client.chat.completions.create(
            model=settings.LLM_MODEL,
            messages=self._to_openai_messages(messages),
            temperature=0.7,
            stream=False,
        )

        usage = None

        if response.usage:
            usage = TokenUsage(
                prompt_tokens=response.usage.prompt_tokens,
                completion_tokens=response.usage.completion_tokens,
                total_tokens=response.usage.total_tokens,
            )

        return LLMResponse(
            content=response.choices[0].message.content or "",
            model=response.model,
            usage=usage,
        )

    async def stream(
        self,
        messages: list[LLMMessage],
    ):
        """Stream chat completion."""

        stream = await self.client.chat.completions.create(
            model=settings.LLM_MODEL,
            messages=self._to_openai_messages(messages),
            temperature=0.7,
            stream=True,
        )

        async for chunk in stream:
            if not chunk.choices:
                continue

            delta = chunk.choices[0].delta

            if delta.content:
                yield delta.content