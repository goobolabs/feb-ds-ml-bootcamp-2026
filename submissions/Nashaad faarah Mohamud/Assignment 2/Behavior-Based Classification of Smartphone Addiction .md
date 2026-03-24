Behavior-Based Classification of Smartphone Addiction Using Screen Time Data

1. Title & Collection Method

Title

Behavior-Based Classification of Smartphone Addiction Using Screen Time Data

Collection Method

This dataset was collected using an observational and manual logging method.
With the consent of participants, I directly inspected system-generated usage statistics from their smartphones, specifically using iOS Screen Time and Android Digital Wellbeing dashboards.

Instead of relying on memory-based surveys, I recorded objective usage metrics such as daily screen time, number of phone checks, and number of social media applications used during the most recent 24-hour period.
The addiction level was collected as a self-assessed response from participants.

This dataset was created manually and was not obtained from Kaggle, UCI, or any other pre-made repository.


2. Description of Features & Label

Input Features (X)
	1.	ScreenTime (hrs/day)
Total daily active screen usage in hours.
	2.	SocialAppsUsed
Number of applications categorized as social media on the device.
	3.	PhoneCheckFreq
Number of times the phone was checked (pickups or unlocks) per day.
	4.	SleepTime (hrs/day)
Average sleep duration reported by the user or synced from health apps.
	5.	Age
Age of the participant in years.

Output Label (y)
	•	AddictionLevel
A categorical variable representing the user’s self-assessed smartphone addiction level:
	•	Low
	•	Medium
	•	High


3. Dataset Structure
	•	Number of Rows: 100
	•	Number of Columns: 6

Sample of the Dataset (First 8 Rows)

ScreenTime	SocialAppsUsed	PhoneCheckFreq	SleepTime	Age	AddictionLevel
2.5	2	45	8.5	45	Low
9.2	8	185	5.0	19	High
5.0	4	90	7.0	30	Medium
11.5	10	240	4.5	16	High
1.8	1	30	9.0	55	Low
7.5	6	120	6.0	24	Medium
4.2	3	75	7.5	38	Medium
10.0	9	210	5.5	21	High




4. Data Quality Issues

To reflect real-world data challenges and prepare for preprocessing in Lesson 3, the dataset includes several quality issues:
	1.	Missing Values
Some rows have missing values in the SocialAppsUsed column due to device privacy restrictions.
	2.	Categorical Inconsistency
A typo exists in one row where “Highs” was entered instead of “High”, requiring text normalization.
	3.	Measurement Variability
Phone checking frequency combines metrics from both iOS (pickups) and Android (unlocks), which are measured slightly differently.
	4.	Potential Outliers
Extremely high screen time values (over 12 hours) appear for some participants and may skew distributions.

These issues make the dataset suitable for cleaning, encoding, scaling, and feature engineering.



5. Use Case in Machine Learning

This dataset is designed for a classification Machine Learning task.

Primary Use Case
	•	Predicting a user’s smartphone addiction level (Low, Medium, High) based on behavioral usage patterns.

ML Applications
	•	Supervised classification models (Logistic Regression, Decision Trees, Random Forests)
	•	Feature importance analysis to identify the strongest predictors of addiction
	•	Digital wellness systems that generate early warning alerts for high-risk usage behavior


