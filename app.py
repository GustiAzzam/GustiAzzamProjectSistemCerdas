import streamlit as st
import speech_recognition as sr

# Fungsi untuk mendeteksi teks dari file audio
def detect_audio(file):
    recognizer = sr.Recognizer()
    
    try:
        with sr.AudioFile(file) as source:
            audio_data = recognizer.record(source)
            text = recognizer.recognize_google(audio_data)
            return text
    except sr.UnknownValueError:
        return "Suara tidak dikenali"
    except sr.RequestError:
        return "Tidak dapat mengakses layanan pengenalan suara"

# Main function untuk aplikasi Streamlit
def main():
    st.title("Aplikasi Pengenalan Suara")

    # Upload file audio dari pengguna
    uploaded_file = st.file_uploader("Unggah file audio", type=['wav'])

    if uploaded_file is not None:
        st.audio(uploaded_file, format='audio/wav')

        # Deteksi audio
        if st.button('Deteksi Suara'):
            result = detect_audio(uploaded_file)
            st.write('Hasil Deteksi:', result)

# Panggil main function untuk menjalankan aplikasi
if __name__ == '__main__':
    main()
