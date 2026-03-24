# Research Paper: Academic Performance Drivers in Higher Education

## 1. Title & Collection Method
**Title:** *An Empirical Study on the Correlation Between Behavioral Habits and Academic Outcomes Among University Students in Somalia.*

**Subject Overview:** This dataset focuses on the academic performance of university students. It seeks to quantify how non-academic factors—such as physical rest, digital connectivity, and class participation—influence the final quantitative outcome of a student's examination score.

**Data Collection Methodology:** The data was collected using a **Primary Research Approach** via a structured survey. The target demographic consisted of 50 students currently enrolled in undergraduate programs. 
* **Method:** Participants provided their daily habits and most recent exam results through a digital questionnaire.
* **Authenticity:** The survey allowed for manual entry to ensure the dataset reflects real-world challenges, such as missing values and categorical text fields that require pre-processing.


## 2. Description of Features & Labels
The dataset is divided into independent variables (**Features**) and a dependent variable (**Label**).

### Input Variables (Features X):
1. **Student_Name (Identifier):** Used for data management and tracking.
2. **Attendance_Rate (%):** Numerical representation of classroom presence.
3. **Study_Hours_Weekly:** Total time dedicated to self-learning outside of class.
4. **Assignments_Done:** Discrete count (0–10) of completed assessment tasks.
5. **Sleep_Hours:** Average nightly rest, representing health and cognitive readiness.
6. **Internet_Access:** Categorical variable (Yes/No) indicating availability of online resources.

### Output Variable (Label y):
* **Exam_Score (0–100):** The target variable representing the grade achieved in the final exam.


## 3. Dataset Structure
The dataset is organized in a tabular format consisting of **50 rows** and **7 columns**.

### Data Sample (First 5 Observations)
| Student_Name | Attendance_Rate | Study_Hours | Assignments_Done | Sleep_Hours | Internet_Access | Exam_Score |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Abdirahman Ali | 95 | 15 | 10 | 7 | Yes | 88 |
| Fartun Hassan | 70 | 5 | 4 | 6 | No | 55 |
| Mohamed Omar | 85 | 10 | 8 | 8 | Yes | 75 |
| Nimco Ahmed | 60 | 3 | 2 | 5 | Yes | 40 |
| Abdikani Muse | 90 | 12 | 9 | 7 | Yes | **NaN** |


## 4. Quality Issues
This dataset includes several critical data quality issues that must be addressed in the next phase:

* **Missing Values (Nulls):** Several records are missing the target `Exam_Score`. These represent gaps in survey responses.
* **Categorical Inconsistency:** The `Internet_Access` column uses "Yes" and "No" strings, which require **Encoding** (converting to 1s and 0s).
* **Feature Scaling:** `Attendance_Rate` (0–100) and `Sleep_Hours` (4–9) have different scales, which can bias the model if not normalized.
* **Redundant Identifiers:** The `Student_Name` column adds no predictive value and will be excluded during the modeling phase.


## 5. Potential Machine Learning Use Cases
This dataset can be used for the following Machine Learning paradigms:

1. **Regression (Supervised Learning):** Building a **Linear Regression** model to predict a student’s `Exam_Score`. This helps in understanding how much an extra hour of study impacts a final grade.

2. **Classification (Supervised Learning):** By setting a threshold (e.g., Score < 50 = "Fail"), we can use **Logistic Regression** to classify students into "At-Risk" or "Safe" categories.

3. **Clustering (Unsupervised Learning):** Using **K-Means Clustering** to discover hidden patterns, such as grouping students into "High-Effort High-Achievers" vs. "Efficient Learners."


## Conclusion
This paper serves as the foundational documentation for the "Data Foundations" project. It demonstrates that raw data is rarely perfect and requires thoughtful cleaning before it can yield meaningful AI predictions.
