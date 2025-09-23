# Prompt-to-JSON Enhancer

The **Prompt-to-JSON Enhancer** is a versatile tool that converts **raw, plain-text prompts** into **structured JSON objects**. This helps improve the consistency and accuracy of outputs from large language models (LLMs) like ChatGPT, Claude, and Gemini.

---

## Features

* **Prompt Capture:** Capture prompts directly from popular LLM platforms such as ChatGPT, Claude, and Gemini.
* **Automatic Enhancement:** Automatically transform prompts into structured JSON with the following fields:
    * Title
    * Description
    * Target Persona
    * Response Format
    * Example Responses
    * Constraints
* **Fast and Reliable:** Utilizes the **Groq API** (Llama 3 models) for rapid and dependable transformations.
* **Dual Functionality:** Available as both a **browser extension** and a **web application**.

---

## Live Demo
* Try the app online without installation:
* [Live Web App](https://prompt-to-json-enhancer.streamlit.app/)

## Setup & Installation

1.  **Clone the Repository**
    * `git clone https://github.com/yourusername/prompt-to-json-enhancer.git`
2.  **Install Dependencies**
    * `pip install -r requirements.txt`
3.  **Set Environment Variables**
    * `GROQ_API_KEY=your_groq_api_key_here`
    * `GROQ_API_URL=https://api.groq.com/openai/v1/chat/completions`

---

## Running Locally

### Option A: FastAPI Backend + Streamlit UI

1.  **Start the Backend:**
    * `uvicorn backend.main:app --reload --port 8000`
2.  **Run the Streamlit UI:**
    * In a new terminal, run: `streamlit run backend/app_ui.py`

### Option B: Chrome Extension

1.  Navigate to `chrome://extensions/` in your Chrome browser.
2.  Enable **Developer Mode**.
3.  Click **Load unpacked** and select the `extension/` folder.
4.  Open an LLM platform (e.g., ChatGPT), highlight a prompt, click the extension icon, and select **"Enhance to JSON"**.

---

## Tech Stack

* **Backend:** FastAPI (Python)
* **Frontend:** Streamlit
* **Browser Extension:** HTML, CSS, JavaScript
* **LLM API:** Groq (`llama-3.1-8b-instant`)

---

## Deliverables

* A GitHub repository with clean, documented code.
* A working deployment on Streamlit Cloud.
* A Chrome extension for manual installation.
