import streamlit as st

# Conversion function
def convert_units(value, from_unit, to_unit, category):
    conversion_factors = {
        "Length": {
            "Meters": 1,
            "Kilometers": 0.001,
            "Miles": 0.000621371,
            "Feet": 3.28084,
        },
        "Weight": {
            "Kilograms": 1,
            "Grams": 1000,
            "Pounds": 2.20462,
            "Ounces": 35.274,
        },
        "Temperature": {
            "Celsius": lambda x: x,
            "Fahrenheit": lambda x: x * 9/5 + 32,
            "Kelvin": lambda x: x + 273.15,
        },
        "Time": {
            "Seconds": 1,
            "Minutes": 1 / 60,
            "Hours": 1 / 3600,
            "Days": 1 / 86400,
        },
        "Area": {
            "Square Meters": 1,
            "Square Kilometers": 0.000001,
            "Square Miles": 3.861e-7,
            "Square Feet": 10.7639,
        },
    }

    # Handle temperature conversions using functions
    if category == "Temperature":
        return conversion_factors[category][to_unit](value)
    else:
        return value * conversion_factors[category][to_unit] / conversion_factors[category][from_unit]

# Streamlit UI setup
st.set_page_config(page_title="Unit Converter", layout="centered")
st.title("🔄 Stylish Unit Converter")

# Add Python logo image to the sidebar
python_image_url = "https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg"  # URL of Python logo
st.sidebar.image(python_image_url, use_container_width=True)  # Display image with the new parameter


# Navigation bar
nav = st.sidebar.radio("Navigate", ["Home", "About"])

# Home section: Unit converter interface
if nav == "Home":
    # Category selection with description tooltip
    category = st.selectbox(
        "Select a category:",
        ["Length", "Weight", "Temperature", "Time", "Area"],
        help="Choose the category of unit you want to convert"
    )

    # Units selection based on category
    conversion_factors = {
        "Length": {
            "Meters": 1,
            "Kilometers": 0.001,
            "Miles": 0.000621371,
            "Feet": 3.28084,
        },
        "Weight": {
            "Kilograms": 1,
            "Grams": 1000,
            "Pounds": 2.20462,
            "Ounces": 35.274,
        },
        "Temperature": {
            "Celsius": lambda x: x,
            "Fahrenheit": lambda x: x * 9/5 + 32,
            "Kelvin": lambda x: x + 273.15,
        },
        "Time": {
            "Seconds": 1,
            "Minutes": 1 / 60,
            "Hours": 1 / 3600,
            "Days": 1 / 86400,
        },
        "Area": {
            "Square Meters": 1,
            "Square Kilometers": 0.000001,
            "Square Miles": 3.861e-7,
            "Square Feet": 10.7639,
        },
    }

    # Unit selection based on category
    units = list(conversion_factors[category].keys())
    from_unit = st.selectbox("From Unit:", units)
    to_unit = st.selectbox("To Unit:", units)

    # User input with formatted value display
    value = st.number_input(
        "Enter Value:",
        min_value=0.0,
        format="%.4f",
        help="Input the value you want to convert"
    )

    # Conversion logic and result display
    if st.button("Convert", use_container_width=True):
        if value < 0:
            st.error("Please enter a value greater than or equal to 0.")
        else:
            result = convert_units(value, from_unit, to_unit, category)
            st.success(f"✅ Conversion Result: {value:.4f} {from_unit} = {result:.4f} {to_unit}")

# About section: Information about the app
elif nav == "About":
    st.header("About This App")
    st.markdown("""
        This is a **Stylish Unit Converter** built using **Streamlit**.
        
        It supports multiple unit conversion categories including:
        - Length (e.g., meters, kilometers, miles, feet)
        - Weight (e.g., kilograms, grams, pounds, ounces)
        - Temperature (e.g., Celsius, Fahrenheit, Kelvin)
        - Time (e.g., seconds, minutes, hours, days)
        - Area (e.g., square meters, square kilometers, square miles, square feet)
        
        You can select a category, choose the units, input the value, and get the converted result instantly.
        
        **Built with ❤️ by [Amna Khan]**.
    """)

# Additional styling for the Streamlit app
st.markdown("""
    <style>
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        padding: 10px 20px;
        border-radius: 8px;
        box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
    }
    .stButton > button:hover {
        background-color: #45a049;
    }
    .stSelectbox, .stNumberInput {
        background-color: #f0f0f0;
        border-radius: 8px;
        padding: 10px;
        box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
    }
    .stSidebar {
        background-color: #f0f0f0;
        padding: 10px;
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)
