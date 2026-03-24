import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

# ===============================
# STEP 1: Load & Inspect
# ===============================

CSV_FILE_PATH = "submissions/Abdisalaam-12/Assignment-Three/car_l3_dataset.csv"
df = pd.read_csv(CSV_FILE_PATH)

# print(df.head(10))
# print(df.shape)
# print(df.info())
# print("missiing values")
# print(df.isnull().sum())
# print(df['Location'].value_counts( dropna=False))

# ===============================
# STEP 2: Clean Target Formatting (Price)
# ===============================

df["Price"]= df["Price"].replace(r"[\$,]", '', regex=True).astype(float)

# print("Price dtype:", df["Price"].dtype)
# print("Price skewness:", df["Price"].skew())

# ===============================
# STEP 3: Fix Category Errors before  Imputation
# ===============================

df["Location"]=df["Location"].replace({"Subrb": "Suburb","??":np.NaN })

# print(" ==== Location counts After fixing ====")
# print(df['Location'].value_counts( dropna=False))

# ===============================
# STEP 4: Impute Missing Values
# ===============================

df["Odometer_km"]=df["Odometer_km"].fillna(df["Odometer_km"].median())
df["Doors"]=df["Doors"].fillna(df["Doors"].mode()[0])
df["Location"]=df["Location"].fillna(df["Location"].mode()[0])

# print(" ==== Missing values after fillig====")
# print(df.isnull().sum())

# ===============================
# STEP 5: Removing  Duplicates
# ===============================

before= df.shape
df= df.drop_duplicates()
after= df.shape
# print("duplicates removed " , before, " " , after)

# ===============================
# STEP 6: Outliers — IQR Capping
# ==============================

def iqr_bounds( series, k=1.5):
    q1, q3 = series.quantile([0.25, 0.75])
    iqr = q3-q1
    lower_bound = q1 - k * iqr
    upper_bound = q3 + k * iqr
    return   lower_bound , upper_bound

price_low, price_high= iqr_bounds(df["Price"])
Odometer_low, Odometer_high= iqr_bounds(df["Odometer_km"])

df["Price"]= df["Price"].clip(lower=price_low, upper=price_high)
df["Odometer_km"]= df["Odometer_km"].clip(lower=Odometer_low, upper=Odometer_high)

# print(" ====  price summary after iqr ====")
# print(df["Price"].describe())

# print(" ====  Odometer  summary after iqr ====")
# print(df["Odometer_km"].describe())

# ===============================
# STEP 7: one hot encoding
# ===============================
df= pd.get_dummies(df, columns=["Location"], drop_first=False, dtype="int")
# print(" location dummy columns")
# print ([c for c in df.columns if c.startswith("Location_")])
# print(df.head(10))

# ===============================
# STEP 8: featture engineering
# ===============================
# Car age in years
current_year= 2026
df["Car_Age"]= current_year - df["Year"]
#  km per year 
df["km_per_year"]= df["Odometer_km"] / df["Car_Age"].replace(0, np.nan)  
# Price per km
df["Price_per_km"]= df["Price"] / df["Odometer_km"].replace(0, np.nan)  
# Log transformation of Price
df["LogPrice"] = np.log1p(df["Price"])
# ratio of accidents to car age
df["Accident_Rate"] = df["Accidents"] / df["Car_Age"].replace(0, np.nan)
# Is the car older than 15 years?
df["Is_OldCar"] = (df["Car_Age"] > 15).astype(int)
# Is the car located in an urban area (City)?
df["Is_Urban"] = df.get("Location_City", pd.Series([0]*len(df))).astype(int)
# print(" ====  new features summary ====")
# print(df[["Car_Age", "km_per_year", "Price_per_km", "LogPrice", "Accident_Rate", "Is_OldCar", "Is_Urban"]].head(10))

# ===============================
# STEP 9:  Features Scaling (only x features, not target)
dont_scale = ["Price", "LogPrice"]
numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.to_list()

exclude = [c for c in df.columns if c.startswith("Location_")]+ ["is_OldCar", "Is_Urban"]
scale_cols = [c  for c  in numeric_cols if c not in dont_scale and c not in exclude]
scaler = StandardScaler()
df[scale_cols] = scaler.fit_transform(df[scale_cols])
# print(" ====  scaled features vlaues  ====")
# print(df[scale_cols].head())


# ===============================
#  step 10 : final checks & saves
## ===============================

print(" === Final info === ")
print(df.info())
print(" === Final missing values ===")
print(df.isnull().sum())
print(" ===Final describe === ")
print(df.describe())

OUT_PATH = "submissions/Abdisalaam-12/Assignment-Three/car_l3_clean_ready.csv"
df.to_csv(OUT_PATH, index=False)
print( " Data preprocessing complete. Cleaned data saved to:", OUT_PATH)