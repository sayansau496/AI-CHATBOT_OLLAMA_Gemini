# ---------- Import libraries ----------
import streamlit as st
import ollama
from google import genai
from google.genai import types

from config import getkey

# ---------- Page setup ----------
st.set_page_config(page_title="AI Chatbot", page_icon="🤖")
st.title("AI CHATBOT")
st.caption("Chat with Google Gemini (cloud) or Ollama (local)")

# ---------- Backend 1: Ollama ----------
def get_ollama_models():
    """Return the names of models downloaded with 'ollama pull'."""
    try:
        return [m.model for m in ollama.list().models]
    except Exception:
        return []          # Ollama is not running

def stream_ollama(model, history, system_prompt, temperature):
    messages = [{"role": "system", "content": system_prompt}] + history
    stream = ollama.chat(
        model=model,
        messages=messages,
        stream=True,
        options={"temperature": temperature},
    )
    for chunk in stream:
        piece = chunk["message"]["content"]
        if piece:
            yield piece

# ---------- Backend 2: Google Gemini ----------
def stream_gemini(history, system_prompt, temperature):
    client = genai.Client(api_key=getkey())

    contents = []
    for m in history:
        role = "user" if m["role"] == "user" else "model"
        contents.append(
            types.Content(role=role, parts=[types.Part(text=m["content"])])
        )

    stream = client.models.generate_content_stream(
        model='gemini-3.5-flash',
        contents=contents,
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            temperature=temperature,
        ),
    )
    for chunk in stream:
        if chunk.text:
            yield chunk.text

# ---------- Memory: chat history ----------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------- Sidebar: settings ----------
with st.sidebar:
    st.header("Settings")

    provider = st.selectbox("AI engine", ["Ollama (local)", "Google Gemini (cloud)"])

    ollama_model = None
    if provider == "Ollama (local)":
        models = get_ollama_models()
        if models:
            ollama_model = st.selectbox("Ollama model", models)
        else:
            st.warning("No Ollama models found. Start Ollama and run: ollama pull llama3.2")
    else:
        st.caption("Model: Gemini Flash")
        if not getkey():
            st.warning("GEMINI_API_KEY is missing in your .env file.")

    system_prompt = st.text_area(
        "System prompt",
        "You are a helpful, friendly assistant. Keep answers clear and simple.",
    )
    temperature = st.slider("Temperature", 0.0, 1.0, 0.7, 0.1)

    if st.button("Clear chat"):
        st.session_state.messages = []
        st.rerun()

# ---------- Show the old messages ----------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# ---------- Handle a new message ----------
if prompt := st.chat_input("Type your message here..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    with st.chat_message("assistant"):
        try:
            if provider == "Ollama (local)":
                if not ollama_model:
                    raise RuntimeError("No Ollama model available.")
                stream = stream_ollama(
                    ollama_model, st.session_state.messages, system_prompt, temperature
                )
            else:
                if not getkey():
                    raise RuntimeError("Gemini API key not found.")
                stream = stream_gemini(
                    st.session_state.messages, system_prompt, temperature
                )

            reply = st.write_stream(stream)
            st.session_state.messages.append({"role": "assistant", "content": reply})

        except Exception as e:
            st.error(f"Error: {e}")
            st.session_state.messages.pop()   # remove the unanswered question
