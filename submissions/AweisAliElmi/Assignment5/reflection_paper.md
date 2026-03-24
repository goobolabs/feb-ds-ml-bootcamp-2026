# Reflection Paper: Spam Detection with Naive Bayes, Logistic Regression, and Random Forest 

---

## 1. What did you implement?

In this project, I created a system to classify SMS messages as either "Ham" (normal) or "Spam". I implemented three different machine learning models to see how they compare: **Logistic Regression**, **Random Forest**, and **Naive Bayes (MultinomialNB)**.

My workflow included:
- Loading the `mail_l7_dataset.csv` dataset.
- Cleaning the data by replacing missing values (NaNs) with empty strings to avoid errors during vectorization.
- Converting the text messages into numeric features using `TfidfVectorizer`.
- Splitting the dataset into an 80% training set and a 20% testing set.
- Evaluating each model using Accuracy, Precision, Recall, and F1-Score to get a full picture of their performance.

---

## 2. Comparison of Models: Sanity Check Results

I tested the models with three specific messages to see their predictions in real scenarios:

1. **"Free entry in 2 a weekly competition!"**  
   - Logistic Regression & Random Forest: **Ham**
   - Naive Bayes: **Spam**
   - *Result:* Naive Bayes was the most realistic here. This is a very common type of spam message that the other two models missed.

2. **"I will meet you at the cafe tomorrow"**  
   - All models: **Ham**
   - *Result:* Correct. All models easily identified this as a normal personal message.

3. **"Congratulations, you won a free ticket"**  
   - All models: **Ham**
   - *Result:* Not realistic. This is clearly a spam message, but all three models failed to catch it. This shows that while the models are good, they aren't perfect and might need more data or better tuning.

**Observation:** Naive Bayes was the only model to catch the first tricky spam message ("Free entry"), while the others were a bit too conservative.

---

## 3. Understanding Naive Bayes

**What is Naive Bayes?**  
Naive Bayes is a probabilistic algorithm based on Bayes’ Theorem. It is called "naive" because it assumes that every word in a message is completely independent of the others. Although this is rarely true in human language, the algorithm is surprisingly effective for text.

**Why is it often used in spam detection?**  
It's a popular choice because it handles high-dimensional data (like text) very well and it is extremely fast. It works by looking at the frequency of words in spam vs. ham messages and calculating the probability of a new message belonging to either category.

**Advantages and Limitations:**
- **Advantages:** It is very fast to train, requires very little data to get started, and works great for simple text classification.
- **Limitations:** Its main weakness is the independence assumption. It can't understand the context or the relationship between words (like sarcasm or complex phrases).

---

## 4. Metrics Discussion

Looking at the performance markers:
- **Random Forest** had the highest overall accuracy (98.3%) and the best recall (87.2%), meaning it caught the highest percentage of spam messages in the test set.
- **Precision:** All models achieved 100% precision. This is great because it means they never accidentally marked a "Ham" message as "Spam". I'd rather miss a few spam messages than have an important personal email go to the spam folder.
- **Recall:** This is where the models varied. Random Forest was best at actually finding the spam, followed by Naive Bayes and then Logistic Regression.

**Confusion Matrix Interpretation:** The matrix showed 0 False Positives for all models, which confirms the high precision. However, the False Negatives (missed spam) were present, especially for Logistic Regression.

---

## 5. Your Findings and Recommendation

Based on my analysis, I would recommend the **Random Forest** model if overall reliability and accuracy are the priority, as it performed best on the large test set. 

However, **Naive Bayes** showed better intuition on the "Free entry" sanity check. For a real-world application, I might suggest using an ensemble approach or further tuning Naive Bayes with more specific "spammy" keywords to improve its catching rate even further. Overall, Random Forest is the most robust model for this particular dataset.