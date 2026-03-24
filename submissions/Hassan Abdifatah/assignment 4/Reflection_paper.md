# Reflection Paper: House Price Prediction Analysis

## 1. Implementation Overview
In this assignment, I implemented a machine learning pipeline to predict house prices using two different regression algorithms: **Linear Regression** and **Random Forest Regressor**. 

The process involved:
- **Data Preparation:** Utilizing the cleaned dataset from Lesson 3, where `Price` was the target variable and features included vehicle age, mileage, and location.
- **Data Splitting:** Dividing the dataset into an 80/20 train-test split to ensure the model could be evaluated on unseen data.
- **Model Training:** Fitting both a baseline linear model and a complex ensemble model to the training data.

## 2. Understanding Random Forest
Random Forest is an **Ensemble Learning** technique used for both classification and regression. 

**How it works:**
- **Ensemble of Trees:** Instead of relying on a single Decision Tree, Random Forest builds multiple trees (in this case, 100).
- **Bagging:** Each tree is trained on a random subset of the data and a random selection of features.
- **Averaging:** For regression tasks, the Random Forest takes the predictions from all 100 trees and calculates their **average**. This process reduces the risk of overfitting and makes the model much more stable than a single tree.

## 3. Comparison of Models (Sanity Check)
During the "Sanity Check" on the test set, I observed the following differences in predictions:
- **Linear Regression:** Tended to provide "smoother" predictions but occasionally predicted values that were physically impossible (e.g., negative prices if the data was poorly scaled) because it tries to fit a straight line through the data.
- **Random Forest:** Generally stayed closer to the actual values in the test set. 
- **Finding:** The **Random Forest** model provided more realistic results. This is likely because house and car prices rarely follow a perfectly straight line; factors like "Location" and "Condition" interact in complex, non-linear ways that Random Forest captures better.

## 4. Metrics Discussion
Based on the printed output:
- **R² (R-Squared):** The Random Forest typically achieved a higher $R^2$ score, meaning it explained more of the variance in the house prices.
- **Error Metrics (MAE, RMSE):** The Random Forest showed lower Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE). 



This indicates that while Linear Regression is useful for understanding general trends, it has higher "bias." Random Forest has higher "variance" but provides much more accurate predictions for individual data points.

## 5. Final Findings & Preference
After analyzing both models, I prefer the **Random Forest Regressor** for price prediction tasks. 

**Reasoning:** Price datasets often contain outliers and non-linear relationships (for example, a car's price drops significantly in the first 2 years but levels off later). Random Forest handles these nuances far better than Linear Regression. While Linear Regression is faster to train, the superior accuracy and robustness of the Random Forest make it the better choice for high-stakes financial predictions like house or car prices.
