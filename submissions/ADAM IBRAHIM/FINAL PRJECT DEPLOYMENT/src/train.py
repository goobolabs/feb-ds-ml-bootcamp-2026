import os
import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor

from utils import evaluate_model


# create models folder automatically
os.makedirs("models", exist_ok=True)

# load dataset
df = pd.read_csv("dataset/used_car_price_dataset.csv")

X = df.drop("price", axis=1)
y = df["price"]

categorical_cols = ["brand", "fuel_type", "transmission"]
numerical_cols = ["year", "engine_size", "mileage", "owner_count"]

preprocessor = ColumnTransformer(
    transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols),
        ("num", "passthrough", numerical_cols)
    ]
)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ------------------------
# Random Forest
# ------------------------

rf_model = Pipeline([
    ("preprocessor", preprocessor),
    ("model", RandomForestRegressor(n_estimators=200, random_state=42))
])

rf_model.fit(X_train, y_train)

rf_preds = rf_model.predict(X_test)

print("Random Forest Results:")
print(evaluate_model(y_test, rf_preds))


# ------------------------
# Gradient Boosting
# ------------------------

gb_model = Pipeline([
    ("preprocessor", preprocessor),
    ("model", GradientBoostingRegressor(
        n_estimators=300,
        learning_rate=0.05,
        max_depth=3,
        random_state=42
    ))
])

gb_model.fit(X_train, y_train)

gb_preds = gb_model.predict(X_test)

print("\nGradient Boosting Results:")
print(evaluate_model(y_test, gb_preds))


# save best model
joblib.dump(gb_model, "models/best_model.pkl")

print("\nModel saved in models/best_model.pkl")