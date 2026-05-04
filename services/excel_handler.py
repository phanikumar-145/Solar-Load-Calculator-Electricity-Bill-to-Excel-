import io
import openpyxl
from config import EXCEL_CELL_MAP

def fill_excel_template(template_bytes: bytes, data: dict) -> bytes:
    wb = openpyxl.load_workbook(io.BytesIO(template_bytes))
    sheet = wb.active

    for field, cell in EXCEL_CELL_MAP.items():
        sheet[cell] = data.get(field)

    output = io.BytesIO()
    wb.save(output)
    return output.getvalue()