# Research Paper: Student Habits and Academic Success

### 1. Title & Collection Method

**Title:** The Impact of Sleep, Coffee, and Study Time on Student Grades

**Collection Method:** This dataset was created using the **Manual Logging (Observation)** method. I conducted a virtual survey of 50 university students. I asked them to track their daily habits for one school week. The data was recorded by hand and then typed into a digital format to simulate a real-world data collection process.

---

### 2. Description of Features & Labels

In this dataset, we are looking at how lifestyle choices affect school performance. To do this, we use **Features** (the facts we know) to predict a **Label** (the result we want to find).

* **Feature 1: Major (X1)** – The student's area of study (Categorical/Text).
* **Feature 2: Sleep_Hrs (X2)** – Average hours of sleep per night (Numerical).
* **Feature 3: Coffee_Cups (X3)** – Number of cups of coffee drank daily (Numerical).
* **Feature 4: Study_Hrs (X4)** – Hours spent studying per day (Numerical).
* **Label: Grade (y)** – The student's current GPA (Numerical). This is what we want to predict.

---

### 3. Dataset Structure

* **Total Rows:** 50
* **Total Columns:** 5 Features + 1 ID column.

**Sample Table (First 10 Rows):**

| ID | Major | Sleep_Hrs | Coffee_Cups | Study_Hrs | Grade (y) |
| --- | --- | --- | --- | --- | --- |
| 1 | Engineering | 5 | 4 | 6 | 3.5 |
| 2 | Nursing | 4 | 5 | 7 | 3.2 |
| 3 | Business | 8 | 0 | 2 | 3.8 |
| 4 | Biology | 6 | 2 | 5 | 3.6 |
| 5 | Design | 5 | 3 | 4 | 3.1 |
| 6 | **Engineeing** | 4 | 4 | 8 | 3.4 |
| 7 | Nursing | **?** | 5 | 6 | 3.0 |
| 8 | Business | 8 | 0 | 3 | 3.9 |
| 9 | Biology | 7 | 2 | 4 | 3.5 |
| 10 | Design | 6 | 3 | 5 | **Missing** |

---

### 4. Quality Issues

Real-world data is rarely perfect. This dataset has four main problems that must be fixed in Lesson 3:

1. **Missing Values:** Rows 7 and 10 have missing information (shown as "?" or "Missing"). We need to decide if we should delete these rows or fill them in.
2. **Typos:** Row 6 has a spelling mistake ("Engineeing"). A computer will think this is a completely different major unless we fix it.
3. **Mixed Formats:** Some rows (like Row 12) have numbers written as words ("six") instead of digits ("6"). Computers need numbers to do math.
4. **Outliers:** Row 32 shows a student drinking 15 cups of coffee. This is a very high number that might confuse our Machine Learning model.

---

### 5. Use Case

This dataset is designed for **Supervised Learning**, specifically **Regression**.

Because the "Label" (Grade) is a continuous number (like 3.5 or 3.8), we can train a Machine Learning model to look at a student’s sleep and study habits and predict their likely grade. In the future, a university counselor could use this tool to identify students who are sleeping too little or drinking too much coffee and might be at risk of lower grades.

---

### 6. The Full Dataset (50 Rows)

| ID | Major | Sleep_Hrs | Coffee_Cups | Study_Hrs | Grade |
| --- | --- | --- | --- | --- | --- |
| 1 | Engineering | 5 | 4 | 6 | 3.5 |
| 2 | Nursing | 4 | 5 | 7 | 3.2 |
| 3 | Business | 8 | 0 | 2 | 3.8 |
| 4 | Biology | 6 | 2 | 5 | 3.6 |
| 5 | Design | 5 | 3 | 4 | 3.1 |
| 6 | **Engineeing** | 4 | 4 | 8 | 3.4 |
| 7 | Nursing | **?** | 5 | 6 | 3.0 |
| 8 | Business | 8 | 0 | 3 | 3.9 |
| 9 | Biology | 7 | 2 | 4 | 3.5 |
| 10 | Design | 6 | 3 | 5 | **NaN** |
| 11 | Engineering | 5 | 4 | 7 | 3.5 |
| 12 | Nursing | 4 | **six** | 8 | 3.2 |
| 13 | Business | 7 | 1 | 3 | 3.7 |
| 14 | Biology | 6 | 2 | 4 | 3.5 |
| 15 | Design | 5 | 4 | 6 | 3.2 |
| 16 | Engineering | 5 | 3 | 7 | 3.6 |
| 17 | Nursing | 4 | 5 | 9 | 3.1 |
| 18 | Business | 8 | 0 | 2 | 3.9 |
| 19 | Biology | 7 | 1 | 5 | 3.4 |
| 20 | Design | 6 | 2 | 4 | 3.3 |
| 21 | Engineering | 4 | 5 | 8 | 3.2 |
| 22 | Nursing | 5 | 4 | 7 | 3.0 |
| 23 | Business | 7 | 1 | 4 | 3.6 |
| 24 | Biology | 6 | 3 | 6 | 3.5 |
| 25 | Design | 5 | 4 | 5 | 3.1 |
| 26 | Engineering | 5 | 4 | 7 | 3.4 |
| 27 | Nursing | 4 | 5 | 8 | 2.9 |
| 28 | Business | 9 | 0 | 2 | 4.0 |
| 29 | Biology | 7 | 2 | 5 | 3.6 |
| 30 | Design | 6 | 3 | 4 | 3.2 |
| 31 | Engineering | 5 | 5 | 8 | 3.3 |
| 32 | Nursing | 4 | **15** | 9 | 2.8 |
| 33 | Business | 7 | 1 | 3 | 3.8 |
| 34 | Biology | 6 | 2 | 5 | 3.5 |
| 35 | Design | 5 | 4 | 6 | 3.1 |
| 36 | Engineering | 5 | 3 | 7 | 3.4 |
| 37 | Nursing | 4 | 5 | 8 | 3.0 |
| 38 | Business | 8 | 0 | 2 | 3.9 |
| 39 | Biology | 7 | 1 | 4 | 3.6 |
| 40 | Design | 6 | 2 | 5 | 3.2 |
| 41 | Engineering | 4 | 5 | 9 | 3.1 |
| 42 | Nursing | 5 | 4 | 7 | 3.3 |
| 43 | Business | 7 | 1 | 3 | 3.7 |
| 44 | Biology | 6 | 3 | 6 | 3.4 |
| 45 | Design | 5 | 4 | 5 | 3.0 |
| 46 | Engineering | 5 | 4 | 7 | 3.5 |
| 47 | Nursing | 4 | 5 | 8 | 2.9 |
| 48 | Business | 9 | 0 | 2 | 4.0 |
| 49 | Biology | 7 | 2 | 5 | 3.7 |
| 50 | Design | 6 | 3 | 4 | 3.3 |

---