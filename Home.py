import gpt4all as gpt
from langchain_community.llms import GPT4All
import streamlit as st

st.title('USBC Chatbot')

MODEL_NAME = 'orca-mini-3b-gguf2-q4_0.gguf'

if 'model' not in st.session_state:

    with st.spinner('Downloading model'):

        gpt.GPT4All(model_name = MODEL_NAME, model_path = './models')
        
    llm = GPT4All(model = f'./models/{MODEL_NAME}')

    st.session_state['model'] = llm

else:

    llm = st.session_state['model']

if 'messages' not in st.session_state:

    st.session_state.messages = []

if prompt := st.chat_input('Ask me anything'):

    st.session_state.messages.append({'role' : 'user', 'content' : prompt})

    response = llm.invoke(prompt)

    st.session_state.messages.append({'role' : 'assistant', 'content' : response})

for message in st.session_state.messages:

    with st.chat_message(message['role']):

        st.markdown(message['content'])