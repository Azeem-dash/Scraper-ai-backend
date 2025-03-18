from fastapi import HTTPException, status
from app.models.user import User, UserInDB
from app.db import users_collection
from app.core.security import hash_password, verify_password, create_access_token
from bson import ObjectId

# Create a new user
async def create_user(user: User):
    existing_user = await users_collection.find_one({"username": user.username})
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already taken")

    hashed_password = hash_password(user.password)
    user_in_db = UserInDB(
        username=user.username,
        email=user.email,
        hashed_password=hashed_password,
        id=str(ObjectId())
    )

    await users_collection.insert_one(user_in_db.dict())
    return {"msg": "User created successfully"}

# Authenticate user and return a token
async def authenticate_user(username: str, password: str):
    user = await users_collection.find_one({"username": username})
    if not user or not verify_password(password, user["hashed_password"]):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
    return user

# Create a JWT token for the user
async def create_token_for_user(user: dict):
    return create_access_token(data={"sub": user["username"]})
