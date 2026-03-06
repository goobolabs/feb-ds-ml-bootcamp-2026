import pandas as pd 
import numpy as np 
from sklearn.preprocessing import StandardScaler

CSV_PATH = 'dataset/car_l3_dataset.csv'
df = pd.read_csv(CSV_PATH)

# === INITIAL SNAPSHOT ===
print("\n === INITIAL HEAD ===")
print(df.head(10))

print("\n === INITIAL INFO")
print(df.info())

print("\n ==== INITIAL MISSING VALUES ")
print(df.isnull().sum())

# === CLEAN TARGET FORMATING ====
df["Price"] = df["Price"].replace(r"[\$,]", "", regex=True).astype(float)

df["Location"] = df["Location"].replace({"Subrb" : "Suburb", "??" : pd.NA})

print("\n === IMPUTE MISSING VALUES ===")

def impute_missing(df):
    if "Odometer_km" in df.columns:
        df["Odometer_km"] = df["Odometer_km"].fillna(df["Odometer_km"].median())
    if "Doors" in df.columns:
        df["Doors"] = df["Doors"].fillna(df["Doors"].mode()[0])
    if "Location" in df.columns:
        df["Location"] = df["Location"].fillna(df["Location"].mode()[0])
    return df

df = impute_missing(df)


print("\n === AFTER IMPUTATION SNAPSHOT ===")
print(df.head(10))

print("\n === AFTER MISSING VALUES ===")
print(df.isnull().sum())

# === remove duplicates ===
before = df.shape 
df = df.drop_duplicates()
after = df.shape

# ===IQR capping ====
def iqr_fun(series, k = 1.5):
    q1, q3 = series.quantile([0.25, 0.75])
    iqr = q3 - q1 
    lower = q1 - k *iqr 
    upper = q3 + k *iqr
    return lower , upper 
low_price, high_price = iqr_fun(df["Price"])
low_odo, high_odo = iqr_fun(df["Odometer_km"])
low_doors, high_doors = iqr_fun(df["Doors"])

df["Price"] = df["Price"].clip(lower = low_price, upper = high_price)
df["Odometer_km"] = df["Odometer_km"].clip(lower = low_odo , upper = high_odo)  
df["Doors"]  = df["Doors"].clip(lower = low_doors, upper = high_doors )    

# Normalize Location before encoding
df["Location"] = df["Location"].str.strip().str.lower()
df["Location"] = df["Location"].replace({"subrb":"suburb", "??": pd.NA, "": "city"})


# === ONE HOT ENCODING ===
df = pd.get_dummies(df, columns=["Location"], drop_first=False, dtype="int")



# ===feature engineering===
CURRENT_YEAR = 2026

# Car age
df["CarAge"] = CURRENT_YEAR - df["Year"]

# Mileage per year (wear indicator)
df["Mileage_per_Year"] = df["Odometer_km"] / df["CarAge"].replace(0, np.nan)

# Doors as categorical flag (e.g., is 4-door sedan)
df["Is_FourDoor"] = (df["Doors"] == 4).astype(int)

# Accident flag (binary: has accidents or not)
df["Has_Accidents"] = (df["Accidents"] > 0).astype(int)

# Location flag 
if "Location_City" in df.columns:
    df["Is_City"] = df["Location_City"].astype(int)

# Log transform of price
df["LogPrice"] = np.log1p(df["Price"])

# === Feature scaling (exclude targets, dummies, and binary flags) ===
dont_scale = {"Price", "LogPrice", "Doors", "Accidents"}  # targets + discrete counts
exclude = [c for c in df.columns if c.startswith("Location_")] \
          + ["Is_City", "Is_FourDoor", "Has_Accidents"]   # dummies + binary flags

numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.to_list()
num_features_to_scale = [c for c in numeric_cols if c not in dont_scale and c not in exclude]

scaler = StandardScaler()
df[num_features_to_scale] = scaler.fit_transform(df[num_features_to_scale])


# === FINAL SNAPSHOT ===
print("\n=== FINAL HEAD ===")
print(df.head())


print("\n=== FINAL INFO ===")
print(df.info())


print("\n=== FINAL MISSING VALUES ===")
print(df.isnull().sum())


# 10) Save
OUT_PATH = " car_l3_clean_ready.csv"
df.to_csv(OUT_PATH, index=False)