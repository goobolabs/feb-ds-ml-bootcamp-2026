import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

CSV_FILE_PATH ="dataset/car_l3_dataset.csv"

df = pd.read_csv(CSV_FILE_PATH)
# 1 initial snapshot of the data
print(df.head())
print("info about the data")
print(df.info())
print("initial missing values in the data")
print(df.isnull().sum())

# 2 Clean target formatting
df["Price"] = df["Price"].replace(r"[\$,]", "", regex=True).astype(float)
# print(df["Price"].head(10))   

# 3 Fixing Category Errors before Imputation
df["Location"] = df["Location"].replace({"Subrb": "Suburb", "??": pd.NA})


# 4 Handling Missing Values
# MEDIAN
df["Odometer_km"] = df["Odometer_km"].fillna(df["Odometer_km"].median())
# MODE 
df["Doors"] = df["Doors"].fillna(df["Doors"].mode()[0])
df["Accidents"] = df["Accidents"].fillna(df["Accidents"].mode()[0])
df["Location"] = df["Location"].fillna(df["Location"].mode()[0])

# print("\nMissing after imputation:")
# print(df.isnull().sum())

# 5 Remove duplicates
df = df.drop_duplicates()

# 6 INTERQUARTILE RANGE (IQR) for outlier detection
def iqr_fun(series, k=1.5):
    q1, q3 = series.quantile([0.25, 0.75])
    iqr = q3 - q1
    lower = q1 - k * iqr
    upper = q3 + k * iqr
    return lower, upper

low_price, high_price = iqr_fun(df["Price"])
low_km, high_km = iqr_fun(df["Odometer_km"])

df["Price"] = df["Price"].clip(lower=low_price, upper=high_price)
df["Odometer_km"] = df["Odometer_km"].clip(lower=low_km, upper=high_km)

# print("\nOutliers handled (IQR clipping)")
# print(df.describe())

# 7 one hot encoding for categorical variables
df = pd.get_dummies(df, columns=["Location"],  drop_first=False, dtype=int)

# print([c for c in df.columns if c.startswith("Location")])

# 8 Feature engineering - creating new features
CURRENT_YEAR = 2026
df["carAge"] = CURRENT_YEAR - df["Year"]

df["Km_per_year"] = df["Odometer_km"] / df["carAge"].replace(0, 1)

df["Is_Urban"] = ((df["Location_City"] == 1) | (df["Location_Suburb"] == 1)).astype(int)

df["LogPrice"] = np.log1p(df["Price"])

# 9  feature scaling
dont_scale = ["Price", "LogPrice"]
exclude = [c for c in df.columns if c.startswith("Location_")] + dont_scale

numeric_cols = df.select_dtypes(include=["int64","float64"]).columns
scale_cols = [c for c in numeric_cols if c not in exclude]

scaler = StandardScaler()
df[scale_cols] = scaler.fit_transform(df[scale_cols])


# 10 Final snapshot of the cleaned and engineered data
print("\nFinal cleaned and engineered data:")

print("\n=== FINAL HEAD ===")
print(df.head())

print("\n....  FINAL INFO ....")
print(df.info())

print("\n.... FINAL MISSING VALUES ....")
print(df.isnull().sum())

# 10) final saved data

OUT_PATH = "data\\cleaned_car_l3_dataset.csv"
df.to_csv(OUT_PATH, index=False)





