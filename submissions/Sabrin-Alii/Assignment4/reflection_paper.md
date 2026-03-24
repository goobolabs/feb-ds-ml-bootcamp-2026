# Part B – Reflection Paper  
## Car Price Prediction Using Linear Regression and Random Forest  

### 1. What Did I Implement?

In this project, I built and evaluated two machine learning models to predict car prices that i used in assignment3: **Linear Regression (LR)** and **Random Forest Regressor (RF)**.

First, I prepared the dataset by cleaning duplicates and creating additional useful features such as:

- CarAge (calculated from Year)
- Km_per_year
- Is_Urban (derived from location)
- LogPrice (log transformation of price)

After preprocessing, the dataset contained 140 rows and 12 columns. I then split the data into:

- 80% Training data (112 rows)
- 20% Testing data (28 rows)

The models were trained using the training dataset and evaluated on the test dataset using performance metrics such as:

- R² Score
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)

Linear Regression was trained using `sklearn.linear_model.LinearRegression`, and Random Forest was trained using `sklearn.ensemble.RandomForestRegressor`.

---

### 2. Comparison of Models

After training both models, I evaluated them using performance metrics.

#### Linear Regression Results:
- R²: 0.436
- MAE: 1,428
- RMSE: 1,938

#### Random Forest Results:
- R²: 0.240
- MAE: 1,235
- RMSE: 2,249

From these results, Linear Regression had a higher R² score and lower RMSE compared to Random Forest. This means Linear Regression explained more of the variance in car prices.

However, when I performed the 3-row sanity check, Random Forest sometimes predicted values closer to the actual price. This shows that although RF had weaker overall metrics, it performed better in some individual cases.

Overall, Linear Regression gave more consistent and realistic results for this dataset.

---

### 3. Understanding Random Forest

Random Forest is an ensemble machine learning algorithm. Instead of building one single decision tree, it builds many decision trees and combines their predictions.

Here is how it works:

1. It randomly samples data from the training set (bootstrap sampling).
2. For each sample, it builds a decision tree.
3. Each tree makes its own prediction.
4. The final prediction is the average of all tree predictions (for regression problems).

This method reduces overfitting compared to a single decision tree because averaging many trees stabilizes predictions.

However, Random Forest usually performs better when:
- The dataset is large
- Relationships between features are complex and non-linear

In my case, the dataset was relatively small (140 rows), which may explain why Random Forest did not outperform Linear Regression.

---

### 4. Metrics Discussion

The R² score measures how much of the variation in house prices is explained by the model.

- Linear Regression R² = 0.436  
- Random Forest R² = 0.240  

This means Linear Regression explained about 43.6% of the variation in prices, while Random Forest explained only 24%.

MAE measures the average prediction error in dollars.  
RMSE penalizes large errors more heavily.

Although Random Forest had slightly lower MAE, it had a higher RMSE and lower R². This suggests that:

- Linear Regression performed more consistently overall.
- Random Forest may have made larger prediction errors on some houses.

Strengths and weaknesses:

**Linear Regression**
- Works well with small datasets.
- Performs better when relationships are mostly linear.
- Easier to interpret.

**Random Forest**
- Handles non-linear relationships.
- More robust to noise.
- Requires more data to perform optimally.

---

### 5. My Findings

Based on my results, I prefer Linear Regression for this specific car price prediction task. The dataset was relatively small, and the relationships between features and price appeared mostly linear. Linear Regression achieved a higher R² score and lower RMSE, making it more reliable overall.

While Random Forest is a powerful and flexible algorithm, it did not perform better in this case due to limited data size. If the dataset were larger and more complex, Random Forest might have outperformed Linear Regression.

In conclusion, model selection depends on dataset size and structure. For small, structured datasets with mostly linear relationships, Linear Regression can be more effective. For larger datasets with complex patterns, Random Forest would likely be a better choice.