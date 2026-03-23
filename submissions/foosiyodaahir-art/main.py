from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
import numpy as np
import joblib
import os

app = FastAPI()

templates = Jinja2Templates(directory="web_interface")

rf_model = joblib.load("models/Models/random_forest_model.pkl")
lr_model = joblib.load("models/Models/logistic_model.pkl")
scaler = joblib.load("models/Models/cv_scaler.pkl")

@app.get("/")
async def read_root(request: Request):
      
    return templates.TemplateResponse("index.html", {"request": request, "results": {}})

@app.post("/predict")
async def predict(
    request: Request,
    age: int = Form(...),
    gender: int = Form(...),
    height: float = Form(...),
    weight: float = Form(...),
    ap_hi: int = Form(...),
    ap_lo: int = Form(...),
    cholesterol: int = Form(...),
    gluc: int = Form(...),
    smoke: int = Form(...),
    active: int = Form(...)
):
    try:
        age_days = age * 365
        input_data = np.array([[
            age_days, gender, height, weight, ap_hi, ap_lo, cholesterol, gluc, smoke, active
        ]])

        input_data_scaled = scaler.transform(input_data)
        
        rf_prob = float(rf_model.predict_proba(input_data_scaled)[0][1])
        lr_prob = float(lr_model.predict_proba(input_data_scaled)[0][1])

        if ap_hi < 130 and weight < 85:
            rf_is_risk = False
            lr_is_risk = False
        else:
            rf_is_risk = rf_prob >= 0.35
            lr_is_risk = lr_prob >= 0.6 

        if ap_hi >= 140 or rf_is_risk or lr_is_risk:
            final_recommendation = "High Risk Detected: Please consult a doctor immediately."
            final_class = "risk-box"
        else:
            final_recommendation = "Your results are normal. Keep maintaining a healthy lifestyle!"
            final_class = "healthy-box"

        
        results_data = {
            "rf": "High Risk" if rf_is_risk else "Healthy",
            "lr": "High Risk" if lr_is_risk else "Healthy",
            "rf_class": "risk-card" if rf_is_risk else "healthy-card",
            "lr_class": "risk-card" if lr_is_risk else "healthy-card",
            "rf_acc": "73.4%",
            "lr_acc": "70.5%",
            "recommendation": final_recommendation,
            "rec_class": final_class
        }

        return templates.TemplateResponse("index.html", {"request": request, "results": results_data})

    except Exception as e:
        
        return templates.TemplateResponse("index.html", {"request": request, "results": {"error": str(e)}})