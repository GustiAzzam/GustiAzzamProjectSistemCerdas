import streamlit as st
import speech_recognition as sr

def main():
    st.title("Pengenalan Suara menggunakan SpeechRecognition")

    # Membuat objek recognizer
    recognizer = sr.Recognizer()

    # Mendefinisikan fungsi untuk menangkap suara
    def capture_audio():
        with sr.Microphone() as source:
            st.write("Silakan mulai berbicara...")
            audio_data = recognizer.listen(source)

        return audio_data

    # Menampilkan tombol untuk memulai pengenalan suara
    if st.button("Mulai Pengenalan Suara"):
        audio_data = capture_audio()

        try:
            text = recognizer.recognize_google(audio_data, language="id-ID")
            st.write("Hasil Pengenalan Suara:")
            st.write(text)
        except sr.UnknownValueError:
            st.write("Maaf, tidak dapat mengenali suara Anda.")
        except sr.RequestError as e:
            st.write(f"Error pada request: {e}")

if __name__ == "__main__":
    main()
