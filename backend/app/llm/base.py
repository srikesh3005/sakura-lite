from abc import ABC, abstractmethod
from typing import Any


class BaseLLMProvider(ABC):
    """Base class for all LLM providers."""

    @abstractmethod
    async def chat(self, messages: list[dict[str, Any]]) -> str:
        """Generate a response from the LLM."""
        raise NotImplementedError

    @abstractmethod
    async def stream(self, messages: list[dict[str, Any]]):
        """Stream a response from the LLM."""
        raise NotImplementedError
    
