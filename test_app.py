from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


valid_car = {
    "Make": "Honda",
    "Model": "Amaze 1.2 VX i-VTEC",
    "Year": 2017,
    "Kilometer": 87150,
    "Fuel_Type": "Petrol",
    "Transmission": "Manual",
    "Location": "Pune",
    "Color": "Grey",
    "Owner": "First",
    "Seller_Type": "Corporate",
    "Engine": "1198 cc",
    "Max_Power": "87 bhp @ 6000 rpm",
    "Max_Torque": "109 Nm @ 4500 rpm",
    "Drivetrain": "FWD",
    "Length": 3990,
    "Width": 1680,
    "Height": 1505,
    "Seating_Capacity": 5,
    "Fuel_Tank_Capacity": 35
}


# Test 1: Valid prediction
def test_valid_prediction():
    response = client.post("/predict", json=valid_car)

    assert response.status_code == 200
    assert "predicted_price" in response.json()


# Test 2: Missing required field
def test_missing_field():
    data = valid_car.copy()
    del data["Make"]

    response = client.post("/predict", json=data)

    assert response.status_code == 422


# Test 3: Invalid data type
def test_invalid_year():
    data = valid_car.copy()
    data["Year"] = "invalid"

    response = client.post("/predict", json=data)

    assert response.status_code == 422


# Test 4: Another valid prediction
def test_another_valid_prediction():
    data = valid_car.copy()
    data["Year"] = 2019
    data["Kilometer"] = 50000

    response = client.post("/predict", json=data)

    assert response.status_code == 200
    assert "predicted_price" in response.json()