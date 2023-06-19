import streamlit as st

import pandas as pd


st.header('Excel Categorizer')

df = None

file_path = st.file_uploader("Upload Excel file", type=["xlsx"])
if file_path:
    df = pd.read_excel(file_path)
    st.write(df)
