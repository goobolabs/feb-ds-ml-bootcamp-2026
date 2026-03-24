# Reflection Paper

## 1. What did I implement?
I built a system to guess how much a house costs. I used two different AI "brains."  

- **Linear Regression** — tries to draw a straight line through data.  
- **Random Forest** — uses many small decision makers to find the answer.

---

## 2. Comparison of Models
In my sanity check, the predictions were different.

- **Linear Regression** gave a guess based on a strict formula.  
- **Random Forest** gave a more realistic result.

This is because real house prices don't always follow a straight line. For example, adding one more bathroom might increase the price a lot in a rich neighborhood but only a little in a poor one. Random Forest can understand these *jumps* better.

---

## 3. Understanding Random Forest

### What is it?
Imagine you are buying a car. Instead of asking one person, you ask 100 people for their opinion. This group of people is the **Forest**.

### How does it work?
Each person (a **Decision Tree**) looks at the car's:
- age
- color
- engine

They each make a guess. Then you take the **average of all guesses**.

### Is it repeating?
If many trees in the forest say:

> "This house is worth \$200,000"

that repeating pattern tells the model that it is likely the correct answer.

---

## 4. Metrics Discussion
The Random Forest model had:

- higher **R²** (closer to 1.0)  
- lower **MAE** and **RMSE**

**Metric meanings**

- **R²** → measures how well the model understands the data  
- **MAE/RMSE** → measure how wrong predictions are  

Lower error = better model.

This shows Random Forest is stronger at handling complex data, while Linear Regression is weaker because it is too simple for house prices.

---

## 5. My Findings
I prefer the **Random Forest model** for predicting house prices.

**Reasons**
- more accurate  
- smaller errors  
- handles complex patterns  

It feels more like a human expert because it considers many details at once. Even though it is more complex, the results are much closer to real home prices.