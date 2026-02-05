import streamlit as st
import joblib
import numpy as np
model = joblib.load("house_price_model.pkl")
model = joblib.load("house_price_model.pkl")
st.title("🏠 House Price Prediction App")
st.write("Enter the house details below to predict the price.")

area = st.number_input("Area (in sq ft)", min_value=500, max_value=20000, step=100)
bedrooms = st.slider("Bedrooms", 1, 10, 2)
bathrooms = st.slider("Bathrooms", 1, 10, 2)
stories = st.slider("Stories", 1, 5, 1)
parking = st.slider("Parking spaces", 0, 5, 0)

mainroad = st.selectbox("Main road access", ["Yes", "No"])
guestroom = st.selectbox("Guest room", ["Yes", "No"])
basement = st.selectbox("Basement", ["Yes", "No"])
hotwaterheating = st.selectbox("Hot water heating", ["Yes", "No"])
airconditioning = st.selectbox("Air conditioning", ["Yes", "No"])
prefarea = st.selectbox("Preferred area", ["Yes", "No"])
furnishingstatus = st.selectbox(
    "Furnishing status",
    ["Furnished", "Semi-furnished", "Unfurnished"]
)

mainroad_yes = 1 if mainroad == "Yes" else 0
guestroom_yes = 1 if guestroom == "Yes" else 0
basement_yes = 1 if basement == "Yes" else 0
hotwaterheating_yes = 1 if hotwaterheating == "Yes" else 0
airconditioning_yes = 1 if airconditioning == "Yes" else 0
prefarea_yes = 1 if prefarea == "Yes" else 0

furnishingstatus_semi = 1 if furnishingstatus == "Semi-furnished" else 0
furnishingstatus_unfurnished = 1 if furnishingstatus == "Unfurnished" else 0

input_data = np.array([[
    area,
    bedrooms,
    bathrooms,
    stories,
    parking,
    mainroad_yes,
    guestroom_yes,
    basement_yes,
    hotwaterheating_yes,
    airconditioning_yes,
    prefarea_yes,
    furnishingstatus_semi,
    furnishingstatus_unfurnished
]])
st.write("Model input:", input_data)

if st.button("Predict Price"):
    prediction = model.predict(input_data)[0]
    st.success(f"Estimated House Price: ₹{prediction:,.0f}")


st.markdown("---")
st.subheader("Prediction")
