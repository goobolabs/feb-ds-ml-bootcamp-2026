import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# STEP 1: Load & Inspect
print("- Step 1: Loading Data -")
df = pd.read_csv('car_l3_dataset.csv')
print(f"Initial Shape: {df.shape}")
print("\nMissing Counts Before:\n", df.isnull().sum())

# STEP 2: Clean Target Formatting (Price)
print("\n- Step 2: Cleaning Price -")
# Remove currency symbols and commas, then convert to float
df['Price'] = df['Price'].astype(str).str.replace('$', '', regex=False).str.replace(',', '', regex=False).astype(float)
print(f"Price Skewness: {df['Price'].skew():.2f}")

# STEP 3: Fix Category Errors before Imputation
print("\n - Step 3: Fixing Location Typos -")
df['Location'] = df['Location'].str.strip().str.capitalize()
# Mapping specific typos and unknowns found in the inspection
typo_map = {'Subrb': 'Suburb', 'Sub-urb': 'Suburb', 'Rrurall': 'Rural', '??': np.nan, 'Unknown': np.nan}
df['Location'] = df['Location'].replace(typo_map)

# STEP 4: Impute Missing Values
print("\n- Step 4: Imputing Missing Values -")
# Numerical: Median (Robust to outliers)
df['Odometer_km'] = df['Odometer_km'].fillna(df['Odometer_km'].median())
# Categorical/Discrete: Mode
df['Doors'] = df['Doors'].fillna(df['Doors'].mode()[0])
df['Accidents'] = df['Accidents'].fillna(df['Accidents'].mode()[0])
df['Location'] = df['Location'].fillna(df['Location'].mode()[0])

# STEP 5: Remove Duplicates
print("\n- Step 5: Removing Duplicates -")
before_dupes = df.shape[0]
df = df.drop_duplicates()
print(f"Rows removed: {before_dupes - df.shape[0]}")

# STEP 6: Outliers (IQR Capping)
print("\n- Step 6: IQR Capping -")
for col in ['Price', 'Odometer_km']:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower, upper = Q1 - 1.5 * IQR, Q3 + 1.5 * IQR
    df[col] = df[col].clip(lower, upper)
    print(f"{col} bounds: [{lower:.1f}, {upper:.1f}]")

# STEP 7: One-Hot Encode Categorical(s)
print("\n- Step 7: One-Hot Encoding -")
df = pd.get_dummies(df, columns=['Location'], prefix='Loc', dtype=int)

# STEP 8: Feature Engineering
print("\n- Step 8: Feature Engineering -")
current_year = 2026
df['CarAge'] = current_year - df['Year']
df['Km_per_year'] = df['Odometer_km'] / (df['CarAge'].replace(0, 1))
df['Is_Urban'] = (df['Loc_City'] == 1).astype(int)
df['LogPrice'] = np.log1p(df['Price'])

# STEP 9: Feature Scaling (X only)
print("\n- Step 9: Scaling Continuous Features -")
scaler = StandardScaler()
cont_features = ['Odometer_km', 'Doors', 'Accidents', 'Year', 'CarAge', 'Km_per_year']
df[cont_features] = scaler.fit_transform(df[cont_features])

# STEP 10: Final Checks & Save
print("\n- Step 10: Final Checks & Save -")
print(f"Final Missing Values: {df.isnull().sum().sum()}")
df.to_csv('car_l3_clean_ready.csv', index=False)
print("SUCCESS: car_l3_clean_ready.csv saved.")
