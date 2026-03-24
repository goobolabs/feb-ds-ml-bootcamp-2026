import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# --- SETTINGS ---
DATA_PATH = "car_l3_dataset.csv"
OUTPUT_PATH = "car_l3_clean_ready.csv"

# 1. Load & Inspect
def load_and_inspect(path):
    print("\n--- STEP 1: LOAD & INSPECT ---")
    df = pd.read_csv(path)
    print(f"Shape: {df.shape}")
    print("\nInitial Head(10):")
    print(df.head(10))
    print("\nInfo Summary:")
    df.info()
    print("\nMissing Values Count:")
    print(df.isnull().sum())
    print("\nLocation Value Counts:")
    print(df['Location'].value_counts(dropna=False))
    return df

df = load_and_inspect(DATA_PATH)

# 2. Clean Target Formatting (Price)
def clean_price(df):
    print("\n--- STEP 2: CLEAN PRICE ---")
    df['Price'] = df['Price'].replace(r"[\$,]", "", regex=True).astype(float)
    print(f"Price Dtype: {df['Price'].dtype}")
    print(f"Price Skewness: {df['Price'].skew():.4f}")
    return df

df = clean_price(df)

# 3. Fix Category Errors before Imputation
def fix_categories(df):
    print("\n--- STEP 3: FIX CATEGORY ERRORS ---")
    # Normalize text and map typos
    df['Location'] = df['Location'].str.strip().replace({
        "Subrb": "Suburb",
        "??": np.nan,
        "": np.nan
    })
    print("\nUpdated Location Value Counts (including NaNs):")
    print(df['Location'].value_counts(dropna=False))
    return df

df = fix_categories(df)

# 4. Impute Missing Values
def impute_missing(df):
    print("\n--- STEP 4: IMPUTE MISSING VALUES ---")
    # Odometer -> Median (robust to outliers)
    df['Odometer_km'] = df['Odometer_km'].fillna(df['Odometer_km'].median())
    
    # Doors/Accidents/Location -> Mode
    for col in ['Doors', 'Accidents', 'Location']:
        df[col] = df[col].fillna(df[col].mode()[0])
        
    print(f"Missing values after imputation:\n{df.isnull().sum()}")
    return df

df = impute_missing(df)

# 5. Remove Duplicates
def remove_duplicates(df):
    print("\n--- STEP 5: REMOVE DUPLICATES ---")
    before = df.shape[0]
    df = df.drop_duplicates().reset_index(drop=True)
    after = df.shape[0]
    print(f"Rows before: {before}, Rows after: {after} (Deleted: {before - after})")
    return df

df = remove_duplicates(df)

# 6. Outliers (IQR capping)
def handle_outliers(df, k=1.5):
    print("\n--- STEP 6: OUTLIERS (IQR CAPPING) ---")
    for col in ['Price', 'Odometer_km']:
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1
        lower = q1 - k * iqr
        upper = q3 + k * iqr
        
        # Verify capping
        outliers_pre = df[(df[col] < lower) | (df[col] > upper)].shape[0]
        df[col] = df[col].clip(lower, upper)
        print(f"{col}: Capping at [{lower:.2f}, {upper:.2f}]. Outliers handled: {outliers_pre}")
    return df

df = handle_outliers(df)

# 7. One-Hot Encode Categorical(s)
def encode_categories(df):
    print("\n--- STEP 7: ONE-HOT ENCODING ---")
    df = pd.get_dummies(df, columns=["Location"], drop_first=False, dtype=int)
    print(f"New Columns: {[c for c in df.columns if c.startswith('Location_')]}")
    return df

df = encode_categories(df)

# 8. Feature Engineering
def feature_engineering(df):
    print("\n--- STEP 8: FEATURE ENGINEERING ---")
    CURRENT_YEAR = pd.Timestamp('now').year
    
    # Feature 1: Car Age
    df['CarAge'] = CURRENT_YEAR - df['Year']
    
    # Feature 2: Km per Year (safe handling for Age 0)
    df['Km_per_year'] = df['Odometer_km'] / (df['CarAge'] + 1)
    
    # Feature 3: Is Urban (City/Suburb vs Rural)
    # Since we one-hot encoded, we check the dummies
    if 'Location_Rural' in df.columns:
        df['Is_Urban'] = (df['Location_Rural'] == 0).astype(int)
    else:
        df['Is_Urban'] = 1 # Fallback
        
    # Extra: LogPrice (Target Alternative)
    df['LogPrice'] = np.log1p(df['Price'])
    
    print(f"Engineered Features: CarAge, Km_per_year, Is_Urban, LogPrice")
    return df

df = feature_engineering(df)

# 9. Feature Scaling (X only)
def scale_features(df):
    print("\n--- STEP 9: FEATURE SCALING ---")
    
    # Targets and Dummies to exclude
    targets = {'Price', 'LogPrice'}
    dummies = {c for c in df.columns if c.startswith('Location_')} | {'Is_Urban'}
    
    # Identify continuous features
    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.to_list()
    num_features_to_scale = [c for c in numeric_cols if c not in targets and c not in dummies]
    
    print(f"Scaling columns: {num_features_to_scale}")
    
    scaler = StandardScaler()
    df[num_features_to_scale] = scaler.fit_transform(df[num_features_to_scale])
    
    # Small sample of scaled values
    print("\nScaled values sample:")
    print(df[num_features_to_scale].head())
    
    # Confirm mean ~ 0 and std ~ 1
    stats = df[num_features_to_scale].agg(['mean', 'std']).round(4)
    print("\nScalability check (mean/std):")
    print(stats)
    
    return df

df = scale_features(df)

# 10. Final Checks & Save
def finalize(df, out_path):
    print("\n--- STEP 10: FINAL CHECKS & SAVE ---")
    print(f"Final Info:")
    df.info()
    print(f"\nFinal Missing Values: {df.isnull().sum().sum()}")
    print("\nFinal Description (Subset):")
    print(df.describe().T.head(10))
    
    df.to_csv(out_path, index=False)
    print(f"\nSUCCESS! Cleaned dataset saved to: {out_path}")

finalize(df, OUTPUT_PATH)
