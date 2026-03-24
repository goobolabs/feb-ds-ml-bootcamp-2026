# Reflection Paper – House Price Prediction

## 1. What I Implemented
In this assignment, I built two regression models: Linear Regression and Random Forest to predict house prices.

I used a cleaned dataset, then separated:
- Target (y): Price  
- Features (X): all other columns except Price and LogPrice  

After that, I split the data into training (80%) and testing (20%) using random_state=42.

Then I trained:
- Linear Regression model  
- Random Forest Regressor (100 trees)

Finally, I evaluated both models using R², MAE, MSE, and RMSE.

---

## 2. Comparison of Models
From the test results and sanity check, the predictions from both models were not the same.

Linear Regression gives straight-line predictions, so it sometimes misses complex patterns.

Random Forest gave predictions closer to the actual price in most cases because it can handle more complex relationships.

So, Random Forest produced more realistic results.

---

## 3. Understanding Random Forest
Random Forest is a model that uses many decision trees.

Each tree makes a prediction, and the final result is the average of all trees.

This helps reduce errors and makes the model more accurate.

---

## 4. Metrics Discussion
I used these metrics:

- R² → shows how well the model explains the data  
- MAE → average error  
- RMSE → error size in real units  

The better model is the one with:
- Higher R²  
- Lower MAE and RMSE  

Random Forest performed better based on these metrics.

---

## 5. Final Findings
Random Forest is better for this task because house prices depend on many factors and are not purely linear.

Linear Regression is simple but limited.

Random Forest handles complex data better, so it gives more accurate predictions.

Therefore, Random Forest is the preferred model for house price prediction.
