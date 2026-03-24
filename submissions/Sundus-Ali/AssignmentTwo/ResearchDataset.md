*1. Title and Collection Method *

*Title:*
A Study on Sleep Habits and Their Effect on Daily Energy Levels

*Collection Method:*
The dataset was collected using an online survey questionnaire distributed among university students. Participants were asked questions related to their sleeping habits, bedtime routines, screen usage before sleep, and their daily energy levels.

The survey method was chosen because it allows the collection of real-world behavioral data directly from individuals. Each participant voluntarily provided responses, which were automatically recorded in a spreadsheet. A total of *128* responses were collected.

The data represents typical daily sleep behaviors and self-reported energy levels of students. Since the data was collected manually from real users, it reflects natural variations and imperfections commonly found in real-world datasets.
---

*2. Description of Features and Label*

The dataset contains several input variables (features) and one main output variable (label).

*Input Variables (Features X)*

*1.Age* : Represents the age group of the respondent (e.g., 19–22, 23–26).
This helps analyze whether age influences sleep patterns.

*2.Sleep Duration* : The number of hours the participant sleeps each night (e.g., <5 hours, 5–6 hours, 7–8 hours).

*3.Bedtime*: The time the participant usually goes to sleep (e.g., Before 10 PM, 10–11 PM).

*4.Screen Time Before Bed* :The amount of time spent using electronic devices before sleeping (e.g., 0–30 min, >3 hours).

*5.Sleep Quality*: Self-reported sleep quality (Good, Average, Poor).

*6.Wake-up Time*: The usual time the participant wakes up.

Output Variable (Label Y)

*7.Daily Energy Level*: This indicates whether the participant feels Energetic or Tired during the day.

This label can be predicted using machine learning techniques based on the input features.
---

*3. Dataset Structure*

Number of Rows (Samples): 128

Number of Columns: 7 total columns (including timestamp and one empty column)
Useful Features: 7 main features

Label: Daily Energy Level


*Sample Data (First 15 Records)*
| Age | Sleep Duration | Bedtime | Screen Time | Sleep Quality | Energy Level | Wake-up Time |
|-----|---------------|---------|-------------|--------------|-------------|-------------|
| 27–30 | Less than 5 hours | Before 10 PM | 0–30 minutes | Poor | Energetic | Before 5 AM |
| 19–22 | 5–6 hours | 10–11 PM | More than 3 hours | Poor | Tired | 5–6 AM |
| 23–26 | 5–6 hours | Before 10 PM | 30–60 minutes | Good | Energetic | Before 5 AM |
| 19–22 | 7–8 hours | Before 10 PM | 30–60 minutes | Good | Energetic | Before 5 AM |
| 23–26 | 5–6 hours | 12–1 AM | 30–60 minutes | Good | Energetic | 5–6 AM |
| 23–26 | 5–6 hours | 10–11 PM | 1–2 hours | Fair | Energetic | 6–7 AM |
| 19–22 | 7–8 hours | 10–11 PM | 0–30 minutes | Good | Energetic | 5–6 AM |
| 19–22 | 7–8 hours | 10–11 PM | 30–60 minutes | Good | Energetic | 5–6 AM |
| 15–18 | 7–8 hours | 11 PM–12 AM | 0–30 minutes | Good | Energetic | Before 5 AM |
| 23–26 | 5–6 hours | After 1 AM | 30–60 minutes | Good | Energetic | Before 5 AM |
| 19–22 | 5–6 hours | 10–11 PM | 30–60 minutes | Good | Energetic | 6–7 AM |
| 23–26 | Less than 5 hours | Before 10 PM | 0–30 minutes | Poor | Energetic | Before 5 AM |
| 19–22 | 9–10 hours | 12–1 AM | 2–3 hours | Poor | Tired | After 8 AM |
| 15–18 | 5–6 hours | 11 PM–12 AM | 30–60 minutes | Good | Tired | 5–6 AM |
| 23–26 | 7–8 hours | 10–11 PM | 1–2 hours | Good | Tired | 7–8 AM |
---

*4. Data Quality Issues*

Since the dataset was collected from real participants, several quality issues are present:

*Missing Data*

*1.* Another issue observed in the dataset is that the target variable (Daily Energy Level) is positioned between feature columns rather than being clearly separated. During preprocessing, the label column should be moved to the final position to improve dataset organization and model preparation.

*2.*One column is completely empty and should be removed during preprocessing.

*3*.Categorical Text Values:

*4.*Many features contain text categories (e.g., “Good”, “Poor”, “5–6 hours”).

 These must be encoded into numeric values before machine learning.

*5.* Inconsistent Feature Naming:Column names are long and include full survey questions.

These should be shortened and standardized.

*6.*Age Stored as Ranges: Age groups are not numeric values.

May need conversion for statistical analysis.

*7.*Human Error: Survey-based data may contain inaccurate or subjective responses.

These issues will require preprocessing such as cleaning, encoding, and feature transformation.
---

*5.* Use Case for Machine Learning

This dataset can be used in several machine learning applications.

*.* Classification is suitable this Dataset :The primary use is classification, where the goal is to predict whether a student will feel: Energetic,Tired

Based on their sleep habits.

For example, a model could learn that:

Longer sleep duration

Earlier bedtime

Lower screen time

May increase the probability of feeling energetic.

*Other Possible Applications*

*.* Regression

Predict a numerical energy score if converted.

*.* Clustering

Group students based on similar sleeping patterns.

Behavior Analysis

Study relationships between screen time and sleep quality.

and i uploaded the excel file of my Dataset 
