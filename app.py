import streamlit as st
import speech_recognition as sr
from langdetect import detect

def recognize_language(audio_file):
    r = sr.Recognizer()
    
    with sr.AudioFile(audio_file) as source:
        audio = r.record(source)
        
    try:
        text = r.recognize_google(audio, language="auto")
        language = detect(text)
        return language
    except sr.UnknownValueError:
        return "Unable to recognize speech"
    except sr.RequestError:
        return "Speech recognition service is unavailable"

def main():
    st.title("Simple Language Recognition from Speech App")
    st.write("Speak something to recognize the language!")

    uploaded_file = st.file_uploader("Choose a WAV file", type="wav")

    if uploaded_file is not None:
        st.audio(uploaded_file, format='audio/wav')

        if st.button('Recognize Language'):
            language = recognize_language(uploaded_file)
            st.write(f"Detected language: {language}")

if __name__ == '__main__':
    main()
