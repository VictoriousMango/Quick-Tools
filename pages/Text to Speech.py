import streamlit as st

st.header('Welcome to Text to Speech Converter')

text = st.text_area('Enter your Text')
st.write(text)