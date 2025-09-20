from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
from services.groq_service import call_groq_model, extract_first_json
from utils.json_validator import validate_json_obj
from config import SYSTEM_PROMPT

app = FastAPI(title="Prompt-to-JSON Enhancer")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:*/", "http://127.0.0.1:*/", "http://localhost:8000", "http://localhost:4200", "chrome-extension://*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class EnhanceRequest(BaseModel):
    prompt: str

@app.post("/enhance")
async def enhance(req: EnhanceRequest):
    user_prompt = req.prompt.strip()
    if not user_prompt:
        raise HTTPException(status_code=400, detail="Prompt is empty")

    try:
        raw_text = call_groq_model(user_prompt)
    except Exception as e:
        raise HTTPException(status_code=502, detail=f"Error calling Groq API: {str(e)}")

    parsed = None

    try:
        parsed = json.loads(raw_text)
    except Exception:
        candidate = extract_first_json(raw_text)
        if candidate:
            try:
                parsed = json.loads(candidate)
            except Exception as e:
                parsed = None

    if not parsed:
        raise HTTPException(
            status_code=500,
            detail=f"Unable to extract a valid JSON object from model output. Raw output: {raw_text[:2000]}"
        )

    try:
        valid = validate_json_obj(parsed)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"JSON validation error: {str(e)}. Parsed JSON: {json.dumps(parsed, indent=2)[:2000]}")

    return parsed
