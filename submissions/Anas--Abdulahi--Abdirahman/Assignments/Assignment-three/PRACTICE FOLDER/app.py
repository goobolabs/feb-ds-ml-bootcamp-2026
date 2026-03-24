import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

CSV_PATH = 'car_l3_dataset.csv'
df = pd.read_csv(CSV_PATH)

## 1) Load & Inspect
print("\n=== INITIAL HEAD ===")
print(df.head(10))

print("\n=== INITIAL SHAPE ===")
print(df.shape)

print("\n=== INITIAL INFO ===")
print(df.info())

print("\n=== INITIAL MISSING VALUES ===")
print(df.isnull().sum())

print("\n=== INITIAL Location ===")
print(df["Location"].value_counts())

## 2) Clean Target Formatting
print("\n=== PRICE ===")
df["Price"] = df["Price"].astype(str)
df["Price"] = df["Price"].str.replace(r"[\$,]", "", regex=True)
df["Price"] = df["Price"].str.replace("USD", "", regex=False)
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")
print(df.head(10))

## 3) Fix Category Errors before Imputation
print("\n=== Location CAPITALIZE ===")
df["Location"] = df["Location"].str.lower().str.strip().str.capitalize()
print(df.head(10))
print("\n=== Location FIXING ===")
df["Location"] = df["Location"].replace({ "Subrb": "Suburb" , "??": pd.NA})
print(df["Location"].value_counts(dropna=False))

## 4) Impute Missing Values
print("\n=== MISSING VALUES ===")
print(df.isnull().sum())

df["Price"] = df["Price"].fillna(df["Price"].median())
df["Odometer_km"] = df["Odometer_km"].fillna(df["Odometer_km"].median())
df["Doors"] = df["Doors"].fillna(df["Doors"].mode()[0])
df["Accidents"] = df["Accidents"].fillna(df["Accidents"].mode()[0])
df["Location"] = df["Location"].fillna(df["Location"].mode()[0])
print(df.head(20))

print(df.isna().sum())

## 5)Remove Duplicates
before = df.shape
df = df.drop_duplicates()
after = df.shape
print("Removed", before[0] - after[0], "duplicates")
print(df.shape)

## 6) Outliers (IQR capping)
def iqr_fun(series, k=1.5):
    q1, q3 = series.quantile([0.25, 0.75])
    iqr = q3 - q1
    lower = q1 -k * iqr
    upper = q3 + k * iqr
    return lower, upper
low_price , high_price = iqr_fun(df["Price"])
print("Price min after capping:", df["Price"].min(), "Price max after capping:", df["Price"].max())
low_odo, high_odo = iqr_fun(df["Odometer_km"])
print("Odometer min after capping:", df["Odometer_km"].min(), "Odometer max after capping:", df["Odometer_km"].max())

## 7) One-Hot Encode Categorical(s)
df = pd.get_dummies(df, columns=["Location"], drop_first=False , dtype=int)
print(df.head(10))

## 8) Feature Engineering (no leakage)
CURRENT_YEAR = 2026
df["CarAge"] = CURRENT_YEAR - df["Year"]
df["Km_per_year"] = df["Odometer_km"] / df["CarAge"].replace(0, 1)
df["Is_City"] = df["Location_City"].astype(int) 
df["LogPrice"] = np.log1p(df["Price"])
print(df.head(10))

# print(df[["CarAge", "Km_per_year", "Is_City", "LogPrice"]].head(10))

## 9) Feature Scaling (X only)
dont_scale = {"Price" , "LogPrice"}
numeric_cols = df.select_dtypes(include=["float64", "Int64"]).columns.to_list()
exclude = [c for c in df.columns if c.startswith("Location")] + ["Is_City"]
num_features_to_scale = [c for c in numeric_cols if c not in dont_scale and c not in exclude]

scaler = StandardScaler()
df[num_features_to_scale] = scaler.fit_transform(df[num_features_to_scale])
print(df.head(10))

## Final Checks & Save
print("\n=== FINAL HEAD ===")
print(df.head(10))

print("\n=== FINAL SHAPE ===")
print(df.shape)

print("\n=== FINAL INFO ===")
print(df.info())

print("\n=== FINAL MISSING VALUES ===")
print(df.isnull().sum())

OUT_PATH = 'car_clean_l3_dataset.csv'
df.to_csv(OUT_PATH)
print("Saved to", OUT_PATH)













