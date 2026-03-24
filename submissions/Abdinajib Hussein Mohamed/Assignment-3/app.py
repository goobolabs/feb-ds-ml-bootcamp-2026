import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

#STEP 1 — LOAD & INSPECT:
CSV_PATH = "car_l3_dataset.csv"
df = pd.read_csv(CSV_PATH)
# print("\nSTEP 1 — INSPECTION")
#print(df.head(10))
# print("\nShape:", df.shape)
# print("\nInfo:")
# print(df.info())
# print("\nMissing values:\n", df.isnull().sum())
# print("\nLocation counts:\n", df["Location"].value_counts(dropna=False))

#STEP 2 — CLEAN PRICE:
df["Price"] = (
    df["Price"]
    .astype(str)
    .str.replace(r"[^\d.]", "", regex=True)
)

df["Price"] = pd.to_numeric(df["Price"], errors="coerce")

print("\nSTEP 2 — Price dtype:", df["Price"].dtype)
print("Price skewness:", df["Price"].skew())
df["Price"] = df["Price"].replace(r"[\$,]", "", regex=True).astype(float)
print(df.head(10))
# STEP 3 — FIXING CATEGORY ERRORS:
df["Location"] = (
    df["Location"]
    .astype(str)
    .str.strip()
    .str.title()
)

location_map = {
    "Subrb": "Suburb",
    "Rurall": "Rural",
    "??": np.nan,
    "Unknown": np.nan,
    "Nan": np.nan
}

df["Location"] = df["Location"].replace(location_map)

print("\nSTEP 3 — Location after cleaning:")
print(df["Location"].value_counts(dropna=False))
df["Location"] = df["Location"].replace({"Subrb": "Suburb", "??": pd.NA})
# print(df.head(50))
# 4) # STEP 4 — IMPUTATION Missing Values:


df["Odometer_km"] = df["Odometer_km"].fillna(df["Odometer_km"].median())
df["Doors"] = df["Doors"].fillna(df["Doors"].mode()[0])
df["Accidents"] = df["Accidents"].fillna(df["Accidents"].mode()[0])
df["Location"] = df["Location"].fillna(df["Location"].mode()[0])

print("\nSTEP 4 — Missing after imputation:\n", df.isnull().sum())

# STEP 5 — REMOVE DUPLICATES
before = df.shape[0]
df = df.drop_duplicates()
after = df.shape[0]

print("\nSTEP 5 — Rows removed:", before - after)
print("\nShape:", df.shape)
# STEP 6 — OUTLIER CAPPING (IQR):

def iqr_clip(dataframe, column):
    Q1 = dataframe[column].quantile(0.25)
    Q3 = dataframe[column].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    dataframe[column] = dataframe[column].clip(lower, upper)
    return lower, upper

price_bounds = iqr_clip(df, "Price")
odo_bounds = iqr_clip(df, "Odometer_km")

print("\nSTEP 6 — Price bounds:", price_bounds)
print("STEP 6 — Odometer bounds:", odo_bounds)
print(df.head(50))


# STEP 7 — ONE HOT ENCODING
df = pd.get_dummies(df, columns=["Location"], drop_first=False)

location_cols = [c for c in df.columns if c.startswith("Location_")]
print("\nSTEP 7 — New dummy columns:", location_cols)
df[location_cols] = df[location_cols].astype(int)
print(df.head(10))

# STEP 8 — FEATURE ENGINEERING

CURRENT_YEAR = 2026

df["CarAge"] = CURRENT_YEAR - df["Year"]
df["CarAge"] = df["CarAge"].clip(lower=0)

df["Km_per_year"] = df["Odometer_km"] / df["CarAge"].replace(0, 1)

df["Is_Urban"] = (
    df.filter(like="Location_City").sum(axis=1) +
    df.filter(like="Location_Suburb").sum(axis=1)
).gt(0).astype(int)

df["LogPrice"] = np.log1p(df["Price"])
print(df.head(10))
# STEP 9 — SCALING (X ONLY)
continuous_cols = [
    "Odometer_km",
    "CarAge",
    "Km_per_year",
    "Doors",
    "Accidents"
]

scaler = StandardScaler()
df[continuous_cols] = scaler.fit_transform(df[continuous_cols])

print("\nSTEP 9 — Scaled sample:")
print(df[continuous_cols].head())
print(df.head(10))
# STEP 10 — FINAL CHECKS & SAVE
assert df["Price"].dtype == float
assert "LogPrice" in df.columns
assert df.isnull().sum().sum() == 0
assert len(location_cols) > 0

print("\nFinal missing values:\n", df.isnull().sum())
print("\nFinal describe:\n", df.describe())

#  Save cleaned dataset
OUTPUT_PATH = "car_l3_clean_ready.csv"
df.to_csv(OUTPUT_PATH, index=False)

print("\nSaved cleaned file as:", OUTPUT_PATH)