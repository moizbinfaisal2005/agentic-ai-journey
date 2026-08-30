from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv
from google import genai
from google.genai import types
import os

# Load environment variables
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Initialize Google GenAI client
client = genai.Client(api_key="api_key")

# FastAPI app
app = FastAPI()

# Schema for incoming review
class Review(BaseModel):
    text: str

# Schema for analysis result
class Analysis(BaseModel):
    label: str   # "positive", "negative", or "neutral"
    score: int   # 1 (very bad) to 5 (very good)
    theme: str   # one word: delivery, taste, price, service, quality

@app.post("/analyze")
def analyze(review: Review):
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=(
                "Analyze this customer review.\n"
                "Return ONLY valid JSON that matches the Analysis schema.\n"
                "Do not include explanations or text outside JSON.\n"
                "Schema fields:\n"
                "- label: 'positive', 'negative', or 'neutral'\n"
                "- score: integer 1–5\n"
                "- theme: ONE lowercase word (delivery, taste, price, service, quality)\n"
                f"Review: {review.text}"
            ),
            config=types.GenerateContentConfig(
                system_instruction=(
                    "You are a strict JSON generator. "
                    "Always return valid JSON that matches the Analysis schema. "
                    "No text outside JSON."
                ),
                response_mime_type="application/json",
                response_schema=Analysis,
            ),
        )
        return response.parsed
    except Exception as e:
        # Fallback if parsing fails
        return {"label": "error", "score": 0, "theme": "error", "detail": str(e)}




