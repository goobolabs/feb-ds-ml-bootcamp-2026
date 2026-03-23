Cardiovascular Disease Prediction: Final Project Report & Reflection
Student Name: Fosia Dahir Ibrahim

Date: March 6, 2026

Tools Used: Python, FastAPI, Scikit-learn, Pandas, HTML/CSS

1. Introduction (Problem Statement & Motivation)
Heart disease is one of the biggest health challenges worldwide. Many people suffer from heart attacks or strokes simply because they didn't realize they were at risk. The motivation behind this project was to see if we could use Machine Learning to help identify these risks early.
By looking at simple data like blood pressure, cholesterol, and age, I wanted to build a tool that could give someone a "heads up" about their heart health. This isn't just a coding exercise for me; it’s about seeing how AI can actually be useful in healthcare.

2. Dataset & Preprocessing
For this project, I used a dataset of 70,000 patients from Kaggle. However, I quickly learned that real-world data is very "messy."

How I cleaned the data:

Fixing Outliers: I noticed some blood pressure readings were impossible (like 10,000 or negative numbers). I filtered these out so they wouldn't confuse the AI.

Feature Engineering: The age was originally in days, which is hard to read, so I converted it into years.

Scaling: Since "Weight" is a big number and "Cholesterol" is a small number (1, 2, or 3), I used scaling to make sure the model treats them fairly.

Encoding: I turned categorical data (like gender) into numbers so the algorithms could process them.

3. Algorithms Used
I decided to test two different models to see which one performed better:

Logistic Regression: I started with this because it’s a classic for "Yes/No" predictions. It's fast and easy to explain.

Random Forest Classifier: This is a much more powerful model. It uses many "Decision Trees" to come to a final conclusion. It’s great for medical data because it can see how different factors (like age and weight together) affect the heart.

The Result: The Random Forest was the clear winner, achieving an accuracy of about 75%.

4. Deployment (API & Frontend)
I didn't want my project to just be a script in a terminal, so I built a full system:

FastAPI Backend: I created a REST API that handles the predictions. It has a /predict endpoint where you can send patient data and get a result back instantly.

Frontend Interface: I used HTML and CSS to build a simple web form. This makes it easy for anyone—even someone who doesn't know how to code—to enter their health info and get a prediction.

5. Results & Discussion
The model works well, but it isn't perfect. A 75% accuracy is a great start, but in medicine, we want to be even more precise. I noticed that Blood Pressure and Age were the most important factors for the model.

I did a "sanity check" by entering very high blood pressure and an older age into the app, and the model correctly flagged it as "High Risk." This gave me confidence that the AI actually learned the right patterns.

6. Reflection (Lessons Learned)
This project was a big learning curve for me. Here are my main takeaways

Data Cleaning is 80% of the work: I spent way more time fixing the dataset than I did writing the actual AI code. If your data is bad, your model will be bad.

Connecting the dots: Learning how to connect a Python model to a web browser using FastAPI was the hardest part. It was frustrating at first when I got "Internal Server Errors," but solving them taught me a lot about how the web works.

Future Improvements: If I had more time, I would like to add more features like "Family History" or "Stress Levels" to make the predictions even more accurate.