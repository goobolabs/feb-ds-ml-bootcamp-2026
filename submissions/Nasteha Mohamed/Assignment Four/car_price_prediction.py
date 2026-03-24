import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

# Load the dataset
df = pd.read_csv('C:/Users/NV/ds-ml-bootcamp/submissions/Nasteha Mohamed/Assignment Three/data/cleaned_car_l3_dataset.csv')
print(df.head(10))

# Define features and target variable
y = df["Price"]
X = df.drop(columns=["Price", "LogPrice"], errors="ignore")


# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Train size:", X_train.shape)
print("Test size:", X_test.shape)

# Train Linear Regression model
lr = LinearRegression()
lr.fit(X_train, y_train)
# Train Random Forest Regressor model
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# Evaluate function
def evaluate_model(name, model, X_test, y_test):
    preds = model.predict(X_test)

    r2 = r2_score(y_test, preds)
    mae = mean_absolute_error(y_test, preds)
    mse = mean_squared_error(y_test, preds)
    rmse = np.sqrt(mse)

    print(f"\n{name} Performance:")
    print(f"R²   : {r2:.4f}")
    print(f"MAE  : {mae:,.2f}")
    print(f"MSE  : {mse:,.2f}")
    print(f"RMSE : {rmse:,.2f}")

    return preds
# Evaluate both models and get predictions
lr_preds = evaluate_model("Linear Regression", lr, X_test, y_test)
rf_preds = evaluate_model("Random Forest", rf, X_test, y_test)

# Single row sanity check
i = 0  

sample_X = X_test.iloc[[i]]
actual_price = y_test.iloc[i]

lr_price = lr.predict(sample_X)[0]
rf_price = rf.predict(sample_X)[0]

print("\n--- Single Row Sanity Check ---")
print(f"Actual Price        : {actual_price:,.2f}")
print(f"Linear Regression   : {lr_price:,.2f}")
print(f"Random Forest       : {rf_price:,.2f}")









