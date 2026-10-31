from fastapi import APIRouter, HTTPException
from ..models.conversation import ChatRequest, ChatResponse
from ..services.conversation_manager import ConversationManager

router = APIRouter(prefix="/api", tags=["chat"])

@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    if not request.message or not request.message.strip():
        raise HTTPException(status_code=400, detail="User message cannot be empty.")

    try:
        response = await ConversationManager.process_message(
            session_id=request.session_id,
            message=request.message,
            language=request.language,
            corrected_fields=request.corrected_fields
        )
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to process chat: {str(e)}")

@router.post("/session/reset")
def reset_session(payload: dict):
    session_id = payload.get("session_id")
    if not session_id:
        raise HTTPException(status_code=400, detail="session_id is required.")
    ConversationManager.reset_session(session_id)
    return {"status": "success", "session_id": session_id, "message": "Session reset successfully."}
