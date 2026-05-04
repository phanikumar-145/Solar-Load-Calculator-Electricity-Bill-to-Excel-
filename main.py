from services.ai_extractor import extract_bill_data
from services.excel_handler import fill_excel_template
from utils.file_utils import get_mime_type

if __name__ == "__main__":
    bill_path = "assets/sample_bill.jpg"
    template_path = "assets/solar_template.xlsx"

    with open(bill_path, "rb") as f:
        bill_bytes = f.read()

    mime = get_mime_type(bill_path)
    data = extract_bill_data(bill_bytes, mime)
    print("Extracted:", data)

    with open(template_path, "rb") as f:
        filled = fill_excel_template(f.read(), data)

    with open("output.xlsx", "wb") as f:
        f.write(filled)
    print("Saved output.xlsx")