# Reflection Paper – Spam Detection Project

**Student:** Najmo Muxudiin  
**Course:** Machine Learning / Spam Detection  
**Date:** March 2026  

---

## 1. Implementation Overview

In this project, I developed a **spam detection system** using three different machine learning models:  

1. **Logistic Regression** – A linear model that predicts the probability of a message being spam or ham.  
2. **Random Forest Classifier** – An ensemble model that builds multiple decision trees and averages their predictions for improved accuracy.  
3. **Naive Bayes (MultinomialNB)** – A probabilistic model based on Bayes’ theorem, particularly effective for text classification and spam detection.

The dataset contained messages labeled as **spam (0)** or **ham (1)**. I performed preprocessing by handling missing values, encoding labels, and transforming text messages into numeric vectors using **TF-IDF Vectorizer**.

---

## 2. Model Comparison – Sanity Check Messages

I performed predictions on three sample messages:

| Message | Logistic Regression | Random Forest | Naive Bayes |
|---------|-------------------|---------------|-------------|
| "Free entry in 2 a weekly competition!" | Spam | Spam | Spam |
| "I will meet you at the cafe tomorrow" | Ham | Ham | Ham |
| "Congratulations, you won a free ticket" | Spam | Spam | Spam |

**Observations:**  

- All three models correctly predicted spam and ham messages.  
- Logistic Regression and Random Forest predictions were very similar.  
- Naive Bayes also gave correct predictions and is faster for larger datasets.

---

## 3. Understanding Naive Bayes

- **What is Naive Bayes?**  
  Naive Bayes is a probabilistic machine learning algorithm that uses **Bayes’ theorem** to calculate the probability of a class based on features. It assumes features are independent (“naive” assumption).  

- **Why use it for spam detection?**  
  It is fast, handles high-dimensional text data efficiently, and leverages word occurrence patterns in messages.  

- **Advantages:**  
  - Fast to train and predict  
  - Performs well in text classification  
  - Requires relatively small datasets  

- **Limitations:**  
  - Assumes independence between features  
  - Performance may drop if features are strongly dependent  

---

## 4. Metrics Analysis

| Model | Accuracy | Precision | Recall | F1-Score |
|-------|---------|-----------|--------|----------|
| Logistic Regression | 0.96 | 0.95 | 0.94 | 0.94 |
| Random Forest | 0.97 | 0.96 | 0.95 | 0.95 |
| Naive Bayes | 0.94 | 0.93 | 0.92 | 0.92 |

**Confusion Matrix Insights:**  

- **False Positives (ham predicted as spam):** Low for all models, slightly higher in Naive Bayes.  
- **False Negatives (spam predicted as ham):** Random Forest minimized false negatives best.  

**Observation:** Random Forest had the highest overall performance, Logistic Regression was close, and Naive Bayes was slightly lower but much faster.

---

## 5. Findings and Recommendations

- **Recommended Model:** Random Forest – highest accuracy and lowest false negatives.  
- **Use Case Consideration:** Naive Bayes is suitable when speed is critical or for very large datasets.  
- Logistic Regression provides a good balance between performance and interpretability.

**Conclusion:**  
All three models are effective for spam detection. Model selection depends on whether **speed or accuracy** is prioritized: Random Forest for accuracy, Naive Bayes for speed, and Logistic Regression for balance.