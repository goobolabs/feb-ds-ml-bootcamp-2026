import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

CSV_PATH = "./car_l3_dataset.csv"
df = pd.read_csv(CSV_PATH)
print("STEP 1 — Load & Inspect")
print(df.head())
print(df.shape )
print(df.info())

print("\nSTEP 2 — Clean Target Formatting (Price)")
df["Price"] = df["Price"].replace(r"[/$,]", "", regex=True).astype(float)

print("\nSTEP 3 — Fix Category Errors before Imputation")
df["Location"] = df["Location"].replace({"Subrb": "Suburb", "??": pd.NA})

print("\nSTEP 4 — Impute Missing Values (justify choices)")

df["Odometer_km"] = df["Odometer_km"].fillna(df["Odometer_km"].median())

df["Location"] = df["Location"].fillna(df["Location"].mode()[0])
df["Doors"] = df["Doors"].fillna(df["Doors"].mode()[0])

print("\nSTEP 5 — Remove Duplicates")
before = df.shape
df = df.drop_duplicates()
after = df.shape
# print("before :", before , "after:" ,after)

print("\nSTEP 6 — IQR Capping for Outliers (Price) and (Odometer_km)")
def iqr_fun(series, k=1.5):
    q1, q3 = series.quantile([0.25, 0.75])
    iqr = q3 - q1
    lower = q1 - k * iqr
    upper = q3 + k * iqr
    return lower, upper


lower_price, high_price = iqr_fun(df["Price"])
lower_Odometer_km, high_Odometer_km = iqr_fun(df["Odometer_km"])
df["Price"] = df["Price"].clip(lower=lower_price, upper=high_price)
df["Odometer_km"] = df["Odometer_km"].clip( lower=lower_Odometer_km, upper=high_Odometer_km)
# print("IQR of price :")
# print("lower price :", lower_price, "high price :", high_price)
# print("IQR of Odometer_km :")
# print("lower Odometer_km :", lower_Odometer_km, "high Odometer_km :", high_Odometer_km)

# print("price after IQR:")
# print(df["Price"].describe())
# print("Odometer_km after IQR:")
# print(df["Odometer_km"].describe())


print("\nSTEP 7 — One-Hot Encode Categorical(s) ")
df = pd.get_dummies(df, columns=["Location"], drop_first=False)
Log_cols = [c for c in df.columns if c.startswith("Location")]
df[Log_cols] = df[Log_cols].astype(int)


print("\nSTEP 8 — Feature Engineering (no leakage) ")
CURRENT_YEAR = 2026
df["Car_year"] = CURRENT_YEAR - df["Year"]
df["Km_per_year"] = df["Odometer_km"] / df["Car_year"]

df["Is_Rural"] = df["Location_Rural"].astype(int)
df["LogPrice"] = np.log1p(df["Price"])

print("\nSTEP 9 — Feature Scaling (X only) ")
dont_scale = {"Price","LogPrice"}
numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns.to_list()

exclude = [c for c in df.columns if c.startswith("Location_")] + ["Is_Rural"]
new_fautere_to_scale = [c for c in numeric_cols if c not in  dont_scale and c not in  exclude ]
scale = StandardScaler()
df[new_fautere_to_scale] = scale.fit_transform(df[new_fautere_to_scale])

sample_cols = ["Price","LogPrice"] 
sample_cols += [c for c in df.columns if c not in sample_cols]
print(df[sample_cols].describe())
print(df.info())
print(df.isnull().sum())

print("\nSTEP 10 — Final Checks & Save")
OUT_PATH = "car_l3_clean_ready.csv"
df.to_csv(OUT_PATH)
print("Saved to out :", OUT_PATH)