Research Paper: The Commuter’s Lag Dataset
Title & Collection Method

Title:

The Commuter’s Lag: Impact of Daily Travel on Professional Productivity

Collection Method:

I designed a survey questionnaire and distributed it to 110 participants, consisting of both students and employees who commute daily. Each participant provided information about:

Distance traveled

Mode of transportation

Departure time

Traffic intensity

Hours of sleep

Level of fatigue or alertness upon arrival

Description of Features & Labels
Features (X)

Distance (numeric)
Distance from home to workplace or school (in kilometers).

Transport Mode (categorical)
Mode of transportation (Bus, Private Car, Walking, Motorbike).

Departure Time (numeric)
Time the person leaves home (e.g., 7:00, 8:30).

Traffic Intensity (categorical)
Level of traffic congestion (Low, Medium, High).

Sleep Hours (numeric)
Number of hours the person slept the previous night.

Label (y)

Productivity Level
Indicates whether the person feels energetic (High) or fatigued (Low) upon arrival.

Dataset Structure

Rows: 110 participants (samples)

Columns: 6 (5 features + 1 label)

Dataset (10 Rows)

Distance,Transport Mode,Departure Time,Traffic,Sleep Hours,Productivity
12,Bus,,High,6,Low
3,Walking,7.45,Low,8,High
25,Private Car,6.30,Medium,7,High
15,?,7.00,High,5,Low
5,Motorbike,8.00,Medium,6,High
10,Bus,7.30,High,,Low
20,Private Car,7.10,High,4,Low
2,Walking,8.15,Low,7,High
18,Bus,6.45,Medium,6,Low

Data Quality Issues

The dataset contains several issues that require preprocessing and cleaning:

1. Missing Values

Some participants did not report Sleep Hours, resulting in NaN values.

2. Categorical Text

Columns such as Transport Mode and Traffic Intensity are text-based and require encoding before being used in machine learning models.

3. Imbalanced Data

80 participants reported Low Productivity, while only 30 participants reported High Productivity, creating a class imbalance problem.

4. Inconsistent Reporting

Some participants wrote “P. Car” while others wrote “Private Car”, requiring data standardization.

Use Case

This dataset can be used to train a classification model to predict whether a commuting individual is likely to experience fatigue (Low Productivity) or not.

Possible Algorithms

Logistic Regression

Decision Tree

Random Forest

Benefit

The dataset can help organizations understand how daily commuting affects productivity, enabling them to design flexible work schedules, improve employee well-being, and increase overall efficiency.