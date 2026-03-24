import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report


CSV_PATH = "Employee.csv"
df = pd.read_csv(CSV_PATH)

# === 0) RENAME COLUMNS TO SAFE NAMES ===
rename_map = {
    "Work Hours": "Work_Hours",
    "Sleep Hours": "Sleep_Hours",
    "Department": "Department",
    "Attendance %": "Attendance_Pct",
    "Performance Rating": "Performance_Rating",
    "Coffee Consumption_Heavy": "Coffee_Heavy",
    "Coffee Consumption_Light": "Coffee_Light",
    # In case your file uses a single column "Coffee Consumption"
    "Coffee Consumption": "Coffee_Consumption"
}
df = df.rename(columns=rename_map)

print("\n=== INITIAL HEAD ===")
print(df.head())

print("\n=== INITIAL INFO ===")
print(df.info())

print("\n=== INITIAL MISSING VALUES ===")
print(df.isnull().sum())

# === 1) STANDARDIZE COFFEE VARIABLE ===
# Your text sample shows two boolean columns: Coffee_Heavy and Coffee_Light.
# If they exist, consolidate them into a single categorical column "Coffee_Consumption".
if {"Coffee_Heavy", "Coffee_Light"}.issubset(df.columns):
    # Coerce to boolean safely
    df["Coffee_Heavy"] = df["Coffee_Heavy"].astype("boolean")
    df["Coffee_Light"] = df["Coffee_Light"].astype("boolean")

    def coffee_label(row):
        if row["Coffee_Heavy"] is True:
            return "Heavy"
        if row["Coffee_Light"] is True:
            return "Light"
        return "None"

    df["Coffee_Consumption"] = df.apply(coffee_label, axis=1)

elif "Coffee_Consumption" in df.columns:
    # If you have one column, clean obvious variants and NaN
    df["Coffee_Consumption"] = (
        df["Coffee_Consumption"]
        .astype("string")
        .str.strip()
        .str.title()
        .replace({"Hevy": "Heavy", "Ligt": "Light"})
    )
else:
    # Fallback if nothing is present
    df["Coffee_Consumption"] = "None"

# === 2) FIX CATEGORICAL ISSUES BEFORE IMPUTATION ===
# Example: normalize Department and Performance_Rating typos if any
df["Department"] = (
    df["Department"]
    .astype("string")
    .str.strip()
    .str.title()
    .replace({"It": "IT"})  # keep IT uppercased
)
df["Performance_Rating"] = (
    df["Performance_Rating"]
    .astype("string")
    .str.strip()
    .str.title()
)

# === 3) IMPUTE MISSING VALUES ===
# Numerics: median. Categoricals: mode.
numeric_cols = []
for c in ["Work_Hours", "Sleep_Hours", "Attendance_Pct"]:
    if c in df.columns:
        # Coerce to numeric if read as object
        df[c] = pd.to_numeric(df[c], errors="coerce")
        numeric_cols.append(c)

categorical_cols = [c for c in ["Department", "Performance_Rating", "Coffee_Consumption"] if c in df.columns]

for c in numeric_cols:
    df[c] = df[c].fillna(df[c].median())

for c in categorical_cols:
    if df[c].isnull().any():
        df[c] = df[c].fillna(df[c].mode()[0])

# === 4) REMOVE DUPLICATES ===
before = df.shape
df = df.drop_duplicates()
after = df.shape
print(f"\nDropped duplicates: {before} → {after}")

# === 5) OUTLIER HANDLING (IQR CLIPPING) ===
def iqr_bounds(series, k=1.5):
    q1, q3 = series.quantile([0.25, 0.75])
    iqr = q3 - q1
    return q1 - k * iqr, q3 + k * iqr

for c in ["Work_Hours", "Sleep_Hours", "Attendance_Pct"]:
    if c in df.columns and pd.api.types.is_numeric_dtype(df[c]):
        low, high = iqr_bounds(df[c])
        df[c] = df[c].clip(lower=low, upper=high)

# Optional sanity caps for human ranges (comment out if not wanted)
if "Work_Hours" in df.columns:
    df["Work_Hours"] = df["Work_Hours"].clip(lower=0, upper=16)
if "Sleep_Hours" in df.columns:
    df["Sleep_Hours"] = df["Sleep_Hours"].clip(lower=0, upper=16)
if "Attendance_Pct" in df.columns:
    df["Attendance_Pct"] = df["Attendance_Pct"].clip(lower=0, upper=100)

# === 6) ONE-HOT ENCODE CATEGORICALS ===
df = pd.get_dummies(
    df,
    columns=[c for c in ["Department", "Performance_Rating", "Coffee_Consumption"] if c in df.columns],
    drop_first=False,
    dtype="int"
)

# === 7) FEATURE ENGINEERING ===
# Ratios and simple flags that could help a model
if {"Work_Hours", "Sleep_Hours"}.issubset(df.columns):
    df["Work_Sleep_Ratio"] = df["Work_Hours"] / df["Sleep_Hours"].replace(0, np.nan)

# Flag excellent performance if that dummy exists
if "Performance_Rating_Excellent" in df.columns:
    df["Is_Excellent"] = df["Performance_Rating_Excellent"].astype(int)
else:
    df["Is_Excellent"] = 0

# Heavy coffee flag from dummies if present
if "Coffee_Consumption_Heavy" in df.columns:
    df["Coffee_Heavy_Flag"] = df["Coffee_Consumption_Heavy"].astype(int)
else:
    df["Coffee_Heavy_Flag"] = 0

# === 8) SCALING (KEEP DUMMIES UNSCALED) ===
dont_scale = set()  # no explicit target here
dummy_prefixes = ["Department_", "Performance_Rating_", "Coffee_Consumption_"]
exclude = [c for c in df.columns if any(c.startswith(p) for p in dummy_prefixes)] + ["Is_Excellent", "Coffee_Heavy_Flag"]

num_cols_all = df.select_dtypes(include=["int64", "float64"]).columns.to_list()
num_to_scale = [c for c in num_cols_all if c not in dont_scale and c not in exclude]

scaler = StandardScaler()
if len(num_to_scale) > 0:
    df[num_to_scale] = scaler.fit_transform(df[num_to_scale])

# === FINAL SNAPSHOT ===
print("\n=== FINAL HEAD ===")
print(df.head())

print("\n=== FINAL INFO ===")
print(df.info())

print("\n=== FINAL MISSING VALUES ===")
print(df.isnull().sum())

# === SAVE ===
OUT_PATH = "Employees_Clean.csv"
df.to_csv(OUT_PATH, index=False)
print(f"\nSaved cleaned dataset to: {OUT_PATH}")