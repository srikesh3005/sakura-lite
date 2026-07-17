from app.pipeline.base import PipelineStage
from app.pipeline.context import PipelineContext
from app.conversation.service import ConversationService


class ConversationStage(PipelineStage):

    def __init__(
        self,
        conversation_service: ConversationService,
    ):
        self.conversation_service = conversation_service

    async def run(
        self,
        context: PipelineContext,
    ) -> PipelineContext:

        if context.conversation_id is None:

            conversation = self.conversation_service.create()

        else:

            conversation = self.conversation_service.get(
                context.conversation_id
            )

            if conversation is None:
                raise ValueError("Conversation not found")

        conversation.add_user_message(
            context.message
        )

        self.conversation_service.save(conversation)

        context.conversation = conversation

        return context