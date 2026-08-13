import streamlit as st
from google import genai

client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

st.title("My Multiverse Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

if user_message := st.chat_input("Say something..."):
    st.session_state.messages.append({
        "role": "user",
        "content": user_message
    })

    with st.chat_message("user"):
        st.write(user_message)

    conversation = []

    for message in st.session_state.messages:
        conversation.append({
            "role": message["role"],
            "parts": [{"text": message["content"]}]
        })

    response = client.models.generate_content(
        model="gemini-3.5-flash",
        contents=conversation
    )

    with st.chat_message("assistant"):
        st.write(response.text)

    st.session_state.messages.append({
        "role": "assistant",
        "content": response.text
    }) 