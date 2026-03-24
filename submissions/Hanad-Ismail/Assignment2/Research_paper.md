# Predicting Personality Type from Study and Technology Habits

## Abstract
Understanding personality traits such as introversion and extroversion can help improve learning environments, collaboration, and productivity. This research presents a self-collected dataset aimed at predicting personality type (Introvert or Extrovert) based on study habits, technology usage, and communication preferences. The dataset was collected through a survey and contains behavioral features related to coding time, study environment, group preference, communication methods, and social connections. The study demonstrates how real-world, messy data can be structured for use in machine learning classification tasks.

---

## 1. Introduction
Personality traits influence how individuals learn, communicate, and interact with technology. In academic and professional settings, understanding whether a person is more introverted or extroverted can help tailor study methods, collaboration styles, and digital tools. The goal of this research is to build a dataset that captures study and technology habits and uses these features to predict personality type.

---

## 2. Dataset Collection Method
The dataset was collected using an online survey distributed to students. Participants voluntarily answered questions related to their daily study routines, coding hours, preferred study environments, communication methods, and social interactions. All data was collected manually and is original.

- **Collection Method:** Survey / Questionnaire  
- **Type of Data:** Categorical and numerical  
- **Number of Samples:** More than 50  

---

## 3. Features and Label Description

### Input Features (X)
The following features were selected for predicting personality type:

1. **Coding_hours** – Daily time spent coding or studying (Less than 1 hour, 1–2 hours, 3–4 hours, 5–6 hours).
2. **Study_env** – Preferred study environment (Alone in silence, In a group with friends, Coffee shop, Depends on mood).
3. **Group_pref** – Preference for group projects on a scale of 1 to 5.
4. **Comm_method** – Preferred communication method (Text/Chat apps, Phone call, Video call, In-person).
5. **Close_friends** – Number of close friends (numeric or approximate).

### Output Label (y)
- **Personality** – Classified as **Introvert** or **Extrovert**.

---

## 4. Dataset Structure
- **Rows:** 50+  
- **Columns:** 6 (5 features + 1 label)

### Sample Data

| Coding_hours | Study_env               | Group_pref | Comm_method      | Close_friends | Personality |
|-------------|-------------------------|------------|------------------|---------------|-------------|
| 1–2 hours   | Alone in silence        | 2          | Text / Chat apps | 2             | Introvert   |
| 5–6 hours   | In a group with friends | 4          | Phone call       | 5             | Extrovert   |
| Less than 1 | Depends on my mood      | 3          | Video call       | 3             | Introvert   |
| 3–4 hours   | Alone in silence        | 1          | In-person        | 1             | Introvert   |
| 3–4 hours   | In a group with friends | 5          | In-person        | 8             | Extrovert   |

---

## 5. Data Quality Issues
The dataset contains several real-world data quality issues:

- Missing or approximate values (e.g., “more than 5”, “approx 20”)
- Inconsistent text formatting
- Mixed categorical and numerical data
- Subjective responses

These issues make the dataset suitable for demonstrating data preprocessing techniques.

---

## 6. Use Case in Machine Learning
This dataset can be used for a **classification task** where the goal is to predict personality type.

Possible algorithms:
- Logistic Regression
- Decision Trees
- Random Forest
- K-Nearest Neighbors (KNN)

The dataset can also be used for clustering and exploratory data analysis.

---

## 7. Conclusion
This study demonstrates the process of collecting an original dataset and preparing it for machine learning applications. The dataset reflects real-world behavior and provides a strong foundation for learning data preprocessing and personality classification techniques.

---

## References
No external datasets were used. All data was collected manually through an original survey.
