# AI-Powered Solar Load Calculator and Electricity Bill to Excel Automation

## Project Overview

The Solar Load Calculator is an AI-powered electricity bill processing application that automates the extraction of important customer and electricity consumption details from electricity bills.

The application uses Google Gemini to extract structured information from uploaded electricity bills in PDF or image format. The extracted information is then automatically inserted into predefined cells in an Excel template.

The application is designed to reduce manual data entry and simplify the preparation of solar-related electricity reports.

The frontend is developed using Streamlit, Google Gemini handles document information extraction, and OpenPyXL manages Excel template processing.

## Key Features

- Upload electricity bills in PDF and image formats.
- Upload an existing Excel template.
- Extract electricity bill information using Google Gemini.
- Identify customer details and electricity consumption information.
- Extract consumer name and consumer number.
- Extract sanctioned load in kilowatts.
- Extract average monthly electricity consumption.
- Convert extracted information into structured JSON.
- Automatically populate predefined Excel cells.
- Download the completed Excel report.
- Support multiple Gemini model options as configured in the application.
- Validate uploaded file types and empty files.

## Technologies Used

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Frontend | Streamlit |
| AI Model | Google Gemini |
| AI Integration | Google Gen AI SDK |
| Excel Processing | OpenPyXL |
| Image Processing | Pillow |
| Configuration | Python dotenv |
| Data Format | JSON |
| File Handling | Python BytesIO |

## Project Architecture

The application follows an AI-powered document extraction and Excel automation workflow.

1. The user uploads an electricity bill in PDF or image format.
2. The user uploads an Excel template.
3. The application validates the uploaded electricity bill.
4. The file is converted into bytes and its MIME type is identified.
5. The Google Gemini API receives the electricity bill and extraction instructions.
6. Gemini extracts the required electricity bill information.
7. The extracted response is converted into structured JSON.
8. OpenPyXL opens the uploaded Excel template.
9. The extracted information is inserted into predefined Excel cells.
10. The completed Excel file is generated and made available for download.

## Technologies and Their Roles

### Python

Used for application development, file processing, API integration, and automation logic.

### Streamlit

Provides the interactive interface for uploading electricity bills, uploading Excel templates, viewing extracted information, and downloading the completed report.

### Google Gemini

Uses multimodal AI capabilities to read electricity bill documents and extract important information.

### OpenPyXL

Reads and modifies Excel workbooks by inserting extracted information into predefined cells.

### Python dotenv

Loads the Google Gemini API key securely from environment variables.

## Project Structure

```text
Solar-Load-Calculator-Electricity-Bill-to-Excel-/
|
├── assets/
|   ├── sample_bill.jpg
|   └── solar_template.xlsx
|
├── services/
|   ├── ai_extractor.py
|   └── excel_handler.py
|
├── utils/
|   └── file_utils.py
|
├── app.py
├── main.py
├── config.py
├── requirements.txt
├── .gitignore
└── README.md
```

## File Description

| File | Description |
|---|---|
| app.py | Streamlit application for uploading documents and downloading completed Excel reports. |
| main.py | Runs the document extraction and Excel generation workflow using sample files. |
| config.py | Stores Gemini configuration, model options, Excel cell mappings, and extraction prompt. |
| services/ai_extractor.py | Integrates Google Gemini to extract electricity bill information. |
| services/excel_handler.py | Uses OpenPyXL to populate the Excel template. |
| utils/file_utils.py | Handles MIME type identification and uploaded file validation. |
| requirements.txt | Contains the required Python dependencies. |
| assets/ | Contains sample input documents and the Excel template. |

## Information Extracted from Electricity Bills

The current extraction prompt is designed to retrieve the following information from MSEDCL electricity bills.

| Field | Description | Excel Cell |
|---|---|---|
| consumer_name | Full name of the customer | B5 |
| consumer_number | 12-digit consumer number | B6 |
| sanctioned_load | Sanctioned electrical load in kW | B10 |
| avg_monthly_units | Average monthly electricity consumption | B12 |

The extracted values are inserted into the corresponding Excel cells using the mapping defined in `config.py`.

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/phanikumar-145/Solar-Load-Calculator-Electricity-Bill-to-Excel-.git
```

### 2. Navigate to the Project Directory

```bash
cd Solar-Load-Calculator-Electricity-Bill-to-Excel-
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment on Windows:

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure the Google Gemini API Key

Create a `.env` file in the project directory.

```env
GEMINI_API_KEY=your_gemini_api_key
```

Replace the placeholder with your actual Google Gemini API key.

Never upload your actual API key to GitHub.

### 6. Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

## How to Use the Application

### Step 1: Upload Electricity Bill

Upload an electricity bill in one of the supported formats:

- PDF
- JPG
- JPEG
- PNG

### Step 2: Upload Excel Template

Upload the Excel template in `.xlsx` format.

The template should contain the required cells and formatting.

### Step 3: Run AI Automation

Click the Run AI Automation button.

The application validates the uploaded bill and sends it to Google Gemini for information extraction.

### Step 4: Review Extracted Information

View the extracted customer and electricity consumption details in the application.

### Step 5: Download Excel Report

The application fills the predefined Excel cells with the extracted information.

Download the completed Excel report for further use.

## Example Extraction Output

The AI extraction process is designed to return structured JSON similar to the following:

```json
{
    "consumer_name": "Sample Customer",
    "consumer_number": "123456789012",
    "sanctioned_load": 3.5,
    "avg_monthly_units": 450
}
```

The values above are illustrative examples, not actual customer information.

## Excel Automation

The application uses OpenPyXL to populate an existing Excel template.

The current cell mapping is:

```python
EXCEL_CELL_MAP = {
    "consumer_name": "B5",
    "consumer_number": "B6",
    "sanctioned_load": "B10",
    "avg_monthly_units": "B12"
}
```

The application preserves the existing workbook structure and writes the extracted values into the mapped cells.

## Error Handling

The application includes basic validation and error handling for:

- Empty uploaded files.
- Unsupported file formats.
- Gemini model failures.
- Failed JSON parsing.
- Excel processing errors.

The extraction service also tries alternative Gemini models when a model request fails.

## Future Improvements

- Support electricity bills from multiple electricity providers.
- Improve extraction accuracy for scanned and low-quality documents.
- Add confidence scores for extracted fields.
- Validate consumer numbers and electricity consumption values.
- Add support for multiple electricity bills in one upload.
- Calculate estimated solar panel capacity using consumption data.
- Estimate solar generation and potential savings.
- Add electricity tariff analysis.
- Generate detailed solar installation reports.
- Add extraction history and report management.
- Add automated comparison between electricity bills.

## Important Limitations

- The current extraction prompt is designed specifically for MSEDCL electricity bills.
- Extraction accuracy depends on document quality and the availability of readable information.
- The application currently extracts four predefined fields.
- The Excel output depends on the uploaded template and predefined cell mappings.
- The current implementation populates an Excel template; it does not independently calculate solar panel sizing, installation costs, or financial savings.

## Author

**Phani Kumar**

AI/ML and Generative AI Developer

GitHub: https://github.com/phanikumar-145
