import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# ==========================================
# Lesson 3 Assignment: Data Preprocessing
# ==========================================

CSV_PATH = 'car_l3_dataset.csv'
df = pd.read_csv(CSV_PATH)

def print_section(title):
    print(f"\n=== {title} ===")

# 1. Load & Inspect
print_section("STEP 1: Load & Inspect")
try:
    df = pd.read_csv(CSV_PATH)
except FileNotFoundError:
    print(f"Error: {CSV_PATH} not found.")
    exit()

print("Head (10 rows):")
print(df.head(10))
print(f"\nShape: {df.shape}")
print("\nInfo:")
df.info()
print("\nMissing Values Count:")
print(df.isnull().sum())
print("\nLocation Value Counts (Raw):")
print(df['Location'].value_counts(dropna=False))

# 2. Clean Target Formatting (Price)
print_section("STEP 2: Clean Target Formatting (Price)")
# Remove currency symbols and commas
if df['Price'].dtype == 'O':
    df['Price'] = df['Price'].replace(r'[\$,]', '', regex=True)

# Convert to numeric
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')

# Drop missing targets as we cannot train without them (Verification Check)
initial_rows = df.shape[0]
df.dropna(subset=['Price'], inplace=True)
dropped_rows = initial_rows - df.shape[0]
print(f"Dropped {dropped_rows} rows with missing 'Price'.")

print(f"Price Dtype: {df['Price'].dtype}")
print(f"Price Skewness: {df['Price'].skew():.2f}")

# 3. Fix Category Errors before Imputation
print_section("STEP 3: Fix Category Errors")
# Normalize typos and convert unknowns to NaN
df['Location'] = df['Location'].replace({
    'Subrb': 'Suburb', 
    '??': np.nan
})
print("Location Value Counts (Fixed, including NaN):")
print(df['Location'].value_counts(dropna=False))

# 4. Impute Missing Values
print_section("STEP 4: Impute Missing Values")
# Odometer_km -> Median
median_odo = df['Odometer_km'].median()
df['Odometer_km'] = df['Odometer_km'].fillna(median_odo)
print(f"Imputed Odometer_km with Median: {median_odo}")

# Doors -> Mode
mode_doors = df['Doors'].mode()[0]
df['Doors'] = df['Doors'].fillna(mode_doors)
print(f"Imputed Doors with Mode: {mode_doors}")

# Accidents -> Mode
mode_accidents = df['Accidents'].mode()[0]
df['Accidents'] = df['Accidents'].fillna(mode_accidents)
print(f"Imputed Accidents with Mode: {mode_accidents}")

# Location -> Mode
mode_loc = df['Location'].mode()[0]
df['Location'] = df['Location'].fillna(mode_loc)
print(f"Imputed Location with Mode: {mode_loc}")

print("\nPost-Imputation Missing Counts:")
print(df.isnull().sum())

# 5. Remove Duplicates
print_section("STEP 5: Remove Duplicates")
shape_before = df.shape
df.drop_duplicates(inplace=True)
shape_after = df.shape
print(f"Shape Before: {shape_before}, Shape After: {shape_after}")
print(f"Rows Removed: {shape_before[0] - shape_after[0]}")

# 6. Outliers (IQR Capping)
print_section("STEP 6: Outliers (IQR Capping)")
def cap_iqr(series, name):
    Q1 = series.quantile(0.25)
    Q3 = series.quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    print(f"Capping {name}: Lower={lower:.2f}, Upper={upper:.2f}")
    return series.clip(lower=lower, upper=upper)

df['Price'] = cap_iqr(df['Price'], 'Price')
df['Odometer_km'] = cap_iqr(df['Odometer_km'], 'Odometer_km')

print("\nSummary after capping:")
print(df[['Price', 'Odometer_km']].describe())

# 7. One-Hot Encode Categorical(s)
print_section("STEP 7: One-Hot Encode")
# Encode Location
df = pd.get_dummies(df, columns=['Location'], prefix='Location', drop_first=False)
# Convert bool to int (0/1) if pandas version creates booleans
cols_to_convert = [c for c in df.columns if 'Location_' in c]
df[cols_to_convert] = df[cols_to_convert].astype(int)

print("New Columns Created:")
print(cols_to_convert)

# 8. Feature Engineering
print_section("STEP 8: Feature Engineering")

CURRENT_YEAR = 2026 # As per assignment usage context or current year

# 1. CarAge
df['CarAge'] = CURRENT_YEAR - df['Year']
# Ensure no negative ages (sanity check)
df['CarAge'] = df['CarAge'].apply(lambda x: max(0, x))

# 2. Km_per_year
# Avoid division by zero
df['Km_per_year'] = df['Odometer_km'] / df['CarAge'].replace(0, 1)

# 3. High_Usage (Binary) - Example of sensible feature
# Flag if car is driven more than standard 20k/year
df['High_Usage'] = (df['Km_per_year'] > 20000).astype(int)

# Target: LogPrice
df['LogPrice'] = np.log1p(df['Price'])

print("Added features: CarAge, Km_per_year, High_Usage, LogPrice")
print(df[['CarAge', 'Km_per_year', 'LogPrice']].head())

# 9. Feature Scaling
print_section("STEP 9: Feature Scaling (X only)")
# Exclude Targets (Price, LogPrice) and Binary/Dummies
regex_exclude = r"Location_|High_Usage|Price|LogPrice|Year|Doors|Accidents" 
# Note: Doors/Accidents are ordinal/discrete, often better unscaled or treated differently, 
# but rubric asks for standardized continuous features. 
# Safe strict set: Odometer_km, CarAge, Km_per_year.

features_to_scale = ['Odometer_km', 'CarAge', 'Km_per_year']
print(f"Standardizing: {features_to_scale}")

scaler = StandardScaler()
df[features_to_scale] = scaler.fit_transform(df[features_to_scale])

print("\nSample of Scaled Values:")
print(df[features_to_scale].head())

# 10. Final Checks & Save
print_section("STEP 10: Final Checks & Save")

# Assertions
assert df.isnull().sum().sum() == 0, "Error: Missing values remain!"
assert 'LogPrice' in df.columns, "Error: LogPrice missing!"
assert any(col.startswith('Location_') for col in df.columns), "Error: No Location columns!"

print("Final Info:")
df.info()
print("\nFinal Description:")
print(df.describe().T)

OUT_PATH = "car_l3_clean_ready.csv"
df.to_csv(OUT_PATH, index=False)
print(f"\n SUCCESS: Cleaned data saved to {OUT_PATH}")

