import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

GEMINI_MODEL_OPTIONS = [
    "gemini-2.5-flash",
    "gemini-2.0-flash",
    "gemini-2.5-flash-lite",
]

EXCEL_CELL_MAP = {
    "consumer_name":    "B5",
    "consumer_number":  "B6",
    "sanctioned_load":  "B10",
    "avg_monthly_units":"B12",
}

EXTRACT_PROMPT = """
Extract the following from this MSEDCL electricity bill as strict JSON.
Return ONLY valid JSON — no markdown, no backticks, no extra text:
{
    "consumer_name": "Full name of the customer",
    "consumer_number": "12 digit consumer number",
    "sanctioned_load": "value in KW as a float",
    "avg_monthly_units": "average monthly units as an int"
}
"""