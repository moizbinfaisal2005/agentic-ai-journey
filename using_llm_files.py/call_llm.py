from dotenv import load_dotenv
import os
from google import genai

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Pass the API key to the client
client = genai.Client(api_key=api_key)

interaction = client.interactions.create(
    model="gemini-3.7-flash",
    input="Explain what is digital marketing in 2 lines"
)

print(interaction.output_text)


