
import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load the trained model
@st.cache_resource
def load_model():
    return joblib.load("house_price_prediction_model_v1_0.joblib")

model = load_model()

# Streamlit UI for Price Prediction
st.title("House Price Prediction App")
st.write("This tool predicts the price of a house based on the property details.")

st.subheader("Enter the house details:")

# Construct a dictionary for Country > State/Region > City relationships

location_data = {
    "Australia": {
        "New South Wales": ["Sydney", "Wollongong"],
        "Victoria": ["Melbourne"],
        "Queensland": [],
    },
    "Brazil": {
        "Bahia": [],
        "Sao Paulo": ["Sao Paulo City"],
        "Rio de Janeiro": [],
    },
    "China": {
        "Guangdong": ["Fengtai"],
        "Shanghai": ["Shanghai"],
        "Beijing": ["Beijing", "Haidian"],
    },
    "South Korea": {
        "Incheon": [],
        "Seoul": ["Seoul"],
        "Busan": [],
    },
    "USA": {
        "Texas": ["Dallas", "Houston"],
        "California": ["Los Angeles", "San Diego", "San Francisco"],
        "New York": ["New York City", "Buffalo"],
    },
    "Germany": {
        "Berlin": ["Berlin"],
        "Bavaria": ["Munich", "Augsburg"],
        "North Rhine-Westphalia": ["Cologne"],
    },
    "India": {
        "Delhi": ["Delhi"],
        "Karnataka": ["Bangalore"],
        "Maharashtra": ["Mumbai", "Pune", "Nagpur"],
        "Uttar Pradesh": [],
    },
    "South Africa": {
        "Gauteng": ["Johannesburg", "Pretoria", "Soweto"],
        "KwaZulu-Natal": [],
        "Western Cape": [],
    },
    "Japan": {
        "Tokyo": ["Tokyo", "Shinjuku", "Chiyoda", "Shibuya"],
        "Osaka": ["Osaka"],
        "Kyoto": ["Kyoto"],
    },
    "Canada": {
        "Ontario": ["Toronto", "Ottawa"],
        "Quebec": ["Montreal", "Quebec City"],
        "British Columbia": ["Vancouver"],
    },
    "Mexico": {
        "Jalisco": ["Guadalajara"],
        "Mexico City": ["Mexico City", "Tlalpan", "Coyoacan", "Iztapalapa"],
        "Nuevo Leon": [],
    },
    "France": {
        "Ile-de-France": ["Paris", "Versailles"],
        "Provence": [],
        "Normandy": [],
    },
    "UK": {
        "England": ["London", "Manchester", "Birmingham", "Newcastle"],
        "Wales": [],
        "Scotland": ["Glasgow"],
    },
    "Italy": {
        "Lombardy": ["Milan", "Brescia", "Bergamo"],
        "Tuscany": [],
        "Sicily": [],
    },
    "Spain": {
        "Madrid": ["Madrid"],
        "Catalonia": [],
        "Andalusia": [],
    }
}

# Collect user input
country = st.selectbox("Select Country", list(location_data.keys()))
state = st.selectbox("Select State", list(location_data[country].keys()))
city = st.selectbox("Select City", location_data[country][state])
bedrooms = st.number_input("Bedrooms", min_value=1, max_value=10, step=1, value=1)
squaremeter = st.number_input("Square Meter (Sqm)", min_value=0, max_value=500, step=10, value=1)

# Convert user input into a DataFrame
input_data = pd.DataFrame([{
    'Country': country,
    'State/Region': state,
    'City': city,
    'Bedrooms': bedrooms,
    'Square Meter (Sqm)': squaremeter,
    'Population Density (people per sq km)': 10000
}])

# Predict button
if st.button("Predict"):
    prediction = model.predict(input_data)
    formatted_price = f"{prediction[0]:,.2f}"
    st.write(f"The predicted price of the house is {formatted_price}.")
