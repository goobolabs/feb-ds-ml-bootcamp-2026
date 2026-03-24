# serve_utils.py
import json
import joblib
import pandas as pd

CURRENT_YEAR = 2025

# Load once at import
TRAIN_COLUMNS = json.load(open("models/train_columns.json"))
SCALER = joblib.load("models/house_scaler.pkl")  # fitted in Lesson-3


def prepare_features_from_raw(record: dict) -> pd.DataFrame:
    """
    Convert raw input (Size_sqft, Bedrooms, Bathrooms, Location, YearBuilt)
    into the engineered, one-hot, scaled feature row that matches training.
    Returns a 1-row DataFrame with columns == TRAIN_COLUMNS.
    """
    size = float(record.get("Size_sqft", 0.0))
    beds = float(record.get("Bedrooms", 0.0))
    baths = float(record.get("Bathrooms", 0.0))
    year = int(record.get("YearBuilt", CURRENT_YEAR))
    loc = str(record.get("Location", "City"))

    # Recreate engineered features exactly like Lesson-3
    house_age = CURRENT_YEAR - year
    rooms_per_1000 = ((beds + baths) / (size / 1000.0)) if size else 0.0
    size_per_bedroom = (size / beds) if beds else 0.0
    is_city = 1 if loc.lower() == "city" else 0

    # Build a full row with zeros for all training columns
    row = {col: 0.0 for col in TRAIN_COLUMNS}

    for name, val in [
        ("Size_sqft", size),
        ("Bedrooms", beds),
        ("Bathrooms", baths),
        ("YearBuilt", year),
        ("HouseAge", house_age),
        ("Rooms_per_1000sqft", rooms_per_1000),
        ("Size_per_Bedroom", size_per_bedroom),
        ("Is_City", is_city),
    ]:
        if name in row:
            row[name] = float(val)

    # One-hot for Location_*
    loc_col = f"Location_{loc}"
    if loc_col in row:
        row[loc_col] = 1.0

    # 1-row DataFrame with correct column order
    df_one = pd.DataFrame([row], columns=TRAIN_COLUMNS)

    # Scale only the columns the scaler was fitted on
    if hasattr(SCALER, "feature_names_in_"):
        cols_to_scale = list(SCALER.feature_names_in_)
        df_one[cols_to_scale] = SCALER.transform(df_one[cols_to_scale])

    return df_one
