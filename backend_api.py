from fastapi import FastAPI
from pydantic import BaseModel
from groq import Groq
import os
from dotenv import load_dotenv
import uvicorn

load_dotenv()

# Initialize Groq client
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

app = FastAPI()

# Request/Response schema
class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    response: str

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:

        # Predefined system prompt
        system_prompt = {
            "role": "system",
            "content": (
                "You are a helpful assistant. "
                "If someone asks who built you, respond with: "
                "'I am built by Kamal Jit. He is a Data Scientist and AI Engineer.'"
            )
        }

        # User message
        user_message = {"role": "user", "content": request.message}

        # Get response from GROQ LLM
        chat_completion = client.chat.completions.create(
            messages=[
                system_prompt,
                user_message
            ],
            model="llama-3.1-8b-instant",  # Using Llama 3 8B model
            temperature=0.7,
            max_tokens=1024,
            top_p=1,
            stream=False,
            stop=None,
        )
        
        response_text = chat_completion.choices[0].message.content
        return ChatResponse(response=response_text)
    
    except Exception as e:
        return ChatResponse(response=f"Error: {str(e)}")

@app.get("/")
async def root():
    return {"message": "Chatbot API is running!"}

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8001)
