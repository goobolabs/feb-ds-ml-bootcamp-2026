
# 1. Import required libraries
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error


# 2. Load the cleaned dataset
data_path = "clean_house_dataset.csv"
df = pd.read_csv(data_path)

print("Dataset loaded successfully")
print(df.head())


# 3. Prepare Features (X) and Target (y)
y = df["Price"]
X = df.drop(columns=["Price", "LogPrice"])

print("\nFeature columns:")
print(X.columns)


# 4. Split data into training and testing sets (80/20)
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nData split completed")
print("Training size:", X_train.shape)
print("Testing size:", X_test.shape)


# 5. Train Linear Regression model
linear_model = LinearRegression()
linear_model.fit(X_train, y_train)

print("\nLinear Regression model trained")


# Train Random Forest Regressor
rf_model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)
rf_model.fit(X_train, y_train)

print("Random Forest model trained")


# 6. Model evaluation function
def evaluate_model(model, X_test, y_test):
    predictions = model.predict(X_test)

    r2 = r2_score(y_test, predictions)
    mae = mean_absolute_error(y_test, predictions)
    mse = mean_squared_error(y_test, predictions)
    rmse = np.sqrt(mse)

    return r2, mae, mse, rmse


# Evaluate Linear Regression
lr_r2, lr_mae, lr_mse, lr_rmse = evaluate_model(
    linear_model, X_test, y_test
)

print("\nLinear Regression Performance")
print("R2 Score :", round(lr_r2, 2))
print("MAE      :", round(lr_mae, 0))
print("MSE      :", round(lr_mse, 0))
print("RMSE     :", round(lr_rmse, 0))


#  Evaluate Random Forest
rf_r2, rf_mae, rf_mse, rf_rmse = evaluate_model(
    rf_model, X_test, y_test
)

print("\nRandom Forest Performance")
print("R2 Score :", round(rf_r2, 2))
print("MAE      :", round(rf_mae, 0))
print("MSE      :", round(rf_mse, 0))
print("RMSE     :", round(rf_rmse, 0))


# 7. Single-row sanity check
index = 0
single_X = X_test.iloc[[index]]
actual_price = y_test.iloc[index]

lr_prediction = linear_model.predict(single_X)[0]
rf_prediction = rf_model.predict(single_X)[0]

print("\nSingle Row Sanity Check")
print("----------------------")
print("Actual Price      :", round(actual_price, 0))
print("Linear Regression :", round(lr_prediction, 0))
print("Random Forest     :", round(rf_prediction, 0))
