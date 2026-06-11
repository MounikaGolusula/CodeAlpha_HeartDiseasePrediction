import streamlit as st
from src.predict import predict_heart_disease

st.set_page_config(
    page_title="Heart Disease Prediction",
    page_icon="❤️"
)

st.title("❤️ Heart Disease Prediction")

st.write("Enter patient details below")

age = st.number_input("Age", 1, 120, 50)
sex_option = st.selectbox(
    "Sex",
    ["Female", "Male"]
)

sex = 0 if sex_option == "Female" else 1
cp = st.number_input("Chest Pain Type (cp)", 0, 3, 0)
trestbps = st.number_input("Resting Blood Pressure", 50, 250, 120)
chol = st.number_input("Cholesterol", 100, 600, 200)
fbs_option = st.selectbox(
    "Fasting Blood Sugar",
    ["Normal", "High"]
)

fbs = 0 if fbs_option == "Normal" else 1
restecg = st.number_input("Resting ECG", 0, 2, 0)
thalach = st.number_input("Maximum Heart Rate", 50, 250, 150)
exang_option = st.selectbox(
    "Exercise Induced Angina",
    ["No", "Yes"]
)

exang = 0 if exang_option == "No" else 1
oldpeak = st.number_input("Oldpeak", 0.0, 10.0, 1.0)
slope = st.number_input("Slope", 0, 2, 1)
ca = st.number_input("Number of Major Vessels (ca)", 0, 4, 0)
thal = st.number_input("Thal", 0, 3, 2)

if st.button("Predict"):

    features = [
        age,
        sex,
        cp,
        trestbps,
        chol,
        fbs,
        restecg,
        thalach,
        exang,
        oldpeak,
        slope,
        ca,
        thal
    ]

    prediction = predict_heart_disease(features)

    st.write("Prediction Value:", prediction)

    if prediction == 1:
        st.error("High Risk of Heart Disease")
    else:
        st.success("Low Risk of Heart Disease")