import pandas as pd
import numpy as np 
from sklearn.preprocessing import StandardScaler
CSV_PATH = r"C:\Users\hp\Documents\sucad-khalif\ds-ml-bootcamp\submissions\sucad-khalif\ASSIGNMENT3\wedding_sample.csv"
df = pd.read_csv(CSV_PATH)
print(df.head(10))

print (df.shape)
print(df.info())

print(df.isnull().sum())

#Missing Values
df["Number_of_Guests"] = df["Number_of_Guests"].fillna(df["Number_of_Guests"].median())
df["Venue_Type"] = df["Venue_Type"].fillna(df["Venue_Type"].mode()[0])
df["Catering_Type"] = df["Catering_Type"].fillna(df["Catering_Type"].mode()[0])
df["Decoration_Level"] = df["Decoration_Level"].fillna(df["Decoration_Level"].mode()[0])
df["Wedding_Duration_Hours"] = df["Wedding_Duration_Hours"].fillna(df["Wedding_Duration_Hours"].median())
df["Wedding_Price"] = df["Wedding_Price"].fillna(df["Wedding_Price"].median())
print(df.isnull().sum())
df = df.drop_duplicates()
print(df.shape)

 # Removing outlier
def iqr_fun (series, k = 1.5):
    q1, q3 = series.quantile([0.25,0.75])
    iqr= q3-q1
    lower = q1-k * iqr
    upper = q3 + k * iqr 
    return lower, upper 

low_price , high_price = iqr_fun(df["Wedding_Price"])
low_duration , high_duration = iqr_fun(df["Wedding_Duration_Hours"])

df["Wedding_Price"] = df["Wedding_Price"].clip (lower= low_price, upper = high_price)
df["Wedding_Duration_Hours"] = df["Wedding_Duration_Hours"].clip (lower= low_duration, upper = high_duration)
# One-Hot Encoding
for col in ["Venue_Type", "Decoration_Level", "Catering_Type"]:
    df[col] = df[col].str.strip().str.title()

#  One-hot encoding manually with bool
# Venue_Type
df["Venue_Home"] = df["Venue_Type"] == "Home"
df["Venue_Hotel"] = df["Venue_Type"] == "Hotel"
df["Venue_Beach"] = df["Venue_Type"] == "Beach"

# Decoration_Level
df["Decoration_Low"] = df["Decoration_Level"] == "Low"
df["Decoration_Medium"] = df["Decoration_Level"] == "Medium"
df["Decoration_High"] = df["Decoration_Level"] == "High"

# Catering_Type
df["Catering_Basic"] = df["Catering_Type"] == "Basic"
df["Catering_Standard"] = df["Catering_Type"] == "Standard"
df["Catering_Premium"] = df["Catering_Type"] == "Premium"

# Drop original text columns
df.drop(columns=["Venue_Type", "Decoration_Level", "Catering_Type"], inplace=True)

# Convert bools to int (optional, for ML models)
bool_cols = df.select_dtypes(include="bool").columns
df[bool_cols] = df[bool_cols].astype(int)

print(df.head())
print("Columns now:", df.columns.tolist())

# Feature Engineering
df["Price_per_Guest"] = df["Wedding_Price"] / df["Number_of_Guests"]
df["Cost_per_Hour"] = df["Wedding_Price"] / df["Wedding_Duration_Hours"]
df["Guests_per_Hour"] = df["Number_of_Guests"] / df["Wedding_Duration_Hours"]
print(df.head())
print("Shape:", df.shape)

#Scaling

dont_scale = {"Wedding_Price"}  # target

numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.to_list()

exclude = [c for c in df.columns if c.startswith(("Venue_Type", "Catering_Type", "Decoration_Level"))]


num_features_scale = [c for c in numeric_cols if c not in dont_scale and c not in exclude]

print("Numeric features to scale:", num_features_scale)

scaler = StandardScaler()
df[num_features_scale] = scaler.fit_transform(df[num_features_scale])

print(df.head())

OUT_PATH = r"C:\Users\hp\Documents\sucad-khalif\ds-ml-bootcamp\submissions\sucad-khalif\ASSIGNMENT3\Wedding_clean_data.csv"
df.to_csv(OUT_PATH, index=False)
print("Saved to :", OUT_PATH)



