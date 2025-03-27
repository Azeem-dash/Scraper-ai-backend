import json
from fastapi import HTTPException
from mistralai import Mistral
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("MISTRAL_API_KEY")
if not api_key:
    raise ValueError("MISTRAL_API_KEY is missing")

client = Mistral(api_key=api_key)
model = "mistral-large-latest"

# Generator function to handle streaming response
async def get_mistral_response(query: str):
    try:
        chat_response = client.chat.stream(
            model=model,
            stream=True,
            messages=[{"role": "user", "content": query}],
        )

        # Process each chunk as it comes
        for chunk in chat_response:
            content = chunk.data.choices[0].delta.content
            if content:  # Only yield non-empty content
                print(content)
                yield content

    except Exception as e:
        print(f"Error during streaming: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))
