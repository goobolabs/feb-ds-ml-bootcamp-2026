"""
Lesson 3 - Data Preprocessing Assignment
Date: February 22, 2026

This script implements a complete preprocessing pipeline for the car price dataset.
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import warnings
warnings.filterwarnings('ignore')

print("="*80)
print("LESSON 3 - DATA PREPROCESSING PIPELINE")
print("="*80)

# STEP 1: LOAD & INSPECT
print("\n" + "="*80)
print("STEP 1: LOAD & INSPECT")
print("="*80)

df = pd.read_csv('car_l3_dataset.csv')

print("\nFirst 10 rows:")
print(df.head(10))

print(f"\nShape: {df.shape}")
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

print("\nData Info:")
print(df.info())

print("\nMissing Values Count:")
print(df.isnull().sum())

print("\nLocation Value Counts:")
print(df['Location'].value_counts(dropna=False))

print("\nKey Issues Identified:")
print("- Price has mixed formats (strings with $ and commas, plain numbers)")
print("- Missing values in Odometer_km, Doors, Accidents, Location")
print("- Location has typos ('Subrb' instead of 'Suburb', '??' for unknown)")
print("- Potential outliers in Price and Odometer_km")
print("- Possible duplicate rows")


# STEP 2: CLEAN TARGET FORMATTING (Price)
print("\n" + "="*80)
print("STEP 2: CLEAN TARGET FORMATTING (Price)")
print("="*80)

df['Price'] = df['Price'].astype(str).str.replace('$', '', regex=False)
df['Price'] = df['Price'].str.replace(',', '', regex=False)
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')

print(f"\nPrice dtype after cleaning: {df['Price'].dtype}")
print(f"Price statistics:")
print(df['Price'].describe())
print(f"\nSkewness: {df['Price'].skew():.4f}")

# STEP 3: FIX CATEGORY ERRORS BEFORE IMPUTATION
print("\n" + "="*80)
print("STEP 3: FIX CATEGORY ERRORS BEFORE IMPUTATION")
print("="*80)

print("\nBefore fixing:")
print(df['Location'].value_counts(dropna=False))

df['Location'] = df['Location'].str.strip().str.title()
df['Location'] = df['Location'].replace({'Subrb': 'Suburb', '??': np.nan, '': np.nan})

print("\nAfter fixing:")
print(df['Location'].value_counts(dropna=False))
print(f"\nMissing values in Location: {df['Location'].isnull().sum()}")

# STEP 4: IMPUTE MISSING VALUES
print("\n" + "="*80)
print("STEP 4: IMPUTE MISSING VALUES")
print("="*80)

print("\nMissing values before imputation:")
print(df.isnull().sum())

odometer_median = df['Odometer_km'].median()
df['Odometer_km'].fillna(odometer_median, inplace=True)
print(f"\nOdometer_km: Filled with median = {odometer_median:.2f}")

doors_mode = df['Doors'].mode()[0]
df['Doors'].fillna(doors_mode, inplace=True)
print(f"\nDoors: Filled with mode = {doors_mode}")

accidents_mode = df['Accidents'].mode()[0]
df['Accidents'].fillna(accidents_mode, inplace=True)
print(f"\nAccidents: Filled with mode = {accidents_mode}")

location_mode = df['Location'].mode()[0]
df['Location'].fillna(location_mode, inplace=True)
print(f"\nLocation: Filled with mode = '{location_mode}'")

print("\nMissing values after imputation:")
print(df.isnull().sum())


# STEP 5: REMOVE DUPLICATES
print("\n" + "="*80)
print("STEP 5: REMOVE DUPLICATES")
print("="*80)

shape_before = df.shape
df_before_count = len(df)

df = df.drop_duplicates()

shape_after = df.shape
df_after_count = len(df)
rows_removed = df_before_count - df_after_count

print(f"\nShape before: {shape_before}")
print(f"Shape after:  {shape_after}")
print(f"Rows removed: {rows_removed}")

# STEP 6: OUTLIERS (IQR CAPPING)
print("\n" + "="*80)
print("STEP 6: OUTLIERS (IQR CAPPING)")
print("="*80)

def cap_outliers_iqr(series, name):
    Q1 = series.quantile(0.25)
    Q3 = series.quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    
    print(f"\n{name}:")
    print(f"   Q1 = {Q1:.2f}, Q3 = {Q3:.2f}, IQR = {IQR:.2f}")
    print(f"   Lower bound = {lower_bound:.2f}")
    print(f"   Upper bound = {upper_bound:.2f}")
    
    outliers_low = (series < lower_bound).sum()
    outliers_high = (series > upper_bound).sum()
    print(f"   Outliers below lower bound: {outliers_low}")
    print(f"   Outliers above upper bound: {outliers_high}")
    
    series_capped = series.clip(lower=lower_bound, upper=upper_bound)
    return series_capped

df['Price'] = cap_outliers_iqr(df['Price'], 'Price')
df['Odometer_km'] = cap_outliers_iqr(df['Odometer_km'], 'Odometer_km')

print("\nOutliers capped using IQR method")
print("\nSummary after capping:")
print(df[['Price', 'Odometer_km']].describe())


# STEP 7: ONE-HOT ENCODE CATEGORICAL
print("\n" + "="*80)
print("STEP 7: ONE-HOT ENCODE CATEGORICAL (Location)")
print("="*80)

print(f"\nUnique locations before encoding: {df['Location'].unique()}")

location_dummies = pd.get_dummies(df['Location'], prefix='Location', drop_first=False)
df = pd.concat([df, location_dummies], axis=1)
df = df.drop('Location', axis=1)

print(f"\nNew columns created:")
for col in location_dummies.columns:
    print(f"   - {col}")

print(f"\nSample of encoded columns:")
print(df[location_dummies.columns].head())

# STEP 8: FEATURE ENGINEERING
print("\n" + "="*80)
print("STEP 8: FEATURE ENGINEERING")
print("="*80)

current_year = 2026
df['CarAge'] = current_year - df['Year']
print(f"\nFeature 1: CarAge = {current_year} - Year")
print(f"   Range: {df['CarAge'].min()} to {df['CarAge'].max()} years")

df['Km_per_year'] = df['Odometer_km'] / (df['CarAge'] + 1)
print(f"\nFeature 2: Km_per_year = Odometer_km / (CarAge + 1)")
print(f"   Range: {df['Km_per_year'].min():.2f} to {df['Km_per_year'].max():.2f} km/year")

df['Is_Urban'] = df['Location_City'].astype(int)
print(f"\nFeature 3: Is_Urban (1 if City, 0 otherwise)")
print(f"   Urban cars: {df['Is_Urban'].sum()}")

df['High_Mileage'] = (df['Odometer_km'] > 150000).astype(int)
print(f"\nFeature 4: High_Mileage (1 if Odometer > 150,000 km)")
print(f"   High mileage cars: {df['High_Mileage'].sum()}")

df['LogPrice'] = np.log(df['Price'] + 1)
print(f"\nAlternative Target: LogPrice = log(Price + 1)")
print(f"   Range: {df['LogPrice'].min():.4f} to {df['LogPrice'].max():.4f}")


# STEP 9: FEATURE SCALING (X only)
print("\n" + "="*80)
print("STEP 9: FEATURE SCALING (X only)")
print("="*80)

continuous_features = ['Odometer_km', 'Doors', 'Accidents', 'Year', 'CarAge', 'Km_per_year']

print(f"\nFeatures to scale:")
for feat in continuous_features:
    print(f"   - {feat}")

print(f"\nFeatures NOT scaled:")
print(f"   - Price (target variable)")
print(f"   - LogPrice (alternative target)")
print(f"   - Location_* (binary dummies, already 0/1)")
print(f"   - Is_Urban (binary, already 0/1)")
print(f"   - High_Mileage (binary, already 0/1)")

scaler = StandardScaler()
df[continuous_features] = scaler.fit_transform(df[continuous_features])

print(f"\nScaling complete using StandardScaler (mean=0, std=1)")
print(f"\nSample of scaled values:")
print(df[continuous_features].head())

print(f"\nVerification (mean ≈ 0, std ≈ 1):")
for feat in continuous_features:
    print(f"   {feat}: mean={df[feat].mean():.6f}, std={df[feat].std():.6f}")

# STEP 10: FINAL CHECKS & SAVE
print("\n" + "="*80)
print("STEP 10: FINAL CHECKS & SAVE")
print("="*80)

print("\nFinal Data Info:")
print(df.info())

print("\nFinal Missing Values Check:")
missing_final = df.isnull().sum()
print(missing_final)
if missing_final.sum() == 0:
    print("SUCCESS: No missing values remain!")

print("\nFinal Describe Table:")
print(df.describe())

print(f"\nFinal Shape: {df.shape}")
print(f"   Rows: {df.shape[0]}, Columns: {df.shape[1]}")

print("\nSanity Checks:")
print(f"   Price is float: {df['Price'].dtype == 'float64'}")
print(f"   LogPrice exists: {'LogPrice' in df.columns}")
print(f"   No missing values: {df.isnull().sum().sum() == 0}")
print(f"   Location dummies exist: {any('Location_' in col for col in df.columns)}")

output_file = 'car_l3_clean_ready.csv'
df.to_csv(output_file, index=False)
print(f"\nCleaned dataset saved to: {output_file}")

print("\n" + "="*80)
print("PREPROCESSING PIPELINE COMPLETE!")
print("="*80)
print(f"\nFinal dataset: {df.shape[0]} rows × {df.shape[1]} columns")
print(f"Output file: {output_file}")
