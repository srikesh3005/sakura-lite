from app.conversation.models import Conversation
from app.conversation.repository import ConversationRepository


class InMemoryConversationRepository(ConversationRepository):
    """In-memory implementation of the conversation repository."""

    def __init__(self):
        self._conversations: dict[str, Conversation] = {}

    def get(self, conversation_id: str) -> Conversation | None:
        return self._conversations.get(conversation_id)

    def save(self, conversation: Conversation) -> None:
        self._conversations[conversation.id] = conversation

    def exists(self, conversation_id: str) -> bool:
        return conversation_id in self._conversations