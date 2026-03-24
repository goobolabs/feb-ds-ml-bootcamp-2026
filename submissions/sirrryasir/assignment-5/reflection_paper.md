# Reflection Paper: Spam Detection

## 1. What Did I Implement?
In this assignment, I implemented a spam detection system using three classifiers: **Logistic Regression**, **Random Forest**, and **Naive Bayes (MultinomialNB)**. I loaded the `mail_l7_dataset.csv`, cleaned the data by replacing missing values with empty strings, and encoded labels (spam = 0, ham = 1). I used **TF-IDF** to convert text into numeric features, split the data 80/20, trained all three models, and evaluated them using Accuracy, Precision, Recall, F1-Score, and a Confusion Matrix.

## 2. Comparison of Models
For the 3 sanity check messages, all three models correctly identified "I will meet you at the cafe tomorrow" as **Ham** and "Congratulations, you won a free ticket" as **Ham**. However, for the spam-like message "Free entry in 2 a weekly competition!", only **Naive Bayes** correctly classified it as **Spam**, while Logistic Regression and Random Forest both predicted it as Ham. This shows that Naive Bayes has a stronger sensitivity to spam-like keywords such as "free," "entry," and "competition."

## 3. Understanding Naive Bayes
**Naive Bayes** is a probabilistic classifier based on Bayes' Theorem. It calculates the probability that a message belongs to a class (spam or ham) based on word frequencies. It's called "naive" because it assumes all words are independent of each other.

**Why it's used in spam detection:** It works very well with text data, is extremely fast to train, and performs well even with small datasets. Its word-level probability approach naturally fits the spam detection problem.

**Advantages:** Fast, simple, effective with text, handles high-dimensional data well.
**Limitations:** The independence assumption can be unrealistic; it may struggle with unseen words or complex word relationships.

## 4. Metrics Discussion
- **Accuracy:** All three models achieved high accuracy — Random Forest led with 0.983, followed by Naive Bayes (0.977), then Logistic Regression (0.968).
- **Precision:** All three models achieved perfect precision (1.000), meaning no ham emails were wrongly flagged as spam.
- **Recall:** Random Forest had the highest recall (0.872), meaning it caught the most spam overall. Naive Bayes had 0.826, and Logistic Regression had 0.758.
- **F1-Score:** Random Forest had the best F1-Score (0.932), followed by Naive Bayes (0.904) and Logistic Regression (0.863).
- **Confusion Matrix:** The matrices showed that false positives were zero across all models. The main differences were in false negatives (spam that slipped through): LR missed 36, NB missed 26, and RF missed only 19.

## 5. My Findings
I would recommend **Random Forest** for spam detection when accuracy is the top priority, as it consistently achieved the best metrics with the highest recall and F1-Score. However, **Naive Bayes** is a strong alternative — it trains much faster and, as shown in the sanity checks, can catch certain spam messages that Logistic Regression and Random Forest miss due to its word-probability approach. For a production system, combining both models could offer the best of both worlds.
