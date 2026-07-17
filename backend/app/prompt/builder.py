from app.prompt.system_prompt import SYSTEM_PROMPT
from app.llm.models import LLMMessage
from app.conversation.models import Conversation


class PromptBuilder:

    @staticmethod
    def build(
        conversation: Conversation,
    ) -> list[LLMMessage]:

        messages = [
            LLMMessage(
                role="system",
                content=SYSTEM_PROMPT,
            )
        ]

        messages.extend(conversation.messages)

        return messages