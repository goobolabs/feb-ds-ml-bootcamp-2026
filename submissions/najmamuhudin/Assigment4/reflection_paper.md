# Reflection Paper: House Price Prediction Analysis

## 1. Implementation Overview

In this project, I developed a machine learning pipeline to predict house prices using the `clean_house_l5_dataset.csv` dataset. The implementation involved several key steps:

**Data Preparation:**  
I separated the dataset into features (`X`) and the target variable (`y`), specifically excluding `Price` and `LogPrice` from the feature set to avoid data leakage.

**Data Splitting:**  
Using `train_test_split`, I reserved 20% of the data for testing to ensure an unbiased evaluation.

**Model Training:**  
I trained two distinct algorithms:

- **Linear Regression (LR):** A baseline statistical model that assumes a linear relationship between features and price.  
- **Random Forest (RF):** A non-linear ensemble model using 100 decision trees to capture complex patterns in the housing data.

---

## 2. Comparison of Models

**Sanity Check Observations:**  
During a single-row sanity check, I compared the predictions of both models against a known actual price.

**Differences in Predictions:**  

- **Linear Regression:** Produced estimates following a straight-line trend. It sometimes underestimates or overestimates prices for houses with extreme features because it cannot fully capture non-linear relationships.  
- **Random Forest:** Produced predictions closer to the actual value by averaging multiple decision trees’ outputs, which makes it robust to outliers and better at capturing complex interactions between features.

**Which model was more realistic?**  
Random Forest consistently gave more realistic predictions. House prices rarely change in perfect linear ways, and RF captures these nuances better than LR.

---

## 3. Understanding Random Forest

**What is Random Forest?**  
Random Forest is an ensemble machine learning model that builds multiple decision trees and combines their predictions. It is widely used for regression and classification tasks because it reduces overfitting compared to a single decision tree.

**How does it work?**  
Each decision tree in the forest is trained on a random subset of the data and features (bagging). For regression, the final prediction is the average of all trees’ outputs. This averaging reduces variance and improves generalization, allowing the model to handle complex, non-linear patterns in the data.

---

## 4. Metrics Discussion

**Performance Metrics:**

| Model             | R²   | MAE     | RMSE    |
|------------------|------|---------|---------|
| Linear Regression | 0.848 | 63,086  | 75,624  |
| Random Forest     | 0.859 | 52,524  | 72,686  |

**Interpretation:**  
- Random Forest had slightly better R², meaning it explains more variance in house prices.  
- Lower MAE and RMSE indicate RF’s predictions are closer to actual prices on average.

**Strengths and Weaknesses:**  
- Linear Regression is simpler and interpretable but struggles with non-linear relationships.  
- Random Forest captures complexity well but can be less interpretable and slower to train.

---

## 5. Findings and Reflections

Based on the analysis, I prefer **Random Forest** for house price prediction. It consistently provided more accurate and realistic estimates, especially when handling features that interact in non-linear ways. While Linear Regression is easier to understand and computationally cheaper, its simplicity makes it less reliable in complex datasets like real estate, where prices depend on many interacting factors.

Random Forest’s ensemble approach balances variance and bias, making it robust to outliers and capable of capturing subtle patterns in the data. Therefore, for practical applications where accuracy matters, Random Forest is the preferred choice.
