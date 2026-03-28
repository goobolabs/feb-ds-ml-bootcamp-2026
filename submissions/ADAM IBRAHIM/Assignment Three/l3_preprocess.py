# STEP ONE LOAD AND INSPECT THE DATA

import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

PATH = 'car_l3_dataset.csv'
df = pd.read_csv(PATH)

#FIRST 10 ROWS
print(df.head(10))

#SHAPE OF THE DATA
print(df.shape)

#INFO OF THE DATA
print(df.info())

#MISING VALUES
print(df.isnull().sum())

#LOCATION VALUE COUNTS
print(df['Location'].value_counts(dropna=False))
#END OF STEP ONE



#STEP TWO CLEAN TARGET FORMATTING(PRICE)

#REMOVE CURRENCY AND SYMBOLS
df['Price'] = df['Price'].replace(r'[\$,]', '', regex=True).astype(float)

#CONFIRM DTYPE
print(df['Price'].dtype)

#CHECK SKEWNESS
print(df['Price'].skew())



#STEP THREE FIXING CATEGORY ERRORS BEFORE IMPUTATION

#NORMALIZE TEXT
df['Location'] = df['Location'].str.strip()

#FIXING TYPOS
df['Location'] = df['Location'].replace({'Subrb':'Suburb'})

#CONVERT UNKNOWN TO MISSING
df['Location'] = df['Location'].replace({'??': pd.NA})

#CHECKING COUNTS
print(df['Location'].value_counts(dropna=False))



#STEP FOUR IMPUTING MISSING VALUES

#odometer_km to median
odometer_median = df['Odometer_km'].median()
df['Odometer_km'] = df['Odometer_km'].fillna(odometer_median)

#Doors to mode
doors_mode = df['Doors'].mode().iloc[0]
df['Doors'] = df['Doors'].fillna(doors_mode)

#Accidents to mode
accidents_mode = df['Accidents'].mode().iloc[0]
df['Accidents'] = df['Accidents'].fillna(accidents_mode)

#Location to mode
location_mode = df['Location'].mode().iloc[0]
df['Location'] = df['Location'].fillna(location_mode)

#CHECKING COUNTS
print(df.isnull().sum())



#STEP FIVE REMOVING DUPLICATES

#BEFORE AND AFTER
before = df.shape
df = df.drop_duplicates()
after = df.shape

print("BEFORE: ", before, "AFTER: ", after)



#STEP SIX FINDING THE OUTLAYERS (IQR capping)

 #COMPUTING IQR FOR PRICE
def get_iqr_bounds(series, k=1.5):
    q1, q3 = series.quantile([0.25, 0.75])
    iqr = q3 - q1
    lower = q1 - k * iqr
    upper = q3 + k * iqr
    return lower, upper

#Ensure data is numeric
cols_to_fix = ['Price', 'Odometer_km']
for col in cols_to_fix:
    df[col] = pd.to_numeric(df[col], errors='coerce')

#THE CLIP VALUES
for col in cols_to_fix:
    low, high = get_iqr_bounds(df[col])
    df[col] = df[col].clip(lower=low, upper=high)

#CHECKING SUMMARY
print(df[cols_to_fix].describe())



#STEP SEVEN ONE-HOT ENCODING CATEGORICAL

#APPLY ONE-HOT ENCODING
df = pd.get_dummies(df, columns=['Location'], prefix='Location')

#CHECK NEW COLUMNS
print(df.columns)

#VERIFY ENCODING
print(df[['Location_City','Location_Suburb','Location_Rural']].head(10))



#STEP EIGHT FUTURE ENGINEERING

#carAge
current_year = 2026  # or use datetime.now().year
df['CarAge'] = current_year - df['Year']

#km_per_year
df['Km_per_year'] = df['Odometer_km'] / df['CarAge'].replace(0, 1)

#is_Urban
df['Is_Urban'] = df[['Location_City','Location_Suburb']].max(axis=1)

#LogPrice
import numpy as np
df['LogPrice'] = np.log(df['Price'] + 1)

#QUICK CHECK
print(df[['CarAge','Km_per_year','Is_Urban','LogPrice']].head(10))


#STEP NINE FEATURE SCALIN

scaler = StandardScaler()

#APPLY STANDARDSCALER
continuous_features = ['Odometer_km','CarAge','Km_per_year']
df[continuous_features] = scaler.fit_transform(df[continuous_features])

#VERIFY SCALING
for col in continuous_features:
    print(col, "mean:", df[col].mean(), "std:", df[col].std())


#STEP TEN FINAL CHECK AND SAVE

print(df.info())
print(df.isnull().sum())

OUT_PATH = 'car_l3_clean_ready.csv'

df.to_csv (OUT_PATH)

print("Saved to: ", OUT_PATH)


