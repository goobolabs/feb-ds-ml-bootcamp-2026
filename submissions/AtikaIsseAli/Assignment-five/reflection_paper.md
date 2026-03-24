# 🎓 Assignment 5: Spam Detection Report
**Author:** Atika Isse Ali
**Date:** September 2025

---

## 1. Project Implementation 🛠️
In this project, I built a machine learning system to classify SMS messages as either **Spam (0)** or **Ham (1)**. I didn't just use one model; I compared three different algorithms to see which one works best:
* **Logistic Regression:** A reliable linear model.
* **Random Forest:** An ensemble model using many decision trees.
* **Naive Bayes (MultinomialNB):** A probabilistic model that is very famous for text classification.

I used **TF-IDF Vectorization** to convert the words into numbers so the models could analyze them. I also split the data into 80% for training and 20% for testing to ensure the results were accurate.

---

## 2. The Battle of the Models: My Results 📊
After running my code, here are the performance metrics I achieved:

| Model | Accuracy | Precision | Recall | F1-Score |
| :--- | :--- | :--- | :--- | :--- |
| **Logistic Regression** | 0.968 | 1.000 | 0.758 | 0.863 |
| **Naive Bayes** | 0.977 | 1.000 | 0.826 | 0.904 |
| **Random Forest** | **0.979** | **1.000** | **0.846** | **0.916** |

**What I learned from these numbers:**
* All models got **1.000 Precision**. This means they never accidentally blocked a "Ham" (good) message. This is perfect for a user's experience!
* **Random Forest** had the highest overall Accuracy and Recall, meaning it was the best at finding the spam.

---

## 3. Comparing the 3 Sanity Checks 🧪
I tested the models with 3 specific messages to see how they behave:

* **Message 1:** *"Free entry in 2 a weekly competition!"* * Only **Naive Bayes** correctly caught this as **Spam**. Logistic Regression and Random Forest were too careful and called it Ham. 
* **Message 2:** *"I will meet you at the cafe tomorrow"* * All models correctly labeled this as **Ham**.
* **Message 3:** *"Congratulations, you won a free ticket"*
  * Naive Bayes was the most sensitive to the "spammy" keywords here.



---

## 4. Understanding Naive Bayes 🧠
* **What is it?** Naive Bayes is a classifier based on probabilities. It’s called "Naive" because it assumes every word in a sentence is independent (it doesn't look at word order).
* **Why use it for Spam?** It is very fast and works amazingly well with word frequencies. It looks at the probability of words like "Free" or "Win" appearing in Spam vs. Ham.
* **Pros/Cons:** It is super fast and needs less data, but its limitation is that it ignores the context or relationship between words.

---

## 5. Metrics & Confusion Matrix Discussion 📈
My **Confusion Matrix** (for example, Random Forest: `[[123, 26], [0, 966]]`) tells a clear story:
* **0 False Positives:** This confirms no good mail was blocked.
* **False Negatives:** There were about 26 spam messages that "leaked" through to the inbox. This shows that while the models are very safe, we could still work on catching those last few tricky spam messages.



---

## 6. My Final Recommendation 🏆
I recommend the **Random Forest** model because it achieved the highest Accuracy (97.9%) and F1-Score. However, I would also recommend using **Naive Bayes** as a backup or "keyword filter" because it was the only model that correctly caught the "Free entry" spam message that the more complex models missed!

---