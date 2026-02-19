import streamlit as st
import numpy as np
import joblib

model_dict = joblib.load("house_price_model.pkl")
model = model_dict["model"]
scaler = model_dict["scaler"]

st.title("🏠 House Price Prediction - India")

st.sidebar.header("Input Features")

bedrooms = st.sidebar.slider("Bedrooms", 1, 10, 2)
postal_code = st.sidebar.slider("Postal Code", 100000, 999999, 400001)
built_year = st.sidebar.slider("Built Year", 1950, 2025, 2010)

house_age = 2026 - built_year

input_data = np.array([[bedrooms, postal_code, built_year, house_age]])

input_scaled = scaler.transform(input_data)

if st.button("Predict Price"):
    prediction = model.predict(input_scaled)
    st.success(f"Predicted House Price: ₹ {int(prediction[0]):,}")
