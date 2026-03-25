# Research Paper: Mobile Internet Usage and Daily Spending Behavior

## 1. Title & Collection Method

**Title:**  
The Relationship Between Mobile Internet Usage and Daily Expense Levels.

**Collection Method:**  
I used the **Manual Survey & Direct Interview** method. I asked 120 people from my local area to report their daily mobile data usage, daily income, transport cost, and call duration. I recorded their answers in a spreadsheet and then categorized their total spending level as **Low, Medium, or High** based on their daily expenses.

---

## 2. Description of Features & Labels

## Dataset Features

**Feature 1: Gender (X1)**  
The gender of the participant (Male / Female / M / F / female).  
**Type:** Categorical  

**Feature 2: Daily_Data_Usage (X2)**  
Amount of mobile internet used per day (e.g., 2.5, 3GB, 2500MB).  
**Type:** Numerical / Categorical  

**Feature 3: Daily_Call_Minutes (X3)**  
Total minutes spent on phone calls per day.  
**Type:** Numerical  

**Feature 4: Daily_Income_USD (X4)**  
The amount of money earned per day.  
**Type:** Numerical  

**Feature 5: Transport_Cost_USD (X5)**  
Daily transport cost.  
**Type:** Numerical  

**Label (y): Expense_Level**  
A category showing if the participant's daily expenses are Low, Medium, or High (The result we want to predict).  

---

## 3. Dataset Structure

- **Rows:** 125 (including some duplicated records)  
- **Columns:** 5 Features + 1 Label  

**Sample Table (First 10 Rows):**

| Name | Gender | Data_Usage | Call_Minutes | Daily_Income | Transport_Cost | Expense_Level (y) |
|------|--------|------------|--------------|--------------|----------------|------------------|
| Ahmed Ali | Male | 2.5 | 30 | 8 | 1.5 | Medium |
| Ayan Hassan | F | 3GB | 20 | 12 | 2 | High |
| Mohamed Yusuf | male | 2500MB | 10 | 5 | 1 | Low |
| Hodan Farah | Female | 4.2 | 40 | ? | 3 | High |
| Abdi Nur | M | 2.0GB | 25 | 7 | Missing | Medium |
| Fadumo Osman | female | 1.2 | 15 | 6 | 1 | Low |
| Hassan Ali | Male | 3.5GB | 35 | 10 | 2.5 | High |
| Hamdi Yusuf | F | 0.8 | 5 | 4 | 0.5 | Low |
| Ibrahim Farah | Male | 3000MB | 50 | 15 | 3.5 | High |
| Nasteexo Nur | Female | 2.7GB | 28 | 9 | 2 | High |

---

## 4. Quality Issues (The "Messy" Data)

1. **Inconsistent Formats:**  
   Data usage is recorded in different formats such as GB, MB, and numeric values.

2. **Missing Values:**  
   Some rows have missing values in `Daily_Income_USD` and `Transport_Cost_USD`.

3. **Typos & Inconsistent Categories:**  
   Gender is written in multiple formats:
   - Male / male / M
   - Female / F / female

4. **Extra Spaces:**  
   Some labels contain spaces (e.g., `" High"` or `"Low "`).

5. **Duplicate Records:**  
   A few participants were recorded more than once.

6. **Outliers:**  
   Very high mobile data usage values (e.g., 3000MB) compared to others.

---

## 5. Use Case

This dataset can be used for a **Classification Machine Learning project**.  

**Goal:**  
Predict whether a person belongs to the **Low, Medium, or High** daily expense group based on their mobile usage and income.

For example:

- If **daily income is high** and **mobile data usage is above 3GB** → the **expense level is likely High**.

- If **income is low** and **transport cost is small** → the **expense level is likely Low**.
