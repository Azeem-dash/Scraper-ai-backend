from mistralai import Mistral
import os
from fastapi import HTTPException
from dotenv import load_dotenv

load_dotenv()
# Initialize the Mistral client
api_key = os.getenv("MISTRAL_API_KEY")
if not api_key:
    raise ValueError("MISTRAL_API_KEY is missing")

client = Mistral(api_key=api_key)
model = "mistral-large-latest"

# Function to interact with Mistral API
def get_mistral_response(query: str):
    try:
        chat_response = client.chat.complete(
            model=model,
            messages=[
                {"role": "user", "content": query},
            ]
        )
        return chat_response.choices[0].message.content
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
