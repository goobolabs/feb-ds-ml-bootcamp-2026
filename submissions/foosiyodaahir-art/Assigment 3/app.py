
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler 
CSV_PATH = 'car_l3_dataset.CSV'
df = pd.read_csv(CSV_PATH)
# print(df.head(10))

# print(df.shape) 
# print(df.info) 
# print('show count of loccation:')
# print(df["Accidents"].value_counts (dropna=False))

df["Price"] = df["Price"].replace(r"[\$,]", "", regex=True).astype(float)
# print(df["Price"].head(10))
# print(df["Price"])
df["Location"] =df["Location"].replace({"Subrb": "Suburb", "??": pd.NA})

df["Odometer_km"] =df["Odometer_km"].fillna(df["Odometer_km"].median())
df["Doors"] =df["Doors"].fillna(df["Doors"].mode()[0])
df["Location"] =df["Location"].fillna(df["Location"].mode()[0])
# print(df.isnull().sum())

before =df.shape
df.drop_duplicates()
after =df.shape
# print("Before:",before,"After:", after)

def iqr_fun(Series, k=1.5):
    Q1 = Series.quantile(0.25)
    Q3 =Series.quantile(0.75)
    IQR =Q3 - Q1
    lower_bound = Q1 - k * IQR
    upper_bound = Q3 + k * IQR
    # return Series[(Series < lower_bound) | (Series > upper_bound)]
    return lower_bound, upper_bound

# low_price  , higth_price = iqr_fun(df["Price"])
# low_odometere, higth_odometre = iqr_fun(df["Odometer_km"])

# print("IQR Of Price:")
# print("low_price:", low_price, "higth_price:", higth_price)

# print("IQR Of Odometer_km:")

# print("low_odometere:", low_odometere, "higth_odometre:", higth_odometre)

# low_price , higth_price = iqr_fun(df["Price"])
# print("price after IQR clipping:")
# print(df["Price"].describe())

df =pd.get_dummies(df,columns=["Location"], drop_first=False) 
loc_cols = [c for c in df.columns if c.startswith("Location")]
df[loc_cols] = df[loc_cols].astype(int)

# print("One Hot Encoding:")
# print([c for c in df.columns if "Location"in c])

# print(df.head(10))

CURRENT_YEAR =2026
df["Car_Age"] = CURRENT_YEAR - df["Year"]

# print(df.head(10))

df["km_per_hour"]= df["Odometer_km"] / df["Car_Age"]

# print(df.head(10))

df["price_per_km"] = df["Price"] / df["Odometer_km"].replace(0, np.nan)

df["Log_price"] = np.log1p(df["Price"])

df["Accidents_Rate"] = df["Accidents"] / df["Car_Age"].replace(0, np.nan)
df["Is_Old"] = (df["Car_Age"] > 10).astype(int)
df["Is_Urban"] = (df["Location_City"] == 1).astype(int)

# print(df.head(10))
dont_Scale ={"Price", "Log_price"}
numeric_cols = df.select_dtypes(include=["Int64", "float64"]).columns.to_list()
# print(df.head(10))
exclude =[c for c in df.columns if c . startswith("Location_")]+ ["Is_Old", "Is_Urban"]
scale =[c for c in numeric_cols if c not in dont_Scale and c not in exclude]
scaler= StandardScaler()
df[scale] = scaler.fit_transform(df[scale])
# print("After Scaling:")
# print(df.head(10))

OUT_PATH = "cleaned_car_l3_dataset.CSV"
df.to_csv(OUT_PATH,)

# print("Saved to :", OUT_PATH)