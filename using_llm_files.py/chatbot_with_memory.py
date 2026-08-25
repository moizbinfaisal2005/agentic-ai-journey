from dotenv import load_dotenv
import os
from google import genai

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

client = genai.Client(api_key="api_key")


conversation = []

def chat(user_message):
    conversation.append({"role": "user","parts": [{"text": user_message}]})

    try:
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=conversation

)
        reply = response.text
    except Exception as e:
        return f"Sorry Somthing Wrong: {e}"


    conversation.append({"role": "model","parts": [{"text": reply}]})
    return reply
while True:
    user_message = input("You: ")   # take input from user
    if user_message.lower() in ["exit", "quit"]:
        print("Chat ended.")
        break
    bot_reply = chat(user_message)
    print("Bot:", bot_reply)



for message in conversation:
    print(message["role"], "->", message["parts"][0]["text"])
    print()

    


                         