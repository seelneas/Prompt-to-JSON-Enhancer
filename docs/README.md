# Prompt-to-JSON Enhancer

### Prompt-to-JSON Enhancer is a tool that transforms **raw plain-text prompts** into **structured JSON objects** for more consistent and accurate outputs from LLMs (ChatGPT, Claude, Gemini, etc).

### It comes in **two flavors**:
#### - **Chrome Extension** – capture prompts directly from LLM platforms.
#### - **Web App (Streamlit UI)** – paste prompts into a simple UI and get structured JSON.



## ✨ Features
### - Capture prompts from ChatGPT, Claude, Gemini, etc.
### - Automatically enhance prompts into structured JSON with:
  #### - Title  
  #### - Description  
  #### - Target Persona  
  #### - Response Format  
  #### - Example Responses  
  #### - Constraints
### - Uses **Groq API (Llama 3 models)** for fast and reliable transformation.
### - Works as both a **browser extension** and a **web app**.


## 📂 Project Structure

### prompt-to-json-enhancer/
### │
### ├── extension/ # Chrome extension
### │ ├── manifest.json
### │ ├── popup.html
### │ ├── popup.css
### │ ├── popup.js
### │ └── content.js
### │
### ├── backend/ # Backend + Streamlit UI
### │ ├── main.py # FastAPI backend (Groq API calls)
### │ ├── config.py # API keys & constants
### │ ├── services/
### │ │ └── groq_service.py # Handles Groq API requests
### │ ├── utils/
### │ │ └── json_validator.py # Validates JSON schema
### │ └── app_ui.py # Streamlit UI
### │
### ├── requirements.txt # Python dependencies
### └── README.md # Project docs


## ⚙️ Setup & Installation

### 1. Clone the Repository

#### git clone https://github.com/yourusername/prompt-to-json-enhancer.git
#### pip install -r requirements.txt
#### GROQ_API_KEY=your_groq_api_key_here
#### GROQ_API_URL=https://api.groq.com/openai/v1/chat/completions

## Running Locally

### Option A – FastAPI Backend + Streamlit UI

#### 1. Start the backend:
#### uvicorn backend.main:app --reload --port 8000

#### 2. In a new terminal, run the Streamlit UI:
#### streamlit run backend/app_ui.py

### Option B - Chrome Extension

#### 1. Go to chrome://extensions/ in Chrome.
#### 2. Enable Developer Mode.
#### 3. Click Load unpacked → select the extension/ folder.
#### 4. Open ChatGPT, Claude, Gemini, etc. → highlight a prompt → click the extension icon → "Enhance to JSON".

## Tech Stack

### Backend: FastAPI (Python)
### Frontend: Streamlit
### Browser Extension: HTML, CSS, JAVASCRIPT
### LLM API: Groq (llama-3.1-8b-instant)

## Deliverables

### GitHub repo with clean, documented code
### Working deployment (Streamlit Cloud)
### Chrome extension (manual install)


