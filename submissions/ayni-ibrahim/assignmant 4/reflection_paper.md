Reflection Paper – House Price Prediction

1. What Did I Implement?

In this assignment, I implemented two machine learning models to predict house prices: Linear Regression and Random Forest Regressor.
First, I loaded a cleaned house dataset and selected Price as the target variable. All remaining columns, except LogPrice, were used as input features.

The dataset was divided into 80% training data and 20% testing data. Both models were trained using the training set and evaluated on the test set using standard performance metrics.

2. Comparison of Models (Sanity Check)

During the sanity check, predictions were made on individual rows from the test dataset.
The results showed that Linear Regression sometimes produced predictions that were farther from the actual house prices. In contrast, Random Forest predictions were generally closer to the real values.

Overall, Random Forest provided more realistic predictions because it can model complex relationships in the data more effectively.

3. Understanding Random Forest

Random Forest is a machine learning algorithm that combines multiple decision trees into a single model.
Each decision tree makes its own prediction, and the final output is obtained by averaging the predictions of all trees.

This approach helps reduce errors and improves model performance, especially when the relationship between features and the target variable is not linear.

4. Metrics Discussion

Based on the evaluation results, Random Forest achieved a higher R² score and lower MAE and RMSE values compared to Linear Regression.
This indicates that Random Forest explained the variation in house prices more accurately and produced smaller prediction errors.

Linear Regression is simple and easy to interpret, but it is less effective when the data contains complex patterns.

5. Final Findings

Based on the results of this experiment, Random Forest is preferred for house price prediction because it produced more accurate and realistic results.
However, Linear Regression remains useful as a baseline model due to its simplicity and fast training time.

In conclusion, Random Forest is more suitable for real-world house price prediction tasks where multiple factors influence prices.
