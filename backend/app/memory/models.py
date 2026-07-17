from datetime import datetime, UTC
from enum import Enum
from uuid import uuid4

from pydantic import BaseModel


class MemoryType(str, Enum):
    PERSONAL = "personal"
    PREFERENCE = "preference"
    GOAL = "goal"
    SKILL = "skill"
    RELATIONSHIP = "relationship"


class Memory(BaseModel):
    id: str = str(uuid4())

    type: MemoryType

    content: str

    confidence: float = 1.0

    created_at: datetime = datetime.now(UTC)

    last_accessed: datetime = datetime.now(UTC)

    access_count: int = 0