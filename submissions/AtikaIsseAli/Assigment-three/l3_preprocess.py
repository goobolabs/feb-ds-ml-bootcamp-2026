import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# 1) Load & Inspect
df = pd.read_csv('car_l3_dataset.csv')

# 2) Clean Target Formatting
df['Price'] = df['Price'].replace(r'[\$,]', '', regex=True).astype(float)

# 3) Fix Category Errors before Imputation
df['Location'] = df['Location'].replace({'Subrb': 'Suburb', '??': np.nan, '': np.nan})

# 4) Impute Missing Values
df['Odometer_km'] = df['Odometer_km'].fillna(df['Odometer_km'].median())
df['Doors'] = df['Doors'].fillna(df['Doors'].mode()[0])
df['Accidents'] = df['Accidents'].fillna(df['Accidents'].mode()[0])
df['Location'] = df['Location'].fillna(df['Location'].mode()[0])

# 5) Remove Duplicates
df = df.drop_duplicates()

# 6) Outliers (IQR capping)
def cap_outliers(df, col):
    q1, q3 = df[col].quantile([0.25, 0.75])
    iqr = q3 - q1
    df[col] = df[col].clip(q1 - 1.5 * iqr, q3 + 1.5 * iqr)

cap_outliers(df, 'Price')
cap_outliers(df, 'Odometer_km')

# 7) One-Hot Encode
df = pd.get_dummies(df, columns=['Location'], prefix='Loc')

# 8) Feature Engineering
df['CarAge'] = 2026 - df['Year']
df['Km_per_year'] = df['Odometer_km'] / (df['CarAge'] + 1)
df['Is_Urban'] = (df.get('Loc_City', 0) == 1).astype(int)
df['LogPrice'] = np.log1p(df['Price'])

# 9) Feature Scaling (Continuous features only)
to_scale = ['Odometer_km', 'Doors', 'Accidents', 'CarAge', 'Km_per_year']
scaler = StandardScaler()
df[to_scale] = scaler.fit_transform(df[to_scale])

# 10) Save Cleaned Data
df.to_csv('car_l3_clean_ready.csv', index=False)
print("--- Success: Preprocessing Complete! ---")