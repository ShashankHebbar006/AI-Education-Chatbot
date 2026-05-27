
import streamlit as st
import requests

API_URL = "http://localhost:8000/chat/"

st.set_page_config(page_title="Education Support Chatbot")

st.title("🎓 AI Education Support Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

prompt = st.chat_input("Ask your question...")

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    response = requests.post(
        API_URL,
        json={"message": prompt}
    )

    bot_reply = response.json()["response"]

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": bot_reply
        }
    )

    with st.chat_message("assistant"):
        st.markdown(bot_reply)
