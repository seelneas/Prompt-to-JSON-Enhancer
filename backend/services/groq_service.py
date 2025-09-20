import requests
import re
import json
from typing import Optional
from config import GROQ_API_KEY, GROQ_API_URL, SYSTEM_PROMPT

def call_groq_model(user_prompt: str, timeout: int = 30) -> str:
    """
    Calls Groq API model with system + user prompt.
    Returns the model's text output (string).
    """
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "model" : "llama-3.1-8b-instant",
        "messages": [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": user_prompt}
        ],
        "temperature": 0.2, 
        "max_tokens": 800
    }

    url = f"{GROQ_API_URL}"  
    resp = requests.post(url, headers=headers, json=payload, timeout=timeout)
    print("DEBUG:", resp.status_code, resp.text)
    resp.raise_for_status()
    data = resp.json()

    text = None
    try:
        text = data.get("output", [])[0].get("content", [])[0].get("text")
    except Exception:
        text = None
    if not text:
        try:
            text = data.get("choices", [])[0].get("message", {}).get("content")
        except Exception:
            text = None
    if not text:
        text = data.get("text") or data.get("response") or json.dumps(data)

    return text

def extract_first_json(text: str) -> Optional[str]:
    """
    Attempts to extract the first JSON object/array substring from text.
    Returns JSON string or None.
    """
    if not text:
        return None
    start = None
    for i, ch in enumerate(text):
        if ch == '{' or ch == '[':
            start = i
            break
    if start is None:
        return None
    for end in range(len(text), start, -1):
        candidate = text[start:end].strip()
        try:
            _ = json.loads(candidate)
            return candidate
        except Exception:
            continue
    match = re.search(r'(\{.*\})', text, flags=re.DOTALL)
    if match:
        try:
            _ = json.loads(match.group(1))
            return match.group(1)
        except Exception:
            return None
    return None
