import joblib
import pandas as pd

model = joblib.load("models/best_model.pkl")

sample = pd.DataFrame([{
    "brand": "Toyota",
    "year": 2019,
    "engine_size": 2.0,
    "mileage": 60000,
    "fuel_type": "Petrol",
    "transmission": "Automatic",
    "owner_count": 1
}])

prediction = model.predict(sample)

print("Predicted Price:", prediction[0])