# 🎓 Student Academic Performance Analysis (Somali University Dataset)

### 📊 Project Overview
This project is a practical assignment for the **Data Foundations for Machine Learning** course. It features a manually collected dataset of 50 Somali university students, tracking their study habits, attendance, and exam results. 

The primary goal is to use this "real-world" dataset to practice data cleaning, handling missing values, and building predictive models.


### 📂 Dataset Description
The dataset contains **50 rows** and **7 columns**. It includes a mix of numerical, categorical, and identifier data.

**1. Identifier:**
- `Student_Name`: The name of the student (used for tracking, not for prediction).

**2. Input Features (X):**
- `Attendance_Rate`: Percentage of lectures attended.
- `Study_Hours`: Weekly hours spent on self-study.
- `Assignments_Done`: Number of assignments completed (out of 10).
- `Sleep_Hours`: Average nightly sleep hours.
- `Internet_Access`: Whether the student has home internet (Yes/No).

**3. Target Label (y):**
- `Exam_Score`: The final grade achieved in the examination (0-100).


### 🛠️ Data Quality Issues (For Lesson 3)
To simulate real-world data challenges, this dataset includes:
- **Missing Values:** Some students (e.g., Abdikani Muse, Ikram Adan) have missing `Exam_Score` values.
- **Categorical Data:** The `Internet_Access` column requires encoding (converting Yes/No to 1/0).
- **Non-Predictive Data:** The `Student_Name` column must be handled or dropped before training a model.


### 🚀 Machine Learning Objectives
- **Data Cleaning:** Use Python (Pandas) to fill missing values and fix inconsistencies.
- **Exploratory Data Analysis (EDA):** Visualize the relationship between `Study_Hours` and `Exam_Score`.
- **Regression Modeling:** Build a model to predict a student's score based on their habits.


### 📋 File Structure
- `student_performance.csv`: The raw dataset with 50 student records.
- `Research_Paper.pdf`: Documentation explaining the collection method and use cases.
- `README.md`: This project overview file.


### 💻 Tools & Technologies
- **VS Code**: Integrated Development Environment.
- **Python & Pandas**: For data manipulation.
- **Markdown**: For professional documentation.
