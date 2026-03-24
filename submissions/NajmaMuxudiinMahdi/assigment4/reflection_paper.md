# 🎓 Reflection Paper – House Price Prediction

---

## 🟦 1️⃣ What Did I Implement?

In this assignment, I implemented a house price prediction system using two regression models: **Linear Regression** and **Random Forest Regressor**.

- I loaded the cleaned dataset (`Housing_Clean.csv`) prepared in Lesson 3.  
- Target variable: `Price`  
- Features: all columns except `Price` and `LogPrice`  
- Split: 80% training, 20% testing (`random_state=42`)  
- Models trained:  
  - Linear Regression  
  - Random Forest Regressor (`n_estimators=100`)  
- Evaluation metrics: R², MAE, MSE, RMSE

---

## 🟩 2️⃣ Comparison of Models

**Single-row sanity check:**  

- **Linear Regression:** Predictions follow a linear trend, may not capture complex relationships.  
- **Random Forest:** Predictions closer to actual prices, handles non-linear patterns well.  

**Conclusion:** Random Forest produced more realistic predictions because it captures non-linear interactions between features.

---

## 🟧 3️⃣ Understanding Random Forest

- **Random Forest** is an ensemble learning algorithm.  
- Works by:  
  - Building multiple Decision Trees on random subsets of data  
  - Averaging predictions from all trees (for regression)  
- Advantages:  
  - Reduces overfitting  
  - Captures non-linear relationships better than Linear Regression

---

## 🟨 4️⃣ Metrics Discussion

- Random Forest had **higher R²** and **lower MAE/RMSE**, indicating better accuracy.  
- Linear Regression is simple and interpretable but may miss non-linear patterns.  
- Metrics help understand **strengths and weaknesses** of each model:
  - LR → good for understanding relationships  
  - RF → better predictive performance

---

## 🟪 5️⃣ My Findings

- I prefer **Random Forest** for house price prediction because it provides more accurate and realistic predictions.  
- Linear Regression is useful for interpretability, but Random Forest better handles complex feature interactions.  
- Overall, Random Forest combines multiple trees to reduce error and capture variance effectively.

---

*End of Reflection*