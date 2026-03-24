import pandas as pd
import numpy as np 
from sklearn.preprocessing import StandardScaler

CSV_FILE = 'data/raw/car_l3_dataset.csv'

# 1- Load & Inspect
# Load the dataset
df = pd.read_csv(CSV_FILE)

# Show the data
print("------------ Data Head 10 ------------\n")
print(df.head(10))
print("------------ Data Tail 10 ------------\n")
print(df.tail(10))

# Show the data shape
shape = df.shape
print("------------ Data Shape ------------\n")
print(shape)

# Show the data info
print("------------ Data Info ------------\n")
info = df.info()

# Show the data description
print("------------ Data Description ------------\n")
print(df.describe())

# show missing values
print("------------ Data Missing Values ------------\n")
print(df.isnull().sum())

# show location value counts
print("------------ Data Location Value Counts ------------\n")
print(df['Location'].value_counts(dropna=False))



# # 2- Clean Target Formatting
# Convert to string
df["Price"] = df["Price"].astype(str)

# Remove non-numeric characters
df["Price"] = df["Price"].str.replace(r"[^\d.]", "", regex=True)

# Convert to numeric
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
print(df.head())

# Data Price Dtype
print("------------ Data Price Dtype ------------\n")
print(df["Price"].dtype)

# Data Price Skewness
print("------------ Data Price Skewness ------------\n")
print(df["Price"].skew())



# 3-Fix Categorical Issues
# Convert to string and lowercase for consistency
df["Location"] = df["Location"].astype(str).str.lower()

# Remove leading/trailing spaces
df["Location"] = df["Location"].str.strip()

# Replace specify values
location_map = {
    "subrb": "suburb",
    "suberb": "suburb",
    "cty": "city",
    "rurl": "rural",
    "??": np.nan,
    "unknown": np.nan,
    "nan": np.nan
}

df["Location"] = df["Location"].replace(location_map)

# show location value counts
print("------------ Data Location Value Counts ------------\n")
print(df["Location"].value_counts(dropna=False))
print(f"{df.isnull().sum()}\n") # nan = missing value in locations


# 4-Impute Missing Values
# Fill missing Odometer with median
df["Odometer_km"] = df["Odometer_km"].fillna(df["Odometer_km"].median())

# Fill missing Doors with mode
df["Doors"] = df["Doors"].fillna(df["Doors"].mode()[0])

# Fill missing location with mode
df["Location"] = df["Location"].fillna(df["Location"].mode()[0])

print("------------ Data Missing Values ------------\n")
print(f"{df.isnull().sum()}\n")



# 5-Remove Duplicates
before = df.shape

df = df.drop_duplicates()

after = df.shape

print("------------ Data Shape Before & After Duplicates ------------\n")
print(f"Before: {before[0]}, After: {after[0]}, Difference: {before[0] - after[0]} \n")



# 6-Remove Outliers
def iqr(series):
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)

    iqr = q3 - q1

    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr

    return series.clip(lower, upper), lower, upper

df["Price"], lower, upper = iqr(df["Price"])
df["Odometer_km"], lower, upper = iqr(df["Odometer_km"])

print("------------ Data Price IQR ------------\n")
print(df["Price"].describe())

print("------------ Data Odometer IQR ------------\n")
print(df["Odometer_km"].describe())



# 7-One-Hot Encode Categorical(s)
df = pd.get_dummies(df, columns=["Location"], prefix="Location")
[c for c in df.columns if c.startswith("Location_")]


print("------------ Data New Columns ------------\n")
print(df.head(10))



# 8-Feature Engineering
CURRENT_YEAR = pd.Timestamp('now').year

# CarAge feature 
df["CarAge"] = CURRENT_YEAR - df["Year"]

# kilorometers per year
df["Km_per_year"] = df["Odometer_km"] / df["CarAge"]

# Is_Urban feature
df["Is_Urban"] = np.where(
    df.filter(like="Location_city").sum(axis=1) > 0,
    1,
    0
)

# LogPrice feature
df["LogPrice"] = np.log1p(df["Price"])

print("------------ Preview engineered features ------------\n")
print(df.head(10))


# 9-Feature scaling
scale_cols = ["Odometer_km", "CarAge", "Km_per_year"]

scaler = StandardScaler()
df[scale_cols] = scaler.fit_transform(df[scale_cols])

print("------------ Scaled features ------------\n")
print(df[scale_cols].head(10))



# Check 
print("------------ Data Check------------\n")

print(df.info())
print(df.isnull().sum())
print(df.describe())



# 10-Save cleaned data
df.to_csv('data/processed/car_l3_clean_ready.csv', index=False)
print(" Data Saved Successfully ")