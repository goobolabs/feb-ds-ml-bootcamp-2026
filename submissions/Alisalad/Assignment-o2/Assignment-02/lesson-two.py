import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# === 1) Load dataset ===
CSV_PATH = r"dataset/Mog_Transport.csv"
df = pd.read_csv(CSV_PATH)

# === 2) Initial snapshot ===
print("\n=== INITIAL HEAD ===")
print(df.head())

print("\n=== INITIAL INFO ===")
print(df.info())

print("\n=== INITIAL MISSING VALUES ===")
print(df.isnull().sum())

# === 3) Clean Transport_Type ===
df["Transport_Type"] = (
    df["Transport_Type"]
    .astype(str)
    .str.strip()
    .str.lower()
    .replace({
        "baj aj": "bajaj",
        "bajaaj": "bajaj",
        "nan": np.nan,
        "": np.nan
    })
)

# === 4) Clean Traffic_Level ===
df["Traffic_Level"] = (
    df["Traffic_Level"]
    .astype(str)
    .str.strip()
    .str.capitalize()
    .replace({"nan": np.nan, "": np.nan})
)

# === 5) Clean Distance_km (remove 'km' and convert to float) ===
df["Distance_km"] = (
    df["Distance_km"]
    .astype(str)
    .str.replace("km", "", regex=False)
    .replace("", np.nan)
    .astype(float)
)

# === 6) Clean Travel_Time_Minutes (remove 'min' and convert to float) ===
df["Travel_Time_Minutes"] = (
    df["Travel_Time_Minutes"]
    .astype(str)
    .str.replace("min", "", regex=False)
    .replace("", np.nan)
    .astype(float)
)

# === 7) Impute missing values ===
for col in ["Start_Location", "Destination", "Time_of_Day", "Day_of_Week", "Transport_Type", "Traffic_Level"]:
    if col in df.columns and not df[col].mode().empty:
        df[col] = df[col].fillna(df[col].mode()[0])

for col in ["Distance_km", "Travel_Time_Minutes"]:
    if col in df.columns:
        df[col] = df[col].fillna(df[col].median())

# === 8) Remove duplicates ===
before = df.shape
df = df.drop_duplicates()
after = df.shape
print(f"Dropped duplicates: {before} → {after}")

# === 9) Handle outliers (IQR capping) ===
def iqr_cap(series, k=1.5):
    q1, q3 = series.quantile([0.25, 0.75])
    iqr = q3 - q1
    lower = q1 - k * iqr
    upper = q3 + k * iqr
    return series.clip(lower, upper)

for col in ["Distance_km", "Travel_Time_Minutes"]:
    df[col] = iqr_cap(df[col])

# === 10) Feature engineering ===
df["Speed_kmh"] = df.apply(
    lambda row: row["Distance_km"] / (row["Travel_Time_Minutes"] / 60)
    if row["Travel_Time_Minutes"] > 0 else np.nan,
    axis=1
)

# === 11) Binary encoding (0/1 flags) ===
# Transport type
df["Is_Bajaj"] = (df["Transport_Type"] == "bajaj").astype(int)
df["Is_Bus"] = (df["Transport_Type"] == "bus").astype(int)
df["Is_Taxi"] = (df["Transport_Type"] == "taxi").astype(int)
df["Is_Walking"] = (df["Transport_Type"] == "walking").astype(int)

# Traffic level
df["Traffic_High"] = (df["Traffic_Level"] == "High").astype(int)
df["Traffic_Medium"] = (df["Traffic_Level"] == "Medium").astype(int)
df["Traffic_Low"] = (df["Traffic_Level"] == "Low").astype(int)

# Time of day
df["Is_Morning"] = (df["Time_of_Day"] == "Morning").astype(int)
df["Is_Afternoon"] = (df["Time_of_Day"] == "Afternoon").astype(int)
df["Is_Evening"] = (df["Time_of_Day"] == "Evening").astype(int)

# Weekend flag
df["Is_Weekend"] = df["Day_of_Week"].isin(["Saturday", "Sunday"]).astype(int)

# === 12) Feature scaling (numeric only) ===
numeric_cols = ["Distance_km", "Travel_Time_Minutes", "Speed_kmh"]
scaler = StandardScaler()
df[numeric_cols] = scaler.fit_transform(df[numeric_cols])

# === 13) Final snapshot ===
print("\n=== FINAL HEAD ===")
print(df.head())

print("\n=== FINAL INFO ===")
print(df.info())

print("\n=== FINAL MISSING VALUES ===")
print(df.isnull().sum())

# === 14) Save cleaned dataset ===
OUT_PATH = r"C:\Users\Alisalad\OneDrive\Desktop\lesson_two\Mog_Transport_Clean.csv"
df.to_csv(OUT_PATH, index=False)
print(f"\nCleaned dataset saved to {OUT_PATH}")
