# Practical Assignment: Data Foundations for Machine Learning

## 1. Title and Data Collection Method

**Title:** Student Daily Habits and Academic Performance Dataset

**Data Collection Method:**  
This dataset was collected manually through a survey among university students. The survey asked students about their age, study hours, sleep hours, internet usage, and class attendance. All responses were recorded manually. No pre-made datasets (like Kaggle or UCI) were used.  

This approach ensures the data reflects real-world student behavior and is slightly messy, mimicking actual data collection challenges.

---

## 2. Description of Features (X) and Label (y)

**Features (X):** The dataset has 5 input variables (features):

- **Age** – Student age in years  
- **Study_Hours** – Average daily study time  
- **Sleep_Hours** – Average daily sleep duration  
- **Internet_Hours** – Average daily internet usage  
- **Attendance** – Class attendance level (Low, Medium, High)  

**Label (y):**

- **GPA** – Grade Point Average on a 0–4 scale (target variable to predict)

---

## 3. Dataset Structure

- **Number of rows (samples):** 50  
- **Number of columns:** 6 (5 features + 1 label)  

**Sample Table (10 rows):**

| Age | Study_Hours | Sleep_Hours | Internet_Hours | Attendance | GPA |
|-----|------------|------------|----------------|-----------|-----|
| 20  | 3          | 6          | 5              | Medium    | 2.8 |
| 22  | 5          | 7          |                | High      | 3.5 |
| 19  | 2          | 5          | 6              | Low       | 2.2 |
| 21  | 4          | 6          | 4              | Medium    | 3.0 |
| 23  | 6          | 7          | 2              | High      | 3.8 |
| 20  | 1          | 4          | 7              | Low       |     |
|     | 5          | 8          | 3              | High      | 3.6 |
| 22  | 3          | 6          | 5              | Medium    | 2.9 |
| 21  | 4          | 7          | 4              | Medium    | 3.1 |
| 19  | 2          | 5          |                | Low       | 2.3 |

> The remaining rows follow the same structure.  
> The dataset is slightly messy with missing values, categorical text, and different scales, making it realistic for preprocessing practice.

---

## 4. Data Quality Issues

- Missing values (`NaN`) in Age, Study_Hours, Internet_Hours, and GPA  
- Categorical data in Attendance column  
- Different scales for numeric features (Age 19–24, Study_Hours 1–6, GPA 0–4)  
- Possible noise from inaccurate self-reporting  
- Slight imbalance in attendance categories (more Medium than Low or High)  

> These issues are intentional to mimic real-world data collection problems.

---

## 5. Use Case in Machine Learning

This dataset can be used in several ML tasks:

- **Regression:** Predict student GPA based on daily habits  
- **Classification:** Categorize students into Low, Medium, or High GPA groups  
- **Clustering:** Group students with similar behavior patterns (study, sleep, internet, attendance)  

**Preprocessing examples:**

- Fill missing values  
- Encode categorical Attendance  
- Scale numeric features (Age, Study_Hours, Sleep_Hours, Internet_Hours, GPA)  
- Detect and handle outliers or noise  

---

## 6. Conclusion

This dataset demonstrates real-world data collection, including common issues like missing values, categorical text, and different scales.  

It is ready for preprocessing and ML modeling, providing a practical foundation for lessons on cleaning, encoding, scaling, and feature engineering.
