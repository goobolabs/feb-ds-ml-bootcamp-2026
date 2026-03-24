import pandas as pd
import numpy as np
import os

# ===============================
# SAFE PATH (working directory problem fix)
# ===============================

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_PATH = os.path.join(BASE_DIR, "car_l3_dataset.csv")
OUTPUT_PATH = os.path.join(BASE_DIR, "car_l3_dataset_step10.csv")

print("Reading from:", CSV_PATH)

df = pd.read_csv(CSV_PATH)

# ===============================
# CLEAN PRICE
# ===============================

df["Price"] = df["Price"].replace(r'[\$,]', '', regex=True)
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")

# ===============================
# FIX LOCATION
# ===============================

df["Location"] = df["Location"].str.lower()
df["Location"] = df["Location"].replace({"subrb": "suburb"})
df["Location"] = df["Location"].replace("??", np.nan)

# ===============================
# HANDLE MISSING VALUES
# ===============================

df["Odometer_km"] = df["Odometer_km"].fillna(df["Odometer_km"].median())
df["Doors"] = df["Doors"].fillna(df["Doors"].mode()[0])
df["Accidents"] = df["Accidents"].fillna(df["Accidents"].mode()[0])
df["Location"] = df["Location"].fillna(df["Location"].mode()[0])
df["Price"] = df["Price"].fillna(df["Price"].median())

# ===============================
# REMOVE DUPLICATES
# ===============================

df.drop_duplicates(inplace=True)

# ===============================
# ONE HOT ENCODE
# ===============================

df = pd.get_dummies(df, columns=["Location"], prefix="Location")
location_cols = [c for c in df.columns if c.startswith("Location_")]
df[location_cols] = df[location_cols].astype(int)

# ===============================
# FEATURE ENGINEERING
# ===============================

df["CarAge"] = 2026 - df["Year"]
df["Km_per_year"] = df["Odometer_km"] / df["CarAge"]
df["Km_per_year"] = df["Km_per_year"].replace([np.inf, -np.inf], np.nan)
df["Km_per_year"] = df["Km_per_year"].fillna(df["Km_per_year"].median())

df["Is_Urban"] = df.get("Location_city", 0) + df.get("Location_suburb", 0)
df["LogPrice"] = np.log(df["Price"])

# ===============================
# FINAL CHECK
# ===============================

assert df.isnull().sum().sum() == 0, "There are still missing values!"

# ===============================
# SAVE
# ===============================

df.to_csv(OUTPUT_PATH, index=False)

print("Final cleaned dataset saved to:", OUTPUT_PATH)
print("Everything worked successfully 🎉")
