from pydantic import BaseModel, validator
from typing import List, Any

class EnhancedPrompt(BaseModel):
    prompt_title: str
    prompt_description: str
    target_persona: str
    response_format: str
    response_examples: List[str]
    constraints: List[str]

    @validator("prompt_title", "prompt_description", "target_persona", "response_format")
    def not_empty(cls, v):
        if not v or not str(v).strip():
            raise ValueError("must not be empty")
        return v

def validate_json_obj(obj: Any) -> EnhancedPrompt:
    """
    Raises ValidationError if invalid.
    """
    return EnhancedPrompt.parse_obj(obj)
