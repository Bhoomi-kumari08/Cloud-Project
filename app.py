from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import numpy as np
import joblib
import category_encoders as ce

app = FastAPI(title="Used Car Price Prediction API")


# Load saved model and preprocessing files
model = joblib.load("used_car_price_model1.pkl")
target_encoder = joblib.load("target_encoder1.pkl")
feature_columns = joblib.load("feature_columns1.pkl")


class CarInput(BaseModel):
    Make: str
    Model: str
    Year: int
    Kilometer: float
    Fuel_Type: str
    Transmission: str
    Location: str
    Color: str
    Owner: str
    Seller_Type: str
    Engine: str
    Max_Power: str
    Max_Torque: str
    Drivetrain: str
    Length: float
    Width: float
    Height: float
    Seating_Capacity: float
    Fuel_Tank_Capacity: float


@app.get("/")
def home():
    return {
        "message": "Used Car Price Prediction API is running!"
    }


@app.post("/predict")
def predict_price(car: CarInput):

    # Convert input into DataFrame
    data = pd.DataFrame([{
        "Make": car.Make,
        "Model": car.Model,
        "Year": car.Year,
        "Kilometer": car.Kilometer,
        "Fuel Type": car.Fuel_Type,
        "Transmission": car.Transmission,
        "Location": car.Location,
        "Color": car.Color,
        "Owner": car.Owner,
        "Seller Type": car.Seller_Type,
        "Engine": car.Engine,
        "Max Power": car.Max_Power,
        "Max Torque": car.Max_Torque,
        "Drivetrain": car.Drivetrain,
        "Length": car.Length,
        "Width": car.Width,
        "Height": car.Height,
        "Seating Capacity": car.Seating_Capacity,
        "Fuel Tank Capacity": car.Fuel_Tank_Capacity
    }])

    # Same preprocessing used during training

    # Engine
    data["Engine"] = data["Engine"].str.replace(
        " cc", "", regex=False
    )
    data["Engine"] = pd.to_numeric(data["Engine"])

    # Max Power
    data["Max Power"] = data["Max Power"].str.extract(
        r"(\d+\.?\d*)"
    )[0]
    data["Max Power"] = pd.to_numeric(data["Max Power"])

    # Max Torque
    data["Max Torque"] = data["Max Torque"].str.extract(
        r"(\d+\.?\d*)"
    )[0]
    data["Max Torque"] = pd.to_numeric(data["Max Torque"])

    # Car Age
    current_year = 2026
    data["Car Age"] = current_year - data["Year"]

    # Remove Year
    data.drop("Year", axis=1, inplace=True)

    # Target Encoding
    data = target_encoder.transform(data)

    # One-Hot Encoding
    data = pd.get_dummies(
        data,
        columns=[
            "Make",
            "Fuel Type",
            "Transmission",
            "Color",
            "Owner",
            "Seller Type",
            "Drivetrain"
        ],
        drop_first=True
    )

    # Convert boolean columns to integers
    bool_cols = data.select_dtypes(include="bool").columns
    data[bool_cols] = data[bool_cols].astype(int)

    # Make sure columns are exactly the same as during training
    data = data.reindex(
        columns=feature_columns,
        fill_value=0
    )

    # Predict
    prediction = model.predict(data)[0]

    return {
        "predicted_price": round(float(prediction), 2)
    }