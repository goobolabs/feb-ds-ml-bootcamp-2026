import pandas as pd
from sklearn.preprocessing import StandardScaler
import numpy as np

CSV_PAT="./data_car_.csv"
df=pd.read_csv(CSV_PAT)

# removing the string at price
df["Price"]=df["Price"].replace(r"[\$,]","", regex=True).astype(float)
# print(df.head(30))
# print(df.shape)
# print(df.info())
# print(df.isnull().sum())

# print(df["Price"].skew())

# filling the missing values location
df["Location"] = df["Location"].str.strip()
df["Location"] = df["Location"].replace("??", np.nan)
df["Location"]=df["Location"].fillna(df["Location"].mode()[0])
# print(df.head(60))

# filling the missing values Odometer_km
df["Odometer_km"]=df["Odometer_km"].fillna(df["Odometer_km"].median())

df=df.drop_duplicates()

def iqr_fun(column, k=1.5):
  q1, q3=column.quantile([0.25, 0.75])
  iqr=q3-q1

  lower=q1-k *iqr
  upper=q3+k *iqr
  return lower, upper


low_price_Price,high_price_Price=iqr_fun(df["Price"])
low_price_Doors,high_price_Doors=iqr_fun(df["Doors"])
low_price_Odometer_km,high_price_Odometer_km=iqr_fun(df["Odometer_km"])
low_price_Accidents,high_price_Accidents=iqr_fun(df["Accidents"])

df["Price"]=df["Price"].clip(lower=low_price_Price,upper=high_price_Price)
df["Doors"]=df["Doors"].clip(lower=low_price_Doors,upper=high_price_Doors)
df["Odometer_km"]=df["Odometer_km"].clip(lower=low_price_Odometer_km,upper=high_price_Odometer_km)
df["Accidents"]=df["Accidents"].clip(lower=low_price_Accidents,upper=high_price_Accidents)


# One hot encoding
df=pd.get_dummies(df, columns=["Location"], drop_first=False)


dont_scale=["Location"]
numeric_cols=df.select_dtypes(include=["float64", "int64"]).columns.to_list()
numeric_features_to_scale=[c for c in numeric_cols if c not in dont_scale]
scaler=StandardScaler()
df[numeric_features_to_scale]=scaler.fit_transform(df[numeric_features_to_scale])
OUT_PATH="car_data_CLean.csv"
df.to_csv(OUT_PATH)
