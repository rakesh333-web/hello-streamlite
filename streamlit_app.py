import streamlit as st 
import pandas as pd

st.balloons()
st.markdown("# Data Evaluation App")

st.write("hi this is rakesh")
def read_excel(file):
    return pd.read_excel(file)

# Streamlit app
st.title("Excel File Viewer")

# File uploader widget
uploaded_file = st.file_uploader("Choose an Excel file", type=["xlsx", "xls", "csv"])
st.write("generate the excel sheet")

