import streamlit as st
import streamlit.components.v1 as components
import time
import random

# Define conversion factors
conversion_factors = {
    'length': {
        'meters': 1,
        'kilometers': 0.001,
        'miles': 0.000621371,
        'feet': 3.28084,
        'inches': 39.3701,
        'centimeters': 100,
        'millimeters': 1000,
        'yards': 1.09361,
        'nautical miles': 0.000539957
    },
    'weight': {
        'grams': 1,
        'kilograms': 0.001,
        'pounds': 0.00220462,
        'ounces': 0.035274,
        'stones': 0.000157473,
        'tons': 0.000001
    },
    'temperature': {
        'celsius': lambda x: x,
        'fahrenheit': lambda x: (x * 9/5) + 32,
        'kelvin': lambda x: x + 273.15
    },
    'time': {
        'seconds': 1,
        'minutes': 1/60,
        'hours': 1/3600,
        'days': 1/86400,
        'weeks': 1/604800,
        'months': 1/2628000,
        'years': 1/31536000
    },
    'speed': {
        'mps': 1,  # meters per second
        'kph': 3.6,  # kilometers per hour
        'mph': 2.23694,  # miles per hour
        'fps': 3.28084,  # feet per second
        'knots': 1.94384
    },
    'area': {
        'square meters': 1,
        'square kilometers': 0.000001,
        'square miles': 3.861e-7,
        'square feet': 10.7639,
        'acres': 0.000247105,
        'hectares': 0.0001
    },
    'volume': {
        'liters': 1,
        'milliliters': 1000,
        'cubic meters': 0.001,
        'gallons': 0.264172,
        'pints': 2.11338
    },
    'energy': {
        'joules': 1,
        'kilojoules': 0.001,
        'calories': 0.239006,
        'kilocalories': 0.000239006,
        'watt-hours': 0.000277778
    },
    'pressure': {
        'pascals': 1,
        'kilopascals': 0.001,
        'bars': 0.00001,
        'atmospheres': 0.00000986923,
        'PSI': 0.000145038
    },
    'digital storage': {
        'bits': 1,
        'bytes': 0.125,
        'kilobytes': 0.000125,
        'megabytes': 0.000000125,
        'gigabytes': 0.000000000125,
        'terabytes': 0.000000000000125
    }
}

# Function to convert units and display formula
def convert_units(value, from_unit, to_unit, conversion_type):
    if conversion_type == 'temperature':
        if from_unit == 'celsius':
            result = conversion_factors['temperature'][to_unit](value)
            formula = f"{value}°C → {result:.2f}°{to_unit.capitalize()}"
        elif from_unit == 'fahrenheit':
            celsius = (value - 32) * 5/9
            result = conversion_factors['temperature'][to_unit](celsius)
            formula = f"({value}°F - 32) × 5/9 → {result:.2f}°{to_unit.capitalize()}"
        elif from_unit == 'kelvin':
            celsius = value - 273.15
            result = conversion_factors['temperature'][to_unit](celsius)
            formula = f"{value}K - 273.15 → {result:.2f}°{to_unit.capitalize()}"
    else:
        result = value * conversion_factors[conversion_type][to_unit] / conversion_factors[conversion_type][from_unit]
        formula = f"{value} {from_unit} × {conversion_factors[conversion_type][to_unit] / conversion_factors[conversion_type][from_unit]} = {result:.5f} {to_unit}"
    return result, formula

# Apply CSS styling with animation
st.markdown("""
    <style>
        @keyframes fadeIn {
            from {opacity: 0;}
            to {opacity: 1;}
        }
        .stApp {
            animation: fadeIn 2s ease-in;
            max-width: 700px;
            margin: auto;
            border-radius: 10px;
            padding: 20px;
            background: white;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        }
        .stButton>button {
            background-color: #007bff;
            color: white;
            border-radius: 5px;
            padding: 10px 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Streamlit UI
st.title("✨ Advanced Unit Converter ✨")

# Select conversion type
conversion_type = st.selectbox("Select conversion type", list(conversion_factors.keys()))

# Input value
value = st.number_input("Enter value to convert", min_value=0.0)

# Select units based on conversion type
from_unit = st.selectbox("From unit", list(conversion_factors[conversion_type].keys()))
to_unit = st.selectbox("To unit", list(conversion_factors[conversion_type].keys()))

# Convert and display result with formula and animation
if st.button("Convert"):
    with st.spinner("Converting..."):
        time.sleep(random.uniform(0.5, 1.5))  # Simulate loading effect
    result, formula = convert_units(value, from_unit, to_unit, conversion_type)
    st.success(f"✅ {value} {from_unit} is equal to {result:.5f} {to_unit}")
    st.info(f"Formula: {formula}")