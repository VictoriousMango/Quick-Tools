import streamlit as st
import pyttsx3
import tempfile
import os

def convert_to_audio(text):
    engine = pyttsx3.init()
    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        temp_filename = temp_file.name
        engine.save_to_file(text, temp_filename)
        engine.runAndWait()
    return temp_filename

def main():
    st.title("StreamSound - Text to Audio Converter")

    # Input text
    text = st.text_area("Enter text to convert", height=200)

    # Convert button
    if st.button("Convert to Audio"):
        if text:
            audio_file = convert_to_audio(text)
            audio_bytes = open(audio_file, "rb").read()
            st.audio(audio_bytes, format="audio/wav")
            os.remove(audio_file)
        else:
            st.warning("Please enter some text to convert.")

if __name__ == "__main__":
    main()
