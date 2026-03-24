# Reflection Paper: House Price Prediction


---

## What did you implement?

I implemented a straightforward supervised learning pipeline that trains two models to predict house prices from a cleaned, feature-engineered dataset (`clean_house_l5_dataset.csv`). The script does the following: loads the CSV into a `pandas` DataFrame, separates features (`X`) from the target price (`y`), performs a train/test split (80/20), fits two models (Linear Regression and Random Forest Regressor), evaluates both on the held-out test set with standard regression metrics (R², MAE, MSE, RMSE), and runs a single-row sanity check to compare individual predictions.

## How the models were trained

### Data split and setup

* The dataset is read into `df` and `X = df.drop(columns=["Price", "LogPrice"])` while `y = df["Price"]`.
* A reproducible train/test split is made with `train_test_split(X, y, test_size=0.2, random_state=42)` so that evaluation is fair and repeatable.

### Linear Regression

* The Linear Regression model (`sklearn.linear_model.LinearRegression`) was instantiated and trained with `lr.fit(X_train, y_train)`.
* This model learns a single weight for each feature and a bias term, producing predictions as a linear combination of input features.
* Linear Regression serves as a simple, interpretable baseline.

### Random Forest

* The Random Forest model (`sklearn.ensemble.RandomForestRegressor`) was created with `n_estimators=100` and `random_state=42`, then trained via `rf.fit(X_train, y_train)`.
* Random Forest builds an ensemble of decision trees, each grown on a bootstrap sample of the training data and considering a random subset of features at each split. Predictions are the average of the trees’ outputs.
* The forest is able to model nonlinear interactions and feature thresholds that linear models cannot.

## Comparison of models — single-row (sanity) check

> **Note:** This write-up is qualitative. If you want exact numeric answers (actual printed outputs from the script), paste the printed values here or run the script and I will update the document with the actual numbers.

For the single-row sanity check (the script uses `i = 0` on `X_test`):

* **How predictions typically differ:**

  * Linear Regression gives a prediction that is a global linear extrapolation based on the learned coefficients. If the particular house has feature values near the training mean, LR’s prediction will be relatively smooth and often conservative; if the house is an outlier in one or more features, LR may extrapolate and produce a value that is not realistic.
  * Random Forest tends to give predictions that are informed by similar houses seen during training. Because the trees partition feature space into regions, RF predictions are usually bounded by the training-range of prices and often reflect local patterns (piecewise-constant behavior). This makes RF less likely to produce extreme extrapolations.

* **Which model is more realistic and why:**

  * In most practical housing datasets with nonlinearities, interactions, and mixed feature types, **Random Forest** produces more realistic single-row predictions. It captures nonlinear dependencies and uses local neighbors in feature space, so its output often aligns better with observed prices for similarly featured houses.

## Understanding Random Forest (in plain words)

* **What is Random Forest?**
  A Random Forest is an ensemble method composed of many decision trees. Each tree is a simple model that splits the feature space into regions and predicts a constant (or mean) price for each region.

* **How it works:**

  * **Bootstrap sampling:** each tree is trained on a random sample (with replacement) of the training data.
  * **Random feature selection:** when splitting a node, the tree considers only a random subset of features. This decorrelates the trees and reduces overfitting.
  * **Ensembling / averaging:** to predict, the forest queries every tree and averages their predictions; averaging reduces variance and generally improves generalization.

## Metrics discussion

* **R² (coefficient of determination):** indicates the fraction of variance in the target explained by the model. Higher is better (max 1.0).
* **MAE (Mean Absolute Error):** average absolute difference between predicted and actual prices — easy to interpret in dollars.
* **RMSE (Root Mean Squared Error):** square root of average squared error — more sensitive to large errors.

**Typical outcome and interpretation:**

* If **Random Forest** shows a higher R² and lower MAE/RMSE than Linear Regression, this suggests the problem has important nonlinear structure and interactions that RF captures but LR cannot. RF’s lower errors indicate better average and large-error performance.
* If **Linear Regression** performs similarly to RF (comparable R² and errors), the dataset’s relationships are likely close to linear or the feature engineering already made relationships linear.
* If LR performs better (rare on complex real-world data), it may indicate overfitting by RF (insufficient regularization / too-deep trees) or insufficient training data for the forest.

## Findings & recommendation

For typical house-price prediction tasks, I prefer **Random Forest** as the primary production model because it reliably captures nonlinear relationships, handles mixed feature types without heavy scaling, and produces robust predictions that stay within the range of observed prices. It usually yields better R² and lower MAE/RMSE than a plain Linear Regression baseline.

That said, Linear Regression remains valuable as a baseline and for interpretability: its coefficients make it easy to explain how each feature affects price. Best practice is to use both: start with LR to build intuition, then use RF (or gradient-boosted trees) for improved predictive accuracy, and finally apply cross-validation and hyperparameter tuning.

---


*End of reflection.*
