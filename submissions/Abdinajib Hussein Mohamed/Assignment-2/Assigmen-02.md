Name: Abdinajib Hussein Mohamed 
Research Paper: Relationship Between Sleep Hours and Academic Performance Dataset

 Title & Data Collection Method

Title: Relationship Between Sleep Hours and Academic Performance Dataset

Data Collection Method:
I designed an online survey questionnaire and collected responses from *students* within a limited time frame. The survey focused on students’ sleep patterns, study habits, and academic results. A total of 50 students participated in the survey, providing information about their average sleep hours per night, daily study hours, screen time, class attendance, and academic performance.

Description of Features & Label

Features (X):

1. Sleep Hours per Night (Numeric): Average number of hours a student sleeps each night.

2. Study Hours per Day(Numeric): Time spent studying on a typical day.

3. Screen Time per Day(hour/Day): Average daily hours spent on phones, computers, or TV.

4. Class Attendance (Categorical: Day/ week):Frequency of attending classes.

5. Semester level (Categorical: Low / Medium / High) (optional if included)

Label (y):

Exam score: (Average / Good / Poor)

This formulation makes the problem a classification task*, where the goal is to predict academic performance based on sleep hours and related factors.


### *Dataset Structure*

Rows: [5] students (samples)
Columns: 8 (7 features + 1 label)

#### Sample Dataset (10 Rows)
Enter your Age?	Status	Simisterkee ayaad maraysaa waxbarashada jaamacadda?	S1: Imisa saacadood ayaad Habeenki Seexataa/Hurudaa?	S2:Imisa Saacadood ayaad maalinki waxbarataa?	S3:Celcelis intee saacadood ayaad Screen/mobile ka isticmaashaa Maalinki?	S4: Imisa Maalin Ayaad soo Xaadirtaa Isbuuci Xisadaha?	S5: Heerka Natiijadii Imtixaankii U danbeyay?
20	Singe	Semester 3	6 Hours	5 Hours	10-5 hour/day	Dhaaman Todobaadka ma maqnaado 6 day/week	80-90%
16	Singe	Semester 3	8 Hours	6 Hours	8 Hour/day	5 day/week	70-80%
22	Singe	Semester 3	7 Hours	3 Hours	8-1 Hour/day	Dhaaman Todobaadka ma maqnaado 6 day/week	80-90%
22	Singe	Semester 3	7 Hours	6 Hours	8 Hour/day	Dhaaman Todobaadka ma maqnaado 6 day/week	80-90%
21	Singe	Semester 4	8 Hours	13 saacad	8-1 Hour/day	Dhaaman Todobaadka ma maqnaado 6 day/week	80-90%


### *Data Quality Issues*

* *Missing values:* Some students skipped optional questions such as Class Attendance and Semester Level.
* *Categorical variables:* Attendance and semester level require encoding before model training.
* *Self-reported data:* Sleep hours and study time may contain minor inaccuracies.
* *Class imbalance:* More students passed than failed, which may affect model performance.

---

### *Use Case*

This dataset can be used to train a *machine learning classification model* that predicts whether a student is likely to perform well academically based on sleep duration and related habits.

*Possible Algorithms:*

* Logistic Regression
* Decision Tree
* Random Forest

The results can help educators and students understand the *importance of adequate sleep* and identify students who may be at risk of poor academic performance due to unhealthy sleep patterns

