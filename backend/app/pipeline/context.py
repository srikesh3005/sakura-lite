from dataclasses import dataclass, field

from app.conversation.models import Conversation
from app.memory.models import Memory


@dataclass
class PipelineContext:

    # Request
    conversation_id: str | None
    message: str

    # Loaded during execution
    conversation: Conversation | None = None

    retrieved_memories: list[Memory] = field(default_factory=list)

    tool_results: list = field(default_factory=list)

    llm_response: str | None = None

    metadata: dict = field(default_factory=dict)