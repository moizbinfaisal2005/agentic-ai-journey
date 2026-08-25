from dotenv import load_dotenv
from google import genai
from google.genai import types
import os
from pydantic import BaseModel
from typing import List
import requests

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")
client = genai.Client(api_key="api_key")


# Correct endpoint with base currency (USD)
import requests

# Correct endpoint with base currency (USD)
response = requests.get(
    # "https://v6.exchangerate-api.com/v6/64cfac7fe06d54f5b7691b77/latest/USD"
)

currency = input("Add Currency You want to Convert: ").upper()

if response.status_code == 200:
    data = response.json()
    
    # Get the rate for the chosen currency
    rate = data["conversion_rates"].get(currency)
    
    if rate:
        amount = int(input("Enter Your USD Amount Here: "))
        convert = amount * rate
        print(f"{amount} USD = {convert:.2f} {currency}")
        
        # Example prompt for LLM
        prompt = f"""
        Suggest 3 stocks according to the amount {convert:.2f} {currency} 
        that a person can invest. Just 3 stock names like:
        abc stock invest 300
        xyz stock invest 400
        ght stock invest 100
        """
        
    else:
        print("Currency not found in conversion rates.")
else:
    print("Error:", response.status_code, response.text)


try:
    answer = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    ).text
except Exception as e:
    answer = f"Something went wrong: {e}"

print(answer)



