# 🎓 Assignment – House Price Prediction with Linear Regression & Random Forest
Due: Tuesday, September 18, 2025 — 12:00 PM (Africa/Mogadishu / EAT)

## **Part A – Practical (Jupyter Notebook)**

**Objective:**
In this part, you will implement **house price prediction** using **Linear Regression** and **Random Forest Regressor**. You will evaluate both models and compare their performance.

---

### **Instructions**

1. **Notebook Setup**

   * Create a Jupyter Notebook named:
     `house_price_prediction.ipynb`.

2. **Load Dataset**

   * Use the cleaned dataset you generated in **Lesson 3** (`clean_house_dataset.csv`).

3. **Prepare Features & Target**

   * Target (`y`) = `Price`
   * Features (`X`) = all other columns except `Price` and `LogPrice`.

4. **Split Data**

   * Split into **80% training** and **20% testing**.
   * Use `random_state=42`.

5. **Train Models**

   * Train a **LinearRegression** model.
   * Train a **RandomForestRegressor** (use `n_estimators=100`, `random_state=42`).

6. **Evaluate Performance**

   * Print **R², MAE, MSE, RMSE** for both models using a helper function.

7. **Single-row Sanity Check**

   * Pick one row from the test set (`X_test.iloc[[i]]`) and compare actual price with predictions from both models.
---

### **Expected Output**

* Metrics printed for both models, e.g.:

  ```
  Linear Regression Performance:
    R²   : 0.84
    MAE  : 63,086
    RMSE : 75,624

  Random Forest Performance:
    R²   : 0.86
    MAE  : 52,524
    RMSE : 72,686
  ```
* A single-row prediction from test set (Actual vs Predicted).

---

## **Part B – Reflection Paper**

Write a short paper (1–2 pages, Markdown or PDF) answering the following:

1. **What did you implement?**

   * Briefly describe how you trained Linear Regression and Random Forest to predict house prices.

2. **Comparison of Models:**

   * When you tested on **3 Sanity Check**, how did predictions differ?
   * Which model gave more **realistic results**? Why?

3. **Understanding Random Forest:**

   * Explain in your own words:

     * What is Random Forest?
     * How does it work (ensemble of decision trees, averaging predictions)?

4. **Metrics Discussion:**

   * Which model (LR or RF) had better **R²** and **error metrics** (MAE, RMSE)?
   * What does that tell you about the strengths and weaknesses of each model?

5. **Your Findings:**

   * Summarize in 1–2 paragraphs which model you prefer for price prediction models and why.

---

### **Submission Format**

* `house_price_prediction.ipynb` (with all code + results).
* `reflection_paper.pdf` or `reflection_paper.md` (your discussion).

---
