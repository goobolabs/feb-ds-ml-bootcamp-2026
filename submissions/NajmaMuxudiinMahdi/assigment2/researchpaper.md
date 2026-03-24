Practical Assignment: Data Foundations for Machine Learning


---

Dataset Title: Student Daily Expenses

This dataset captures the daily spending habits of students, including expenses on transportation, food, internet, and study materials. It aims to analyze how different daily habits impact total daily expenses and to provide real-world data for Machine Learning practice.


---



Features & Labels

Features (X):

Age: Numeric

Transport_Cost_USD: Numeric

Food_Cost_USD: Numeric

Internet_Cost_USD: Numeric

Study_Materials_Cost_USD: Numeric


Label (y):

Total_Daily_Expense_USD: Numeric, sum of all expenses (Regression problem)



---

Dataset Structure

Number of rows (samples): 50

Number of columns (features + label): 6

Sample Table (8 rows):




Data Quality Issues

Missing values: Some students may not report all expenses.

Typos or errors: Data entry may contain mistakes.

Imbalance: Variation in spending patterns.

Outliers: Extreme high or low spending by some students.



---

Use Case in Machine Learning

Regression: Predict total daily expense based on age and individual expense categories.

Optional Classification: Categorize expenses into Low, Medium, High for classification.

Clustering: Group students by spending behavior patterns.




