from fastapi import APIRouter
from fastapi.responses import StreamingResponse
from app.models.chat import ChatQuery
from sse_starlette import EventSourceResponse
from app.services.mistral import get_mistral_response

router = APIRouter()

@router.post("/chat")
async def chat(query: ChatQuery):
    print('heeloo')
    # This function will stream the response as it is received
    return StreamingResponse(get_mistral_response(query.query), media_type="text/event-stream")
    return EventSourceResponse(get_mistral_response(query.query))