# 🚗 Used Car Price Appraiser

A machine learning-based web application that predicts the estimated price of a used car based on its specifications.

The project uses a **FastAPI backend**, **Streamlit frontend**, and a trained **machine learning model**. The backend is containerized using **Docker**.

## Features

- Used car price prediction
- FastAPI REST API
- Interactive Streamlit interface
- Categorical feature encoding using Target Encoding
- Machine learning model for price prediction
- Dockerized backend
- Automated testing using Pytest
- Four API test cases
- GitHub Actions CI/CD

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Category Encoders
- Joblib
- FastAPI
- Uvicorn
- Streamlit
- Requests
- Pytest
- Docker
- GitHub Actions

## Project Structure

```text
Used-Car-Price-Appraiser/
│
├── app.py
├── streamlit_app.py
├── test_app.py
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .gitignore
├── README.md
│
├── used_car_price_model1.pkl
├── target_encoder1.pkl
└── feature_columns1.pkl
```

## How the Project Works

```text
User
  │
  ▼
Streamlit Frontend
  │
  │ POST /predict
  ▼
FastAPI Backend
  │
  ▼
Data Preprocessing
  │
  ▼
Target Encoding
  │
  ▼
Trained ML Model
  │
  ▼
Predicted Car Price
  │
  ▼
Streamlit
```

## Running the Project Locally

### 1. Create and activate virtual environment

For Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\activate
```

### 2. Install dependencies

```powershell
pip install -r requirements.txt
```

### 3. Start the FastAPI backend

```powershell
uvicorn app:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Swagger API documentation:

```text
http://127.0.0.1:8000/docs
```

### 4. Start Streamlit

Open another terminal, activate the virtual environment, and run:

```powershell
streamlit run streamlit_app.py
```

The Streamlit application will be available at:

```text
http://localhost:8501
```

## API Endpoint

### POST `/predict`

The API accepts the following car information:

- Make
- Model
- Year
- Kilometer
- Fuel Type
- Transmission
- Location
- Color
- Owner
- Seller Type
- Engine
- Maximum Power
- Maximum Torque
- Drivetrain
- Length
- Width
- Height
- Seating Capacity
- Fuel Tank Capacity

Example response:

```json
{
  "predicted_price": 540039.92
}
```

## Docker

### Build the Docker image

```powershell
docker build -t used-car-price-api .
```

### Run the Docker container

```powershell
docker run -p 8000:8000 used-car-price-api
```

The FastAPI backend can then be accessed at:

```text
http://127.0.0.1:8000/docs
```

## Testing

The project contains four automated test cases using Pytest:

1. Valid car prediction
2. Missing required field
3. Invalid year data type
4. Another valid car prediction

Run the tests using:

```powershell
pytest -v
```

All four tests currently pass successfully.

## CI/CD

GitHub Actions is used to automate project validation.

The workflow will:

1. Install project dependencies
2. Run the automated tests
3. Build the Docker image
4. Report whether the workflow succeeds or fails


## Future Scope

- Improved user interface
- Additional car datasets
- Model performance improvements
- More comprehensive automated tests
- Continuous deployment