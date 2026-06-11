import joblib
import pandas as pd

model = joblib.load("model/heart_model.pkl")

columns = [
    "age",
    "sex",
    "cp",
    "trestbps",
    "chol",
    "fbs",
    "restecg",
    "thalach",
    "exang",
    "oldpeak",
    "slope",
    "ca",
    "thal"
]

def predict_heart_disease(features):
    data = pd.DataFrame([features], columns=columns)
    prediction = model.predict(data)
    return prediction[0]