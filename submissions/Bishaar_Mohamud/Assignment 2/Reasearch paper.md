The Relationship Between Mobile Phone Usage and Academic Performance Among University Students
Author: Bishaar Mohamud Abdirizak
Course: Data Foundations for Machine Learning
Date: 2026
1. Introduction
In recent years, mobile phone usage has significantly increased among university students. Smartphones are widely used for communication, entertainment, social media, and academic purposes. While mobile devices can support learning through online resources and educational applications, excessive usage—especially for social media—may negatively affect academic performance.
This study aims to examine the relationship between mobile phone usage habits and students’ Grade Point Average (GPA). The dataset was created specifically for this assignment to simulate real-world data collection and prepare it for future machine learning preprocessing and analysis.

2. Data Collection Method
The dataset was manually created to reflect realistic academic and behavioral patterns among university students. It contains data for 50 students. The data simulates responses that could be collected through a structured survey distributed via Google Forms.
The survey would include questions related to:
•	Age
•	Gender
•	Daily mobile phone usage (hours per day)
•	Daily social media usage (hours per day)
•	Daily study hours
•	Current GPA
The values were generated within realistic ranges:
•	Age: 20–24 years
•	Mobile usage: 2–10 hours per day
•	Social media usage: 1–7 hours per day
•	Study hours: 1–8 hours per day
•	GPA: 2.0–4.0
This approach ensures that the dataset reflects plausible student behavior while meeting the assignment requirement of at least 50 samples and 5 features.
________________________________________

3. Description of Features and Label
The dataset consists of seven columns: one identifier column (Name), five input variables (features), and one output variable (label).
Features (Independent Variables – X)
1.	Age – The age of the student (numeric).
2.	Gender – Male or Female (categorical).
3.	Mobile_Hours – Total hours spent using a mobile phone daily (numeric).
4.	Social_Media_Hours – Hours spent specifically on social media daily (numeric).
5.	Study_Hours – Hours spent studying per day (numeric).
Label (Dependent Variable – y)
•	GPA (Grade Point Average) – A numerical value between 2.0 and 4.0 representing academic performance.
The primary objective of this dataset is to analyze how mobile phone usage and study habits influence GPA.
________________________________________
4. Dataset Structure
The dataset contains:
•	50 rows (students)
•	7 columns (variables)
Below is a small sample (first 5 rows):
| Name	|Age	|Gender|  	Mobile_Hours	|Social_Media_Hours	|Study_Hours	|GPA
Ahmed Ali	|21	|Male	|6	|4	|2	|2.8
Ayaan Omar|	|22	|Female|	3	|2	|5	|3.6
Mohamed Hassan	|20	|Male	|8	|5	|1	|2.4
Fatima Nur	|23	|Female	|4	|2	|6	|3.8
Abdirahman Yusuf	|24	|Male	|7	|4	|2	|2.7
The structure is suitable for machine learning tasks because:
•	It includes both numerical and categorical variables.
•	It has a clearly defined target variable (GPA).
•	The dataset size meets the minimum assignment requirement.
________________________________________
5. Data Quality Issues
Since the dataset simulates real-world survey responses, several potential quality issues may exist:
1. Self-Reported Bias
Students may not accurately report their study hours or mobile usage. Some may overestimate study time or underestimate social media usage.
2. Missing Values
In real-world collection, some students may skip questions, leading to missing data.
3. Outliers
Some students might report extreme values (e.g., 12+ hours of mobile usage), which may require cleaning or normalization.
4. Categorical Encoding
The Gender variable is categorical and will need encoding (e.g., Male = 0, Female = 1) before being used in machine learning models.
5. Multicollinearity
Mobile_Hours and Social_Media_Hours may be strongly correlated, which could affect certain models.
These issues make the dataset suitable for preprocessing tasks such as:
•	Handling missing values
•	Encoding categorical variables
•	Feature scaling
•	Detecting outliers
________________________________________
6. Potential Use Cases in Machine Learning
This dataset can be applied to multiple machine learning tasks:
1. Regression
Because GPA is a continuous numerical value, this dataset is well-suited for regression analysis.
A regression model could predict GPA based on:
•	Mobile usage
•	Social media usage
•	Study hours
•	Age and gender
Example question:
How does an increase in daily mobile usage affect GPA?
Models that could be used:
•	Linear Regression
•	Decision Tree Regressor
•	Random Forest Regressor
________________________________________
2. Classification
The dataset can also be converted into a classification problem by categorizing GPA into groups such as:
•	High Performance (GPA ≥ 3.0)
•	Low Performance (GPA < 3.0)
In this case, models like:
•	Logistic Regression
•	K-Nearest Neighbors (KNN)
•	Support Vector Machines (SVM)
could be used to classify students into performance categories.
________________________________________
3. Clustering
Unsupervised learning techniques like K-Means clustering could group students based on behavioral patterns, such as:
•	High mobile use, low study time
•	Moderate mobile use, balanced study time
•	Low mobile use, high study time
This could help universities identify behavioral trends among students.
________________________________________
7. Conclusion
This project demonstrates the process of creating a real-world dataset for machine learning applications. The “Mobile Usage and GPA” dataset includes 50 student records with both numerical and categorical variables.
The dataset is suitable for regression, classification, and clustering tasks. It also contains realistic data challenges such as categorical variables and potential bias, making it ideal for preprocessing and feature engineering in future lessons.
By collecting and structuring this dataset, we gain practical experience in data preparation, which is a fundamental step in any machine learning project. Understanding how behavioral factors such as mobile phone usage influence academic performance can provide valuable insights for educational institutions and policymakers.

