import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler  # scaling features
from sklearn.model_selection import train_test_split
from datetime import datetime



CSV_PATH = 'car_l3_dataset.csv'

df = pd.read_csv(CSV_PATH)

# =========================
# STEP 1: LOAD & INSPECT
# =========================

print("\n=== HEAD (10 rows) ===")
print(df.head(10))  # wuxuu tusayaa 10ka row ee ugu horeeya si aad u fahanto qaabka data

print("\n=== SHAPE ===")
print(df.shape)  # wuxuu muujinayaa (rows, columns)

print("\n=== INFO ===")
df.info()  # wuxuu tusayaa column names, dtypes, missing values

print("\n=== MISSING VALUES ===")
print(df.isnull().sum())  # wuxuu tirinayaa missing values column walba

print("\n=== LOCATION VALUE COUNTS ===")
print(df["Location"].value_counts(dropna=False))  
# wuxuu tusayaa categories-ka Location iyo inta jeer ee ay soo noqdeen


# =========================
# STEP 2: CLEAN TARGET (Price)
# =========================

df["Price"] = df["Price"].replace(r"[\$,]", "", regex=True)
# wuxuu ka saarayaa $ iyo comma

df["Price"] = pd.to_numeric(df["Price"], errors="coerce")
# wuxuu u rogaa float; haddii qalad jiro wuxuu ka dhigaa NaN

print("\nPrice dtype:", df["Price"].dtype)
# hubi in uu noqday float

print("Price skewness:", df["Price"].skew())
# wuxuu cabbiraa leexashada distribution-ka


# =========================
# STEP 3: FIX CATEGORY ERRORS
# =========================

df["Location"] = df["Location"].str.strip().str.lower()
# wuxuu ka saarayaa space, kana dhigaa lowercase

df["Location"] = df["Location"].replace({
    "subrb": "suburb",
    "??": np.nan,
    "unknown": np.nan
})
# wuxuu saxayaa typo iyo unknown values

print("\nLocation after cleaning:")
print(df["Location"].value_counts(dropna=False))
# hubi categories-ka saxda ah

print(df.dtypes)

# df["Odometer_km"] = pd.to_numeric(df["Odometer_km"], errors="coerce")
# df["Doors"] = pd.to_numeric(df["Doors"], errors="coerce")
# print(df["Odometer_km"].unique())

# =========================
# STEP 4: IMPUTATION
# =========================

df["Odometer_km"] = df["Odometer_km"].fillna(df["Odometer_km"].median())
# median sababtoo ah outliers ayuu iska caabiyaa

df["Doors"] = df["Doors"].fillna(df["Doors"].mode()[0])
# mode sababtoo ah waa discrete

df["Accidents"] = df["Accidents"].fillna(df["Accidents"].mode()[0])

df["Location"] = df["Location"].fillna(df["Location"].mode()[0])
# category missing lagu buuxiyay value ugu badan

print("\nMissing after imputation:")
print(df.isnull().sum())
# waa inuu noqdaa 0

# print("IMPUTATION RUNNING...")


# =========================
# STEP 5: REMOVE DUPLICATES
# =========================

print("\nShape before duplicates removal:", df.shape)

before_rows = df.shape[0]
df = df.drop_duplicates()
after_rows = df.shape[0]

print("Shape after duplicates removal:", df.shape)
print("Rows removed:", before_rows - after_rows)


# =========================
# STEP 6: IQR CAPPING
# =========================

def iqr_bounds(series):
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr
    return lower, upper

# xadka IQR
low_p, high_p = iqr_bounds(df["Price"])
low_o, high_o = iqr_bounds(df["Odometer_km"])

print("Price bounds:", low_p, high_p)
print("Odometer bounds:", low_o, high_o)

# tirinta inta outlier ah ka hor capping
price_outliers = ((df["Price"] < low_p) | (df["Price"] > high_p)).sum()
odo_outliers = ((df["Odometer_km"] < low_o) | (df["Odometer_km"] > high_o)).sum()

print("Price values capped:", price_outliers)
print("Odometer values capped:", odo_outliers)

# capping
df["Price"] = df["Price"].clip(low_p, high_p)
df["Odometer_km"] = df["Odometer_km"].clip(low_o, high_o)

print("\nAfter capping summary:")
print(df[["Price", "Odometer_km"]].describe())



# =========================
# STEP 7: ONE HOT ENCODE
# =========================

df = pd.get_dummies(df, columns=["Location"], dtype=int)

print("New dummy columns:")
print([c for c in df.columns if c.startswith("Location_")])


# =========================
# STEP 8: FEATURE ENGINEERING
# =========================

CURRENT_YEAR = datetime.now().year

df["CarAge"] = CURRENT_YEAR - df["Year"]

df["Km_per_year"] = df["Odometer_km"] / df["CarAge"].replace(0, np.nan)
df["Km_per_year"] = df["Km_per_year"].fillna(0)

# Urban = city ama suburb
df["Is_Urban"] = 0
if "Location_city" in df.columns:
    df["Is_Urban"] += df["Location_city"]
if "Location_suburb" in df.columns:
    df["Is_Urban"] += df["Location_suburb"]

df["LogPrice"] = np.log1p(df["Price"])



# =========================
# STEP 9: SCALING
# =========================

# =========================
# FINAL MODEL PREPARATION
# =========================

# 1️⃣ Year ka saar sabab CarAge ayaan isticmaaleynaa
df = df.drop(columns=["Year"])

# 2️⃣ Target = LogPrice
y = df["LogPrice"]

# 3️⃣ Features = wax kasta oo kale marka laga reebo Price iyo LogPrice
X = df.drop(columns=["Price", "LogPrice"])

print("Target shape:", y.shape)
print("Features shape:", X.shape)

# 4️⃣ Columns aan rabno in la scale gareeyo
scale_cols = [
    "Odometer_km",
    "Doors",
    "Accidents",
    "CarAge",
    "Km_per_year"
]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

scaler = StandardScaler()
X_train[scale_cols] = scaler.fit_transform(X_train[scale_cols])
X_test[scale_cols] = scaler.transform(X_test[scale_cols])

print("\nAfter Scaling (train sample):")
print(X_train.head())
print("Train shape:", X_train.shape, "Test shape:", X_test.shape)


# dont_scale = ["Price", "LogPrice"]
# dummy_cols = [c for c in df.columns if c.startswith("Location_")]

# numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.tolist()

# features_to_scale = [
#     c for c in numeric_cols
#     if c not in dont_scale and c not in dummy_cols
# ]

# X = df.drop(columns=["Price", "LogPrice"])
# y = df["Price"]

# scaler = StandardScaler()
# df[features_to_scale] = scaler.fit_transform(df[features_to_scale])

# print(df[features_to_scale].head())
# sample scaled values


# =========================
# STEP 10: FINAL CHECKS
# =========================

df.info()
print(df.isnull().sum())
print(df.describe())
print("\nScaled train missing values:")
print(X_train.isnull().sum())

assert df["Price"].dtype == float
assert "LogPrice" in df.columns
assert df.isnull().sum().sum() == 0
assert len([c for c in df.columns if c.startswith("Location_")]) > 0
assert X_train[scale_cols].isnull().sum().sum() == 0
assert X_test[scale_cols].isnull().sum().sum() == 0

df.to_csv("car_l3_clean_ready.csv", index=False)
