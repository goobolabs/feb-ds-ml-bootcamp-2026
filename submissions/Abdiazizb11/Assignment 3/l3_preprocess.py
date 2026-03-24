import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

#STEP 1
df = pd.read_csv('dataset\car_l3_dataset.csv')
print(df.head(10))
print(df.shape)
print(df.info())
print(df.isna().sum())
print(df["Location"].value_counts())

# STEP 2  Clean target formatting
df["Price"] = df["Price"].replace(r"[\$,]", "", regex=True).astype(float).abs()
print(f"Price Skewness: {df['Price'].skew()}")

# STEP 3 Fix categorical issues BEFORE imputation
df["Location"] = df["Location"].replace({"Subrb": "Suburb", "??": np.nan})
df["Location"] = df["Location"].str.lower().str.strip()

#STEP 4  fill missing values 
df["Odometer_km"] = df["Odometer_km"].abs().fillna(df["Odometer_km"].median())
df["Location"] = df["Location"].fillna(df["Location"].mode()[0])
df["Accidents"] = df["Accidents"].fillna(df["Accidents"].mode()[0])
df["Doors"] = df["Doors"].fillna(df["Doors"].mode()[0])

#STEP 5 remove duplicates 
print(f"Before: {df.shape}")
df = df.drop_duplicates()
print(f"After: {df.shape}")

#STEP 6 use IQR to get the outliers and also remave outliers
def iqr_fun(series, k=1.5):
    q1, q3 = series.quantile([0.25, 0.75])
    iqr = q3 - q1
    lower = q1 - k * iqr
    upper = q3 + k * iqr
    return max(0, lower), upper

low_price, high_price = iqr_fun(df["Price"])
low_odo, high_odo = iqr_fun(df["Odometer_km"])

df["Price"] = df["Price"].clip(lower=low_price, upper=high_price)
df["Odometer_km"] = df["Odometer_km"].clip(lower=low_odo, upper=high_odo)

#STEP 7  on hot endcoding
df = pd.get_dummies(df, columns=["Location"], drop_first=False, dtype="int")

#STEP 8 
df["Log_price"] = np.log1p(df["Price"])
df["CarAge"] = 2026 - df["Year"]
df["Km_per_year"] = df["Odometer_km"] / (df["CarAge"] + 1)
df["Is_Urban"] = df["Location_city"]

# STEP 9 scaling the data 
scaler = StandardScaler()
features_to_scale = ["Odometer_km", "Doors", "Accidents", "CarAge", "Km_per_year"]
df_scaled = df.copy()
df_scaled[features_to_scale] = scaler.fit_transform(df[features_to_scale])
print("Scaled sample:\n", df_scaled[features_to_scale].head())

#STEP 10
print(df.info())
print(df.describe())


df_scaled.to_csv("car_l3_clean_ready.csv", index=False)
print("file saved")