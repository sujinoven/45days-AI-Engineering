
import os

from dotenv import load_dotenv
from openai import OpenAI
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field


# Load environment variables
load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY was not found.")

client = OpenAI(api_key=api_key)

# Create FastAPI application
app = FastAPI(
    title="My AI Assistant API",
    description="An API that answers questions using an LLM.",
    version="1.0.0"
)


# Define the request structure
class QuestionRequest(BaseModel):
    question: str = Field(
        min_length=1,
        max_length=2000
    )


# Keep LLM logic in a separate function
def generate_answer(question: str) -> str:
    response = client.responses.create(
        model="gpt-4.1-mini",
        instructions=(
            "You are a helpful AI assistant. "
            "Answer clearly and concisely."
        ),
        input=question,
        max_output_tokens=250
    )

    return response.output_text


# Health-check endpoint
@app.get("/")
def home():
    return {"status": "running", "message": "AI API is ready."}


# Question-answering endpoint
@app.post("/ask")
def ask_ai(request: QuestionRequest):
    try:
        answer = generate_answer(request.question)

        return {
            "question": request.question,
            "answer": answer
        }

    except Exception:
        # In production, log the exception securely.
        raise HTTPException(
            status_code=500,
            detail="The AI service could not process your request."
        )
