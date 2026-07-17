from abc import ABC, abstractmethod

from app.conversation.models import Conversation


class ConversationRepository(ABC):

    @abstractmethod
    def get(
        self,
        conversation_id: str,
    ) -> Conversation | None:
        ...

    @abstractmethod
    def save(
        self,
        conversation: Conversation,
    ) -> None:
        ...

    @abstractmethod
    def exists(
        self,
        conversation_id: str,
    ) -> bool:
        ...