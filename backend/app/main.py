from fastapi import FastAPI
import os
from pathlib import Path
from app.routes import upload
from app.routes import chat
from dotenv import load_dotenv
from openai import OpenAI
from fastapi.middleware.cors import CORSMiddleware


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(upload.router)
app.include_router(chat.router)

@app.get("/")
def root():
    return {"message": "Clarify Backend Running"}
