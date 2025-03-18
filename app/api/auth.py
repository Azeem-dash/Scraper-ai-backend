from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.services.user import create_user, authenticate_user, create_token_for_user
from app.models.user import User
from fastapi import status

router = APIRouter()

@router.post("/signup")
async def signup(user: User):
    return await create_user(user)

@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await authenticate_user(form_data.username, form_data.password)
    token = await create_token_for_user(user)
    return {"access_token": token, "token_type": "bearer"}
