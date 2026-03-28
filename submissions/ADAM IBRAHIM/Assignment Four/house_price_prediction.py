# Step 1: Import libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error


# 2- Load data
data = pd.read_csv("car_l3_clean_ready.csv")
data.head()

# 3- Features and target
X = data.drop(columns=["Price", "LogPrice"])
y = data["Price"]

# 4- Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 5- Train models
lr_model = LinearRegression()
lr_model.fit(X_train, y_train)

# Train Random Forest
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# 6- Evaluate perfomance
def evaluate_model(model, X_test, y_test, name="Model"):
    predictions = model.predict(X_test)
    r2 = r2_score(y_test, predictions)
    mae = mean_absolute_error(y_test, predictions)
    mse = mean_squared_error(y_test, predictions)
    rmse = np.sqrt(mse)
    print(f"{name} Performance:")
    print(f"  R²   : {r2:.2f}")
    print(f"  MAE  : {mae:,.0f}")
    print(f"  RMSE : {rmse:,.0f}")
    return predictions

# Evaluate both models
lr_preds = evaluate_model(lr_model, X_test, y_test, "Linear Regression")
rf_preds = evaluate_model(rf_model, X_test, y_test, "Random Forest")


# 7- Single-row sanity check
i = 5  
row = X_test.iloc[[i]]
actual_price = y_test.iloc[i]

lr_pred = lr_model.predict(row)[0]
rf_pred = rf_model.predict(row)[0]

print("Sanity Check:")
print(f"Actual Price       : {actual_price:,.0f}")
print(f"Linear Regression  : {lr_pred:,.0f}")
print(f"Random Forest      : {rf_pred:,.0f}")
