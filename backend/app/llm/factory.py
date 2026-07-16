from app.core.config import settings
from app.llm.providers.nvidia import NvidiaProvider
from app.llm.providers.openrouter import OpenRouterProvider


class LLMFactory:
    @staticmethod
    def get_provider():
        if settings.LLM_PROVIDER == "openrouter":
            return OpenRouterProvider()

        elif settings.LLM_PROVIDER == "nvidia":
            return NvidiaProvider()

        raise ValueError(
            f"Unsupported provider: {settings.LLM_PROVIDER}"
        )