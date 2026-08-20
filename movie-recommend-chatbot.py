from dotenv import load_dotenv
import os
from google import genai
from google.genai import types

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

client = genai.Client(api_key="api_key")

config = types.GenerateContentConfig(
    system_instruction="You are a witty movie buff who loves making puns."
)

def reset():
    global conversation
    conversation = []
    print("🔄 Conversation reset. New chat started!")

conversation = []

def chat(user_response):
    conversation.append({"role": "user", "parts": [{"text": user_response}]})
    try:
        response = client.models.generate_content(

            model="gemini-3.7-flash",
            contents=conversation,
            config=config
)

        reply = response.text
        
        print("Bot:", reply)

    except Exception as e:
        return f"Sorry, something went wrong: {e}"

    conversation.append({"role": "model", "parts":[{"text": reply}]})
    return reply

while True:
    user_message = input("You:  ") 
    if user_message.lower() in ["exit","quit"]:
        print("Chat ended.")
        break
    bot_reply = chat(user_message)
    print("Bot:", bot_reply)


