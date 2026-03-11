import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("heart_model.pkl","rb"))

st.title("Heart Disease Prediction")

age = st.number_input("Age")
sex = st.selectbox("Sex (0=Female, 1=Male)",[0,1])
cp = st.number_input("Chest Pain Type")
trestbps = st.number_input("Resting Blood Pressure")
chol = st.number_input("Cholesterol")
fbs = st.number_input("Fasting Blood Sugar")
restecg = st.number_input("Rest ECG")
thalach = st.number_input("Max Heart Rate")
exang = st.number_input("Exercise Induced Angina")
oldpeak = st.number_input("Oldpeak")
slope = st.number_input("Slope")
ca = st.number_input("Number of Major Vessels")
thal = st.number_input("Thal")

if st.button("Predict"):

    features = np.array([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])

    prediction = model.predict(features)

    if prediction[0]==1:
        st.error("Heart Disease Detected")
    else:
        st.success("No Heart Disease")
