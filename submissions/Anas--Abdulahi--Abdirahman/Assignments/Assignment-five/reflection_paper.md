# Part B – Reflection Paper  
## Spam Detection Using Logistic Regression, Random Forest, and Naive Bayes  

---

## 1. What I Implemented

In this assignment, I implemented three supervised machine learning models to detect spam messages: **Logistic Regression**, **Random Forest**, and **Naive Bayes (MultinomialNB)**.

First, I loaded the dataset `mail_l7_dataset.csv` using pandas. The dataset contains two columns: **Category** (spam or ham) and **Message** (text content). I cleaned the labels using `.str.lower()` and `.str.strip()` to ensure consistency, then encoded them as:

- spam = 0  
- ham = 1  

Next, I separated the dataset into:

- **X** → Message column (features)  
- **y** → Category column (target)  

I split the dataset into 80% training and 20% testing using `train_test_split` with `random_state=42` for reproducibility.

Since machine learning models cannot process raw text directly, I used **TF-IDF (Term Frequency–Inverse Document Frequency)** to transform text into numerical feature vectors. This method converts words into weighted numerical values based on their importance.

After preprocessing, I trained:

- Logistic Regression  
- Random Forest Classifier  
- Naive Bayes (MultinomialNB)  

Finally, I evaluated each model using **Accuracy, Precision, Recall, F1-Score, and Confusion Matrix**. I also performed a single-message sanity check using unseen test data.

---

## 2. Comparison of Models

To compare the models, I tested sample messages from the test set and observed the predictions from all three models.

For clearly defined spam or ham messages, all models generally agreed. However, in some borderline cases, small differences appeared.

- **Logistic Regression** produced stable and balanced predictions.
- **Random Forest** captured more complex patterns in text and often performed slightly better.
- **Naive Bayes** relied heavily on word probabilities and sometimes classified messages as spam if strong spam-related keywords appeared.

Overall, Random Forest and Logistic Regression gave more realistic predictions in uncertain cases, while Naive Bayes was more sensitive to specific words.

---

## 3. Understanding Naive Bayes

### What is Naive Bayes?

Naive Bayes is a probabilistic classification algorithm based on **Bayes’ Theorem**. It calculates the probability that a message belongs to a class (spam or ham) based on the probability of its words appearing in that class.

It is called “naive” because it assumes that all words are independent of each other. In real language, this assumption is not completely true, but it simplifies the computation.

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
- Simple and easy to implement  
- Strong baseline model  

**Limitations:**

- Assumes independence between words  
- Cannot capture complex word relationships  
- May be overly sensitive to certain keywords  

---

## 4. Metrics Discussion

To evaluate performance, I used:

- **Accuracy** → Overall correctness of predictions  
- **Precision** → Percentage of predicted spam that was actually spam  
- **Recall** → Percentage of actual spam correctly detected  
- **F1-Score** → Balance between Precision and Recall  
- **Confusion Matrix** → Detailed breakdown of prediction results  

The Confusion Matrix shows:

- **True Positives (TP)** → Spam correctly detected  
- **True Negatives (TN)** → Ham correctly detected  
- **False Positives (FP)** → Ham incorrectly predicted as spam  
- **False Negatives (FN)** → Spam incorrectly predicted as ham  

False Positives are important because legitimate messages should not be blocked. False Negatives are also critical because spam should not reach users’ inboxes.

Among the three models, **Random Forest achieved the best overall balance of Accuracy, Precision, Recall, and F1-Score**, followed closely by Logistic Regression. Naive Bayes performed slightly lower but remained effective.

---

## 5. My Findings

After comparing the three models, I would recommend **Random Forest** for spam detection because it achieved the highest overall performance and handled complex patterns in text more effectively.

However, **Logistic Regression** is also a strong option because it is simpler, interpretable, and still highly accurate. **Naive Bayes** is a good baseline model, especially when computational speed and simplicity are important.

In conclusion, all three models performed well in detecting spam messages, but Random Forest provided the most reliable and balanced results for this task.