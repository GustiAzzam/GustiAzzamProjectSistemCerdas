import streamlit as st
import tensorflow as tf
from PIL import Image
import numpy as np

# Load model (contoh dengan model pre-trained MobileNetV2)
model = tf.keras.applications.MobileNetV2(weights='imagenet')

# Fungsi untuk memprediksi gambar
def predict_image(image):
    # Resize gambar ke ukuran yang diterima oleh model (224x224 untuk MobileNetV2)
    img = image.resize((224, 224))
    img_array = np.asarray(img)  # Konversi gambar ke array numpy
    img_array = np.expand_dims(img_array, axis=0)  # Tambahkan dimensi batch

    # Normalisasi gambar sesuai dengan persyaratan model
    img_array = tf.keras.applications.mobilenet_v2.preprocess_input(img_array)

    # Prediksi dengan model
    predictions = model.predict(img_array)
    label = tf.keras.applications.mobilenet_v2.decode_predictions(predictions, top=1)[0][0]

    return label[1], label[2]  # Kembalikan label kelas dan probabilitas

# Main function untuk aplikasi Streamlit
def main():
    st.title("Aplikasi Pengenalan Gambar dengan Streamlit")

    # Upload gambar dari pengguna
    uploaded_image = st.file_uploader("Upload gambar", type=["jpg", "jpeg", "png"])

    if uploaded_image is not None:
        # Tampilkan gambar yang diupload
        image = Image.open(uploaded_image)
        st.image(image, caption='Gambar yang diupload', use_column_width=True)

        # Prediksi gambar
        if st.button('Prediksi'):
            label, confidence = predict_image(image)
            st.write(f'Prediksi: {label}, Kepercayaan: {confidence:.2f}')

# Panggil main function untuk menjalankan aplikasi
if __name__ == '__main__':
    main()
