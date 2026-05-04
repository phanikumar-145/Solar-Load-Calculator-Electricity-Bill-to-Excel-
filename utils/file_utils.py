ALLOWED_BILL_TYPES = ["image/jpeg", "image/png", "application/pdf"]

def get_mime_type(filename: str) -> str:
    name = filename.lower()
    if name.endswith(".pdf"):
        return "application/pdf"
    elif name.endswith(".png"):
        return "image/png"
    return "image/jpeg"

def validate_file(file_bytes: bytes, mime_type: str) -> None:
    if not file_bytes:
        raise ValueError("Uploaded file is empty.")
    if mime_type not in ALLOWED_BILL_TYPES:
        raise ValueError(f"Unsupported file type: {mime_type}")