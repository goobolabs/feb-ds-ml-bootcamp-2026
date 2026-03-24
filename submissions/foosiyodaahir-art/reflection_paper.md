 Car Price Prediction Using Linear Regression and Random Forest
 
 1. What Did I Implement?

In this assignment, I implemented two regression models to predict car prices using a cleaned dataset. The target variable was **Price**, and all other columns except **Price** and **Log_price** were used as input features.

First, I split the dataset into 80% training data and 20% testing data using `random_state=42` to ensure reproducibility. Then, I trained two models:

- Linear Regression model  
- Random Forest Regressor  

After training, I evaluated both models using **R², MAE, MSE, and RMSE** metrics.

 2. Comparison of Models

When comparing the predictions from both models, Random Forest generally produced results closer to the actual car prices.
Linear Regression assumes a linear relationship between the features and car price. However, car pricing often depends on complex factors such as brand, year, mileage, engine size, and condition. Because of this, Linear Regression may sometimes overestimate or underestimate prices.
Random Forest performed better because it can capture non-linear patterns and interactions between features.

3. Understanding Random Forest
Random Forest is an ensemble learning algorithm that builds multiple decision trees and combines their predictions.
Instead of relying on a single model:

- It creates many decision trees using random subsets of data.  
- Each tree makes its own prediction.  
- The final prediction is the average of all trees (for regression tasks).  

This approach reduces overfitting and improves prediction accuracy.

 4. Metrics Discussion
The evaluation metrics showed that Random Forest achieved:

- Higher R² score  
- Lower MAE  
- Lower RMSE  

A higher R² indicates that the model explains more variance in car prices. Lower MAE and RMSE mean the prediction errors are smaller.

This confirms that Random Forest is more accurate for this dataset.

 5. Reflection and Conclusion

Through this project, I learned how to:

- Prepare and split data for machine learning  
- Train regression models  
- Evaluate model performance using multiple metrics  
- Compare different algorithms  

Based on the results, Random Forest is more reliable for car price prediction because it captures complex relationships between features.

However, Linear Regression remains useful because it is simple, fast, and easy to interpret.

In real-world applications, choosing the best model depends on the dataset and business requirements.
