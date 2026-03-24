import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


CSV_PATH = "car_clean_dataset_.csv"
df=pd.read_csv(CSV_PATH)
# print(df.shape)


x = df.drop(columns=["Price", "Log_price"])
y = df["Price"]

X_train, X_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

lr = LinearRegression()
rf = RandomForestRegressor(n_estimators=100, random_state=42)


lr.fit(X_train, y_train)
rf.fit(X_train, y_train)

lr_pred = lr.predict(X_test)
rf_pred = rf.predict(X_test)

# print(lr_pred[:10])


mse = mean_squared_error(y_test, lr_pred)
mae = mean_absolute_error(y_test, lr_pred)
r2 = r2_score(y_test, lr_pred)
rmse = np.sqrt(mse)
    


def print_metrics(name, y_true, y_pred):

    mse = mean_squared_error(y_true, y_pred)
    mae = mean_absolute_error(y_true, y_pred)
    r2 = r2_score(y_true, y_pred)
    rmse = np.sqrt(mse)

    print(f"\nPrediction of {name}")
    print(f"R2: {r2:.5f}")
    print(f"MAE: {mae:.0f}")
    print(f"MSE: {mse:,.0f}")
    print(f"RMSE: {rmse:.0f}")


print_metrics("LR", y_test, lr_pred)
print_metrics("RF", y_test, rf_pred)

i = 1
x_one_df = X_test.iloc[[i]]
y_true = y_test.iloc[i]

p_lr_one = float(lr.predict(x_one_df)[0])
p_lr_one = float(rf.predict(x_one_df)[0])

# print("Single Row Sanity check")

# print(f"Actual Price: ${y_true:,.0f}")
# print(f"LR PREDCITION: ${y_true:,.0f}")
# print(f"RF PREDCITION: ${y_true:,.0f}")
