from pydantic import BaseModel
from datetime import datetime

from app.llm.models import LLMMessage




class Conversation(BaseModel):
    id: str
    messages: list[LLMMessage]
    created_at: datetime
    updated_at: datetime

    def add_user_message(self, content: str):
        self.messages.append(
            LLMMessage(
                role="user",
                content=content,
            )
        )
        self.updated_at = datetime.utcnow()

    def add_assistant_message(self, content: str):
        self.messages.append(
            LLMMessage(
                role="assistant",
                content=content,
            )
        )
        self.updated_at = datetime.utcnow()