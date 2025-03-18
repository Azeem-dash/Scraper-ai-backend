from fastapi import APIRouter
from app.models.chat import ChatQuery
from app.services.mistral import get_mistral_response

router = APIRouter()

@router.post("/chat")
async def chat(query: ChatQuery):
    response = get_mistral_response(query.query)
    return {
        "response": response
       }
