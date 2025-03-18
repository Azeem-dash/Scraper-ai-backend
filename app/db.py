import motor.motor_asyncio
from app.core.config import settings

# MongoDB client connection setup
client = motor.motor_asyncio.AsyncIOMotorClient(settings.MONGO_URI)
db = client.chat_db  # Replace 'chat_db' with the name of your database

# MongoDB collections
users_collection = db["users"]
