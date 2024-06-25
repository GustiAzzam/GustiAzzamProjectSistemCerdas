import streamlit as st
from google.cloud import speech_v1p1beta1 as speech

# Fungsi untuk mengenali teks dari audio menggunakan Google Cloud Speech-to-Text
def recognize_audio(audio_file):
    client = speech.SpeechClient()

    # Konfigurasi untuk pemrosesan audio
    config = {
        "encoding": speech.RecognitionConfig.AudioEncoding.LINEAR16,
        "sample_rate_hertz": 44100,
        "language_code": "en-US",
    }

    # Baca file audio sebagai binary
    content = audio_file.read()

    # Request ke Google Cloud Speech-to-Text
    audio = {"content": content}
    response = client.recognize(config=config, audio=audio)

    # Ambil hasil teks dari response
    results = [result.alternatives[0].transcript for result in response.results]
    return results

# Main function untuk aplikasi Streamlit
def main():
    st.title("Aplikasi Pengenalan Suara dengan Google Cloud")

    # Upload file audio dari pengguna
    uploaded_file = st.file_uploader("Unggah file audio", type=['wav'])

    if uploaded_file is not None:
        st.audio(uploaded_file, format='audio/wav')

        # Deteksi audio menggunakan Google Cloud Speech-to-Text
        if st.button('Deteksi Suara'):
            results = recognize_audio(uploaded_file)
            st.write('Hasil Deteksi:', results)

# Panggil main function untuk menjalankan aplikasi
if __name__ == '__main__':
    main()
