from pydantic import BaseModel, EmailStr
from typing import Optional
from bson import ObjectId
from app.db import db

# Pydantic model for user input
class User(BaseModel):
    username: str
    email: EmailStr
    password: str

# MongoDB User model (includes hashed password)
class UserInDB(User):
    id: str
    hashed_password: str

    class Config:
        # This helps convert ObjectId to string
        json_encoders = {
            ObjectId: str
        }
