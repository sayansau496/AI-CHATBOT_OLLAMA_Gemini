#  AI Chatbot – Ollama & Google Gemini

A dual-engine AI Chatbot developed using **Python and Streamlit**, allowing users to interact with two different Large Language Model (LLM) providers:

1. **Ollama (Local AI):** Run AI models locally on your computer.
2. **Google Gemini (Cloud AI):** Generate AI responses using Google's Gemini API.

The application provides a simple, interactive chat interface with conversation history, streaming responses, customizable system prompts, and temperature settings.

##  Features

- **Dual AI Engine:** Switch between Ollama and Google Gemini.
- **Local AI with Ollama:** Run downloaded models such as Llama 3.2 locally.
- **Google Gemini Integration:** Connect with Google's Gemini Flash model.
- **Real-Time Streaming:** Display AI responses as they are generated.
- **Chat History:** Maintain conversation history using Streamlit Session State.
- **Model Selection:** Automatically detect available Ollama models.
- **Custom System Prompt:** Define the chatbot's behaviour and instructions.
- **Temperature Control:** Adjust AI response creativity.
- **Clear Chat:** Reset the conversation whenever required.
- **Error Handling:** Handle missing API keys and unavailable Ollama models.

##  Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web application interface |
| Ollama | Local LLM integration |
| Google Gemini API | Cloud-based AI integration |
| Google GenAI SDK | Gemini API communication |
| Python-dotenv | Environment variable management |

##  Project Structure

```text
AI-CHATBOT_OLLAMA_Gemini/
│
├── app.py              # Main Streamlit application
├── config.py           # Gemini API key configuration
├── .env                # API key (not uploaded to GitHub)
├── .gitignore          # Files excluded from Git
└── README.md           # Project documentation
```

## Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/sayansau496/AI-CHATBOT_OLLAMA_Gemini.git
```

### Step 2: Navigate to the Project Folder

```bash
cd AI-CHATBOT_OLLAMA_Gemini
```

### Step 3: Install Required Libraries

```bash
pip install streamlit ollama google-genai python-dotenv
```

##  Configuration – Google Gemini API

### Step 1: Get Gemini API Key

Visit Google AI Studio:

https://aistudio.google.com/apikey

Generate your API key.

### Step 2: Create a `.env` File

Inside your project folder, create a file named `.env`.

Add:

```env
GEMINI_API_KEY=your_actual_api_key
```

### Step 3: Create `config.py`

```python
import os
from dotenv import load_dotenv

load_dotenv()

def getkey():
    return os.getenv("GEMINI_API_KEY")
```

**Important:** Never upload your actual API key to GitHub.

## 🦙 Ollama Setup (Local AI)

### Step 1: Install Ollama

Download Ollama from:

https://ollama.com/download

### Step 2: Download an AI Model

Open Command Prompt or Terminal and execute:

```bash
ollama pull llama3.2
```

### Step 3: Start Ollama

Make sure the Ollama application or service is running.

To check downloaded models:

```bash
ollama list
```

## Run the Application

Execute the following command from your project directory:

```bash
streamlit run app.py
```

The application will open in your default browser.

Default local URL:

```text
http://localhost:8501
```

## How to Use

1. Open the AI Chatbot web application.
2. Select your preferred AI engine from the sidebar:
   - Ollama (local)
   - Google Gemini (cloud)
3. If using Ollama, select an available downloaded model.
4. Enter or modify the System Prompt.
5. Adjust the Temperature setting.
6. Type your question in the chat input box.
7. Click Enter to receive the AI-generated response.
8. Use Clear Chat to start a new conversation.

## Important Settings

| Setting | Description |
|---|---|
| AI Engine | Select Ollama or Gemini |
| Ollama Model | Choose an installed local model |
| System Prompt | Define chatbot instructions |
| Temperature | Control response creativity (0.0–1.0) |
| Clear Chat | Remove conversation history |

##  Security

Add the following `.gitignore` file:

```text
.env
__pycache__/
*.pyc
.venv/
venv/
```

This prevents sensitive API credentials and unnecessary Python files from being uploaded to GitHub.

## Learning Outcomes

Through this project, learners can understand:

- Building interactive web applications using Streamlit.
- Integrating multiple AI providers into one application.
- Working with Large Language Models (LLMs).
- Connecting Python applications with REST-based AI services through SDKs.
- Implementing streaming AI responses.
- Managing conversation history using Session State.
- Working with environment variables and API keys.
- Understanding the difference between local and cloud-based AI models.

## Author

**Sayan Sau**

GitHub: https://github.com/sayansau496

##  Repository

https://github.com/sayansau496/AI-CHATBOT_OLLAMA_Gemini
## Screenshot
<img width="1920" height="3129" alt="AI-Chatbot" src="https://github.com/user-attachments/assets/774475f9-0067-4b8e-96e7-42b271e7bb49" />
## Special Thanks to Mr Amitava Chattopadhya Sir & Mrs Arpita Gupta Madam (CoE Kolkata)


---

⭐ If you find this project useful, consider giving the repository a star!
