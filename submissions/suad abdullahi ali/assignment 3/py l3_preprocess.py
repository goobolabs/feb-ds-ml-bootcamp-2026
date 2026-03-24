# File: l3_preprocess.py
# Lesson 3 — Data Preprocessing
# Dataset: car_l3_dataset.csv

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# ---------------------------
# STEP 1: Load & Inspect
# ---------------------------
print("STEP 1: Load & Inspect")
df = pd.read_csv("car_l3_dataset.csv")
print(df.head(10))
print("Shape:", df.shape)
print(df.info())
print("\nMissing values:\n", df.isna().sum())
print("\nLocation counts:\n", df["Location"].value_counts(dropna=False))

# ---------------------------
# STEP 2: Clean Price
# ---------------------------
print("\nSTEP 2: Clean Price")
df["Price"] = df["Price"].astype(str).str.replace(
    "$", "", regex=False).str.replace(",", "", regex=False)
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")
print("Price dtype:", df["Price"].dtype)
print("Price skewness:", df["Price"].skew())

# ---------------------------
# STEP 3: Fix Location
# ---------------------------
print("\nSTEP 3: Fix Location")
df["Location"] = df["Location"].astype(str).str.strip()
df["Location"] = df["Location"].replace({
    "Subrb": "Suburb",
    "??": np.nan,
    "": np.nan
})
print(df["Location"].value_counts(dropna=False))

# ---------------------------
# STEP 4: Impute Missing Values
# ---------------------------
print("\nSTEP 4: Imputation")
df["Odometer_km"] = pd.to_numeric(df["Odometer_km"], errors="coerce")
df["Odometer_km"] = df["Odometer_km"].fillna(df["Odometer_km"].median())
df["Doors"] = df["Doors"].fillna(df["Doors"].mode()[0])
df["Accidents"] = df["Accidents"].fillna(df["Accidents"].mode()[0])
df["Location"] = df["Location"].fillna(df["Location"].mode()[0])
print("Missing after imputation:\n", df.isna().sum())

# ---------------------------
# STEP 5: Remove Duplicates
# ---------------------------
print("\nSTEP 5: Remove Duplicates")
before = df.shape[0]
df = df.drop_duplicates()
after = df.shape[0]
print(f"Rows before: {before}, after: {after}, removed: {before-after}")

# ---------------------------
# STEP 6: Outlier Capping (IQR)
# ---------------------------
print("\nSTEP 6: Outlier Capping")


def iqr_clip(series):
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    return series.clip(lower, upper)


df["Price"] = iqr_clip(df["Price"])
df["Odometer_km"] = iqr_clip(df["Odometer_km"])
print(df[["Price", "Odometer_km"]].describe())

# ---------------------------
# STEP 7: One-Hot Encoding
# ---------------------------
print("\nSTEP 7: One-Hot Encoding")
df = pd.get_dummies(df, columns=["Location"], drop_first=False)
print([c for c in df.columns if c.startswith("Location_")])

# ---------------------------
# STEP 8: Feature Engineering
# ---------------------------
print("\nSTEP 8: Feature Engineering")
CURRENT_YEAR = 2025
df["CarAge"] = CURRENT_YEAR - df["Year"]
df["CarAge"] = df["CarAge"].apply(lambda x: max(x, 0))
df["Km_per_year"] = df["Odometer_km"] / df["CarAge"].replace(0, 1)
urban_cols = [col for col in df.columns if col in [
    "Location_City", "Location_Suburb"]]
df["Is_Urban"] = df[urban_cols].sum(axis=1).clip(0, 1)
df["LogPrice"] = np.log1p(df["Price"])

# ---------------------------
# STEP 9: Scaling
# ---------------------------
print("\nSTEP 9: Scaling")
scale_cols = ["Odometer_km", "CarAge", "Km_per_year"]
scaler = StandardScaler()
df[scale_cols] = scaler.fit_transform(df[scale_cols])
print(df[scale_cols].head())

# ---------------------------
# STEP 10: Final Checks & Save
# ---------------------------
print("\nSTEP 10: Final Checks")
print(df.info())
print("\nFinal missing values:\n", df.isna().sum())

# Assertions
assert df["Price"].dtype != "object"
assert "LogPrice" in df.columns
assert df.isna().sum().sum() == 0
assert any(col.startswith("Location_") for col in df.columns)

# Save cleaned data
df.to_csv("car_l3_clean_ready.csv", index=False)
print("\n✅ Saved file: car_l3_clean_ready.csv")
