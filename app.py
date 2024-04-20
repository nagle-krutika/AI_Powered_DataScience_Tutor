import streamlit as st
import google.generativeai as genai

st.title("AI Powered Data Science Tutor")

x = open(r"Keys/api_key.txt")
key = x.read()
genai.configure(api_key=key)
model = genai.GenerativeModel(model_name="gemini-1.5-pro-latest", system_instruction="""You are a data science expert. Given upon a data science question you should answer it politely. If you don't answer to any question your response should be, 'That is beyond my knowledge.'.""")

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []
    # Add the initial message from the bot with the role "model"
    st.session_state["chat_history"].append({"role": "model", "parts": [{"text": "Hello! I am your data science tutor. How may I help you?"}]})

chat = model.start_chat(history=st.session_state["chat_history"])

# Display the chat history
for msg in chat.history:
    if msg.role == "user":
        st.chat_message("user").write(msg.parts[0].text)
    else:
        st.chat_message("model").write(msg.parts[0].text)

user_prompt = st.chat_input()
if user_prompt:
    st.chat_message("user").write(user_prompt)
    response = chat.send_message(user_prompt)
    st.chat_message("model").write(response.text)
    st.session_state["chat_history"] = chat.history