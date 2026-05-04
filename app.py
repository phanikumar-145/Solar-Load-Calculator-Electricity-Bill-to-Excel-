import streamlit as st
from services.ai_extractor import extract_bill_data
from services.excel_handler import fill_excel_template
from utils.file_utils import get_mime_type, validate_file

st.set_page_config(page_title="EnergyBae | Solar Automator", page_icon="☀️")
st.title("☀️ Solar Load Calculator")
st.caption("AI-Powered Electricity Bill Automation for EnergyBae")

st.write("### 📤 Upload Documents")
col1, col2 = st.columns(2)
with col1:
    bill_file = st.file_uploader("Electricity Bill (Image/PDF)", type=["png", "jpg", "jpeg", "pdf"])
with col2:
    template_file = st.file_uploader("Solar Excel Template", type=["xlsx"])

if bill_file and template_file:
    if st.button("🚀 Run AI Automation"):
        try:
            with st.spinner("Analyzing bill with AI..."):
                bill_bytes = bill_file.read()
                mime = get_mime_type(bill_file.name)
                validate_file(bill_bytes, mime)
                data = extract_bill_data(bill_bytes, mime)

            st.success("Extraction complete!")
            with st.expander("👁️ View Extracted Data"):
                st.json(data)

            with st.spinner("Filling Excel template..."):
                template_file.seek(0)
                filled = fill_excel_template(template_file.read(), data)

            st.download_button(
                label="📥 Download Filled Solar Report",
                data=filled,
                file_name=f"Solar_{data.get('consumer_number', 'output')}.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            )
        except Exception as e:
            st.error(f"Error: {e}")
else:
    st.info("Upload both files to begin.")