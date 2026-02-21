import streamlit as st
from mistralai import Mistral

st.title("📌 Mistral Chatbot")

# Load API key
MISTRAL_API_KEY = st.secrets["MISTRAL"]["api_key"]

if not MISTRAL_API_KEY:
    st.error("❗ API key missing in secrets.toml")
    st.stop()

client = Mistral(api_key=MISTRAL_API_KEY)

# Store chat history
if "history" not in st.session_state:
    st.session_state["history"] = []

user_input = st.chat_input("Type your message...")

def get_response(user_message):
    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": user_message}
    ]

    response = client.chat.complete(
        model="mistral-small-latest",
        messages=messages
    )

    return response.choices[0].message.content

if user_input:
    st.session_state.history.append({"role": "user", "content": user_input})

    with st.spinner("🤖 Thinking..."):
        reply = get_response(user_input)

    st.session_state.history.append({"role": "assistant", "content": reply})

for chat in st.session_state.history:
    with st.chat_message(chat["role"]):
        st.markdown(chat["content"])