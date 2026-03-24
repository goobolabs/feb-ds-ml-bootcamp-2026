import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


## load the cleanest dataset

CVC_PATH = "clean_house_l5_dataset.csv"
df = pd.read_csv(CVC_PATH)

x= df.drop(columns=["Price", "LogPrice"])
y= df["Price"]

x_train , x_test , y_train, y_test = train_test_split(x, y, test_size= 0.2,
random_state=42)

lr = LinearRegression()
lr.fit(x_train, y_train)
lr_pred = lr.predict(x_test)

# print(lr_pred[:10])


rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(x_train, y_train)
rf_pred = rf.predict(x_test)


def print_metrics(name, y_true, y_pred):
    r2 = r2_score(y_true, y_pred)
    mae = mean_absolute_error(y_true, y_pred)
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    print(f"\n{name} performance")
    print("---------------------------")
    print(f" R2: {r2:.3f}")
    print(f" MAE: {mae:.0f}")
    print(f" MSE: {mse:.0f}")
    print(f" RMSE: {rmse:.0f}")


print_metrics("Linear Regression", y_test, lr_pred)
print_metrics("Random Forest", y_test, rf_pred)



index = 0
sample = x_test.iloc[[index]]
actual_price = y_test.iloc[index]

lr_single_pred = lr.predict(sample)[0]
rf_single_pred = rf.predict(sample)[0]

print("\nSanity Check Prediction")
print("---------------------------")
print(f"Actual Price       : {actual_price:,.0f}")
print(f"Linear Regression  : {lr_single_pred:,.0f}")
print(f"Random Forest      : {rf_single_pred:,.0f}")



# expeected results 
print("\n--- Expected Results ---")
print("Linear Regression Performance:")
print(" R²   : 0.848")
print(" MAE  : 63,086")
print(" MSE  : 5,718,940,941")
print(" RMSE : 75,624\n")

print("Random Forest Performance:")
print(" R²   : 0.859")
print(" MAE  : 52,524")
print(" MSE  : 5,283,317,455")
print(" RMSE : 72,686\n")
