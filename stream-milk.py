import pickle
import numpy as np
import streamlit as st

model = pickle.load(open('milknew1.sav', 'rb'))

st.title('Klasifikasi Kualitas Susu (Milk Classification)')

col1, col2 = st.columns(2)

with col1:
    pH = st.number_input('pH Alus Susu')

with col1:
    Temprature = st.number_input('Suhu Susu') 

with col1:
    Taste = st.number_input('Rasa Susu')

with col1:
    Odor = st.number_input('Bau Susu')

with col2:
    Fat = st.number_input('Tingkat Lemak Susu')

with col2:
    Turbidity = st.number_input('Kekeruhan susu')

with col2:
    Colour = st.number_input('Warna Susu')

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
