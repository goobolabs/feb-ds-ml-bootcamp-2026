import json
import joblib
import pandas as pd

# Load artifacts
TRAIN_COLUMNS = json.load(open("models/train_columns.json"))
SCALER = joblib.load("models/scaler.pkl")


def prepare_features_from_raw(record: dict) -> pd.DataFrame:
    """
    Convert user input into model-ready format
    """

    # ============================
    # STEP 1 — Extract user input
    # ============================
    Age = float(record.get("Age", 0))
    Gender = float(record.get("Gender", 0))
    Smoking = float(record.get("Smoking", 0))
    Alcohol_Use = float(record.get("Alcohol_Use", 0))
    Obesity = float(record.get("Obesity", 0))
    Family_History = float(record.get("Family_History", 0))
    Diet_Red_Meat = float(record.get("Diet_Red_Meat", 0))
    Diet_Salted_Processed = float(record.get("Diet_Salted_Processed", 0))
    Fruit_Veg_Intake = float(record.get("Fruit_Veg_Intake", 0))
    Physical_Activity = float(record.get("Physical_Activity", 0))
    Air_Pollution = float(record.get("Air_Pollution", 0))
    Occupational_Hazards = float(record.get("Occupational_Hazards", 0))
    BRCA_Mutation = float(record.get("BRCA_Mutation", 0))
    H_Pylori_Infection = float(record.get("H_Pylori_Infection", 0))
    Calcium_Intake = float(record.get("Calcium_Intake", 0))
    BMI = float(record.get("BMI", 0))
    Physical_Activity_Level = float(record.get("Physical_Activity_Level", 0))

        # ============================
    # STEP 2 — Create empty row
    # ============================
    row = {col: 0.0 for col in TRAIN_COLUMNS}


        # ============================
    # STEP 3 — Fill row values
    # ============================
    for name, val in [
        ("Age", Age),
        ("Gender", Gender),
        ("Smoking", Smoking),
        ("Alcohol_Use", Alcohol_Use),
        ("Obesity", Obesity),
        ("Family_History", Family_History),
        ("Diet_Red_Meat", Diet_Red_Meat),
        ("Diet_Salted_Processed", Diet_Salted_Processed),
        ("Fruit_Veg_Intake", Fruit_Veg_Intake),
        ("Physical_Activity", Physical_Activity),
        ("Air_Pollution", Air_Pollution),
        ("Occupational_Hazards", Occupational_Hazards),
        ("BRCA_Mutation", BRCA_Mutation),
        ("H_Pylori_Infection", H_Pylori_Infection),
        ("Calcium_Intake", Calcium_Intake),
        ("BMI", BMI),
        ("Physical_Activity_Level", Physical_Activity_Level),
    ]:
        if name in row:
            row[name] = float(val)



    # ============================
    # STEP 4 — Convert to DataFrame
    # ============================
    df_one = pd.DataFrame([row], columns=TRAIN_COLUMNS)

    # ============================
    # STEP 5 — Apply scaling
    # ============================
    if hasattr(SCALER, "feature_names_in_"):
        cols_to_scale = list(SCALER.feature_names_in_)
        df_one[cols_to_scale] = SCALER.transform(df_one[cols_to_scale])

    return df_one