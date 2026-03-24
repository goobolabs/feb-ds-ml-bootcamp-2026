# Spam Detection Reflection Paper



### 1. What did you implement?

In this assignment, I implemented a **Spam Detection system** using three different machine learning models: **Logistic Regression**, **Random Forest Classifier**, and **Naive Bayes (MultinomialNB)**. The dataset consisted of email messages labeled as either **spam (0)** or **ham (1)**.  

I preprocessed the data by handling missing values and encoding the labels. Then, I converted the text messages into numerical features using **TF-IDF vectorization**. Each of the three models was trained on 80% of the data and tested on the remaining 20%. Finally, I evaluated the models using **accuracy, precision, recall, F1-score**, and **confusion matrices**. I also performed **single-message sanity checks** to compare predictions on three example messages.

---

### 2. Comparison of Models – Single-message Predictions

The three sample messages used for testing were:

1. `"Free entry in 2 a weekly competition!"`  
2. `"I will meet you at the cafe tomorrow"`  
3. `"Congratulations, you won a free ticket"`  

**Predictions:**

| Message | Logistic Regression | Random Forest | Naive Bayes |
|---------|-------------------|---------------|-------------|
| Free entry… | Ham (1) | Ham (1) | Spam (0) |
| I will meet… | Ham (1) | Ham (1) | Ham (1) |
| Congratulations… | Ham (1) | Ham (1) | Ham (1) |

- **Observation:** Logistic Regression and Random Forest misclassified the first message as Ham, while Naive Bayes correctly identified it as Spam. None of the models correctly predicted the third message as Spam.  
- **Conclusion:** Naive Bayes showed more realistic predictions for messages with clear spam indicators.

---

### 3. Understanding Naive Bayes

**Naive Bayes** is a probabilistic machine learning algorithm based on **Bayes’ theorem**, assuming that all features are **independent** of each other. Despite this "naive" assumption, it performs very well in text classification tasks like spam detection.  

- **Why often used in spam detection:**  
  - Works well with high-dimensional text data.  
  - Efficient and fast to train on large datasets.  
  - Handles probabilistic word occurrence effectively.  

- **Advantages:**  
  - Simple and easy to implement.  
  - Works well with small datasets.  
  - Requires less computational resources.  

- **Limitations:**  
  - Assumes independence of features, which may not always hold.  
  - Sensitive to very rare words or phrases.  
  - Sometimes less accurate compared to ensemble methods on complex datasets.

---

### 4. Metrics Discussion

**Performance metrics from the test set:**

| Model | Accuracy | Precision | Recall | F1-score |
|-------|---------|-----------|--------|----------|
| Logistic Regression | 0.968 | 1.000 | 0.758 | 0.863 |
| Random Forest | 0.983 | 1.000 | 0.872 | 0.932 |
| Naive Bayes | 0.977 | 1.000 | 0.826 | 0.904 |

**Observations:**

- **Random Forest** achieved the highest overall accuracy and F1-score, with the best recall for spam detection.  
- **Confusion Matrices** showed that Logistic Regression missed 36 spam messages, Random Forest missed 19, and Naive Bayes missed 26.  
- **False positives** (ham predicted as spam) were 0 for all models, indicating excellent precision.

---

### 5. Findings and Recommendation

Based on both the metrics and single-message sanity checks:

- **Random Forest** is the best model overall due to its **high accuracy, precision, recall, and F1-score**.  
- **Naive Bayes** is particularly strong in identifying clear spam messages in single-message tests, showing its suitability for text-based spam detection.  
- **Logistic Regression** performed reasonably well but had lower recall, missing more spam messages.

**Recommendation:** I would recommend **Random Forest** for this spam detection system in real-world scenarios, potentially combined with **Naive Bayes** in an ensemble approach to capture simple, obvious spam patterns efficiently.

---

*End of Reflection Paper*