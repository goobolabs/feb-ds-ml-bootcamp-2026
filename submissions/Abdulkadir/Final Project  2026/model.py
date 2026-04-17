import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import random






# ===============================
# STEP 1 — Load Clean Dataset
# ===============================
CSV_PATH = "dataset/clean_cancer_dataset.csv"
df = pd.read_csv(CSV_PATH)
# print("\n=== DATA LOADED ===")
# print(df.head())

# ===============================
# STEP 2 — Split Features & Target
# ===============================

# Target (what we want to predict)
y = df["Cancer_Type_Encoded"]

# Features (everything else except target columns)
X = df.drop(columns=["Cancer_Type", "Cancer_Type_Encoded"])

# print("\n=== FEATURES & TARGET READY ===")
# print("X shape:", X.shape)
# print("y shape:", y.shape)

# ===============================
# STEP 3 — Train/Test Split
# ===============================
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,      # 80% train, 20% test
    random_state=42,
    stratify=y          # IMPORTANT for classification
)

# print("\n=== DATA SPLIT ===")
# print("X_train:", X_train.shape)
# print("X_test :", X_test.shape)

# ===============================
# STEP 4 — Train Multiple Models
# ===============================


# 1) Logistic Regression
lr = LogisticRegression(max_iter=1000)
lr.fit(X_train, y_train)
y_pred_lr = lr.predict(X_test)

# 2) Random Forest
rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
y_pred_rf = rf.predict(X_test)

# 3) XGBoost
xgb = XGBClassifier(
    n_estimators=300,
    learning_rate=0.1,
    max_depth=6,
    random_state=42,
    subsample=0.8,
    colsample_bytree=0.8,
    eval_metric="mlogloss"
)

xgb.fit(X_train, y_train)
y_pred_xgb = xgb.predict(X_test)
#print("\nAll models trained successfully!")

# ===============================
# STEP 5 — Evaluate Models
# ===============================


def evaluate_model(name, y_true, y_pred):
    print(f"\n=== {name} Evaluation ===")
    
    acc = accuracy_score(y_true, y_pred)
    print(f"Accuracy: {acc:.4f}")
    
    print("\nClassification Report:")
    print(classification_report(y_true, y_pred))
    
    print("\nConfusion Matrix:")
    print(confusion_matrix(y_true, y_pred))


#Evaluate all models
evaluate_model("Logistic Regression", y_test, y_pred_lr)
evaluate_model("Random Forest", y_test, y_pred_rf)
evaluate_model("XGBoost", y_test, y_pred_xgb)





# ===============================
# STEP 6 — Single-row sanity check
# ===============================


# pick random samples from test set
sample_indices = random.sample(range(len(X_test)), 5)

print("\n🔹 Sanity Check (Random Samples) 🔹")

for i in sample_indices:
    x_one_df = X_test.iloc[[i]]   # keep as DataFrame
    y_true   = y_test.iloc[i]

    # Predictions from all models
    p_lr  = int(lr.predict(x_one_df)[0])
    p_rf  = int(rf.predict(x_one_df)[0])
    p_xgb = int(xgb.predict(x_one_df)[0])

    # print(f"\nSample index {i}:")
    # print(f"  Actual Class : {y_true}")
    # print(f"  LR Pred      : {p_lr}")
    # print(f"  RF Pred      : {p_rf}")
    # print(f"  XGB Pred     : {p_xgb}")


    # ===============================
# STEP 7 — Save ALL Models
# ===============================

import joblib
import os

# create models folder if it doesn't exist
os.makedirs("models", exist_ok=True)

# save models
joblib.dump(lr,  "models/logistic_model.joblib")
joblib.dump(rf,  "models/random_forest_model.joblib")
joblib.dump(xgb, "models/xgb_model.joblib")

print("\nAll models saved successfully!")


# ===============================
# STEP 8 — Custom Prediction
# ===============================

# Example input (you will later connect this to frontend)
custom_input = X_test.iloc[[0]]   # using real row as safe example

print("\n🔹 Custom Prediction (Using Saved Models) 🔹")

# Load models
import joblib

lr_model  = joblib.load("models/logistic_model.joblib")
rf_model  = joblib.load("models/random_forest_model.joblib")
xgb_model = joblib.load("models/xgb_model.joblib")

# Predictions
pred_lr  = int(lr_model.predict(custom_input)[0])
pred_rf  = int(rf_model.predict(custom_input)[0])
pred_xgb = int(xgb_model.predict(custom_input)[0])

print("Logistic Regression Prediction:", pred_lr)
print("Random Forest Prediction     :", pred_rf)
print("XGBoost Prediction           :", pred_xgb)