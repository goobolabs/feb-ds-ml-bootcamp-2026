# ===============================
# STEP 1 — Import Libraries
# ===============================

import pandas as pd
import numpy as np

# visualization (useful for EDA later)
import matplotlib.pyplot as plt
import seaborn as sns

# machine learning tools
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder

from sklearn.preprocessing import StandardScaler




# ===============================
# STEP 2 — Load Dataset
# ===============================

CSV_PATH = "dataset/cancer-risk-factors.csv"

df = pd.read_csv(CSV_PATH)

#print(df.head())

# ===============================
# STEP 3 — Inspect Dataset
# ===============================

#print("\n=== FIRST 5 ROWS ===")
#print(df.head())

#print("\n=== DATASET INFO ===")
#print(df.info())

# print("\n=== DATASET SHAPE ===")
# print(df.shape)

# print("\n=== MISSING VALUES ===")
# print(df.isnull().sum())

# ===============================
# STEP 4 — Target Distribution
# ===============================

# print("\n=== CANCER TYPE DISTRIBUTION ===")
# print(df["Cancer_Type"].value_counts())

# sns.countplot(x="Cancer_Type", data=df)
# plt.title("Cancer Type Distribution")
# plt.show()

# ===============================
# STEP 5 — Encode Target Column
# ===============================


le = LabelEncoder()
df["Cancer_Type_Encoded"] = le.fit_transform(df["Cancer_Type"])
#print("\n=== LABEL MAPPING ===")
for i, label in enumerate(le.classes_):
    print(f"{label} → {i}")



# Save label mapping for frontend use
label_mapping = dict(zip(le.classes_, le.transform(le.classes_)))

# Reverse mapping (VERY IMPORTANT)
reverse_mapping = {int(v): k for k, v in label_mapping.items()}

import json

with open("models/label_mapping.json", "w") as f:
    json.dump(reverse_mapping, f, indent=4)







# ===============================
# STEP 6 — Remove Duplicates
# ===============================

before = df.shape
df = df.drop_duplicates()
after = df.shape
# print("\n=== DUPLICATE REMOVAL ===")
# print(f"Before: {before}")
# print(f"After : {after}")


# ===============================
# STEP 7 — Feature Scaling
# ===============================
# Do NOT scale target columns
exclude_cols = ["Cancer_Type", "Cancer_Type_Encoded"]
numeric_cols = df.select_dtypes(include=["int64", "float64"]).columns
features_to_scale = [col for col in numeric_cols if col not in exclude_cols]
scaler = StandardScaler()
df[features_to_scale] = scaler.fit_transform(df[features_to_scale])


# Save the scaler and the training feature order (X columns) for serving
import os
import joblib
import json

os.makedirs("models", exist_ok=True)
# Save scaler
joblib.dump(scaler, "models/scaler.pkl")
# Save training feature columns (VERY IMPORTANT for inference)
TRAIN_COLUMNS = df.drop(columns=["Cancer_Type", "Cancer_Type_Encoded"]).columns.tolist()
json.dump(TRAIN_COLUMNS, open("models/train_columns.json", "w"))




# print("\n=== AFTER SCALING ===")
# print(df.head())

# ===============================
# STEP 8 — Save Clean Dataset
# ===============================

OUT_PATH = "dataset/clean_cancer_dataset.csv"
df.to_csv(OUT_PATH, index=False)
print("\nClean dataset saved successfully!")