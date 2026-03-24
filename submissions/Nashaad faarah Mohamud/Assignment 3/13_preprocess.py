import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler


CSV_FILE_PATH = "car_13_dataset.csv"
df = pd.read_csv(CSV_FILE_PATH)

print("=== STEP 1: Load & Inspect ===")
print("First 10 rows:")
print(df.head(10))
print("Dataset shape:", df.shape)
print("Missing values per column:")
print(df.isnull().sum())
print("Location counts:")
print(df['Location'].value_counts(dropna=False))
print("\n")


df["Price"] = df["Price"].replace(r"[\$,]", '', regex=True).astype(float)
print("=== STEP 2: Price Formatting ===")
print("Price dtype:", df["Price"].dtype)
print("Price stats:\n", df["Price"].describe())
print("\n")

df["Location"] = df["Location"].replace({"Subrb": "Suburb", "??": np.NaN})
print("=== STEP 3: Fixed Location Categories ===")
print(df['Location'].value_counts(dropna=False))
print("\n")


df["Odometer_km"] = df["Odometer_km"].fillna(df["Odometer_km"].median())
df["Doors"] = df["Doors"].fillna(df["Doors"].mode()[0])
df["Location"] = df["Location"].fillna(df["Location"].mode()[0])
print("=== STEP 4: Missing Values Imputed ===")
print(df.isnull().sum())
print("\n")


before = df.shape
df = df.drop_duplicates()
after = df.shape
print("=== STEP 5: Duplicates Removed ===")
print("Before:", before, "After:", after)
print("\n")


def iqr_bounds(series, k=1.5):
    q1, q3 = series.quantile([0.25, 0.75])
    iqr = q3 - q1
    lower = q1 - k*iqr
    upper = q3 + k*iqr
    return lower, upper

price_low, price_high = iqr_bounds(df["Price"])
odom_low, odom_high = iqr_bounds(df["Odometer_km"])
df["Price"] = df["Price"].clip(price_low, price_high)
df["Odometer_km"] = df["Odometer_km"].clip(odom_low, odom_high)

print("=== STEP 6: Outliers Capped ===")
print("Price summary:\n", df["Price"].describe())
print("Odometer summary:\n", df["Odometer_km"].describe())
print("\n")

df = pd.get_dummies(df, columns=["Location"], drop_first=False, dtype=int)
print("=== STEP 7: One-Hot Encoding ===")
print("Columns after encoding:", [c for c in df.columns if c.startswith("Location_")])
print(df.head(5))
print("\n")


current_year = 2026
df["Car_Age"] = current_year - df["Year"]
df["km_per_year"] = df["Odometer_km"] / df["Car_Age"].replace(0, np.nan)
df["Price_per_km"] = df["Price"] / df["Odometer_km"].replace(0, np.nan)
df["LogPrice"] = np.log1p(df["Price"])
df["Accident_Rate"] = df["Accidents"] / df["Car_Age"].replace(0, np.nan)
df["Is_OldCar"] = (df["Car_Age"] > 15).astype(int)
df["Is_Urban"] = df.get("Location_City", pd.Series([0]*len(df))).astype(int)

print("=== STEP 8: Feature Engineering ===")
print(df[["Car_Age", "km_per_year", "Price_per_km", "LogPrice", "Accident_Rate", "Is_OldCar", "Is_Urban"]].head(10))
print("\n")


dont_scale = ["Price", "LogPrice"]
numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.to_list()
exclude = [c for c in df.columns if c.startswith("Location_")] + ["Is_OldCar", "Is_Urban"]
scale_cols = [c for c in numeric_cols if c not in dont_scale and c not in exclude]

scaler = StandardScaler()
df[scale_cols] = scaler.fit_transform(df[scale_cols])

print("=== STEP 9: Feature Scaling ===")
print(df[scale_cols].head(5))
print("\n")
print("=== STEP 10: Final Dataset Info ===")
print(df.info())
print("\nMissing values after preprocessing:")
print(df.isnull().sum())
print("\nDataset description:")
print(df.describe())

OUT_PATH = "car_13_clean_ready.csv"
df.to_csv(OUT_PATH, index=False)
print("\nData preprocessing complete. Cleaned data saved to:", OUT_PATH)