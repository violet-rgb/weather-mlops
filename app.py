from src.ingest_data import *

import streamlit as st
import pandas as pd
import numpy as np

st.title("Weather Data Visualization")

# Load data
data = pd.read_csv("data/raw/weather_data.csv")

# Convert date column
data["date"] = pd.to_datetime(data["date"])

# Line chart
st.line_chart(data.set_index("date")["temperature_2m"])

# Metrics
st.subheader("Forecasted Weather Metrics")

col1, col2 = st.columns(2)

col1.metric(
    "Temperature (°C)",
    f"{data['temperature_2m'].iloc[-1]:.2f}"
)

col2.metric(
    "Humidity (%)",
    f"{data['relative_humidity_2m'].iloc[-1]:.2f}"
)