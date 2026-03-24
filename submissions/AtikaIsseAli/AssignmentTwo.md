# Student Daily Study Habits and Academic Performance in Mogadishu Universities

## 1. Introduction and Data Collection Method
This study presents a self-collected dataset focused on university students in Mogadishu, Somalia. The data was collected manually using a short online questionnaire distributed among university students. Participants voluntarily provided information related to their daily study habits, lifestyle factors, and academic performance. Data collection was conducted over a one-week period and resulted in 52 valid responses. No external or pre-existing datasets were used in this study.

## 2. Dataset Description
The dataset consists of 52 samples (rows) and 7 attributes (columns). Each row represents a single student. The objective of the dataset is to analyze how daily habits such as study time, sleep duration, and attendance influence academic performance.

### Features (Input Variables)
* **Age (Numerical):** Student age in years.
* **Gender (Categorical):** Male or Female.
* **Study_Hours_Per_Day (Numerical):** Average daily study hours.
* **Internet_Access (Categorical):** Availability of internet access at home.
* **Sleep_Hours (Numerical):** Average number of hours slept per night.
* **Attendance_Rate (Numerical):** Percentage of class attendance.

### Label (Output Variable)
* **GPA (Numerical):** Student grade point average on a 4.0 scale.

## 3. Sample of the Dataset
| Age | Gender | Study Hours | Internet | Sleep Hours | Attendance % | GPA |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 20 | Male | 2.5 | Yes | 6 | 75 | 2.6 |
| 22 | Female | 4 | Yes | 7 | 90 | 3.4 |
| 21 | Male | 1.5 | No | 5 | 60 | 2.1 |
| 23 | Female | 5 | Yes | 8 | 95 | 3.8 |
| 19 | Male | 3 | Yes | 6 | 80 | 2.9 |
| 24 | Female | 2 | No | 5 | 70 | 2.4 |

## 4. Data Quality Issues
Several data quality issues exist within the dataset:
* Some records contain missing values, particularly in Attendance and Sleep.
* Inconsistencies in text (e.g., 'Yes' vs 'yes').
* Outliers in study hours.
* GPA distribution is slightly imbalanced.

## 5. Potential Machine Learning Applications
* **Regression:** Predict GPA based on lifestyle and study habits.
* **Clustering:** Group students into performance categories (e.g., at-risk vs. high-performing).

## 6. Conclusion
The dataset provides a realistic example of manually collected educational data from a Somali context, perfect for practicing data cleaning and preprocessing.
