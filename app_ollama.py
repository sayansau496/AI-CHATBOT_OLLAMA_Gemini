import streamlit as st
import ollama

st.title('OLLAMA CHATBOT')
question=st.text_input('enter the question')

if st.button('TALK to OLLAMA'):
    response=ollama.chat(
        model='gemma4',
        messages=[{'role':'user','content':question}]
    )
    st.write(f"OLLAMA: {response.message.content}")

