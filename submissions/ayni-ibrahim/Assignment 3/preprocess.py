import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

CSV_PATH = "car_data.csv"

df = pd.read_csv("car_data.csv")

# =========================
# 1. Load & Inspect
# =========================

print(df.head(10))
print(df.shape)
print(df.info())
print(df.isna().sum())
print(df["Location"].value_counts(dropna=False))

# =========================
# 2. Clean Price column
# =========================
df["Price"] = (
    df["Price"]
    .astype(str)
    .str.replace("$", "", regex=False)
    .str.replace(",", "", regex=False)
)

df["Price"] = pd.to_numeric(df["Price"], errors="coerce")
print("Price dtype:", df["Price"].dtype)
print("Price skew:", df["Price"].skew())

# =========================
# 3. Fix Location categories
# =========================
df["Location"] = df["Location"].str.strip().str.title()

df["Location"] = df["Location"].replace({
    "Subrb": "Suburb",
    "??": np.nan,
    "Nan": np.nan
})

print(df["Location"].value_counts(dropna=False))

# =========================
# 4. Impute Missing Values
# =========================
df["Odometer_km"] = df["Odometer_km"].fillna(df["Odometer_km"].median())
df["Doors"] = df["Doors"].fillna(df["Doors"].mode()[0])
df["Accidents"] = df["Accidents"].fillna(df["Accidents"].mode()[0])
df["Location"] = df["Location"].fillna(df["Location"].mode()[0])

print(df.isna().sum())

# =========================
# 5. Remove Duplicates
# =========================
before = df.shape[0]
df = df.drop_duplicates()
after = df.shape[0]
print("Duplicates removed:", before - after)

# =========================
# 6. IQR Capping
# =========================
def iqr_cap(col):
    q1 = col.quantile(0.25)
    q3 = col.quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    return col.clip(lower, upper)

df["Price"] = iqr_cap(df["Price"])
df["Odometer_km"] = iqr_cap(df["Odometer_km"])

# =========================
# 7. One-Hot Encode Location
# =========================
df = pd.get_dummies(df, columns=["Location"], drop_first=False)

# =========================
# 8. Feature Engineering
# =========================
CURRENT_YEAR = 2025

df["CarAge"] = CURRENT_YEAR - df["Year"]
df["Km_per_year"] = df["Odometer_km"] / df["CarAge"].replace(0, 1)
df["Is_Urban"] = ((df.get("Location_City", 0) == 1) | (df.get("Location_Suburb", 0) == 1)).astype(int)

df["LogPrice"] = np.log(df["Price"] + 1)

# =========================
# 9. Feature Scaling (X only)
# =========================
scale_cols = ["Odometer_km", "CarAge", "Km_per_year"]

scaler = StandardScaler()
df[scale_cols] = scaler.fit_transform(df[scale_cols])

print(df[scale_cols].head())

# =========================
# 10. Final Checks & Save
# =========================
assert df["Price"].dtype != object
assert df["LogPrice"].isna().sum() == 0
assert df.isna().sum().sum() == 0
assert any(col.startswith("Location_") for col in df.columns)

print(df.info())
print(df.describe())

df.to_csv("car_clean_l3_dataset.csv", index=False)
print("Saved: car_clean_l3_dataset.csv")





