# Reflection Paper – House Price Prediction

## 1. What I Implemented
In this assignment, I built two predictive models — **Linear Regression** and **Random Forest Regressor** — to estimate house prices using a cleaned dataset. I prepared the features by excluding `Price` and `LogPrice`, split the data into training and testing sets (80/20), and trained both models. Finally, I evaluated their performance using metrics such as **R², MAE, MSE, and RMSE**, and performed a single-row sanity check to compare actual versus predicted values.

---

## 2. Comparison of Models
During the sanity check, both models produced predictions close to the actual price, but with noticeable differences.  
- **Linear Regression** tended to give smoother, generalized predictions.  
- **Random Forest** produced results that were closer to the actual values, especially when the data had non-linear relationships.  

Overall, Random Forest predictions felt more realistic because the model captures complex feature interactions better than a simple linear fit.

---

## 3. Understanding Random Forest
Random Forest is an **ensemble learning method** that combines multiple decision trees. Each tree is trained on a random subset of the data and features. When making predictions, the forest averages the outputs of all trees (for regression) or takes a majority vote (for classification).  
This approach reduces overfitting, improves accuracy, and makes the model more robust compared to a single decision tree.

---

## 4. Metrics Discussion
When comparing metrics:  
- **Random Forest** achieved a higher R² and lower error values (MAE, RMSE).  
- **Linear Regression** performed reasonably well but struggled with capturing non-linear patterns in the data.  

This shows that Linear Regression is strong for simple, linear relationships, while Random Forest excels in handling complex, non-linear interactions.

---

## 5. My Findings
Based on the results, I prefer **Random Forest** for house price prediction. It consistently produced better metrics and more realistic predictions during the sanity check. While Linear Regression is easier to interpret and faster to train, Random Forest’s ability to model complex relationships makes it more suitable for real-world housing data.  

In conclusion, Random Forest is the stronger choice for this task because it balances accuracy, robustness, and practical applicability in predicting house prices.
