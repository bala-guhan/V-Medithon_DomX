import streamlit as st
import random
import model

st.markdown("""
<style>
body {
    background-color: #f0f8ff;
    font-family: 'Arial', sans-serif;
}
.chat-container {
    background: rgba(255, 255, 255, 0.8);
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
}
.user-message {
    background-color: #e0ffe0;
    padding: 10px;
    border-radius: 8px;
    margin: 5px 0;
}
.bot-message {
    background-color: #f0f0ff;
    padding: 10px;
    border-radius: 8px;
    margin: 5px 0;
}
</style>
""", unsafe_allow_html=True)

chat_container = st.container()

# Store chat messages
if 'messages' not in st.session_state:
    st.session_state.messages = []

# Function to generate a simple bot response
def generate_bot_response(user_input):
    return model.func(user_input)

# User input
user_input = st.chat_input("You: ")

# On submit, store the message and generate a response
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    bot_response = generate_bot_response(user_input)
    st.session_state.messages.append({"role": "bot", "content": bot_response})

# Display messages
with chat_container:
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.markdown(f'<div class="user-message">You: {message["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="bot-message">Bot: {message["content"]}</div>', unsafe_allow_html=True)

