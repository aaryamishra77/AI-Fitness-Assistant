from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import json
from dotenv import load_dotenv
load_dotenv()

app = FastAPI(title="AI Fitness Assistant")

@app.get("/")
def read_root():
    return {"msg": "AI Fitness Assistant backend running"}

@app.get("/health")
def health():
    return {"status": "ok"}
