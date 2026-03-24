# Reflection Paper: House Price Prediction

## 1. Implementation Overview
In this assignment, I implemented house price prediction using two different supervised learning algorithms: **Linear Regression** and **Random Forest Regressor**. The project involved loading a cleaned dataset, splitting it into training (80%) and testing (20%) sets, and training both models to predict the continuous `Price` variable based on various house features.

## 2. Model Comparison
After evaluating the models on the test set, both provided reasonable predictions. However, the **Random Forest** model generally yielded more realistic results across the **3 sanity checks** and achieved better overall performance. This is because house price relationships are often non-linear and multi-faceted, which a single linear equation might struggle to capture fully compared to an ensemble approach.

## 3. Understanding Random Forest
**Random Forest** is an ensemble learning method that builds multiple **Decision Trees** during the training phase. Instead of relying on a single tree, it merges the predictions from all trees to produce a more stable and accurate result. For regression tasks, the final prediction is typically the average of the predictions from all individual trees in the "forest."

## 4. Performance Metrics Discussion
- **R² Score:** The Random Forest model typically achieves a higher $R^2$ score, meaning it explains a larger percentage of the variance in the target variable compared to Linear Regression.
- **Error Metrics (MAE, RMSE):** Random Forest tends to have lower Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE), indicating that its predictions are, on average, closer to the actual values.

## 5. Conclusion
Based on the results, I prefer the **Random Forest Regressor** for house price prediction tasks. Its ability to capture complex patterns and provide more accurate predictions makes it a superior choice over the simpler Linear Regression model for this specific dataset.
