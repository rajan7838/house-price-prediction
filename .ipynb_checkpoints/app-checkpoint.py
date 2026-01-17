import streamlit as st
import pandas as pd
import joblib

# Load Model
model = joblib.load("best_model.pkl")

st.title("House Price Predictor")

# Input - Sidebar
with st.sidebar:
    area = st.number_input("Sq Ft", value=5000)
    beds = st.slider("Bedrooms", 1, 10, 3)
    baths = st.slider("Bathrooms", 1, 10, 2)
    stories = st.slider("Stories", 1, 5, 1)
    parking = st.slider("Parking", 0, 5, 1)
    
    # Binary options (Checks = 1, Unchecked = 0)
    ac = st.checkbox("Air Conditioning")
    road = st.checkbox("Main Road")
    furnish = st.radio("Furnishing", ["Furnished", "Semi-Furnished", "Unfurnished"])

# Create Dataframe (Map values directly)
data = {
    "area": area, "bedrooms": beds, "bathrooms": baths, "stories": stories,
    "mainroad": int(road), "guestroom": 0, "basement": 0, "hotwaterheating": 0,
    "airconditioning": int(ac), "parking": parking, "prefarea": 0,
    "furnishingstatus_semi-furnished": 1 if furnish == "Semi-Furnished" else 0,
    "furnishingstatus_unfurnished": 1 if furnish == "Unfurnished" else 0
}

# Predict and Display
if st.button("Calculate Price"):
    pred = model.predict(pd.DataFrame([data]))[0]
    st.success(f"### Predicted Price: ₹{pred:,.2f}")
