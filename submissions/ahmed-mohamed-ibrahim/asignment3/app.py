import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
CSV_PATH = 'car-dataset.csv'
df=pd.read_csv(CSV_PATH)
#1 load&inspect
# print(df.head(10))
# print(df.shape)
# print(df.info())
# print(df.describe())
#showing missing values
print(df.isnull().sum())
# initial location
print(df["Location"].value_counts())
#2 cleaning
df['Price'] = df['Price'].astype(str).str.replace(r'[$,]', '', regex=True)
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
print(df['Price'].dtype)
print(df['Price'].skew())
#3 fix category errors
df["Location"] = df["Location"].str.lower().str.strip().str.capitalize()
df['Location'] = df['Location'].replace({'Subrb': 'Suburb', '??': np.nan})
#4 imute missing values
df["Price"]=df["Price"].fillna(df["Price"].median())
df["Odometer_km"]=df["Odometer_km"].fillna(df["Odometer_km"].median())
df["Doors"]=df["Doors"].fillna(df["Doors"].mode()[0])
df["Accidents"]=df["Accidents"].fillna(df["Accidents"].mode()[0])
df["Year"]=df["Year"].fillna(df["Year"].mode()[0])
df["Location"]=df["Location"].fillna(df["Location"].mode()[0])
print(df.isnull().sum())
#5 remove duplicates
df=df.drop_duplicates()
print(df.shape)
## 6) Outliers 
def iqr_fun(series, k=1.5):
    q1, q3 = series.quantile([0.25, 0.75])
    iqr = q3 - q1
    lower = q1 -k * iqr
    upper = q3 + k * iqr
    return lower, upper
low_price, high_price = iqr_fun(df["Price"])
low_odometer, high_odometer = iqr_fun(df["Odometer_km"])
df["Price"]=df["Price"].clip(lower=low_price, upper=high_price)
df["Odometer_km"]=df["Odometer_km"].clip(lower=low_odometer, upper=high_odometer)
print(df[["Price", "Odometer_km"]].max())
#7 one hot encoding
df=pd.get_dummies(df,columns=["Location"],drop_first=False,dtype=int)
print(df.head(10))
# feature engineering
df["Car_age"]=2026-df["Year"]
df["Km_per_year"]=df['Odometer_km'] / (df['Car_age'] + 1)
df['Is_Urban'] = df[['Location_City']].max(axis=1)
df["LogPrice"] = np.log1p(df["Price"])
print(df.head(10))
# 9 scale features
dont_scale = {"Price" , "LogPrice"}
numeric_cols = df.select_dtypes(include=["float64", "Int64"]).columns.to_list()
exclude = [c for c in df.columns if c.startswith("Location")] + ["Is_City"]
num_features_to_scale = [c for c in numeric_cols if c not in dont_scale and c not in exclude]
scaler = StandardScaler()
df[num_features_to_scale] = scaler.fit_transform(df[num_features_to_scale])
print(df.head(10))
## Final Checks & Save
print("\n=== FINAL HEAD ===")
print(df.head(10))
print("\n=== FINAL SHAPE ===")
print(df.shape)
print("\n=== FINAL INFO ===")
print(df.info())
print("\n=== FINAL MISSING VALUES ===")
print(df.isnull().sum())
OUT_PATH = 'car_clean_l3_dataset.csv'
df.to_csv(OUT_PATH)
print("Saved to", OUT_PATH)