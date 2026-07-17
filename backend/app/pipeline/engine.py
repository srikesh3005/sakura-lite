from app.pipeline.base import PipelineStage
from app.pipeline.context import PipelineContext


class PipelineEngine:

    def __init__(
        self,
        stages: list[PipelineStage],
    ):
        self.stages = stages

    async def run(
        self,
        context: PipelineContext,
    ) -> PipelineContext:

        for stage in self.stages:
            context = await stage.run(context)

        return context