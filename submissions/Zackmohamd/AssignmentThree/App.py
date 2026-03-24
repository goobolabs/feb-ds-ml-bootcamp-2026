import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

CVS_FILE = 'car_l3_dataset.csv'

df = pd.read_csv(CVS_FILE)

# 1. Load & Inspect Data
# === INITIAL SNAPSHOT ===
print("\n=== INITIAL HEAD ===")
print(df.head())

# print(df.head(10))
# print(df.info())

# print('Shape of the DataFrame:', df.shape)
#print("\n=== INITIAL MISSING VALUES ===")
print(df.isnull().sum())

# print(df["Location"].value_counts(dropna=False))

# 2. Cleaning Target formatting
# Remove $ and , from Price and convert to float   
df['Price'] =df['Price'].replace(r'[\$,]', '', regex=True).astype(float) 
# print(df['Price'].head(10))
# print(df['Price'].skew())

# 3. Fix Category Errors before Imputation
df["Location"] = df["Location"].replace({"Subrb": "Suburb", "??": pd.NA})

# print("Value counts for Location column:")
# print(df["Location"].value_counts(dropna=False))


# 4 Impute Missing Values
df['Odometer_km'] = df['Odometer_km'].fillna(df['Odometer_km'].mode()[0])

df['Doors'] = df['Doors'].fillna(df['Doors'].median()) 

df['Location'] = df['Location'].fillna(df['Location'].mode()[0])
# print(df.isnull().sum())

#5. Removing Duplicates
before = df.shape

df = df.drop_duplicates()
after = df.shape
# print("Before removing duplicates:", before, "After removing duplicates:", after)


#6. Outlier Detection using IQR
def iqr_function(series,k=1.5):
   q1, q3 = series.quantile([0.25, 0.75])
   iqr = q3 - q1
   lower_bound = q1 - k * iqr  
   upper_bound = q3 + k * iqr
   return lower_bound, upper_bound
low_price, up_price = iqr_function(df['Price'])
low_odometer, up_odometer = iqr_function(df['Odometer_km'])
# print("IQE PRICE: ")
# print("Low Price: ", low_price,"Upper Price: ", up_price)
# print("IQE OF ODOMETER: ")
# print("low Odometer_km: ", low_odometer,"Upper Odometer_km: ", up_odometer)

df['Price'] = df['Price'].clip(lower=low_price, upper=up_price)
df['Odometer_km'] = df['Odometer_km'].clip(lower=low_odometer, upper=up_odometer)

# print("After clipping:")
# print("Price: ", df['Price'].describe())
# print("Odometer_km: ", df['Odometer_km'].describe())

# 7. One-Hot Encode Categorical(s)
df = pd.get_dummies(df, columns=['Location'], drop_first=False, dtype=int)
print("One Hot Encoded Location")

CURRENT_YEAR=2025

df["CarAge"] = CURRENT_YEAR - df["Year"]

df["KmPerYear"] = df["Odometer_km"] / df["CarAge"].replace(0,np.nan)
# print("Added CarAge and KmPerYear features")
# print(df.head(10))
df["AccidentsPerYear"] = df["Accidents"] / df["CarAge"].replace(0,np.nan)
df["had_accidents"] = (df["Accidents"] > 0).astype(int)
# print(df.head(10))

df["log_Price"] = np.log1p(df["Price"]) 
# Check new features
print("\n=== FEATURE ENGINEERING SAMPLE ===")
print(df[[ "CarAge", "AccidentsPerYear", "had_accidents", "KmPerYear", "log_Price"]].head())

#9. Feature Scaling
doNotScale = ["Price", "log_Price"]
numiricCol = df.select_dtypes(include = ("int64", "float64")).columns.to_list()
excludedFeatures = [col for col in df.columns if col.startswith("Location_")] + ["Is_City", "had_accidents"]
featuresToScale = [col for col in numiricCol if col not in doNotScale + excludedFeatures]
# print("Features to scale:", featuresToScale) 

scaler = StandardScaler()
df[featuresToScale] = scaler.fit_transform(df[featuresToScale])
# Check scaled features
print("\n=== SCALED FEATURES SAMPLE ===")
print(df[featuresToScale].head())

# FINAL SNAPSHOt
print("\n=== FINAL HEAD ===")
print(df.head())

print("\n=== FINAL INFO ===")
print(df.info())

print("\n=== FINAL MISSING VALUES ===")
print(df.isnull().sum())

#10. Save
OUT_PATH = "Car_l3_clean_dataset.csv"
df.to_csv(OUT_PATH, index=False)

print(f"\nData cleaning and feature engineering completed. Cleaned dataset saved to '{OUT_PATH}'.")


