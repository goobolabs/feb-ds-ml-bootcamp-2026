# Reflection Paper — House Price Prediction

## What Did I Implement?

In this assignment, I implemented a house price prediction system using two machine learning models: Linear Regression and Random Forest Regressor. First, I loaded the cleaned dataset and prepared the features (X) by removing the Price and LogPrice columns, while the target variable (y) was the Price column. Then, I split the dataset into training and testing sets using an 80/20 split with a random state of 42 to ensure reproducibility.

After preparing the data, I trained a Linear Regression model to learn the linear relationship between the features and house prices. Next, I trained a Random Forest Regressor with 100 decision trees to capture more complex patterns in the data. Finally, I evaluated both models using performance metrics including R², Mean Absolute Error (MAE), Mean Squared Error (MSE), and Root Mean Squared Error (RMSE), and performed a single-row sanity check to compare predictions with the actual price.

---

## Comparison of Models

During the sanity check, I compared predictions from both models using a single test sample. The actual house price was **$554,800**. The Linear Regression model predicted **$594,041**, while the Random Forest model predicted **$557,028**.

The Random Forest prediction was much closer to the actual price, with only a small difference, while Linear Regression overestimated the price by a larger margin. This shows that Random Forest produced more realistic results because it can capture non-linear relationships and interactions between features, whereas Linear Regression assumes a strictly linear relationship.

---

## Understanding Random Forest

Random Forest is an ensemble learning algorithm that combines multiple decision trees to make predictions. Instead of relying on a single model, it builds many trees using random subsets of the data and features.

Each decision tree makes its own prediction, and the final prediction is calculated by averaging the results of all trees. This approach reduces overfitting and improves accuracy because errors from individual trees tend to cancel out. As a result, Random Forest is powerful for handling complex datasets with non-linear patterns.

---

## Metrics Discussion

Based on the evaluation results:

* **Linear Regression** achieved an **R² of 0.848**, **MAE of 63,086**, and **RMSE of 75,624**.
* **Random Forest** achieved a higher **R² of 0.859**, lower **MAE of 52,524**, and lower **RMSE of 72,686**.

The higher R² value for Random Forest indicates that it explains more variance in house prices compared to Linear Regression. Additionally, the lower error metrics (MAE and RMSE) show that Random Forest predictions are generally closer to the actual prices.

These results suggest that Linear Regression is simpler and easier to interpret but may not capture complex relationships in the data. On the other hand, Random Forest is more flexible and accurate but less interpretable.

---

## My Findings

Based on the results, I prefer the Random Forest model for house price prediction because it provided more accurate predictions and lower error values. The sanity check also confirmed that Random Forest predictions were closer to the actual price compared to Linear Regression.

Overall, while Linear Regression is useful for understanding basic relationships and is computationally efficient, Random Forest is better suited for real-world prediction tasks where data relationships are complex. Therefore, Random Forest would be my preferred choice for building reliable house price prediction systems.

---


