from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from groq import Groq
import os
from dotenv import load_dotenv
import uvicorn
from fastapi.responses import StreamingResponse
import asyncio
from typing import AsyncIterator

load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Request/Response schema
class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str

# Helper function to handle streaming
async def stream_chat_response(chat_completion) -> AsyncIterator[str]:
    for choice in chat_completion.stream():
        # Yield each chunk of the stream
        yield choice['message']['content']

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        # Get response from GROQ LLM
        chat_completion = client.chat.completions.create(
            messages=[{"role": "user", "content": request.message}],
            model="llama-3.1-8b-instant",  # Using Llama 3 8B model
            temperature=0.7,
            max_tokens=1024,
            top_p=1,
            stream=True,  # Enable streaming
            stop=None,
        )
        
        # Create a streaming response
        return StreamingResponse(stream_chat_response(chat_completion), media_type="text/plain")

    except Exception as e:
        return ChatResponse(response=f"Error: {str(e)}")

# # To run the server (optional if running outside of this script)
# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)
