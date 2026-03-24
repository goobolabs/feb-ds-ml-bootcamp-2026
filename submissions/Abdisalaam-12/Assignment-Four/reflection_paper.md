

# House Price Prediction Using Linear Regression and Random Forest

## 1. What Did I Implement?

In this assignment, I implemented two regression models to predict house prices using a cleaned dataset. The target variable was **Price**, and all other columns except **Price** and **LogPrice** were used as input features.

First, I split the dataset into 80% training data and 20% testing data using `random_state=42` to ensure reproducibility. Then, I trained two models:

- Linear Regression model  
- Random Forest Regressor with 100 trees  

After training, I evaluated both models using **R², MAE, MSE, and RMSE** metrics.

---

## 2. Comparison of Models

When performing the sanity check using a single row from the test set, the predictions from both models were close to the actual value. However, Random Forest predictions were generally closer to the real house price.

Linear Regression sometimes slightly overestimated or underestimated prices because it assumes a strictly linear relationship between features and price. Random Forest provided more realistic results because it can capture complex, non-linear patterns in the data.

---

## 3. Understanding Random Forest

Random Forest is an ensemble learning algorithm. It builds multiple decision trees during training and combines their predictions.

Instead of relying on a single tree, Random Forest:

- Creates many decision trees using different random samples of the data.  
- Each tree makes its own prediction.  
- The final prediction is the average of all trees (for regression).  

This reduces overfitting and improves model stability and accuracy.

---

## 4. Metrics Discussion

In my results, Random Forest achieved a higher R² score and lower MAE and RMSE values compared to Linear Regression.

- Higher R² means the model explains more variance in house prices.  
- Lower MAE and RMSE mean smaller prediction errors.  

This shows that Random Forest is better at capturing complex relationships in the housing data. However, Linear Regression is simpler, faster, and easier to interpret.

---

## 5. My Findings

Based on the evaluation metrics and prediction comparisons, I prefer Random Forest for house price prediction. It provides more accurate and stable predictions because it models non-linear relationships effectively.

However, Linear Regression is still useful when interpretability is important and when the relationship betweeen variables is mostly linear.

In real-world applications, Random Forest would be more releiable for price prediction tasks.
