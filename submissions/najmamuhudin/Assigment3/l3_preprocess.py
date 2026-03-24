#Load Pakeges

# packages
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

#versions
print("NumPy version:", np.__version__)
print("Pandas version:", pd.__version__)
print("Scikit-learn version:", sklearn.__version__)

#Step one
# Read Data
#csv_path
CSV_PATH ='car_l3_dataset.csv'

#Read data
df = pd.read_csv(CSV_PATH)
#read first 10
print(df.head(10))

#shape data
print("Shape data:",df.shape)

#information
print("information:",df.info())

#missing value
print("missing value:",df.isnull().sum())

#location
print("Location Counts:",df["Location"].value_counts(dropna=False))

#Step two
#Clean Target Formatting (Price)

#remove sign ?,
df["Price"]=df["Price"].replace(r"[\$,]", "", regex=True).astype(float)
#check data
print(df.head(10))

#Step three
#Fix Category Errors before Imputation
#the way that fix
df["Location"]=df["Location"].replace({"Subrb":"Suburb", "??":pd.NA})

#after fix
print("\nLocation counts after type/unknown fix:")
print(df["Location"].value_counts(dropna=False))

#Step four
#Impute Missing Values
#the way cleaned
df["Odometer_km"]=df["Odometer_km"].fillna(df["Odometer_km"].median())
df["Doors"]=df["Doors"].fillna(df["Doors"].mode()[0])
df["Location"]=df["Location"].fillna(df["Location"].mode()[0])

#after cleaned
print(df.isnull().sum())

#Step Five
#Remove Duplicates
#remove duplicate
before=df.shape
df=df.drop_duplicates()
after=df.shape
print("Before:",before, "After:",after)

#Step six
#Outliers

# Outlier Handling using IQR

# Output: lower and upper bounds for outlier capping
def iqr_fun(series, k=1.5):
    q1, q3 = series.quantile([0.25, 0.75])
    iqr = q3 - q1                           
    lower = q1 - k * iqr                      
    upper = q3 + k * iqr                      
    return lower, upper

# Compute IQR bounds for Price and Odometer_km
price_lower, price_upper = iqr_fun(df["Price"])
odo_lower, odo_upper = iqr_fun(df["Odometer_km"])

# Print the calculated bounds for reference
print("\nIQR bounds for Price:")
print("Lower:", price_lower, "Upper:", price_upper)

print("\nIQR bounds for Odometer_km:")
print("Lower:", odo_lower, "Upper:", odo_upper)

# This reduces the influence of extreme outliers without removing rows
df["Price"] = df["Price"].clip(lower=price_lower, upper=price_upper)
df["Odometer_km"] = df["Odometer_km"].clip(lower=odo_lower, upper=odo_upper)

# Print summary statistics after capping to verify changes
print("\nPrice after IQR clipping:")
print(df["Price"].describe())

print("\nOdometer_km after IQR clipping:")
print(df["Odometer_km"].describe())

#step seven.
df = pd.get_dummies(df, columns=["Location"], drop_first=False,dtype="int")
# print("One Hot Encode of Location:")
# print([c for c in df.columns if c.startswith("Location")])

#Step eight
#Feature Engineering
#car year
CURRENT_YEAR=2026
df["Car_Age"]=CURRENT_YEAR -df["Year"]

#  km per year 
df["km_per_year"]= df["Odometer_km"] / df["Car_Age"].replace(0, np.nan)

# Price per-km
df["Price_per_km"]= df["Price"] / df["Odometer_km"].replace(0, np.nan)  

# Log-Price
df["Log_Price"] = np.log1p(df["Price"])

#accidents of car age
df["Accident_Rate"] = df["Accidents"] / df["Car_Age"].replace(0, np.nan)

# Is the car older than 15 years?
df["Is_OldCar"] = (df["Car_Age"] > 15).astype(int)

# Is the car located in an urban area (City)?
df["Is_Urban"] = df.get("Location_City", pd.Series([0]*len(df))).astype(int)

print(df[["Car_Age", "km_per_year", "Price_per_km", "Log_Price", "Accident_Rate", "Is_OldCar", "Is_Urban"]].head(10))

#Step nine
#Feature Scaling
dont_scale = ["Price", "Log_Price"]
numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.to_list()
exclude = [c for c in df.columns if c.startswith("Location_")]+ ["is_OldCar", "Is_Urban"]
num_feature_to_scale = [c  for c  in numeric_cols if c not in dont_scale and c not in exclude]
scaler = StandardScaler()
df[num_feature_to_scale] = scaler.fit_transform(df[num_feature_to_scale])
print(df[num_feature_to_scale].head()) 

#Step ten
#Final ChecksandSave
print("\n==FINAL HEAD==")
print(df.head())

print("\n==FINAL INFO==")
print(df.info())
