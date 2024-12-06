from langchain_community.llms import GPT4All
import streamlit as st

st.title('USBC Chatbot')

llm = GPT4All(
    model="./qwen2-1_5b-instruct-q4_0.gguf"
)

if 'messages' not in st.session_state:

    st.session_state.messages = []

if prompt := st.chat_input('Ask me anything'):

    st.session_state.messages.append({'role' : 'user', 'content' : prompt})

    response = llm.invoke(prompt)

    st.session_state.messages.append({'role' : 'assistant', 'content' : response})

for message in st.session_state.messages:

    with st.chat_message(message['role']):

        st.markdown(message['content'])