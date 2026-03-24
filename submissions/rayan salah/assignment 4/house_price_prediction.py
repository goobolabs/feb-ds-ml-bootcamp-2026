# ==========================================================
# Assignment: House Price Prediction (LR & RF)
# ==========================================================

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# 1. Load Dataset
df = pd.read_csv('clean_house_l5_dataset.csv')

# 2. Prepare Features & Target
# Target (y) is Price. Drop LogPrice to avoid target leakage.
X = df.drop(columns=['Price', 'LogPrice'])
y = df['Price']

# 3. Split Data (80% Training, 20% Testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Train Models
# Train Linear Regression
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)

# Train Random Forest Regressor
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# 5. Evaluate Performance (Helper Function)
def print_metrics(model_name, y_true, y_pred):
    r2 = r2_score(y_true, y_pred)
    mae = mean_absolute_error(y_true, y_pred)
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    
    print(f"{model_name} Performance:")
    print(f"  R²   : {r2:.3f}")
    print(f"  MAE  : {mae:,.0f}")
    print(f"  RMSE : {rmse:,.0f}")
    print("-" * 30)

# Predictions
lr_preds = lr_model.predict(X_test)
rf_preds = rf_model.predict(X_test)

# Show Metrics
print_metrics("Linear Regression", y_test, lr_preds)
print_metrics("Random Forest", y_test, rf_preds)

# 6. Single-row Sanity Check
# Picking the first row (index 0) from the test set
i = 0
sample_row = X_test.iloc[[i]]
actual_price = y_test.iloc[i]

lr_prediction = lr_model.predict(sample_row)[0]
rf_prediction = rf_model.predict(sample_row)[0]

print("\n--- Single-row Sanity Check ---")
print(f"Actual Price     : ${actual_price:,.0f}")
print(f"LR Prediction    : ${lr_prediction:,.0f}")
print(f"RF Prediction    : ${rf_prediction:,.0f}")
