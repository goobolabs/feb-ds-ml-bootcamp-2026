from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import joblib
import pandas as pd

app = FastAPI()

# Allow frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = joblib.load("models/best_model.pkl")

@app.get("/")
def home():
    return {"message": "Used Car Price Prediction API"}

    return {"predicted_price": float(prediction[0])}

@app.post("/predict")
def predict(data: dict):

    try:
        df = pd.DataFrame([data])
        prediction = model.predict(df)

        return {"predicted_price": float(prediction[0])}

    except Exception as e:
        print("Prediction error:", e)
        return {"predicted_price": 0}