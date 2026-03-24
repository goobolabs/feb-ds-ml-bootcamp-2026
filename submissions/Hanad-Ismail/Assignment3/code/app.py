from datetime import datetime
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("car_l3_dataset.csv")

##removing $ sign and change the data type to float
df["Price"] = df["Price"].replace(r"[\$,]" , "",regex = True).astype(float)
df["Location"] = df["Location"].replace({"Subrb" : "Suburb" , "??" : pd.NA})

#filling missing values with median and mode
df["Odometer_km"] = df["Odometer_km"].fillna(df["Odometer_km"].median())
df["Doors"] = df["Doors"].fillna(df["Doors"].mode()[0])
df["Location"] = df["Location"].fillna(df["Location"].mode()[0])

#checking duplicates
#print(df.duplicated().sum())
#print(df.shape)

#dropping duplicates
df = df.drop_duplicates()

def iqr_func(series , k =1.5):
    q1, q3 = series.quantile([0.25 , 0.75])
    iqr = q3 - q1
    lower = q1 - k * iqr
    upper = q3 + k * iqr
    return lower, upper

low_price , high_price = iqr_func(df["Price"])
low_Odometer_km , high_Odometer_km = iqr_func(df["Odometer_km"])

df["Price"] = df["Price"].clip(lower=low_price, upper = high_price )
df["Odometer_km"] = df["Odometer_km"].clip(lower = low_Odometer_km , upper = high_Odometer_km)

#print(df["Price"].describe())

df = pd.get_dummies(df, columns = ["Location"] , drop_first = False , dtype = "int")
#print([c for c in df.columns if c.startswith ("Location")])

#faeture Engineering
CURRENT_YEAR = datetime.now().year
df["Car_age"] = CURRENT_YEAR - df["Year"]
df["Is_Modern"] = df["Year"] >= 2015
df["High_Mileage"] = df["Odometer_km"] > 150000
df["Is_city"] = df["Location_City"].astype(int)
df["Log_Price"] = np.log1p(df["Price"])

#feature scaling
dont_scale = {"Price" ,"Log_Price"}
numeric_cols = df.select_dtypes(include = ["float64" , "int64"]).columns.to_list()
Exclude = [c for c in df.columns if c.startswith("Location")] + ["Is_city"]

num_features_to_scale = [c for c in numeric_cols if c not in dont_scale and c  not in Exclude]
scaler = StandardScaler()
df[num_features_to_scale] = scaler.fit_transform(df[num_features_to_scale])

print(df.head())
OUT_PATH = 'car_clean_data.csv'
df.to_csv(OUT_PATH)
