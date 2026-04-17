import joblib
import json
from utils import prepare_features_from_raw

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "Cancer Prediction API",
        "status": "running"
    })


# Load models
MODELS = {
    "lr": joblib.load("models/logistic_model.joblib"),
    "rf": joblib.load("models/random_forest_model.joblib"),
    "xgb": joblib.load("models/xgb_model.joblib"),
}

# Load label mapping
label_map = json.load(open("models/label_mapping.json"))
reverse_map = {int(k): v for k, v in label_map.items()}


@app.route("/predict", methods=["POST"])
def predict():

    # ============================
    # STEP 1 — Choose model
    # ============================
    choice = (request.args.get("model") or "").lower()

    if choice not in MODELS:
        return jsonify({
            "error": "Invalid model. Use model=lr, rf, or xgb"
        }), 400

    model = MODELS[choice]

    # ============================
    # STEP 2 — Get input JSON
    # ============================
    data = request.get_json(silent=True) or {}

    required = [
        "Age", "Gender", "Smoking", "Alcohol_Use", "Obesity",
        "Family_History", "Diet_Red_Meat", "Diet_Salted_Processed",
        "Fruit_Veg_Intake", "Physical_Activity", "Air_Pollution",
        "Occupational_Hazards", "BRCA_Mutation",
        "H_Pylori_Infection", "Calcium_Intake",
        "BMI", "Physical_Activity_Level"
    ]

    missing = [k for k in required if k not in data]

    if missing:
        return jsonify({
            "error": f"Missing fields: {missing}"
        }), 400

    # ============================
    # STEP 3 — Prepare input
    # ============================
    try:
        X_new = prepare_features_from_raw(data)
    except Exception as e:
        return jsonify({
            "error": f"Feature processing failed: {str(e)}"
        }), 500

    # ============================
    # STEP 4 — Predict + Probabilities
    # ============================
    try:
        # Prediction
        pred_class = int(model.predict(X_new)[0])
        pred_label = reverse_map[pred_class]

        # Probabilities
        probs = model.predict_proba(X_new)[0]

        # Convert to readable format
        prob_dict = {
            reverse_map[i]: float(probs[i])
            for i in range(len(probs))
        }

        # Confidence of predicted class
        confidence = float(probs[pred_class])

    except Exception as e:
        return jsonify({
            "error": f"Prediction failed: {str(e)}"
        }), 500

    # ============================
    # STEP 5 — Return result
    # ============================
    return jsonify({
        "model": choice,
        "prediction_class": pred_class,
        "prediction_label": pred_label,
        "confidence": round(confidence, 4),
        "probabilities": prob_dict,
        "input": data
    })


app.run(host="0.0.0.0", port=8000, debug=False)