import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import joblib
import os

CSV_PATH = "dataset/cardiovascular_diseases_dv3.csv"

df = pd.read_csv(CSV_PATH, sep=";")

print("\n INITIAL DATA")
print(df.head())
print(df.info())


df = df.drop(columns=["ALCOHOL"])
print("\n=== AFTER DROPPING ALCOHOL ===")

print(df.columns)
# BP logic: systolic >= diastolic
df = df[df["AP_HIGH"] >= df["AP_LOW"]]


df = df[(df["HEIGHT"] >= 120) & (df["HEIGHT"] <= 220)]
df = df[(df["WEIGHT"] >= 40) & (df["WEIGHT"] <= 200)]


df = df.sample(n=2000, random_state=42).reset_index(drop=True)

print("\n=== AFTER DROPPING TO 2000 ROWS ===")
print(df.shape)


TARGET = "CARDIO_DISEASE"

X = df.drop(columns=[TARGET])
y = df[TARGET]


scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


os.makedirs("models", exist_ok=True)
joblib.dump(scaler, "models/cardiovascular_diseases_scaler.pkl")

# TRAIN_COLUMNS = df.drop (columns= ["ALCOHOL"]).columns.to_list
# Json.dump(TRAIN_COLUMNS,open("model/train_columns.json", "w"))



clean_df = pd.DataFrame(X_scaled, columns=X.columns)
clean_df[TARGET] = y.values

OUT_PATH = "dataset/cardiovascular_diseases_cleaned_2000.csv"
clean_df.to_csv(OUT_PATH, index=False)


print("\n FINAL DATA ")
print(clean_df.head())
print(clean_df.info())
print("\nMissing values:")
print(clean_df.isnull().sum())