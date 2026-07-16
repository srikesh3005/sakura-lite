from fastapi import APIRouter, Depends
from app.core.dependencies import get_chat_service
from app.llm.service import LLMService
from app.schemas.chat import ChatRequest, ChatResponse
from backend.app.chat.service import ChatService

router = APIRouter(prefix="/chat", tags=["Chat"])

@router.post("/", response_model=ChatResponse)
async def chat(
    request: ChatRequest,
    chat_service: ChatService = Depends(get_chat_service),
):
    return await chat_service.chat(
        conversation_id=request.conversation_id,
        message=request.message,
    )