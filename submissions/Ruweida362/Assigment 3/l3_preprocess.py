import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# STEP 1: LOAD & INSPECT DATA

df = pd.read_csv(
    r"d:/DS & ML/ds-ml-bootcamp/submissions/Ruweida362/Assigment 3/car_l3_dataset.csv"
)
# print(df.head(10))
# print(df.shape)
# print(df.info())
# print("missiing values")
# print(df.isnull().sum())
# print(df['Location'].value_counts( dropna=False))


# STEP 2: CLEAN PRICE COLUMN

df["Price"] = df["Price"].replace(r"[\$,]", "", regex=True).astype(float)

# STEP 3: FIX CATEGORY ERRORS

df["Location"] = df["Location"].replace({
    "Subrb": "Suburb",
    "??": np.nan
})

# STEP 4: IMPUTE MISSING VALUES

df["Odometer_km"] = df["Odometer_km"].fillna(df["Odometer_km"].median())
df["Doors"] = df["Doors"].fillna(df["Doors"].mode()[0])
df["Location"] = df["Location"].fillna(df["Location"].mode()[0])

print("Missing values after imputation:")
print(df.isna().sum())

# STEP 5: REMOVE DUPLICATES

shape_before = df.shape
df = df.drop_duplicates()
shape_after = df.shape

print("Shape before:", shape_before)
print("Shape after:", shape_after)
print("Duplicates removed:", shape_before[0] - shape_after[0])

# STEP 6: OUTLIER CAPPING (IQR)

def iqr_cap(series, k=1.5):
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1
    lower = q1 - k * iqr
    upper = q3 + k * iqr
    return lower, upper

price_low, price_high = iqr_cap(df["Price"])
odo_low, odo_high = iqr_cap(df["Odometer_km"])

df["Price"] = df["Price"].clip(lower=price_low, upper=price_high)
df["Odometer_km"] = df["Odometer_km"].clip(lower=odo_low, upper=odo_high)

# STEP 7: ONE-HOT ENCODING

df = pd.get_dummies(df, columns=["Location"], drop_first=False)

location_cols = [col for col in df.columns if col.startswith("Location_")]
print("New dummy columns created:")
print(location_cols)

# STEP 8: FEATURE ENGINEERING

CURRENT_YEAR = 2025

# 1. Car Age
df["Car_Age"] = CURRENT_YEAR - df["Year"]
df["Car_Age"] = df["Car_Age"].replace(0, 1)

# 2. Kilometers per year
df["km_per_year"] = df["Odometer_km"] / df["Car_Age"]

# 3. Price per km
df["Price_per_km"] = df["Price"] / (df["Odometer_km"] + 1)

# 4. Accident rate
df["Accident_Rate"] = df["Accidents"] / df["Car_Age"]

# 5. Old car indicator
df["Is_OldCar"] = np.where(df["Car_Age"] > 10, 1, 0)

# 6. Urban indicator
df["Is_Urban"] = np.where(
    (df.get("Location_City", 0) == 1) |
    (df.get("Location_Suburb", 0) == 1),
    1,
    0
)

# 7. Log price
df["LogPrice"] = np.log(df["Price"] + 1)

print(df[
    [
        "Car_Age",
        "km_per_year",
        "Price_per_km",
        "LogPrice",
        "Accident_Rate",
        "Is_OldCar",
        "Is_Urban"
    ]
].head())

# STEP 9: FEATURE SCALING (X ONLY)

scaler = StandardScaler()
scale_cols = ["Odometer_km", "Car_Age", "km_per_year"]

df[scale_cols] = scaler.fit_transform(df[scale_cols])

print("Scaled features:", scale_cols)
print(df[scale_cols].head())

# STEP 10: FINAL CHECKS & SAVE

print("\nFinal dataset info:")
print(df.info())

print("\nFinal missing values:")
print(df.isna().sum())

df.to_csv(
    r"d:/DS & ML/ds-ml-bootcamp/submissions/Ruweida362/Assigment 3/car_l3_clean_ready.csv",
    index=False
)

print("\nDataset saved as car_l3_clean_ready.csv")
