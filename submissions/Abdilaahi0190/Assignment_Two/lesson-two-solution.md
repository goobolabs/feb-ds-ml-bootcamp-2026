# Research Paper: Student Study Habits Dataset

## Title & Collection Method

**Title:** Student Study Habits and Performance Dataset
**Collection Method:** I designed a **survey questionnaire** and asked 110 students at my university about their daily study habits and performance. Each student provided answers about study hours, sleep, subjects studied, attendance, and whether they passed or failed the last exam.

---

## Description of Features & Labels

* **Features (X):**

  1. **Study Hours per Day** (numeric)
  2. **Sleep Hours per Day** (numeric)
  3. **Subjects Studied** (categorical: Science, Arts, Business, IT, etc.)
  4. **Attendance %** (numeric, 0–100)
  5. **Snacks Consumed while Studying** (categorical: None, Light, Heavy)

* **Label (y):**

  * **Exam Result** → Pass / Fail

This makes the problem a **classification task** (predicting Pass/Fail).

---

## Dataset Structure

* **Rows:** 110 students (samples)
* **Columns:** 6 (5 features + 1 label)

### Sample Table (10 rows)

| Study Hours | Sleep Hours | Subjects | Attendance % | Snacks | Exam Result |
| ----------- | ----------- | -------- | ------------ | ------ | ----------- |
| 2           | 5           | Science  | 60           | Light  | Fail        |
| 4           | 6           | IT       | 85           | None   | Pass        |
| 3           | 7           | Arts     | 72           | Heavy  | Pass        |
| 5           | 8           | Science  | 90           | Light  | Pass        |
| 1           | 4           | Business | 50           | Heavy  | Fail        |
| 6           | 7           | IT       | 95           | None   | Pass        |
| 2           | 6           | Arts     | 65           | Light  | Fail        |
| 3           | 5           | Science  | 70           | None   | Pass        |
| 4           | 6           | Business | 80           | Heavy  | Pass        |
| 5           | 7           | IT       | 88           | Light  | Pass        |

---

## Quality Issues

* **Missing values:** A few students skipped the “Snacks” question.
* **Categorical text:** Subjects and Snacks must be encoded for ML.
* **Imbalance:** 85 students passed, only 25 failed (imbalanced dataset).
* **Inconsistent reporting:** Some students wrote “Sci” instead of “Science.”

---

## Use Case

This dataset can be used to train a **classification model** to predict whether a student is likely to **Pass** or **Fail** based on their study habits.

* Possible algorithms: Logistic Regression, Decision Tree, Random Forest.
* It could help educators identify **at-risk students** early and provide extra support.

---
