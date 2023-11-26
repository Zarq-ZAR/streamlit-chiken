import pandas as pd
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu 
from sklearn.preprocessing import LabelEncoder


from web_functions import predict


def app(df, x, y):

    st.title("Halaman Prediksi Ayam Pedaging")

    df = pd.read_csv('ayam_pedaging_fix.csv')
    kota = df['Kota']
    data = df[['Populasi 2017', 'Populasi 2018', 'Produksi 2017', 'Produksi 2018']]

    col1, col2 = st.columns(2)

    with col1:
        po17 = st.text_input ('Input Nilai Populasi 2017')
    with col1:
        po18 = st.text_input ('Input Nilai Populasi 2018')
    with col2:    
        pro17 = st.text_input ('Input Nilai Produksi 2017')
    with col2:
        pro18 = st.text_input ('Input Nilai Produksi 2018')

    features = [po17,po18,pro17,pro18]

    # Tombol prediksi
    if st.button("Prediksi"):
        prediction, score = predict(x, y, features)
        st.info("Prediksi Sukses...")

        # Buat objek LabelEncoder
        label_encoder = LabelEncoder()

        # Lakukan enkoding pada kolom 'Kota'
        encoded_kota = label_encoder.fit_transform(kota)

        # Ubah input data ke tipe float
        input_data = np.array(features, dtype=float)
        input_data_reshape = input_data.reshape(1, -1)

        # Lakukan prediksi
        prediction = model.predict(np.array(features).reshape(1,-1))
        # Decode nilai prediksi
        decoded_prediction = label_encoder.inverse_transform(prediction)

        # Temukan kota yang sesuai dengan input
        matching_kota = kota.iloc[np.where((x == input_data).all(axis=1))[0][0]]

        if decoded_prediction[0] == 0:
            st.warning(f"Skala Produksi Ayam Pedaging di kota {matching_kota} rendah")
        else:
            st.success(f"Skala Produksi Ayam Pedaging di kota {matching_kota} tinggi")

        st.write("Model yang digunakan memiliki tingkat akurasi", (score*100), "%")

# Menjalankan aplikasi Streamlit jika file ini dijalankan sebagai program utama
# if __name__ == "__main__":
#     app(df1, df2, x1, y1, x2, y2)