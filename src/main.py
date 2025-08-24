import os
from fastapi import Depends, FastAPI
from pydantic import BaseModel


# --- App Initialization ---
app = FastAPI()








# --- Pydantic Models ---
class ChatRequest(BaseModel):
    prompt: str


class ChatResponse(BaseModel):
    response: str



@app.get("/")
async def root():
    return {"message": "API is running"}

# Chat endpoint
@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    #TODO: Implement AI integration
    reponse_text="..."
    return ChatResponse(response=reponse_text)