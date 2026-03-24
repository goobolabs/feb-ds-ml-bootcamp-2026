Step 1: Clean the Dataset
1. Remove Duplicates
•	Record_ID 6006–6009 for Wadajir appears twice → remove duplicates.
2. Handle Missing Values
We can fill missing values with approximate or average numbers:
Column	How to fill missing values
Patients	Use average patients for the same Department & Area
Avg_Wait_Time_Min	Use median wait time for that Department
Treatment_Cost_USD	Use median cost for that Department
Recovery_Rate_%	Use average recovery rate for that Department
Example:
•	Record 6003 (Hodan, Mar, Surgery) → Avg_Wait_Time_Min missing → fill with 55 min (median Surgery wait time in Hodan).
•	Record 6004 (Hodan, Apr, OPD) → Patients missing → fill with 150 (average OPD patients in Hodan).
________________________________________
Step 2: Structure the Dataset
Your dataset has 8 columns (features + label):
1.	Area – categorical
2.	Month – categorical
3.	Department – categorical
4.	Patients – numeric
5.	Avg_Wait_Time_Min – numeric
6.	Treatment_Cost_USD – numeric
7.	Recovery_Rate_% – numeric
8.	Status – categorical (label)
________________________________________
Step 3: Sample Table (5–10 rows)
Record_ID	Area	Month	Department	Patients	Avg_Wait_Time_Min	Treatment_Cost_USD	Recovery_Rate_%	Status
6001	Hodan	Jan	Emergency	120	45	80000	88	Open
6002	Hodan	Feb	OPD	150	30	50	92	Open
6003	Hodan	Mar	Surgery	80	55	300	85	Open
6004	Hodan	Apr	OPD	150	45	90	90	Closed
6005	Hodan	May	Maternity	140	35	50	88	Open
6006	Wadajir	Jan	Emergency	110	50	75	86	Open
6007	Wadajir	Feb	OPD	145	32	55	91	Open
You can continue the pattern for all 50 rows.
________________________________________
Step 4: Describe Dataset Quality Issues
•	Missing values: Patients, Avg_Wait_Time_Min, Treatment_Cost_USD, Recovery_Rate_%
•	Duplicates: Some rows repeated → removed
•	Inconsistencies: Treatment costs vary widely (50–360 USD)
•	Imbalance: Some departments (OPD) appear more frequently than others (Surgery)
________________________________________
Step 5: Use Case in Machine Learning
1.	Regression: Predict Recovery_Rate_% from Patients, Wait Time, Cost
2.	Classification: Predict Status (Open/Closed) based on department metrics
3.	Clustering: Group similar departments or areas based on cost, recovery, and wait times

