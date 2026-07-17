from abc import ABC, abstractmethod

from app.pipeline.context import PipelineContext


class PipelineStage(ABC):

    @abstractmethod
    async def run(
        self,
        context: PipelineContext,
    ) -> PipelineContext:
        pass