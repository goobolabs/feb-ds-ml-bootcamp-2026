# Reflection Paper: House Price Prediction Analysis


---

## 1. Project Implementation
In this project, I developed a machine learning workflow to predict house prices using two different regression algorithms. Following the data cleaning process from Lesson 3, I used the `clean_house_dataset.csv` to build and compare predictive models.

* **Target Variable ($y$):** The `Price` column.
* **Features ($X$):** All available columns except `Price` and `LogPrice`.
* **Methodology:** I split the data into **80% training** and **20% testing** sets using `random_state=42`. I then trained a **Linear Regression** model (as a baseline) and a **Random Forest Regressor** (an ensemble method) to compare their predictive power.

---

## 2. Comparison of Models
When performing the **Single-row Sanity Check**, I noticed distinct differences in how the models handled the data:

* **Linear Regression:** This model often predicted a more "centralized" price. Since it tries to fit a straight line through the data, it can struggle with houses that have unique luxury features or are located in highly specific high-value pockets.
* **Random Forest:** This model's predictions were generally closer to the actual price in the test set. It was better at picking up on specific "rules" (e.g., *if square footage is > 2000 AND bedrooms > 3, then price increases significantly*).
* **Realistic Results:** The **Random Forest** provided more realistic results. House pricing is rarely a simple linear addition; features interact with each other in complex ways that a forest of trees can capture much more effectively than a single line.

---

## 3. Understanding Random Forest



**What is it?** Random Forest is an **Ensemble Learning** technique. Instead of relying on a single model to make a prediction, it combines the outputs of many individual Decision Trees to reach a single result.

**How does it work?**
1. **Bootstrap Aggregating (Bagging):** The algorithm creates multiple random subsets of the training data.
2. **Individual Trees:** A Decision Tree is grown for each subset. To ensure variety, each tree only considers a random selection of features at each split.
3. **Averaging:** For a regression task, each tree outputs a predicted price. The Random Forest then calculates the **average** of all these individual predictions. This "wisdom of the crowd" approach reduces the risk of overfitting and makes the model much more stable.

---

## 4. Metrics Discussion
Based on the performance metrics generated in the Jupyter Notebook:

| Metric | Linear Regression | Random Forest |
| :--- | :--- | :--- |
| **$R^2$ Score** | Lower (e.g., 0.84) | Higher (e.g., 0.86) |
| **MAE (Mean Absolute Error)** | Higher | Lower |
| **RMSE (Root Mean Squared Error)** | Higher | Lower |

**Analysis:**
* **Linear Regression Strengths:** It is simple and highly interpretable. We can easily see the "weight" of each feature. However, its weakness is its "bias"—it assumes the world is linear, which it often isn't.
* **Random Forest Strengths:** It consistently achieved a higher $R^2$ and lower error (MAE/RMSE). This tells us that the model is more flexible and accurate. Its main weakness is that it is a "black box," making it harder to explain exactly *why* a specific price was chosen compared to a simple linear equation.

---

## 5. Findings & Conclusion
After evaluating both models, I prefer the **Random Forest Regressor** for house price prediction. 

The housing market is driven by non-linear trends—for example, the jump in value between a 2-bedroom and 3-bedroom home is often larger than the jump between a 4-bedroom and 5-bedroom home. Random Forest handles these "thresholds" and interactions automatically. While Linear Regression is a vital tool for understanding general trends, Random Forest provides the precision and robustness required for reliable real-world price estimates.