Name: Fosia Dahir Ibrahim

# Cardiovascular Disease Prediction System

  What is this project about?
This is my final project where I built a Machine Learning system to help predict the risk of heart disease in patients. I wanted to create something practical, so I didn't just stop at the AI model
I also built a web interface using FastAPI so that anyone (like a doctor or a patient) can easily enter data and get a prediction instantly.

The goal is Prevention. By catching the risk factors early, we can help people make lifestyle changes before things get serious.

 # The Data (Dataset)
I used a well-known dataset from Kaggle containing about 70,000 patient records.
The AI looks at several factors to make its decision:

Medical data: Age, Gender, Height, Weight.

Health measurements: Blood Pressure (High/Low), Cholesterol levels, and Glucose.

Lifestyle: Whether the person smokes, drinks alcohol, or stays active (physical activity).
## Note Based on the project refinement, the "Alcohol" feature was removed from the input data and model logic to focus on the remaining 10 features.


#  Technical Overview
To meet the project requirements and evaluation criteria, this system includes:

 Data: Cleaned and preprocessed 70,000 patient records from Kaggle.
 Algorithms: Implemented and compared Random Forest (Best performing) and Logistic Regression.
 Evaluation: Achieved a prediction accuracy of 73-75%.
 API: Fully functional REST API built with FastAPI for real-time predictions.


 # How I built it (Algorithms)
I experimented with two different models to see which one works best

Random Forest: This was the winner with the best accuracy. It uses multiple decision trees to come to a final conclusion.

Logistic Regression: I used this as a baseline to compare the results.

The models were trained in Python using libraries like scikit-learn, pandas, and joblib.

# How to run the project
First, make sure you have the requirements installed. Then

1. To train the models again

Bash
python train.py
2. To start the Web Server

Bash
uvicorn main:app --reload
After running this, just open your browser and go to http://127.0.0.1:8000.

#  Testing the API (For Developers)
If you want to test the REST API directly using curl, you can use this command:

Bash
curl -X 'POST' \
  'http://127.0.0.1:8000/predict' \
  -H 'Content-Type: application/json' \
  -d '{
  "age": 45,
  "gender": 1,
  "height": 170,
  "weight": 75,
  "ap_hi": 130,
  "ap_lo": 85,
  "cholesterol": 2,
  "gluc": 1,
  "smoke": 0,
  "active": 1
}'
 # Final Results
Accuracy: The system is around 73-75% accurate, which is a good start for this type of medical data.

Tech Stack: Python, FastAPI, Jinja2 Templates (HTML/CSS), and Scikit-learn.

I'm really happy with how it turned out, and I'm planning to improve the accuracy in the future by adding more data.

# GitHub Link:
https://github.com/foosiyodaahir7-art/cardiovascular_diseases_project



