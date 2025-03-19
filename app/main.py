# # main.py

# api_key = aMMDwxogZkfE5IbI4rRiTNRHrWnnIpDQ

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.chat import router as chat_router
from .api.scrap_articles import router as scraping_router
# from .api.auth import router as auth_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)
# Include chat route from the 'chat' module
app.include_router(chat_router)

app.include_router(scraping_router, prefix="/scraping", tags=["scraping"])
# app.include_router(auth_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Chat API!"}

# from fastapi import FastAPI, HTTPException, Depends, status
# from pydantic import BaseModel, EmailStr
# from passlib.context import CryptContext
# from pymongo import MongoClient
# from jose import JWTError, jwt
# from datetime import datetime, timedelta

# # FastAPI app
# app = FastAPI()

# # MongoDB connection setup
# mongo_uri = "mongodb+srv://hafizmhuzaifa1234gf:admin12345@cluster0.xpqa0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# client = MongoClient(mongo_uri)
# db = client.get_database("mydatabase")  # Replace 'mydatabase' with your actual database name
# users_collection = db.users  # Users collection

# # Secret key for JWT encoding and decoding
# SECRET_KEY = "your_secret_key"  # Replace with a secure random key in production
# ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 60  # Token expiration time (in minutes)

# # Password hashing context
# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# # Pydantic models
# class User(BaseModel):
#     name: str
#     email: EmailStr
#     password: str
#     role: str


# class UserInDB(User):
#     hashed_password: str


# class Token(BaseModel):
#     access_token: str
#     token_type: str


# # Helper functions for password hashing and token generation
# def hash_password(password: str) -> str:
#     return pwd_context.hash(password)


# def verify_password(plain_password: str, hashed_password: str) -> bool:
#     return pwd_context.verify(plain_password, hashed_password)


# def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=15)) -> str:
#     to_encode = data.copy()
#     expire = datetime.utcnow() + expires_delta
#     to_encode.update({"exp": expire})
#     encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
#     return encoded_jwt


# # Function to get a user by email
# def get_user_by_email(email: str):
#     return users_collection.find_one({"email": email})


# # Function to add user to DB
# def add_user_to_db(user_data: dict):
#     result = users_collection.insert_one(user_data)
#     return str(result.inserted_id)


# # ✅ SIGNUP (Create a new user)
# @app.post("/signup", response_model=Token)
# async def signup(user: User):
#     # Check for missing fields (FastAPI will automatically validate Pydantic models)
#     if not all([user.name, user.email, user.password, user.role]):
#         raise HTTPException(status_code=400, detail="All fields are required")

#     # Check if user already exists
#     existing_user = get_user_by_email(user.email)
#     if existing_user:
#         raise HTTPException(status_code=409, detail="Email already registered")

#     # Hash the password
#     hashed_password = hash_password(user.password)

#     # Create user object
#     user_dict = user.dict()
#     user_dict["hashed_password"] = hashed_password

#     # Insert user into MongoDB
#     user_id = add_user_to_db(user_dict)

#     # Create JWT token
#     access_token = create_access_token(data={"sub": user.email, "role": user.role})
    
#     return {"access_token": access_token, "token_type": "bearer"}


# # ✅ LOGIN (Authenticate User)
# @app.post("/login", response_model=Token)
# async def login(user: User):
#     # Check for missing fields
#     if not user.email or not user.password:
#         raise HTTPException(status_code=400, detail="Email and password are required")

#     # Find user by email
#     db_user = get_user_by_email(user.email)

#     if not db_user:
#         raise HTTPException(status_code=401, detail="Invalid email or password")

#     # Verify the password
#     if not verify_password(user.password, db_user["hashed_password"]):
#         raise HTTPException(status_code=401, detail="Invalid email or password")

#     # Generate JWT Token
#     access_token = create_access_token(data={"sub": user.email, "role": db_user["role"]})
    
#     return {"access_token": access_token, "token_type": "bearer"}

