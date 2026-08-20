import streamlit as st
from dotenv import load_dotenv
import os
from google import genai

# ---------- Setup ----------
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

st.set_page_config(page_title="Custom GPT", page_icon="💬", layout="wide")



client = genai.Client(api_key="api_key")  # fixed: was passing literal string "api_key"

MODEL_NAME = "gemini-3.6-flash"

# ---------- Session state ----------
if "conversation" not in st.session_state:
    st.session_state.conversation = []  # list of {"role": ..., "parts": [{"text": ...}]}

# ---------- Sidebar ----------
with st.sidebar:
    st.header("⚙️ Settings")
    st.write(f"**Model:** `{MODEL_NAME}`")
    st.write(f"**Messages in history:** {len(st.session_state.conversation)}")

    if st.button("🗑️ Clear conversation", use_container_width=True):
        st.session_state.conversation = []
        st.rerun()

    st.divider()
    with st.expander("📜 Raw conversation log"):
        for msg in st.session_state.conversation:
            role = msg["role"]
            text = msg["parts"][0]["text"]
            st.markdown(f"**{role}** → {text}")

# ---------- Main chat function ----------
def chat(user_message: str) -> str:
    st.session_state.conversation.append(
        {"role": "user", "parts": [{"text": user_message}]}
    )
    try:
        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=st.session_state.conversation,
        )
        reply = response.text
    except Exception as e:
        reply = f"Sorry, something went wrong: {e}"

    st.session_state.conversation.append(
        {"role": "model", "parts": [{"text": reply}]}
    )
    return reply

# ---------- Main UI ----------
st.title("💬 Custom GPT Through Claude")
st.caption("A Streamlit front-end for your Gemini chatbot script.")

# Render existing conversation as chat bubbles
for msg in st.session_state.conversation:
    role = "user" if msg["role"] == "user" else "assistant"
    with st.chat_message(role):
        st.markdown(msg["parts"][0]["text"])

# Chat input pinned to the bottom
user_message = st.chat_input("Type your message...")

if user_message:
    with st.chat_message("user"):
        st.markdown(user_message)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            bot_reply = chat(user_message)
        st.markdown(bot_reply)