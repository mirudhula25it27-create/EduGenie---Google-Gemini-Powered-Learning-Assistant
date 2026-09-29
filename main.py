import os
from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from explanation_module import explain_topic
from qna import answer_question
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import get_learning_recommendations

BASE_DIR = Path(__file__).resolve().parent

app = FastAPI(title="EduGenie", version="1.0.0")
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

class TextRequest(BaseModel):
    text: str

class QuizRequest(BaseModel):
    text: str

class LearningRequest(BaseModel):
    topic: str

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
   return templates.TemplateResponse(
    request=request,
    name="index.html",
    context={"request": request}
)

@app.post("/qa")
async def qa(payload: TextRequest):
    return {"result": answer_question(payload.text)}

@app.post("/explain")
async def explain(payload: TextRequest):
    return {"result": explain_topic(payload.text)}

@app.post("/quiz")
async def quiz(payload: QuizRequest):
    return {"result": generate_quiz(payload.text)}

@app.post("/summarize")
async def summarize(payload: TextRequest):
    return {"result": summarize_text(payload.text)}

@app.post("/learn/recommendations")
async def recommendations(payload: LearningRequest):
    return {"result": get_learning_recommendations(payload.topic)}

@app.get("/health")
async def health():
    return {"status": "ok", "app": "EduGenie"}
