# 📘 Lesson 4 – Regression

✅ In **Lesson 1**, we explored what Machine Learning is, its main types, and the overall workflow — that gave us the big picture.

✅ In **Lesson 2**, we focused on the **theory of data foundation**: features, preprocessing, and metrics — the building blocks of any ML project.

✅ In **Lesson 3**, we moved to the **practical side of data foundation**, applying coding exercises based on the concepts we learned in Lesson 2.

👉 **Now in Lesson 4, we focus on Regression — one of the core supervised learning methods.**

## 🎯 Learning Objectives

By the end of this lesson, students will be able to:

- What regression is used for (e.g., predicting house prices).
- Variants: **Linear Regression, Multiple Regression, Polynomial Regression**.
- Understanding metrics:
  - **MAE (Mean Absolute Error)**
  - **MSE (Mean Squared Error)**
  - **RMSE (Root Mean Squared Error)**
  - **R² (Coefficient of Determination)**

---

## Introduction

This is where ML starts to feel powerful: instead of just talking about data, we’ll actually **predict numbers**. Think house prices, car values, sales forecasts — anywhere you want to estimate a continuous outcome.

---

## 2) What is Regression?

### Definition

- **Regression** is a type of supervised learning that predicts **continuous outputs** (numbers on a scale).
- The goal is to find the **relationship between input features (X)** and a **numeric target (y)**.

---

### Real-World Examples

- 🏡 **House Prices:** Predict the price of a house based on size, location, bedrooms, etc.
- 📈 **Stock Prices:** Forecast the next day’s stock price using past prices and market indicators.
- 🌡️ **Weather Temperature:** Estimate tomorrow’s temperature from historical data, humidity, and pressure.

---

### Contrast with Classification

- **Regression:** Output is a **number** (e.g., \$350,000, 25°C).
- **Classification:** Output is a **category** (e.g., Spam vs Not Spam, Cat vs Dog, Pass vs Fail).

👉 Quick check:

- Predicting whether an email is spam → **Classification**
- Predicting the rent price of an apartment → **Regression**

---

📌 **Key Point:**
Regression = predicting **how much**.
Classification = predicting **which class**.

---

## 3) Regression Basics

### a) Linear Regression

**Simple Idea:**

- Linear Regression is the most basic way to predict numbers.
- It looks for a **straight-line relationship** between one input and one output.

---

#### Example (House Prices)

- **Input (feature):** Size of the house (sq ft).
- **Output (label):** Price of the house.

👉 As the size goes up, the price usually goes up too.
Linear Regression draws a straight line that shows this trend.

---

#### Visual Intuition

- Imagine a scatter plot of houses: size on the X-axis, price on the Y-axis.
- Each house is a dot.
- Linear Regression draws the **best line** through those dots.
- That line can then be used to **predict prices** of new houses (e.g., a 2200 sq ft house).

📊 Example Graph:

![Linear Regression — House Size vs Price](../images/lesson-four/linear_regression_example.png)

(Blue dots = actual houses, Red line = best-fit prediction line).

---

#### Why It’s Useful

- Simple.
- Helps us see the **general relationship** between one factor and the target.
- But it’s limited — most real-world problems need **more than one factor** (that’s where multiple regression comes in).

---

📌 **Takeaway:**
Linear Regression = predicting an outcome using **just one main factor** with a straight-line relationship.

---

### b) Multiple Linear Regression

**Simple Idea:**

- Real-world problems usually depend on **more than one factor**.
- Multiple Linear Regression extends the idea of Linear Regression: instead of one line with one input, it looks at **several inputs together** to predict the output.

---

#### Example (House Prices)

- **Inputs (features):**

  - Size of the house (sq ft)
  - Number of bedrooms
  - Location (city/suburb/rural)
  - Year built

- **Output (label):**

  - Price of the house

👉 This way, the model doesn’t just say “bigger houses cost more” — it also adjusts for **location**, **bedrooms**, and **other factors**.

---

#### Visual Intuition

- In 2D (one feature) → regression is a straight line.
- In 3D (two features, e.g., Size & Bedrooms) → regression becomes a flat **plane**.
- With even more features → the “plane” extends into higher dimensions (we can’t see it, but the math still works).

📊 Example Graph:

![Multiple Linear Regression — Size & Bedrooms vs Price](../images/lesson-four/multiple_linear_regression_example.png)

- **Blue dots** = actual houses (data points).
- **Red surface** = regression plane predicting price from **Size + Bedrooms**.

---

#### Why It’s Useful

- More realistic: considers **all important factors**, not just one.
- Gives better predictions when the output depends on **multiple things**.

---

📌 **Takeaway:**
Multiple Linear Regression = predicting an outcome using **several factors together**, instead of just one.

---

### c) Polynomial Regression

**Simple Idea:**

- Not all relationships in real life are straight lines.
- **Polynomial Regression** allows us to fit a **curve** instead of a line by adding new features like `size²`, `size³`, etc.
- This helps capture situations where the effect of a feature changes as the values increase.

---

#### Example (House Prices)

- **Input (feature):** Size of the house (sq ft).
- **Output (label):** Price of the house.

👉 In reality, the price doesn’t always rise in a perfectly straight line with size.

- A 1000 → 1500 sq ft jump might increase price a lot,
- But a 2800 → 3300 sq ft jump may not increase price as much.

Polynomial Regression draws a **curved line** to capture this pattern.

---

#### Visual Intuition

- Imagine plotting house sizes on the X-axis and prices on the Y-axis.
- Each house is still a dot.
- Instead of one straight line, Polynomial Regression fits a **smooth curve** that bends with the data.
- With degree 2 (quadratic), the curve bends once.
- With degree 3 (cubic), it can bend twice, making an S-shape.

