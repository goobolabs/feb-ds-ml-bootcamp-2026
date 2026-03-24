import pandas as pd
import numpy as np

# STEP 1: Load dataset
df = pd.read_csv("dataset.csv")

print("First 10 rows:")
print(df.head(10))
print("\nShape:", df.shape)
print("\nMissing values:\n", df.isnull().sum())

# STEP 2: Clean Price column
df["Price"] = df["Price"].replace("[$,]", "", regex=True)
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")

print("\nPrice datatype:", df["Price"].dtype)

# STEP 3: Fix Location text errors
df["Location"] = df["Location"].astype(str).str.strip().str.title()
df["Location"] = df["Location"].replace({
    "Subrb": "Suburb",
    "??": np.nan
})

print("\nLocation values after cleaning:")
print(df["Location"].value_counts(dropna=False))

# STEP 4: Impute missing values
df["Odometer_km"] = df["Odometer_km"].fillna(df["Odometer_km"].median())
df["Doors"] = df["Doors"].fillna(df["Doors"].mode()[0])
df["Accidents"] = df["Accidents"].fillna(df["Accidents"].mode()[0])
df["Location"] = df["Location"].fillna(df["Location"].mode()[0])

print("\nMissing values after imputation:\n", df.isnull().sum())

# STEP 5: Remove duplicates
before = df.shape[0]
df = df.drop_duplicates()
after = df.shape[0]

print("\nDuplicates removed:", before - after)

# STEP 6: Outlier capping (IQR method)
def cap_outliers(column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    df[column] = df[column].clip(lower, upper)

cap_outliers("Price")
cap_outliers("Odometer_km")

print("\nOutliers capped.")

# STEP 7: One-hot encode Location
df = pd.get_dummies(df, columns=["Location"], dtype=int)

print("\nEncoded columns:")
print([col for col in df.columns if "Location_" in col])

# STEP 8: Feature Engineering
current_year = 2026
df["CarAge"] = current_year - df["Year"]
df["Km_per_year"] = df["Odometer_km"] / df["CarAge"].replace(0, 1)
df["LogPrice"] = np.log(df["Price"] + 1)

print("\nFeature engineering completed.")

# STEP 9: Final check
print("\nFinal missing values:\n", df.isnull().sum())
print("\nDataset summary:")
print(df.describe())

# STEP 10: Save dataset
df.to_csv("car_l3_clean_ready.csv", index=False)

print("\nData processing completed successfully.")
