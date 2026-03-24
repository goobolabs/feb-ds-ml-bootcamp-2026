1\. Title \& Collection Method

Title: Student Study Habits and Academic Performance Dataset (Ages 18–25)



Collection Method



This dataset examines how daily habits of students aged 18 to 25 relate to their academic performance. The data was collected using a survey-based manual logging approach, where information about students’ personal habits and academic behavior was recorded.



Students were observed or surveyed regarding their daily study hours, sleep duration, internet quality, and class attendance. Exam results were recorded as a binary outcome (pass or fail). The dataset was created specifically for this assignment and does not rely on any pre-existing datasets such as Kaggle or UCI repositories. The collection process reflects real-world conditions where data may be noisy or imperfect.



2\. Description of Features and Label

Input Variables (Features X)



The dataset includes the following five input features:



Age: Age of the student (between 18 and 25 years).



Daily\_Study\_Hours: Average number of hours the student studies per day.



Internet\_Quality: Quality of internet access available to the student (Poor, Average, Good, Excellent).



Sleep\_Hours: Average number of hours the student sleeps per night.



Attendance\_Percentage: Percentage of classes attended by the student.



Output Variable (Label y)



Passed\_Exam: Indicates whether the student passed the exam (Yes or No).



This label serves as the target variable for machine learning prediction tasks.



3\. Dataset Structure



Number of Rows: 50



Number of Columns: 6



Number of Features: 5



Number of Labels: 1



Sample Records from the Dataset

Age	Study Hours	Internet Quality	Sleep Hours	Attendance %	Passed Exam

24	7.5	Poor	7.8	83	Yes

22	1.0	Poor	7.0	96	Yes

19	4.8	Excellent	7.3	98	Yes

18	1.9	Poor	8.8	74	No

23	6.3	Excellent	8.6	80	No

4\. Data Quality Issues



The dataset contains several realistic data quality challenges commonly found in real-world machine learning projects:



Categorical data (Internet\_Quality) that requires encoding before modeling.



Class imbalance, as the number of students who passed and failed the exam is not perfectly balanced.



Noisy patterns, such as students with low study hours but high attendance still passing the exam.



Mixed data types, including numerical and categorical variables.



Outliers, such as extremely high study hours or very low sleep durations.



These issues make the dataset suitable for practicing data preprocessing and cleaning techniques.



5\. Use Case in Machine Learning



This dataset can be applied to multiple machine learning tasks:



Classification



The primary use case is binary classification, where the objective is to predict whether a student will pass or fail an exam based on their daily habits.



Regression



The dataset may also be used for regression problems, such as predicting attendance percentage or estimating daily study hours.



Clustering



Unsupervised learning techniques can be applied to group students with similar behavior patterns, such as highly disciplined students or at-risk students.



6\. Conclusion



This dataset provides hands-on experience with real-world data collection and preparation for machine learning. By focusing on students aged 18–25, the dataset reflects realistic academic behavior patterns and includes natural variability and imperfections. It is well-suited for preprocessing, exploratory data analysis, and machine learning model development.

