
from fastapi import APIRouter
from app.schemas.chat_schema import ChatRequest
from app.services.rag_service import generate_response
from app.services.analytics_service import log_chat

router = APIRouter(prefix="/chat", tags=["Chat"])

@router.post("/")
def chat(request: ChatRequest):

    response = generate_response(request.message)

    log_chat(
        user_message=request.message,
        bot_response=response
    )

    return {
        "response": response
    }
