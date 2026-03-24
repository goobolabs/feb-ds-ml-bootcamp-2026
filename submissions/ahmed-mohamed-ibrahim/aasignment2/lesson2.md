# 1. Collect Your Own Dataset
## Dataset Description
I created a dataset titled **"Fast Food Habits and Customer Satisfaction."** The goal is to see if things like price, waiting time, and healthiness affect how much a person likes their meal.
## Dataset Requirements
- **Number of samples:** 50 people
- **Number of features:** 7 features + 1 label
- **Source:** I asked 50 friends and family members about their last fast-food meal.
## Collection Method
I used a **simple survey**. I asked people to remember the last time they ate at a fast-food restaurant and answer 7 quick questions about it.
---
# 2. Short Research Paper
## Title
**What Makes a Happy Customer? Analyzing Fast Food Experiences**
## Collection Method
I collected this data by interviewing 50 people. I asked them about their age, how much they spent, and how long they waited for their food. This is original data collected specifically for this assignment.
---
## Features (X) and Label (y)
### The 7 Features (Input X):
1. **Age** – Age of the customer.
2. **Restaurant_Type** – Burger, Pizza, Chicken, or Healthy/Salad.
3. **Price_Paid** – Total cost of the meal.
4. **Wait_Time_Min** – How many minutes they waited for the food.
5. **Is_Healthy** – Did they think the meal was healthy? (Yes/No).
6. **Visit_Time** – Lunch, Dinner, or Late Night.
7. **Order_Method** – Dine-in, Takeout, or Delivery.
### The Label (Output y):
- **Satisfied**
  - **Yes** (They liked the meal and would go back).
  - **No** (They did not like the experience).
---
## Sample of the Data (5 Rows)
| Age | Type | Price | Wait (min) | Healthy? | Time | Method | Satisfied |
|-----|------|-------|------------|----------|------|--------|-----------|
| 20 | Burger | $12 | 10 | No | Dinner | Delivery | Yes |
| 45 | Salad | $15 | 5 | Yes | Lunch | Dine-in | Yes |
| 28 | Pizza | $20 | 35 | No | Night | Delivery | No |
| 19 | Chicken | $8 | 15 | No | Dinner | Takeout | Yes |
| 33 | Burger | $11 | 20 | No | Lunch | Takeout | No |
---
## Quality Issues
I noticed a few "messy" things in my data:
1. **Missing Data:** Some people forgot to say how many minutes they waited.
2. **Text to Numbers:** We need to change "Burger" and "Pizza" into numbers.
3. **Typos:** Some people wrote "Pizzaa" or "Burgerr" by mistake.
4. **Formatting:** Prices were written as "$12" and "12 dollars." We need them to just be "12."
---
## Use Case in Machine Learning
- **Classification:** Predict if a customer will be **Satisfied** based on their wait time and price.
- **Regression:** Predict the **Price** someone is willing to pay based on their age and restaurant type.