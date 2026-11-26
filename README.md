# Solar Load Calculator - Electricity Bill to Excel

## Project Overview

This Streamlit application automates the extraction of selected details from electricity bills and transfers the extracted values into an uploaded Excel template.

It uses Google Gemini to extract information from supported PDF and image files, and OpenPyXL to populate the Excel workbook.

**Important:** The current implementation extracts electricity-bill information and fills an Excel template. It does not yet calculate solar panel capacity, installation cost, savings, or payback period.

## Features

- Upload an electricity bill as PDF, JPG, JPEG, or PNG.
- Upload an Excel template in XLSX format.
- Extract selected bill information using Google Gemini.
- Display the extracted data for review.
- Populate predefined cells in the uploaded workbook.
- Download the completed Excel file.

## Technology Stack

- Python
- Streamlit
- Google Gen AI SDK
- OpenPyXL
- Pillow
- python-dotenv

## Project Structure

```text
Solar-Load-Calculator-Electricity-Bill-to-Excel-/
├── assets/
├── services/
│   ├── ai_extractor.py
│   └── excel_handler.py
├── utils/
│   └── file_utils.py
├── app.py
├── config.py
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Information Extracted

The current extraction prompt requests these fields:

| Field | Description | Excel cell |
|---|---|---|
| consumer_name | Customer name | B5 |
| consumer_number | Consumer number | B6 |
| sanctioned_load | Sanctioned load in kW | B10 |
| avg_monthly_units | Average monthly units | B12 |

The cell locations are configured in `config.py`. The Excel template must contain the expected worksheet and cell layout.

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/phanikumar-145/Solar-Load-Calculator-Electricity-Bill-to-Excel-.git
cd Solar-Load-Calculator-Electricity-Bill-to-Excel-
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
```

Windows PowerShell:

```powershell
venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the Gemini API key

Create a local file named `.env` in the project root. Use `.env.example` as a reference:

```env
GEMINI_API_KEY=your_actual_gemini_api_key
```

Do not commit `.env` or publish your API key.

### 5. Run the application

```bash
streamlit run app.py
```

## How to Use

1. Start the Streamlit application.
2. Upload an electricity bill in PDF, JPG, JPEG, or PNG format.
3. Upload the Excel template in XLSX format.
4. Select **Run AI Automation**.
5. Review the extracted information displayed by the application.
6. Download the completed Excel report.

## Processing Workflow

1. The application receives the uploaded bill and Excel template.
2. It checks the bill file and determines its MIME type.
3. The extraction service sends the bill and extraction prompt to Gemini.
4. The response is parsed as JSON.
5. The Excel service writes the extracted fields into the configured cells.
6. The completed workbook is offered as a download.

## Configuration

The following settings are maintained in `config.py`:

- Gemini API key is loaded from the `GEMINI_API_KEY` environment variable.
- Gemini model options are defined in `GEMINI_MODEL_OPTIONS`.
- Excel field-to-cell mappings are defined in `EXCEL_CELL_MAP`.
- The extraction instructions are defined in `EXTRACT_PROMPT`.

The current extraction prompt is written for MSEDCL electricity bills. Other electricity providers may require prompt changes and validation.

## Limitations

- Extraction quality depends on the clarity and readability of the uploaded bill.
- The extraction prompt currently targets MSEDCL bills.
- Only the configured fields are extracted and written to Excel.
- The workbook must have the expected template structure.
- AI-generated values should be checked against the original bill before use.
- The application does not currently perform solar system sizing or financial calculations.

## Security

- Store the real Gemini API key in a local `.env` file.
- Never commit `.env` or API credentials.
- Review extracted personal and electricity-consumption information before sharing generated reports.
- Avoid committing real customer bills or reports unless you have permission and have removed sensitive information.

## Possible Future Improvements

- Support bills from additional electricity providers.
- Add validation and confidence indicators for extracted fields.
- Support processing multiple bills in one session.
- Calculate estimated solar capacity from electricity consumption.
- Estimate solar generation, savings, and payback period.
- Add downloadable extraction summaries and validation reports.

## Author

**Phani Kumar**

AI/ML and Generative AI Developer

GitHub: https://github.com/phanikumar-145
