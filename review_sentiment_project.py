from dotenv import load_dotenv
from google import genai
from google.genai import types
import os
from pydantic import BaseModel
from typing import List


load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")





class ReviewAnalysis(BaseModel):
    sentiment: str
    rating: int
    pros: List[str]
    cons: List[str]
    recommendation: str

client = genai.Client(api_key="api_key")


user = input("Enter Your Review Here: ")
review_text = user

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=review_text,
    config=types.GenerateContentConfig(
        response_mime_type="application/json",   # "reply in JSON"
        response_schema=ReviewAnalysis,                   # "...in exactly THIS shape"
    ),
)

analysis = response.parsed

print(f"Sentiment: {analysis.sentiment} (Ratings: {analysis.rating}/5)")








