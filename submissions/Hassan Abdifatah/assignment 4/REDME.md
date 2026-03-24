# House Price Prediction: Linear Regression vs. Random Forest

## 🎯 Project Objective
The goal of this assignment is to implement and compare two machine learning models—**Linear Regression** and **Random Forest Regressor**—to predict house prices. By evaluating metrics like $R^2$ and RMSE, we determine which model handles the dataset's complexity more effectively.

## 🛠️ Implementation Details

### 1. Data Setup
- **Dataset:** `clean_house_l5_dataset.csv`
- **Target (y):** `Price`
- **Features (X):** All columns except `Price` and `LogPrice`.
- **Split:** 80% Training / 20% Testing (`random_state=42`).

### 2. Models Trained
- **Linear Regression:** Used as a baseline linear model.
- **Random Forest Regressor:** An ensemble model using 100 decision trees and `random_state=42`.



### 3. Evaluation Metrics
Both models were evaluated using:
- **R² (Coefficient of Determination)**
- **MAE (Mean Absolute Error)**
- **MSE (Mean Squared Error)**
- **RMSE (Root Mean Squared Error)**

## 📂 Submission Files
- `house_price_prediction.ipynb`: Jupyter Notebook containing the full code, model training, and performance metrics.
- `reflection_paper.md`: A detailed discussion comparing the two models, explaining the Random Forest algorithm, and final findings.

## 🚀 How to Run
1. Ensure you have the cleaned dataset (`clean_house_dataset.csv`) in the root directory.
2. Install required libraries:
   ```bash
   pip install pandas numpy scikit-learn
