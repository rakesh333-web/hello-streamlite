import streamlit as st 
import pandas as pd

    
st.markdown("# Data Evaluation App")

st.write("HI: this is B.rakesh welcome ")
def read_excel(file):
    return pd.read_excel(file)


st.title("Excel File Viewer")

# File uploader widget
uploaded_file = st.file_uploader("Choose an Excel file", type=["xlsx", "xls", "csv"])
st.write("generate the excel sheet")
if uploaded_file is not None:
    df=pd.read_excel(EXAMPLEINPUT.xlsx)
    st.dataframe(df)
    st.write(df.to_string())

