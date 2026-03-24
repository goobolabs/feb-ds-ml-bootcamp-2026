NAME: Abdislaam Salad Ali
Assingnment 2: Data Foundations for Machine Learning

Research Paper: Impact of Internet Usage on University Students’ Academic Grades

1. Title & Collection Method

Title: Impact of Internet Usage on University Students’ Academic Grades
Collection Method:
I created a short survey using Google Forms and shared it with university students to collect information about their internet usage habits and academic performance. The survey included questions about daily internet hours, sleep hours, internet purpose, night internet usage, online learning hours, and final grades. Participation was voluntary and responses were anonymous. 

2. Description of Features & Label
Features (X):
•	Daily Internet Hours (numeric): Hours a student spends on the internet each day
•	Sleep Hours per Day (numeric): Average sleep hours per night
•	Internet Purpose (categorical): Main purpose of internet usage (Study, Social Media, or Mixed)
•	Night Internet Use (categorical: Yes/No): Whether a student uses the internet after 10 PM
•	Online Learning Hours (numeric): Hours spent on online courses or educational content
•	
Label (y):
•	Final Grade: A, A-, B+, B, B-, C+, C, C-, D, F
This makes the problem a multi-class classification task.

3. Dataset Structure
•	Rows: Responses collected from university students (more than 50 samples)
•	Columns: 6 (5 features + 1 label)

Sample Table (6 rows):

Year,Daily Internet Hours,Internet Purpose,Night Internet Use,Online Learning Hours ,Sleep Hours,Grade	
Year 3	5	Mixed 	No	 	5	A-
Year 2	10	Mixed 	Yes	1	6	A-
Year 2	9	Social Media	No	0	6	B-
Year 3	24	Mixed 	Yes	 	10	B-
Year 3	2	Mixed 	No	1	8	A
Year 2	18	Mixed 	No	6	9	C
This table represents a small sample of the collected dataset

4. Data Quality Issues
•	Some optional questions may contain missing values
•	Data is self-reported, which may introduce slight inaccuracies
•	Class imbalance exists (more A/B grades than D/F)
•	Categorical features require encoding before applying Machine Learning models

5. Use Case
   
This dataset can be used to train Machine Learning models to predict students’ academic grades based on their internet usage habits.
Possible Machine Learning tasks include:
•	Classification: Predict final grades (A–F)
•	Regression: Predict numerical academic performance (if converted)
•	Clustering: Group students based on similar internet usage behaviors
Suitable algorithms include Logistic Regression, Decision Trees, Random Forests, and Gradient Boosting.
6.  Conclusion

This study presents a real-world dataset collected from university students to analyze the relationship between internet usage and academic performance. The dataset provides valuable insights and will be further preprocessed and analyzed for Machine Learning model training. The results can help identify patterns and support early intervention strategies for students at academic risk.





	
