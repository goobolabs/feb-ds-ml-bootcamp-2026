import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler

CSV_PATH  =  'car13.csv'

df   = pd.read_csv(CSV_PATH )

# initial
print("\n === INITIAL HEAD  ===")
print(df.head())

print("\n === INITIAL INFO  ===")
print(df.info())

print("\n === INITIAL MISSING VALUES ===")
print(df.isnull())

# 2 clean target
df["Price"] = df["Price"] .replace(r"[\$,]" , "" , regex=True).astype(float)

# 3 fix categoral isuues
df["Location"] = df["Location"] .replace({"Subrb": "Suburb" , "??" : pd.NA})

#  4 imput mising value

df["Odometer_km"] = df["Odometer_km"].fillna(df["Odometer_km"].median())
df["Doors"] = df["Doors"].fillna(df["Doors"].mode()[0])
df["Location"] = df["Location"].fillna(df["Location"].mode()[0])

# print(df.isnull().sum())

# 5 remove duplicates

before  = df.shape

df  = df.drop_duplicates ()

after  = df.shape
# print("Before: " , before ,"After: " , after)

# 6 IQR

def iqr_fun(series, k=1.5):
    q1, q3 = series.quantile([0.25, 0.75])
    iqr = q3 - q1
    lower = q1 - k * iqr
    upper = q3 + k * iqr
    return lower, upper

low_price, high_price = iqr_fun(df["Price"])
low_size,  high_size  = iqr_fun(df["Odometer_km"])

# print("IQR of Price is: ")

# print("Low_Price : ",low_price , "high_price: ",high_price)

# print("IQR of Size is: ")

# print("Low_Size : ",low_size, "high_Size: ",high_size)


df["Price"]     = df["Price"].clip(lower=low_price, upper=high_price)
df["Odometer_km"] = df["Odometer_km"].clip(lower=low_size,  upper=high_size)


# print("Price after IQR clipping : ")
# print(df["Price"].describe())

# 7 one hot encoding
df  = pd.get_dummies(df,columns = ["Location"] , drop_first =False, dtype="int") 
# print ("one hot encoding  :")
# print([c for c in df.columns if c.startswith("Location")])
# print(df.head())


# 8 feature engineering

CURRENT_YEAR  = 2026
df["age_of_car"]  = CURRENT_YEAR - df["Year"]
df["odometer_per_year"]  = df["Odometer_km"] / df["age_of_car"] 
df["log_price"] = np.log1p (df["Price"])

# print(df.head())


# scalling numeric
dont_scale =  {"Price" , "log_price"}
numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.to_list()
exclude = [c for c in df.columns if c.startswith("Location_")] 
num_features_to_scale = [c for c in numeric_cols if c not in dont_scale and c not in exclude]

scaler = StandardScaler()
df[num_features_to_scale] = scaler.fit_transform(df[num_features_to_scale])
print(df[num_features_to_scale].head()) 


# === FINAL ===
print("\n=== FINAL HEAD ===")
print(df.head())

print("\n=== FINAL INFO ===")
print(df.info())

print("\n=== FINAL MISSING VALUES ===")
print(df.isnull().sum())

# 10 Save
OUT_PATH = "car_13_clean_ready.csv"
df.to_csv(OUT_PATH, index=False)  


