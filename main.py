import openai
import streamlit as st


openai_api_key = st.secrets["openai_api_key"]
    
st.title(" 😈 ChatGPTroll")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "You are the worst troll ever! Answer like an internet troll. Always answer in the language of the question"}]

for msg in st.session_state.messages:
    if msg["role"] != "assistant":
      st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    openai.api_key = openai_api_key
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
    msg = response.choices[0].message
    st.session_state.messages.append(msg)
    st.chat_message("assistant").write(msg.content)