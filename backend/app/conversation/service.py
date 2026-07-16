from uuid import uuid4
from datetime import datetime, UTC

from app.conversation.models import Conversation
from app.conversation.repository import ConversationRepository


class ConversationService:
    def __init__(self, repository: ConversationRepository):
        self.repository = repository

    def create(self) -> Conversation:
        conversation = Conversation(
            id=str(uuid4()),
            messages=[],
            created_at=datetime.now(UTC),
            updated_at=datetime.now(UTC),
        )

        self.repository.save(conversation)
        return conversation

    def get(self, conversation_id: str) -> Conversation | None:
        return self.repository.get(conversation_id)

    def save(self, conversation: Conversation) -> None:
        self.repository.save(conversation)