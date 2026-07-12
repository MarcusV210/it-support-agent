import streamlit as st
import requests
import uuid

API_URL = "http://127.0.0.1:8000/chat"

st.title("IT Support Assistant")

# Create a fresh session_id once per browser session
if "session_id" not in st.session_state:
    st.session_state.session_id = str(uuid.uuid4())

if "history" not in st.session_state:
    st.session_state.history = []

# Display conversation so far
for role, text in st.session_state.history:
    with st.chat_message(role):
        st.write(text)

# Input box
user_input = st.chat_input("Describe your issue...")

if user_input:
    st.session_state.history.append(("user", user_input))
    with st.chat_message("user"):
        st.write(user_input)

    response = requests.post(API_URL, json={
        "message": user_input,
        "session_id": st.session_state.session_id
    })

    agent_reply = response.json()["response"]
    st.session_state.history.append(("assistant", agent_reply))
    with st.chat_message("assistant"):
        st.write(agent_reply)