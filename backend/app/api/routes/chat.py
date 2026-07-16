from fastapi import APIRouter

from app.llm.service import LLMService
from app.schemas.chat import ChatRequest, ChatResponse

router = APIRouter(prefix="/chat", tags=["Chat"])

@router.post("/", response_model=ChatResponse)
async def chat(request: ChatRequest):
    llm = LLMService()

    response = await llm.chat(request.messages)

    return ChatResponse(
        response=response.content
    )