import pickle
import numpy as np
import streamlit as st

model = pickle.load(open('milknew1.sav', 'rb'))

st.title('Klasifikasi Kualitas Susu (Milk Classification)')

col1, col2 = st.columns(2)

with col1:
    pH = st.text_input('pH Alus Susu')

with col1:
    Temprature = st.text_input('Suhu Susu') 

with col1:
    Taste = st.text_input('Rasa Susu')

with col1:
    Odor = st.text_input('Bau Susu')

with col2:
    Fat = st.text_input('Tingkat Lemak Susu')

with col2:
    Turbidity = st.text_input('Kekeruhan susu')

with col2:
    Colour = st.text_input('Warna Susu')

milknew_diagnosis = ''

if st.button('Klasifikasi Kualitas Susu'):
    milknew_prediction = model.predict([[pH, Temprature,  Taste, Odor, Fat, Turbidity, Colour]])

    if(milknew_prediction[0]==0):
        milknew_diagnosis = 'Kualitas Susu Rendah'
    elif(milknew_prediction[0]==1):
        milknew_diagnosis = 'Kualitas Susu Sedang'
    else:
        milknew_diagnosis = 'Kualitas Susu Tinggi'

st.success(milknew_diagnosis)  
