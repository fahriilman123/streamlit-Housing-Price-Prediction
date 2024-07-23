import pickle
import streamlit as st
import numpy as np

# Load the trained model
model = pickle.load(open('housing_prediction.sav', 'rb'))

option_mapping = {
    "Iya": 1,
    "Tidak" : 0
}

furnishing_mapping = {
    "Lengkap": 2,
    "Semi Lengkap": 1,
    "Tidak ada": 0
}


st.title('House Price Prediction')
st.markdown("""
Selamat datang di aplikasi prediksi harga rumah. Masukkan informasi rumah yang anda inginkan untuk di prediksi harga rumah tersebut berdasarkan model regresi linier.

**Fitur:**
- Luas Rumah
- Jumlah Kamar Tidur
- Jumlah Kamar Mandi
- dan banyak lagi!
""")


# Input fields
area = st.number_input('Luas Rumah (dalam meter persegi)', min_value=0)
bedrooms = st.number_input('Jumlah Kamar Tidur', min_value=0)
bathrooms = st.number_input('Jumlah Kamar Mandi', min_value=0)
stories = st.number_input('Jumlah Lantai', min_value=0)
mainroad = st.selectbox("Apakah Terhubung ke Jalan Utama", list(option_mapping.keys()))
guestroom = st.selectbox("Apakah Terdapat Kamar Tamu", list(option_mapping.keys()))
basement = st.selectbox("Apakah Ada Basement", list(option_mapping.keys()))
hotwaterheating = st.selectbox("Apakah Ada Pemanas Air", list(option_mapping.keys()))
airconditioning = st.selectbox("Apakah Ada AC", list(option_mapping.keys()))
parking = st.number_input("Jumlah Tempat Parkir", min_value=0)
prefarea = st.selectbox("Apakah Terletak di Area Pilihan", list(option_mapping.keys()))
furnishingstatus = st.selectbox("Status Furnitur", list(furnishing_mapping.keys()))

mainroad = option_mapping[mainroad]
guestroom = option_mapping[guestroom]
basement = option_mapping[basement]
hotwaterheating = option_mapping[hotwaterheating]
airconditioning = option_mapping[airconditioning]
prefarea = option_mapping[prefarea]
furnishing = furnishing_mapping[furnishingstatus]
# Convert categorical input to numerical format using pre-fitted LabelEncoders
input_data = np.array([
    area,
    bedrooms,
    bathrooms,
    stories,
    mainroad,
    guestroom,
    basement,
    hotwaterheating,
    airconditioning,
    parking,
    prefarea,
    furnishing
]).reshape(1, -1)

# Predict the house price
if st.button("Prediksi Harga"):
    prediction = model.predict(input_data)
    st.write(f'Prediksi harga rumah: {prediction[0]:,.2f}')
