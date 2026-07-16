from functools import lru_cache

from app.conversation.repository import ConversationRepository
from app.conversation.service import ConversationService
from app.llm.service import LLMService
from app.chat.service import ChatService


@lru_cache
def get_conversation_repository():
    return ConversationRepository()


@lru_cache
def get_conversation_service():
    return ConversationService(
        repository=get_conversation_repository()
    )


@lru_cache
def get_llm_service():
    return LLMService()


def get_chat_service():
    return ChatService(
        conversation_service=get_conversation_service(),
        llm_service=get_llm_service(),
    )