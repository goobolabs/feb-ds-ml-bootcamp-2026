# 1. Collect Your Own Dataset

## Dataset Description
I collected my own dataset related to **university students’ daily habits and academic performance**.  
The dataset focuses on how **study behavior, sleep, phone usage, attendance, and stress levels** affect academic results.

## Dataset Requirements
- **Number of samples (rows):** 50 students
- **Number of features (columns):** 8 features + 1 label
- **Source:** Self-collected (not from Kaggle, UCI, or any repository)

## Collection Method
The dataset was collected using a **survey questionnaire**.

University students were asked to answer questions about their **daily routines and academic life**.

### The survey included:
- Age
- Gender
- Study hours per day
- Sleep hours
- Phone usage
- Attendance rate
- Part-time job status
- Stress level
- Academic performance

---

# 2. Short Research Paper (2–3 Pages)

## Title and Collection Method

### Title
**A Dataset on University Students’ Study Habits and Academic Performance**

### Collection Method
The data was collected through a **self-created survey** distributed among university students.  
Responses were recorded manually.  
No external or pre-made datasets were used.

---

## Description of Features and Label

### Input Variables (Features X)
1. **Age** – Age of the student in years
2. **Gender** – Male or Female
3. **Study_Hours_Per_Day** – Average hours spent studying daily
4. **Sleep_Hours** – Average sleep hours per day
5. **Phone_Usage_Hours** – Daily phone usage time
6. **Attendance_Rate** – Class attendance percentage
7. **Part_Time_Job** – Yes or No
8. **Stress_Level** – Low, Medium, or High

### Output Variable (Label y)
- **Academic_Performance**
  - Low
  - Average
  - High

---

## Dataset Structure
- **Total Rows:** 50
- **Total Columns:** 9
- **Features:** 8
- **Label:** 1

---

## Sample of the Dataset (5 Rows)

| Age | Gender | Study Hours | Sleep Hours | Phone Usage | Attendance | Job | Stress | Performance |
|-----|--------|-------------|-------------|-------------|------------|-----|--------|-------------|
| 19 | Male | 2.5 | 6 | 5 | 72 | No | Medium | Average |
| 21 | Female | 4.0 | 7 | 3 | 88 | No | Low | High |
| 22 | Male | 1.5 | 5 | 6 | 60 | Yes | High | Low |
| 20 | Female | 3.0 | 8 | 2 | 90 | No | Low | High |
| 23 | Male | 2.0 | 6 | 4 | 70 | Yes | Medium | Average |

---

## Quality Issues in the Dataset
The dataset contains real-world data problems, including:
1. Missing values (some students skipped questions)
2. Categorical text data that requires encoding
3. Inconsistent text entries (e.g., "High", "high")
4. Class imbalance in academic performance categories
5. Noise due to self-reported answers

These issues will be handled during preprocessing.

---

## Use Case in Machine Learning

### Classification
Predict **Academic_Performance** using:
- Logistic Regression
- Decision Tree
- Random Forest
- K-Nearest Neighbors

### Regression
Convert performance categories into numeric values and predict academic scores.

### Clustering
Group students based on habits and lifestyle patterns using:
- K-Means
- Hierarchical Clustering
