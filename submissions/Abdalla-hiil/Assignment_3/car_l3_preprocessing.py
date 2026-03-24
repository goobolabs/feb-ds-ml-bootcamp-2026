import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# === STEP 1: LOAD & INSPECT ===
CSV_PATH = r"C:\Users\MR HIIL\Desktop\DS and Machine learning\ds-ml-bootcamp\dataset\car_l3_dataset.csv"
df = pd.read_csv(CSV_PATH)

print("\n=== INITIAL HEAD ===")
print(df.head(10))

print("\n=== INITIAL MISSING VALUES ===")
print(df.isnull().sum())

# === STEP 2: CLEAN TARGET FORMATTING ===
# Removing $ and commas to make Price a number
df["Price"] = df["Price"].replace(r"[ \$, ]", "", regex=True).astype(float)

# === STEP 3: FIX CATEGORY ERRORS BEFORE IMPUTATION ===
# Normalizing spelling and marking unknowns as holes
df["Location"] = df["Location"].replace({"Subrb": "Suburb", "??": pd.NA})

# === STEP 4: IMPUTE MISSING VALUES ===
# Filling holes with Median for numbers and Mode for categories
df["Odometer_km"] = df["Odometer_km"].fillna(df["Odometer_km"].median())
df["Doors"] = df["Doors"].fillna(df["Doors"].mode()[0])
df["Location"] = df["Location"].fillna(df["Location"].mode()[0])

# === STEP 5: REMOVE DUPLICATES ===
# Is it repeating? We keep only one copy
before = df.shape
df = df.drop_duplicates()
after = df.shape
print(f"\nDropped duplicates: {before} → {after}")

# === STEP 6: IQR CAPPING (OUTLIERS) ===
def iqr_fun(series, k = 1.5):
    q1, q3 = series.quantile([0.25, 0.75])
    iqr = q3 - q1
    lower = q1 - k * iqr
    upper = q3 + k * iqr
    return lower, upper

low_price, high_price = iqr_fun(df["Price"])
low_Odometer_km, high_Odometer_km = iqr_fun(df["Odometer_km"])

df["Price"] = df["Price"].clip(lower = low_price, upper = high_price)
df["Odometer_km"] = df["Odometer_km"].clip(lower = low_Odometer_km, upper = high_Odometer_km)

# === STEP 7: ONE-HOT ENCODE ===
# Turning city/suburb names into 0 and 1 columns
df = pd.get_dummies(df, columns=["Location"], drop_first=False, dtype="int")

# === STEP 8: FEATURE ENGINEERING ===
CURRENT_YEAR = 2026

# Feature 1: CarAge
df["CarAge"] = CURRENT_YEAR - df["Year"]

# Feature 2: Accidents_per_year (using +1 to avoid division by zero)
df["Accidents_per_year"] = df["Accidents"] / (df["CarAge"] + 1)

# Feature 3: Km_per_year
df["Km_per_year"] = df["Odometer_km"] / (df["CarAge"] + 1)

# Feature 4: Is_City
df["Is_City"] = df["Location_City"].astype(int)

# Alternative Target: LogPrice
df["LogPrice"] = np.log1p(df["Price"])

# === STEP 9: FEATURE SCALING (X ONLY) ===
dont_scale = {"Price", "LogPrice"}

# Finding all number columns
numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.to_list()

# Protecting 0/1 dummies and the target
exclude = [c for c in df.columns if c.startswith("Location_")] + ["Is_City"]
num_features_to_scale = [c for c in numeric_cols if c not in dont_scale and c not in exclude]

scaler = StandardScaler()
df[num_features_to_scale] = scaler.fit_transform(df[num_features_to_scale])

# === STEP 10: FINAL SNAPSHOT & SAVE ===
print("\n=== FINAL HEAD ===")
print(df.head(10))

print("\n=== FINAL MISSING VALUES ===")
print(df.isnull().sum())

# Saving the cleaned car data
OUT_PATH = "car_l3_clean_ready.csv"
df.to_csv(OUT_PATH, index=False)
print(f"\nSuccess! Cleaned data saved to {OUT_PATH}")




