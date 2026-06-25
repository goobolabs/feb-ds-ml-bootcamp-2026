import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error


CSV_FILE_PATH = "ds-ml-bootcamp/dataset/clean_house_l5_dataset.csv"
df = pd.read_csv(CSV_FILE_PATH)

# print(df.head(10))


X = df.drop(columns=["Price", "LogPrice"])
y = df["Price"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, )

lr = LinearRegression()
rf = RandomForestRegressor(n_estimators=100, random_state=42)

lr.fit(X_train, y_train)
rf.fit(X_train, y_train)

lr_pred = lr.predict(X_test)
rf_pred = rf.predict(X_test)


def print_metrics(name, y, y_pred):
    r2 = r2_score(y, y_pred)
    mae = mean_absolute_error(y, y_pred)
    mse = mean_squared_error(y, y_pred)
    rmse = np.sqrt(mse)

    print(name)
    print(f" R2: {r2:.3f}")
    print(f" MAE: {mae:.0f}")
    print(f" MSE: {mse:.0f}")
    print(f" RMSE: {rmse:.0f}")


print_metrics("Linear Regression", y_test, lr_pred)
print_metrics("Random Forest", y_test, rf_pred)


i = 9

x_one_df = X_test.iloc[[i]]   # 1-row DataFrame (keeps feature names)
y_true = y_test.iloc[i]     # scalar

p_lr_one = float(lr.predict(x_one_df)[0])
p_rf_one = float(rf.predict(x_one_df)[0])

print("\nSingle-row sanity check:")
print(f"  Actual Price: ${y_true:,.0f}")
print(f"  LR Pred     : ${p_lr_one:,.0f}")
print(f"  RF Pred     : ${p_rf_one:,.0f}")
