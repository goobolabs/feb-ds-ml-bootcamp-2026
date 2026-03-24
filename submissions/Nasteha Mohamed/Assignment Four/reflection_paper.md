1. What did you implement?

###  In this assignment, I trained two regression models — Linear Regression and Random Forest — to predict car prices using a cleaned dataset. I prepared features and target, split the data into training and testing sets, trained both models, and evaluated them using R², MAE, MSE, and RMSE.

## Comparison of Models

### During testing and sanity check, Random Forest predictions were usually closer to the actual car price. Linear Regression sometimes overestimated or underestimated because it assumes a linear relationship, while car prices depend on more complex patterns.

- Random Forest gave more realistic predictions because it averages many decision trees and captures non-linear relationships.

## Understanding Random Forest

- Random Forest is an ensemble model made of many decision trees. Each tree learns from a random sample of the dataset, and the final prediction is the average of all trees. This reduces overfitting and improves prediction accuracy.

## Metrics Discussion

- Random Forest achieved higher R² and lower MAE and RMSE compared to Linear Regression. This shows that Random Forest explained  more variation in car prices and produced more accurate predictions.

- Linear Regression is simple and fast but cannot capture complex feature interactions, while Random Forest is more powerful but  computationally heavier.

## My Findings

### Based on the results, Random Forest is better for car price prediction because it produces more accurate and stable predictions. It handles non-linear relationships such as car age, mileage, and location better than Linear Regression.

- However, Linear Regression is still useful as a baseline model and for understanding feature relationships