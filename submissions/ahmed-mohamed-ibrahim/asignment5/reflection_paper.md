# Spam Detection Using Logistic Regression, Random Forest, and Naive Bayes
---
## 1. What I Implemented
In this assignment, I implemented three supervised machine learning models to detect spam messages: **Logistic Regression**, **Random Forest**, and **Naive Bayes (MultinomialNB)**.
First, I loaded the dataset `mail_l7_dataset.csv` using pandas. The dataset contains two columns:
- **Category** → target label (spam or ham)
- **Message** → input text
I handled missing values by replacing them with empty strings. Then, I standardized the labels using `.str.lower()` and `.str.strip()` and encoded them as:
- spam = 0  
- ham = 1  
Next, I separated the dataset into:
- **X (Features)** → Message column  
- **y (Target)** → Category column  
I split the dataset into 80% training data and 20% testing data using `train_test_split` with `random_state=42` to ensure reproducibility.
Because machine learning models cannot process raw text directly, I used **TF-IDF (Term Frequency–Inverse Document Frequency)** to convert text into numerical feature vectors. TF-IDF assigns weights to words based on how important they are within a message compared to the entire dataset.
After preprocessing, I trained three models:
1. Logistic Regression  
2. Random Forest Classifier  
3. Naive Bayes (MultinomialNB)  
Finally, I evaluated each model using:
- Accuracy  
- Precision  
- Recall  
- F1-Score  
- Confusion Matrix  
I also performed sanity checks using three custom example messages.
---
## 2. Comparison of Models
To compare the models, I tested the following three example messages:
1. "Free entry in 2 a weekly competition!"  
2. "I will meet you at the cafe tomorrow"  
3. "Congratulations, you won a free ticket"  
For the clearly spam messages (1 and 3), all three models predicted **Spam (0)**.  
For the normal message (2), all models predicted **Ham (1)**.
In most cases, the models agreed on the predictions. However, in some borderline or ambiguous test messages, small differences appeared.
- **Logistic Regression** produced stable and balanced predictions.
- **Random Forest** captured more complex patterns and often achieved slightly better overall performance.
- **Naive Bayes** relied heavily on word probabilities and sometimes classified messages as spam when strong spam-related keywords were present.
Overall, Random Forest and Logistic Regression provided more balanced predictions in uncertain cases, while Naive Bayes was more sensitive to keyword patterns.
---
## 3. Understanding Naive Bayes
### What is Naive Bayes?
Naive Bayes is a probabilistic classification algorithm based on **Bayes’ Theorem**. It calculates the probability that a message belongs to a specific class (spam or ham) based on the probabilities of its words appearing in that class.
It is called "naive" because it assumes that all words (features) are independent of each other. In real language, this assumption is not fully true, but it simplifies calculations and works effectively in practice.
---
### Why is it often used in spam detection?
Naive Bayes is widely used in spam detection because:
- It works very well with text data.
- It is computationally efficient.
- It handles large vocabularies effectively.
- Spam detection mainly depends on word frequency patterns.
---
### Advantages and Limitations
**Advantages:**
- Fast training and prediction  
- Works well with high-dimensional text data  
- Easy to implement  
- Strong baseline model  
**Limitations:**
- Assumes independence between words  
- Cannot capture complex word relationships  
- May be overly sensitive to certain keywords  
---
## 4. Metrics Discussion
To evaluate the models, I used the following metrics:
- **Accuracy** → Overall correctness of predictions  
- **Precision** → Percentage of predicted spam that was actually spam  
- **Recall** → Percentage of actual spam correctly detected  
- **F1-Score** → Balance between Precision and Recall  
- **Confusion Matrix** → Detailed breakdown of predictions  
The Confusion Matrix shows:
- **True Positives (TP)** → Spam correctly detected  
- **True Negatives (TN)** → Ham correctly detected  
- **False Positives (FP)** → Ham incorrectly predicted as spam  
- **False Negatives (FN)** → Spam incorrectly predicted as ham  
False Positives are important because legitimate messages should not be blocked. False Negatives are also critical because spam should not reach the user’s inbox.
Based on the evaluation results:
- **Random Forest achieved the best overall performance**, with the highest balance of Accuracy and F1-Score.
- Logistic Regression performed very closely and showed strong Precision and Recall.
- Naive Bayes performed slightly lower but remained effective and efficient.
---
## 5. My Findings
After comparing all three models, I would recommend **Random Forest** for spam detection because it achieved the best overall balance of performance metrics and handled complex text patterns effectively.
However, **Logistic Regression** is also a strong option due to its simplicity, interpretability, and high accuracy. If computational speed and simplicity are priorities, **Naive Bayes** is a good alternative.
In conclusion, all three models performed well in detecting spam messages, but Random Forest provided the most reliable and balanced results for this task.