# Data Foundations for Machine Learning
## Student Study Habits Dataset

---

## 1. Title and Data Collection Method

### Data Collection Method
This dataset was created to study the relationship between students’ daily study habits and their academic performance. The data represents university-level students and was collected using a simple survey-style approach, combined with realistic estimation based on common student behavior.

The goal of the data collection was to create a dataset that reflects real-world educational data rather than using pre-existing datasets. The values were designed to be reasonable and diverse, representing different learning patterns and outcomes among students.

---

## 2. Description of Features and Label

### Input Features (X)

- **Age**  

- **Gender**  

- **Hours_Studied_Per_Day**  

- **Attendance_Percentage**  

- **Sleep_Hours_Per_Day**  

### Output Label (y)

- **Final_Exam_Score**  
  The final exam score of the student, measured on a scale from 0 to 100.

---

## 3. Dataset Structure

The dataset consists of:

- 50 rows
- 6 columns:
  - 5 input features
  - 1 output label


| Age | Gender | Hours_Studied_Per_Day | Attendance_Percentage | Sleep_Hours_Per_Day | Final_Exam_Score |
|----|--------|----------------------|----------------------|--------------------|-----------------|
| 18 | Male | 1.5 | 65 | 5 | 54 |
| 21 | female | 4 | 85 | 7 | 8 |
| 20 | male | 3 | 80 | 6 | 72 |
| 22 | Female | 5 | 92 | 8 | 90 |
| 19 | Female | 2 | 70 | 6 | 60 |

---

## 4. Data Quality Issues

Although the dataset was carefully organized, it still represents real-world educational data and may require preprocessing. Potential data quality issues include:

- Differences in feature scales (for example, attendance percentage versus study hours)
- Possible outliers in exam scores
- The need to encode categorical variables such as gender


---

## 5. Use Case in Machine Learning

This dataset can be used for several Machine Learning tasks:

- **Regression**  

- **Feature Importance Analysis**  

- **Educational Analysis**  
---
