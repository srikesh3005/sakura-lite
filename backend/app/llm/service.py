from app.llm.factory import LLMFactory
from app.llm.models import LLMMessage


class LLMService:

    def __init__(self):
        self.provider = LLMFactory.get_provider()

    async def chat(self, messages):
        llm_messages = [
            LLMMessage(
                role=message.role,
                content=message.content,
            )
            for message in messages
        ]

        return await self.provider.chat(llm_messages)

    async def stream(self, messages):
        llm_messages = [
            LLMMessage(
                role=message.role,
                content=message.content,
            )
            for message in messages
        ]

        return self.provider.stream(llm_messages)