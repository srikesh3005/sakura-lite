from app.conversation.service import ConversationService
from app.llm.service import LLMService
from app.prompt.builder import PromptBuilder


class ChatService:
    def __init__(
        self,
        conversation_service: ConversationService,
        llm_service: LLMService,
    ):
        self.conversation_service = conversation_service
        self.llm_service = llm_service

    async def chat(
        self,
        conversation_id: str | None,
        message: str,
    ):
        # Load or create conversation
        if conversation_id is None:
            conversation = self.conversation_service.create()
        else:
            conversation = self.conversation_service.get(conversation_id)

            if conversation is None:
                raise ValueError("Conversation not found")

        # Add user message
        conversation.add_user_message(message)

        # Call the LLM
        messages = PromptBuilder.build(conversation)

        response = await self.llm_service.chat(messages)

        # Save assistant response
        conversation.add_assistant_message(response.content)

        # Save conversation
        self.conversation_service.save(conversation)

        return {
            "conversation_id": conversation.id,
            "response": response.content,
        }
