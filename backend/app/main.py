from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel
from app.analyzer import analyze_answer

app = FastAPI()

# ✅ MUST be here
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class AnswerRequest(BaseModel):
    answer: str

@app.get("/")
def read_root():
    return {"message": "Interview Analyzer API is running 🚀"}

@app.post("/analyze")
def analyze(data: AnswerRequest):
    return analyze_answer(data.answer)