📊 Example Graph:

![Polynomial Regression Curve](../images/lesson-four/polynomial_regression_example.png)

(Blue dots = actual houses, Red curve = polynomial regression prediction).

---

#### Why It’s Useful

- Better captures **non-linear trends** in data.
- Still simple and interpretable compared to more complex models.
- Useful when a straight line is too simple but you don’t want to jump into advanced algorithms.

---

📌 **Takeaway:**
Polynomial Regression = still a linear model, but by adding **powers of a feature**, it can **bend the line into a curve** that fits real-world patterns more accurately.

---

#### Linear vs Polynomial Regression

##### 📏 1. Linear Regression

- Draws a **straight line** through the data.
- Assumes every **+1 unit of X (size)** always adds the **same amount of Y (price)**.
- Works best when the relationship is **steady and constant**.

**Example:**

| Size (sq ft) | Price (\$) |
| ------------ | ---------- |
| 1000         | 100,000    |
| 1500         | 150,000    |
| 2000         | 200,000    |

**Rule:** Each +500 sq ft adds exactly +50,000.

---

##### 📈 2. Polynomial Regression

- Draws a **curved line** through the data.
- Captures patterns where the **effect changes** as X increases.
- Useful when **small sizes get big jumps** but **big sizes get smaller jumps.**

**Example:**

| Size (sq ft) | Price (\$) |
| ------------ | ---------- |
| 1000         | 100,000    |
| 1500         | 180,000    |
| 2000         | 230,000    |
| 2500         | 260,000    |
| 3000         | 280,000    |

**Rule:** Early +500 adds +80k, later +500 adds only +20k.

---

##### 💡 3. Key Difference

| Feature        | Linear Regression      | Polynomial Regression                     |
| -------------- | ---------------------- | ----------------------------------------- |
| Shape of line  | Straight               | Curved                                    |
| Growth pattern | Constant               | Changing (can slow down)                  |
| Best used when | Data is simple, steady | Data has ups/downs or diminishing returns |

---

##### 📊 Example Graph

![Linear vs Polynomial Regression](../images/lesson-four/linear-vs-polynomial-regression.png)

- 🔵 **Blue (Linear):** A straight line — price rises evenly as size increases.
- 🟢 **Green (Polynomial):** A curved line — price rises quickly at first, then slows down for bigger houses.

---

## 4) Regression Metrics (How Do We Measure Performance?)

When we build a regression model, it makes predictions.
👉 But how do we know if those predictions are **good or bad**?

That’s where **metrics** come in — numbers that tell us **how close our predictions are to the actual values**.

---

### 1. Mean Absolute Error (MAE)

- **Idea:**
  Take the average of the **absolute differences** between predicted and actual values.

- **Interpretation:**
  “On average, how far off are we?”

- **Example:**
  If MAE = **10,000**, it means our price predictions are off by about \$10,000 on average.

---

### 2. Mean Squared Error (MSE)

- **Idea:**
  Square the errors before averaging.

- **Why square?**
  To punish **big mistakes** more heavily.

- **Interpretation:**
  A few very wrong predictions will push MSE up a lot.

---

### 3. Root Mean Squared Error (RMSE)

- **Idea:**
  Just the **square root of MSE** (RMSE = √18.7 = **4.3**).

- **Why useful?**
  Brings the error back to the **same units** as the target.

- **Example:**
  If RMSE = **12,000**, it means our predictions are usually off by about \$12,000.

- **Interpretation:**
  Like MAE but more sensitive to big mistakes.

---

### 4. R² Score (Coefficient of Determination)

- **Idea:**
  R² tells us **how much of the variation** in the target can be explained by the model.

- **Range:**

  - 1.0 → perfect fit
  - 0.0 → model is no better than guessing the average
  - Negative → worse than just guessing the average!

- **Interpretation:**
  How much does the model understand the trend?

- **Example:**
  R² = 0.85 → “Our model explains 85% of the variation in house prices.”

---

### 📝 Summary Table

| Metric | Meaning                | Sensitive to Big Errors? | Units         |
| ------ | ---------------------- | ------------------------ | ------------- |
| MAE    | Average absolute error | ❌ No                     | Same as data  |
| MSE    | Average squared error  | ✅ Yes                    | Squared units |
| RMSE   | Root of MSE            | ✅ Yes                    | Same as data  |
| R²     | % of pattern explained | ❌ No                     | 0 to 1        |

---

## ✅ Lesson Summary

- **Regression:** A supervised learning method used to **predict continuous values** (like house prices, sales, temperatures).
- **Linear Regression:** Uses **one feature** to fit a **straight line** — assumes the relationship stays constant.
- **Multiple Regression:** Uses **several features together** to fit a **plane (or higher-dimensional surface)** — handles more realistic, multi-factor problems.
- **Polynomial Regression:** Adds **powers of features (x², x³, …)** to fit **curved relationships** — captures non-linear trends.
- **Key Difference:**

  - Linear → straight, steady growth.
  - Polynomial → curved, changing growth (e.g. fast at first, slows later).

- **Metrics to Evaluate Models:**

  - **MAE:** Average size of prediction errors.
  - **MSE:** Like MAE but **squares errors** to punish large mistakes.
  - **RMSE:** Square root of MSE — average error in original units, **more sensitive to large errors**.
  - **R²:** How much of the variation in the target is explained by the model.

---

## 🔚 End of Lesson 4

🎉 Congratulations! You’ve completed **Regression – your first predictive modeling technique in Machine Learning.**