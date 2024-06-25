import speech_recognition as sr

# Fungsi untuk mengenali suara dari mikrofon
def recognize_speech():
    # Inisialisasi recognizer
    recognizer = sr.Recognizer()

    # Gunakan microphone sebagai source
    with sr.Microphone() as source:
        print("Silakan mulai berbicara...")
        recognizer.adjust_for_ambient_noise(source)  # Menyesuaikan dengan noise lingkungan
        audio = recognizer.listen(source)  # Mendengarkan input audio dari mikrofon

    try:
        # Menggunakan Google Web Speech API untuk mentranskripsi audio menjadi teks
        text = recognizer.recognize_google(audio, language="id-ID")
        print("Anda berkata:", text)
    except sr.UnknownValueError:
        print("Maaf, tidak dapat mengenali apa yang Anda katakan.")
    except sr.RequestError as e:
        print(f"Error pada request API: {e}")

# Panggil fungsi untuk memulai pengenalan suara
recognize_speech()
