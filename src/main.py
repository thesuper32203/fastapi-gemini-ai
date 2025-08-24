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
