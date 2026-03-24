# CAR DATA PREPROCESSING PIPELINE
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

print("STARTING CAR DATA PREPROCESSING...")

# STEP 1: Load & Inspect
print("\n--- STEP 1: LOAD & INSPECT ---")
df = pd.read_csv('car_l3_dataset.csv')
print(f"Dataset: {df.shape[0]} rows, {df.shape[1]} columns")
print("\nFirst 5 rows:")
print(df.head())
print("\nMissing values:")
print(df.isnull().sum())
print("\nLocation value counts:")
print(df['Location'].value_counts(dropna=False))

# STEP 2: Clean Price
print("\n--- STEP 2: CLEAN PRICE ---")
df['Price'] = df['Price'].astype(str).str.replace('[\$,]', '', regex=True).astype(float)
print(f"Price dtype: {df['Price'].dtype}")
print(f"Price range: ${df['Price'].min():,.2f} - ${df['Price'].max():,.2f}")

# STEP 3: Fix Location
print("\n--- STEP 3: FIX LOCATION ---")
df['Location'] = df['Location'].replace({'Subrb':'Suburb', '??':np.nan})

# STEP 4: Impute Missing Values
print("\n--- STEP 4: IMPUTE MISSING VALUES ---")
df['Odometer_km'].fillna(df['Odometer_km'].median(), inplace=True)
df['Doors'].fillna(int(df['Doors'].mode()[0]), inplace=True)
df['Location'].fillna(df['Location'].mode()[0], inplace=True)
df['Doors'] = df['Doors'].astype(int)

# STEP 5: Remove Duplicates
print("\n--- STEP 5: REMOVE DUPLICATES ---")
initial_rows = len(df)
df.drop_duplicates(inplace=True)
final_rows = len(df)
print(f"Duplicates removed: {initial_rows - final_rows}")

# STEP 6: Outlier Capping
print("\n--- STEP 6: OUTLIER CAPPING ---")
for col in ['Price', 'Odometer_km']:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    df[col] = df[col].clip(lower, upper)
    print(f"{col} capped: ${lower:,.2f}-${upper:,.2f}" if col == 'Price' else f"{col} capped: {lower:,.0f}-{upper:,.0f} km")

# STEP 7: One-Hot Encoding
print("\n--- STEP 7: ONE-HOT ENCODING ---")
df = pd.get_dummies(df, columns=['Location'], prefix='Location')
print(f"New columns: {[col for col in df.columns if 'Location_' in col]}")

# STEP 8: Feature Engineering
print("\n--- STEP 8: FEATURE ENGINEERING ---")
df['CarAge'] = 2026 - df['Year']
df['Km_per_year'] = df['Odometer_km'] / (df['CarAge'] + 1e-6)
df['Is_Urban'] = ((df.get('Location_City', 0) == 1) | (df.get('Location_Suburb', 0) == 1)).astype(int)
df['LogPrice'] = np.log1p(df['Price'])
print("Added: CarAge, Km_per_year, Is_Urban, LogPrice")

# STEP 9: Feature Scaling
print("\n--- STEP 9: FEATURE SCALING ---")
cols_to_scale = [col for col in ['Odometer_km', 'Doors', 'Accidents', 'Year', 'CarAge', 'Km_per_year'] if col in df.columns]
scaler = StandardScaler()
df[cols_to_scale] = scaler.fit_transform(df[cols_to_scale])
print(f"Scaled columns: {cols_to_scale}")

# STEP 10: Save & Final Checks
print("\n--- STEP 10: FINAL CHECKS & SAVE ---")
print(f"Final shape: {df.shape[0]} rows, {df.shape[1]} columns")
print(f"Missing values: {df.isnull().sum().sum()}")
df.to_csv('car_l3_clean_ready.csv', index=False)
print(" File saved: car_l3_clean_ready.csv")
print(" PROCESSING COMPLETE!")
