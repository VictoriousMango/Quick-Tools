import streamlit as st
import pandas as pd

st.header('Excel Categorizer')

uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)

if uploaded_files:
    df = pd.read_excel(file_path, engine="openpyxl")

if df is not None:
    st.dataframe(df)
