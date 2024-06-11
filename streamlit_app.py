import streamlit as st 
import pandas as pd

    
st.markdown("# Data Evaluation App")

st.write("HI: this is B.rakesh welcome ")



st.title("Excel File Viewer")

# File uploader widget

st.write("generate the excel sheet")

    df=pd.read_excel(EXAMPLEINPUT.xlsx)
    st.dataframe(df)
    st.write(df.to_string())

