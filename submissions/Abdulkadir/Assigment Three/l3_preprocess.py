import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

CSV_PATH = 'car_l3_dataset.csv'
df = pd.read_csv(CSV_PATH)

# === INITIAL SNAPSHOT ===
# print("\n=== INITIAL HEAD ===")
# print(df.head())

# print("\n=== INITIAL INFO ===")
# print(df.info())

# print("\n=== Shape ===")
# print(df.shape)

# print("\n=== INITIAL MISSING VALUES ===")
# print(df.isnull().sum())

# print("\n=== LOCATION VALUE COUNTS ===")
# print("\n=Before Fixing categorical issues===")
# print(df["Location"].value_counts(dropna=False))

# 2) Clean target formatting
df["Price"] = df["Price"].replace(r"[\$,]", "", regex=True).astype(float)

# 3) Fix categorical issues BEFORE imputation
# print("\n=After Fixing categorical issues===")
df["Location"] = df["Location"].replace({"Subrb": "Suburb", "??": pd.NA})
# print(df.head())
# print(df["Location"].value_counts(dropna=False))


# 4) Impute missing values
df["Odometer_km"] = df["Odometer_km"].fillna(df["Odometer_km"].median())
df["Doors"]  = df["Doors"].fillna(df["Doors"].mode()[0])
df["Accidents"]  = df["Accidents"].fillna(df["Accidents"].mode()[0])
df["Location"]  = df["Location"].fillna(df["Location"].mode()[0])

# print(df["Location"].value_counts(dropna=False))

# 5) Remove duplicates
before = df.shape
df = df.drop_duplicates()
after = df.shape
print(f"Dropped duplicates: {before} → {after}")


# 6) IQR capping
def iqr_fun(series, k=1.5):
    q1, q3 = series.quantile([0.25, 0.75])
    iqr = q3 - q1
    lower = q1 - k * iqr
    upper = q3 + k * iqr
    return lower, upper

low_price, high_price = iqr_fun(df["Price"])
low_Odometer_km,  high_Odometer_km  = iqr_fun(df["Odometer_km"])

df["Price"]     = df["Price"].clip(lower=low_price, upper=high_price)
df["Odometer_km"] = df["Odometer_km"].clip(lower=low_Odometer_km,  upper=high_Odometer_km)

# print(df.head(30))

# 7) One-hot encode
df = pd.get_dummies(df, columns=["Location"], drop_first=False, dtype="int")
# print(df.head(10))


# === 8) FEATURE ENGINEERING (no leakage) ===

CURRENT_YEAR = 2026
# 1. CarAge 
df["CarAge"] = CURRENT_YEAR - df["Year"]
# Safely handle future years or missing values
df["CarAge"] = df["CarAge"].apply(lambda x: x if x >= 0 else 0)
# 2. Km_per_year
# Average kilometers per year; avoid division by zero
df["Km_per_year"] = df.apply(lambda row: row["Odometer_km"] / row["CarAge"] 
                             if row["CarAge"] > 0 else row["Odometer_km"], axis=1)

# 3. Is_Urban
# Assuming one-hot encoded Location columns contain urban info (e.g., Location_City, Location_Urban)
urban_cols = [col for col in df.columns if "City" in col or "Urban" in col]
if urban_cols:
    df["Is_Urban"] = df[urban_cols].max(axis=1).astype(int)  # 1 if any urban location, else 0
else:
    df["Is_Urban"] = 0

# 4. LogPrice as alternative target
df["LogPrice"] = np.log1p(df["Price"])
# --- Quick sanity check ---
# print("\n=== FEATURE ENGINEERING SAMPLE ===")
# print(df[["CarAge", "Km_per_year", "Is_Urban", "Price", "LogPrice"]].head(10))
# print(df.head())

# 9) Feature scaling (X only; keep targets & dummies unscaled)
# Targets not to scale
dont_scale = {"Price", "LogPrice"}
# All numeric columns
numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.to_list()
# Columns to exclude from scaling: all Location dummies + binary flags like Is_Urban
exclude = [c for c in df.columns if c.startswith("Location_")] + ["Is_Urban"]
# Columns to actually scale
num_features_to_scale = [c for c in numeric_cols if c not in dont_scale and c not in exclude]
# Apply StandardScaler
scaler = StandardScaler()
df[num_features_to_scale] = scaler.fit_transform(df[num_features_to_scale])
# --- Quick check ---
# print("\n=== SCALED FEATURES SAMPLE ===")
# print(df[num_features_to_scale].head())



# === FINAL SNAPSHOT ===
print("\n=== FINAL HEAD ===")
print(df.head())

print("\n=== FINAL INFO ===")
print(df.info())

print("\n=== FINAL MISSING VALUES ===")
print(df.isnull().sum())

# 10) Save
OUT_PATH = "car_l3_clean_ready.csv"
df.to_csv(OUT_PATH, index=False)