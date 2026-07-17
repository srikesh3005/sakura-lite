from app.memory.service import MemoryService
from app.llm.service import LLMService


class CognitiveEngine:
    def __init__(
        self,
        memory_service: MemoryService,
        llm_service: LLMService,
    ):
        self.memory_service = memory_service
        self.llm_service = llm_service

    async def think(
        self,
        message: str,
    ):
        pass