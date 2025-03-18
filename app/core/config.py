from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MONGO_URI: str
    SECRET_KEY: str  # Secret key for JWT
    ALGORITHM: str = "HS256"  # JWT algorithm
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 180  # Access token expiration time in minutes

    class Config:
        env_file = ".env"  # Load values from the .env file

settings = Settings()
