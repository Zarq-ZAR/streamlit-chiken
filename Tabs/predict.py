import pandas as pd
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu 

from web_functions import predict

df = pd.read_csv('Poultry_Chiken_Village.csv')
df1 = pd.read_csv('Poultry-ChikenVillage.csv')
df2 = pd.read_csv('Poultry-Pedaging.csv', encoding='latin1')
kota = df['Kota/Kabupaten']

def app(df1, df2, x1, y1, x2, y2):

    st.title("Halaman Prediksi")

    # Tambahkan dropdown menu untuk pilihan jenis daging unggas
    selected_option = st.selectbox("Pilih Jenis Daging Unggas", ["Ayam Kampung", "Ayam Pedaging"])

    if selected_option == "Ayam Kampung":
        data = df1   # Gunakan data Ayam Kampung
    elif selected_option == "Ayam Pedaging":
        data = df2  # Gunakan data Ayam Pedaging
    # elif selected_option == "Ayam Petelur":
        # data = df  # Gunakan data Ayam Petelur

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

    # tombol prediksi
    if st.button("Prediksi"):
        prediction, score = predict(x1, y1, x2, y2, features)
        score = score
        st.info("Prediksi Sukses...")

        if (prediction == 1):
            st.success(f'Skala Produksi {selected_option} di kota {kota} sangat tinggi')
        else:
            st.warning(f'Skala Produksi {selected_option} di kota {kota} sangat rendah')
        
            st.write("Model yang digunakan memiliki tingkat akurasi ", (score*100),"%")

# Menjalankan aplikasi Streamlit jika file ini dijalankan sebagai program utama
# if __name__ == "__main__":
#     app(df1, df2, x1, y1, x2, y2)