import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler


CSV_FILE_PATH = "ds-ml-bootcamp/dataset/car_l3_dataset.csv"


df = pd.read_csv(CSV_FILE_PATH)

# print(df.head(10))

# print(df.shape)

# print(df.info())

# print("missiing values")

# print(df.isnull().sum())

# print(df['Location'].value_counts(dropna=False))


# replace invalid values


df['Price'] = df['Price'].replace(r"[ \$, ]", "", regex=True).astype(float)

df['Location'] = df['Location'].replace({
    "Subrb": "Suburb",
    "??": pd.NA,
    "": pd.NA
})


# print(df['Location'].value_counts(dropna=False))


# fill missing values

df["Odometer_km"] = df["Odometer_km"].fillna(df["Odometer_km"].median())
df["Doors"] = df["Doors"].fillna(df["Doors"].mode()[0])
df["Location"] = df["Location"].fillna(df["Location"].mode()[0])
df["Accidents"] = df["Accidents"].fillna(df["Accidents"].mode()[0])


# print(df.isnull().sum())

# Remove duplicates

before = df.shape


df = df.drop_duplicates()

after = df.shape


df['Price'] = pd.to_numeric(df['Price'], errors='coerce')


def iqr_outliers(series, k=1.5):
    q1, q3 = series.quantile([0.25, 0.75])
    iqr = q3 - q1
    lower_bound = q1 - k * iqr
    upper_bound = q3 + k * iqr
    return lower_bound, upper_bound


lower_price, upper_price = iqr_outliers(df['Price'])
lower_odo, upper_odo = iqr_outliers(df['Odometer_km'])


# Adjust outliers from price

df["Price"] = df["Price"].clip(lower=lower_price, upper=upper_price)

# df = df[(df['price'] >= lower_price) & (df['price'] <= upper_price)]


# Adjust outliers from odometer

df["Odometer_km"] = df["Odometer_km"].clip(lower=lower_odo, upper=upper_odo)


# Encoding categorical variables

df = pd.get_dummies(df, columns=["Location"], drop_first=False).astype(int)


# feature engineering


current_year = 2025

df["Car_Age"] = current_year - df["Year"]


df["KM_per_Year"] = df["Odometer_km"] / df["Car_Age"]


df["Is_Old"] = np.where(df["Car_Age"] > 15, 1, 0)


df["is_City"] = np.where(df["Location_City"] == 1, 1, 0)


df["Accident_Risk"] = pd.cut(
    df["Accidents"],
    bins=[-1, 0, 2, 10],
    labels=["No_Accident", "Medium", "High"]
)

df = pd.get_dummies(df, columns=["Accident_Risk"],
                    drop_first=False).astype(int)


df["Log_Price"] = np.log1p(df["Price"])


# Scaling


do_not_scale = ["Log_Price", "Price", "Is_Old", "Accidents",  "Accident_Risk_No_Accident", "Accident_Risk_Medium", "Accident_Risk_High",
                "Location_Suburb", "Location_City", "Location_Rural", "is_City"]

exclude_cols = [col for col in df.columns if col not in do_not_scale]

features_to_scale = [col for col in df.columns if col not in do_not_scale]

scaler = StandardScaler()

df[features_to_scale] = scaler.fit_transform(df[features_to_scale])


OUT_PATH = "ds-ml-bootcamp/submissions/Bidaar114/assignment-3/processed_car_data.csv"

df.to_csv(OUT_PATH)

print(f"Data preprocessing completed. Processed data saved to", OUT_PATH)
