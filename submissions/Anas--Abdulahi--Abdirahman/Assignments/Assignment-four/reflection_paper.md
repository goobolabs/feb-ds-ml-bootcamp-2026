# Part B – Reflection Paper  
## House Price Prediction Using Linear Regression and Random Forest

---

## 1. What I Implemented

In this assignment, I built two supervised machine learning models to predict house prices: Linear Regression and Random Forest Regressor.

First, I prepared the dataset by selecting all numerical and encoded categorical features as input variables (X) and used house price as the target variable (y). I split the dataset into training and testing sets using an 80/20 split.

I then trained:

- A **Linear Regression** model using scikit-learn’s `LinearRegression()`
- A **Random Forest Regressor** using `RandomForestRegressor()` with 100 trees

After training, I evaluated both models using R², Mean Absolute Error (MAE), and Root Mean Squared Error (RMSE). I also performed sanity checks by predicting individual house prices from the test set and comparing them to actual values.

---

## 2. Comparison of Models

When testing individual samples (sanity checks), both models produced predictions that were reasonably close to the actual house prices. However, the Random Forest predictions were generally closer to the true values, especially for houses with more complex feature combinations (e.g., size, age, and location interactions).

The Random Forest model gave more realistic results overall because it can capture non-linear relationships between features and price. In contrast, Linear Regression assumes a strictly linear relationship, which limits its flexibility when patterns in the data are more complex.

---

## 3. Understanding Random Forest

Random Forest is an ensemble learning method based on multiple decision trees.

Instead of building a single model, Random Forest builds many decision trees using random subsets of the data and random subsets of features. Each tree makes its own prediction. For regression problems like house price prediction, the final output is the average of all tree predictions.

This approach reduces overfitting and improves prediction stability. Because different trees capture different patterns in the data, the combined prediction is usually more accurate and more robust than a single model.

In simple terms:
- One tree may overfit.
- Many trees averaged together create a stronger and more reliable model.

---

## 4. Metrics Discussion

The evaluation results were:

### Linear Regression
- R² = 0.84  
- MAE = 63,086  
- RMSE = 75,624  

### Random Forest
- R² = 0.86  
- MAE = 52,524  
- RMSE = 72,686  

Random Forest had a higher R² score and lower MAE and RMSE values. This indicates that Random Forest explains more variance in house prices and makes smaller prediction errors on average.

The results suggest:

**Linear Regression strengths:**
- Simple and interpretable
- Fast to train
- Works well when relationships are mostly linear

**Linear Regression weaknesses:**
- Cannot capture complex, non-linear patterns
- Sensitive to feature interactions

**Random Forest strengths:**
- Handles non-linear relationships
- Captures feature interactions
- More accurate and robust

**Random Forest weaknesses:**
- Less interpretable
- Slightly more computationally expensive

---

## 5. My Findings

Based on the results, I prefer the Random Forest model for house price prediction. Although Linear Regression performed well and explained a large portion of the variance (84%), Random Forest consistently produced lower error metrics and slightly higher predictive power.

The improvement in MAE (over $10,000 reduction in average error) is meaningful in real estate pricing. Since housing markets often involve complex relationships between features like size, location, and age, a model that can capture non-linear patterns is more appropriate.

Overall, while Linear Regression is a strong baseline model and useful for interpretability, Random Forest is better suited for practical house price prediction tasks because of its higher accuracy and robustness.

