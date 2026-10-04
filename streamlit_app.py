import streamlit as st
import requests

st.set_page_config(
    page_title="Used Car Price Appraiser",
    page_icon="🚗",
    layout="wide"
)

st.markdown(
    """
    <div style="text-align: center;">
        <h1>🚗 Used Car Price Appraiser</h1>
        <p>Enter the details of the used car to estimate its price.</p>
    </div>
    """,
    unsafe_allow_html=True
)

API_URL = "http://127.0.0.1:8000/predict"

st.subheader("Car Details")

col1, col2, col3 = st.columns(3)

with col1:
    make = st.text_input("Make", value="Honda")
    model = st.text_input("Model", value="Amaze 1.2 VX i-VTEC")
    year = st.number_input("Year", min_value=1990, max_value=2026, value=2017)
    kilometer = st.number_input("Kilometer", min_value=0, value=87150)

    fuel_type = st.selectbox(
        "Fuel Type",
        ["Petrol", "Diesel", "CNG", "Electric", "LPG"]
    )

    transmission = st.selectbox(
        "Transmission",
        ["Manual", "Automatic"]
    )

with col2:
    location = st.text_input("Location", value="Pune")
    color = st.text_input("Color", value="Grey")

    owner = st.selectbox(
        "Owner",
        ["First", "Second", "Third", "Fourth & Above"]
    )

    seller_type = st.selectbox(
        "Seller Type",
        ["Individual", "Dealer", "Corporate"]
    )

    engine = st.text_input("Engine", value="1198 cc")
    max_power = st.text_input(
        "Max Power",
        value="87 bhp @ 6000 rpm"
    )

    max_torque = st.text_input(
        "Max Torque",
        value="109 Nm @ 4500 rpm"
    )

with col3:
    drivetrain = st.selectbox(
        "Drivetrain",
        ["FWD", "RWD", "AWD", "4WD"]
    )

    length = st.number_input("Length", min_value=0, value=3990)
    width = st.number_input("Width", min_value=0, value=1680)
    height = st.number_input("Height", min_value=0, value=1505)
    seating_capacity = st.number_input(
        "Seating Capacity",
        min_value=1,
        max_value=20,
        value=5
    )
    fuel_tank_capacity = st.number_input(
        "Fuel Tank Capacity",
        min_value=0,
        value=35
    )

st.divider()

if st.button("🚗 Predict Used Car Price", type="primary"):

    car_data = {
        "Make": make,
        "Model": model,
        "Year": int(year),
        "Kilometer": int(kilometer),
        "Fuel_Type": fuel_type,
        "Transmission": transmission,
        "Location": location,
        "Color": color,
        "Owner": owner,
        "Seller_Type": seller_type,
        "Engine": engine,
        "Max_Power": max_power,
        "Max_Torque": max_torque,
        "Drivetrain": drivetrain,
        "Length": int(length),
        "Width": int(width),
        "Height": int(height),
        "Seating_Capacity": int(seating_capacity),
        "Fuel_Tank_Capacity": int(fuel_tank_capacity)
    }

    try:
        response = requests.post(API_URL, json=car_data)

        if response.status_code == 200:
            result = response.json()

            predicted_price = result["predicted_price"]

            st.success("Prediction generated successfully!")

            st.metric(
                "Estimated Used Car Price",
                f"₹{predicted_price:,.2f}"
            )

        elif response.status_code == 422:
            st.error("Invalid input. Please check the entered details.")

        else:
            st.error(
                f"API Error: {response.status_code}"
            )

    except requests.exceptions.ConnectionError:
        st.error(
            "Cannot connect to the FastAPI server. "
            "Please make sure the Docker container is running."
        )

    except Exception as e:
        st.error(f"Something went wrong: {e}")