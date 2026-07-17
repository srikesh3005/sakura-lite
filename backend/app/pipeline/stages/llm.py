from app.pipeline.base import PipelineStage
from app.pipeline.context import PipelineContext
from app.llm.service import LLMService


class LLMStage(PipelineStage):

    def __init__(
        self,
        llm_service: LLMService,
    ):
        self.llm_service = llm_service

    async def run(
        self,
        context: PipelineContext,
    ) -> PipelineContext:

        return context