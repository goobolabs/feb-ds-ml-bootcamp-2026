import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import os

# ===============================
# STEP 1 — Load Dataset Safely
# ===============================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

CSV_INPUT = os.path.join(BASE_DIR, "car_l3_dataset.csv")
CSV_OUTPUT = os.path.join(BASE_DIR, "car_l3_dataset_step10.csv")

df = pd.read_csv(CSV_INPUT)

print("Loaded from:", CSV_INPUT)
print(df.head())
print(df.shape)
print(df.isnull().sum())

# ===============================
# STEP 2 — Clean Price
# ===============================

df["Price"] = df["Price"].replace(r'[\$,]', '', regex=True)
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")

# ===============================
# STEP 3 — Fix Location Issues
# ===============================

df["Location"] = df["Location"].str.lower()
df["Location"] = df["Location"].replace({"subrb": "suburb"})
df["Location"] = df["Location"].replace("??", np.nan)

# ===============================
# STEP 4 — Handle Missing Values
# ===============================

df["Odometer_km"] = df["Odometer_km"].fillna(df["Odometer_km"].median())
df["Doors"] = df["Doors"].fillna(df["Doors"].mode()[0])
df["Accidents"] = df["Accidents"].fillna(df["Accidents"].mode()[0])
df["Location"] = df["Location"].fillna(df["Location"].mode()[0])
df["Price"] = df["Price"].fillna(df["Price"].median())

# ===============================
# STEP 5 — Remove Duplicates
# ===============================

print("Before duplicates:", df.shape)
df.drop_duplicates(inplace=True)
print("After duplicates:", df.shape)

# ===============================
# STEP 6 — Handle Outliers (IQR)
# ===============================

def clip_outliers(column):
    Q1 = column.quantile(0.25)
    Q3 = column.quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    return column.clip(lower, upper)

df["Price"] = clip_outliers(df["Price"])
df["Odometer_km"] = clip_outliers(df["Odometer_km"])

# ===============================
# STEP 7 — One-Hot Encode Location
# ===============================

df = pd.get_dummies(df, columns=["Location"], prefix="Location")
location_cols = [col for col in df.columns if col.startswith("Location_")]
df[location_cols] = df[location_cols].astype(int)

# ===============================
# STEP 8 — Feature Engineering
# ===============================

df["CarAge"] = 2026 - df["Year"]
df["Km_per_year"] = df["Odometer_km"] / df["CarAge"]
df["Km_per_year"] = df["Km_per_year"].replace([np.inf, -np.inf], np.nan)
df["Km_per_year"] = df["Km_per_year"].fillna(df["Km_per_year"].median())

df["Is_Urban"] = df.get("Location_city", 0) + df.get("Location_suburb", 0)

df["LogPrice"] = np.log(df["Price"])

# ===============================
# STEP 9 — Scaling (X only)
# ===============================

scaler = StandardScaler()
scaled_cols = ["Odometer_km", "Km_per_year", "CarAge"]

df[scaled_cols] = scaler.fit_transform(df[scaled_cols])

# ===============================
# STEP 10 — Minimal Sanity Checks
# ===============================

assert df["Price"].dtype in [float, np.float64], "Price must be float"
assert "LogPrice" in df.columns and np.issubdtype(df["LogPrice"].dtype, np.number), "LogPrice missing or not numeric"
assert df.isnull().sum().sum() == 0, "There are still missing values"
assert any(col.startswith("Location_") for col in df.columns), "Location dummy columns missing"

for col in scaled_cols:
    mean_val = df[col].mean()
    std_val = df[col].std(ddof=0)
    assert abs(mean_val) < 1e-6, f"{col} mean not approx 0"
    assert abs(std_val - 1) < 1e-6, f"{col} std not approx 1"

print("All sanity checks passed ✅")

# ===============================
# STEP 11 — Save Final Dataset
# ===============================

df.to_csv(CSV_OUTPUT, index=False)

print("Saved cleaned dataset to:", CSV_OUTPUT)
print("Assignment completed successfully 🎉")
