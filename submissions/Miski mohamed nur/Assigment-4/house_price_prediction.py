import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
# 2️⃣ Load Dataset

CSV_PATH = "Data_set/clean_house_l5_dataset.csv"


df = pd.read_csv(CSV_PATH)

df.head(10)
# print(df.head(10))

# 3️⃣ Prepare Features (X) and Target (y)

# Target = Price
y = df["Price"]

X = df.drop(["Price", "LogPrice"], axis=1)
#4️⃣ Split Dataset

# 80% training
# 20% testing

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
# 5️⃣ Train Models
# Linear Regression
lr_model = LinearRegression()

lr_model.fit(X_train, y_train)
# Random Forest
rf_model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

rf_model.fit(X_train, y_train)
# 6️⃣ Predictions


lr_pred = lr_model.predict(X_test)

rf_pred = rf_model.predict(X_test)
# 7️⃣ Evaluation Function

def evaluate_model(y_true, y_pred, name):

    r2 = r2_score(y_true, y_pred)
    mae = mean_absolute_error(y_true, y_pred)
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)

    print(name)
    print("R²  :", r2)
    print("MAE :", mae)
    print("MSE :", mse)
    print("RMSE:", rmse)
    print()
# 8️⃣ Evaluate Both Models

evaluate_model(y_test, lr_pred, "Linear Regression Performance")

evaluate_model(y_test, rf_pred, "Random Forest Performance")

# # 9️⃣ Single Row Sanity Check

# 9️⃣ Single Row Sanity Check

i = 0

sample = X_test.iloc[[i]]

actual_price = y_test.iloc[i]

lr_prediction = lr_model.predict(sample)[0]
rf_prediction = rf_model.predict(sample)[0]

print("Actual Price:", round(actual_price,2))
print("Linear Regression Prediction:", round(lr_prediction,2))
print("Random Forest Prediction:", round(rf_prediction,2))
print("Model trained successfully")


















