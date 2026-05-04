import json
from google import genai
from google.genai import types
from config import GEMINI_API_KEY, GEMINI_MODEL_OPTIONS, EXTRACT_PROMPT

client = genai.Client(api_key=GEMINI_API_KEY)

def extract_bill_data(file_bytes: bytes, mime_type: str) -> dict:
    last_error = None
    for model_id in GEMINI_MODEL_OPTIONS:
        try:
            response = client.models.generate_content(
                model=model_id,
                contents=[
                    EXTRACT_PROMPT,
                    types.Part.from_bytes(data=file_bytes, mime_type=mime_type),
                ]
            )
            raw = response.text.strip()
            if "```" in raw:
                raw = raw.split("```json")[-1].split("```")[0].strip()
            return json.loads(raw)
        except Exception as e:
            last_error = e
            continue
    raise RuntimeError(f"All models failed. Last error: {last_error}")