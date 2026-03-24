# 🎓 Reflection: House Price Prediction
**By Atika Isse Ali**

---

## 1. Project Implementation 🛠️
In this assignment, I successfully built a machine learning pipeline to predict prices. My process included:
* **Data Splitting**: Used an **80/20 train-test split** to ensure the model was evaluated on unseen data.
* **Model Comparison**: Implemented and compared two different algorithms: **Linear Regression** and **Random Forest Regressor**.

---

## 2. Comparison of Models 📊
The performance results between the two models were significantly different:

### **Model Metrics**
| Metric | Linear Regression | **Random Forest** |
| :--- | :--- | :--- |
| **R² Score** | -0.023 | **0.791** |
| **Prediction Accuracy** | Poor | **Strong** |

> **Sanity Check Analysis**: On a specific test row with an actual price of **$4,171**, the Random Forest predicted **$3,339** (fairly close), while Linear Regression predicted **$5,992** (significantly over-predicted).

---

## 3. Understanding Random Forest 🌲
In my own words, **Random Forest** is an **"ensemble"** model. Instead of relying on a single logic path, it creates an entire forest of **Decision Trees**. 



Each tree in the forest makes its own prediction, and the model then takes the **average** of all these trees to reach a final result. This "teamwork" approach makes it much more robust and better at handling complex, real-world data than a simple linear model.

---

## 4. Final Findings & Conclusion 🏆
I strongly prefer the **Random Forest** model for price prediction tasks. It proved much more reliable at capturing the non-linear relationships in the data, resulting in a significantly higher R² score and much more realistic price estimates.