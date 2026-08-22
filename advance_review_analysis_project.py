from dotenv import load_dotenv
from google import genai
from google.genai import types
import os
from pydantic import BaseModel
from typing import List

# Load API key
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
client = genai.Client(api_key=api_key)

# Define schema
class ReviewAnalysis(BaseModel):
    sentiment: str
    rating: int
    pros: List[str]
    cons: List[str]
    recommendation: str

# Storage for all customer reviews
customer_reviews = {}

def analyze_review(name: str, review_text: str):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=review_text,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            response_schema=ReviewAnalysis,
        ),
    )
    analysis = response.parsed
    # Save under customer name
    customer_reviews[name] = analysis
    return analysis

# --- Main loop ---
while True:
    name = input("Enter your name (or type 'exit' to quit): ")
    if name.lower() == "exit":
        break

    review = input("Enter your review: ")

    analysis = analyze_review(name, review)

    print(f"\nThank you {name}!")
    print(f"Sentiment: {analysis.sentiment}")
    print(f"Rating: {analysis.rating}/5")
    print("Pros:")
    for p in analysis.pros:
        print(f"- {p}")
    print("Cons:")
    for c in analysis.cons:
        print(f"- {c}")
    print(f"Recommendation: {analysis.recommendation}\n")

# --- Company view ---
print("\n📊 Company Dashboard: All Customer Reviews")
for name, analysis in customer_reviews.items():
    print(f"{name}: {analysis.sentiment} ({analysis.rating}/5) → {analysis.recommendation}")
