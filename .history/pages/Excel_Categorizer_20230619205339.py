import streamlit as st
import pandas as pd

st.header('Excel Categorizer')

uploaded_files = st.file_uploader("Choose a CSV file", type=["xlsx"])

df = None

if uploaded_files:
    df = pd.read_excel(uploaded_files, engine="openpyxl")

if df is not None:
    st.dataframe(df)
