from app.conversation.service import ConversationService
from app.llm.service import LLMService
from app.conversation.repository import ConversationRepository

class ChatService:
    def __init__(self):
        self.conversation_service = ConversationService(ConversationRepository())
        self.llm_service = LLMService()

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
        response = await self.llm_service.chat(conversation.messages)

        # Save assistant response
        conversation.add_assistant_message(response.content)

        # Save conversation
        self.conversation_service.save(conversation)

        return {
            "conversation_id": conversation.id,
            "response": response.content,
        }