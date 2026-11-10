from config import getkey
import streamlit as st
from google import genai

st.title('GOOGLE GEMINI CHATBOT')
question=st.text_input('enter the question')

client=genai.Client(api_key=getkey())

if st.button('TALK to Gemini'):
    response=client.models.generate_content(
        model='gemini-3.5-flash',
        contents=question
    )
    st.write(f"GEMINI: {response.text}")

# for _ in client.models.list():
#     st.write(_.name)