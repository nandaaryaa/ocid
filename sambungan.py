import pickle
import streamlit as st
import numpy as np

# Membaca model
customer_model = pickle.load(open('pelanggan_model.sav','rb'))

# Judul web
st.title('Prediksi Status Pelanggan')

# Input data dengan contoh angka valid untuk pengujian
CreditScore = st.text_input('Skor Kredit')
Gender = st.selectbox('Jenis Kelamin', [0, 1])  # Misalnya, 0 untuk pria, 1 untuk wanita
Age = st.text_input('Umur')
Tenure = st.text_input('Tenure')
Balance = st.text_input('Saldo')
NumOfProducts = st.text_input('Jumlah Produk')
HasCrCard = st.selectbox('Memiliki Kartu Kredit', [0, 1])  # 0 untuk tidak, 1 untuk ya
IsActiveMember = st.selectbox('Anggota Aktif', [0, 1])  # 0 untuk tidak, 1 untuk ya
EstimatedSalary = st.text_input('Gaji Perkiraan')

Prediksi_Status_Pelanggan = ''

# Membuat tombol untuk prediksi
if st.button('Prediksi'):
    try:
        # Konversi input menjadi numerik
        inputs = np.array([[float(CreditScore), float(Gender), float(Age), float(Tenure), float(Balance), float(NumOfProducts), 
                            float(HasCrCard), float(IsActiveMember), float(EstimatedSalary)]])
        # Lakukan prediksi
        status_prediksi = customer_model.predict(inputs)
        
        if status_prediksi[0] == 0:
            status_prediksi_str = 'Pelanggan Tidak Keluar dari Bank'
            st.success(status_prediksi_str)
        elif status_prediksi[0] == 1:
            status_prediksi_str = 'Pelanggan Keluar dari Bank'
            st.success(status_prediksi_str)
        else:
            st.error("Prediksi tidak valid.")
    except ValueError:
        st.error("Pastikan semua input diisi dengan angka yang valid.")
    except Exception as e:
        st.error(f"Terjadi kesalahan: {e}")
