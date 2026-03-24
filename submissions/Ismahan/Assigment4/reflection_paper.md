# Assignment: House Price Prediction Reflection Paper

**Student Name:** Ismahan Ahmed Osman 
**Date:** September 20, 2025  
**Course:** Data Science / Machine Learning  

---

## 1. What did I implement?
In this assignment, I implemented a house price prediction system using two popular machine learning algorithms:
* **Linear Regression (LR):** A fundamental statistical model that assumes a linear relationship between input features and the house price.
* **Random Forest Regressor (RF):** An ensemble learning method that builds multiple decision trees and averages their results to improve accuracy.

I used the `scikit-learn` library to train these models on a cleaned dataset, splitting the data into **80% training** and **20% testing** sets.

---

## 2. Comparison of Models (Based on Results)

### Model Performance Summary:
| Metric | Linear Regression | Random Forest |
| :--- | :--- | :--- |
| **R² (Accuracy)** | 0.848 | **0.859** |
| **MAE (Mean Absolute Error)** | 63,086 | **52,524** |
| **RMSE (Root Mean Squared Error)** | 75,624 | **72,686** |

### Single-row Sanity Check:
* **Actual Price:** $642,500
* **LR Prediction:** $656,755 (Diff: ~$14,255)
* **RF Prediction:** $789,031 (Diff: ~$146,531)

**Observation:** Even though Random Forest has better overall metrics (higher $R^2$ and lower MAE), in this specific sanity check, **Linear Regression** was much closer to the actual price. This shows that while one model is better on average, individual predictions can still vary.

---

## 3. Understanding Random Forest
**What is Random Forest?**
Random Forest is an "Ensemble" model, meaning it combines the strength of many learners to make a final decision. 

**How does it work?**
1. It creates a "forest" of many **Decision Trees**.
2. Each tree is trained on a random subset of the data and features.
3. When making a prediction, every tree in the forest gives its own result.
4. The model then takes the **average** of all those results. This prevents the model from being swayed by noise in the data and helps it capture non-linear relationships.



---

## 4. Metrics Discussion
* **R² Score:** The Random Forest model achieved a higher $R^2$ (0.859 vs 0.848), meaning it explains the variance in house prices slightly better than Linear Regression.
* **Error Metrics (MAE & RMSE):** Random Forest has a significantly lower **MAE (52,524)** compared to Linear Regression (63,086). This tells us that, on average, Random Forest predictions are off by about $10,500 less than the Linear model.

---

## 5. My Findings
After analyzing the results, I prefer the **Random Forest Regressor** for overall price prediction. Although Linear Regression was closer in our single-row test, the Random Forest model is more consistent across the entire dataset, as proven by the lower MAE and RMSE. 

For a real estate business, having a model that is more accurate on average (Random Forest) is usually more valuable than one that gets lucky on a single house.