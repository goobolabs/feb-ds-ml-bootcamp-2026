# Part B – Reflection Paper  
**Topic: Spam Detection Using Machine Learning**

## 1. What Did You Implement?

In this assignment, I implemented a spam detection system using three different machine learning models: **Logistic Regression**, **Random Forest**, and **Naive Bayes**. The dataset consisted of SMS messages labeled as either *spam* or *ham*. Before training the models, the text data was preprocessed and converted into numerical features using **TF-IDF (Term Frequency–Inverse Document Frequency)**.

Logistic Regression was used as a baseline linear classifier because it performs well on high-dimensional text data. Random Forest was implemented as an ensemble, tree-based model to capture more complex patterns in the data. Naive Bayes, specifically Multinomial Naive Bayes, was applied because it is a classical and widely used model for text and spam classification tasks. All three models were trained on the same training data and evaluated using the same test set to ensure a fair comparison.

---

## 2. Comparison of Models (Sanity Check Messages)

A sanity check was performed by selecting a single SMS message from the test set and predicting its label using all three models. In this experiment, **Logistic Regression, Random Forest, and Naive Bayes all agreed on the prediction**, correctly classifying the message as *ham*.

Since all models produced the same output for the sanity check message, there was no disagreement in this case. However, when comparing realism, Logistic Regression and Naive Bayes are generally considered more reliable for text-based problems because they are specifically designed for sparse, high-dimensional data. Random Forest also performed well, but it required converting TF-IDF features into dense format, which is less efficient for large-scale text data.

---

## 3. Understanding Naive Bayes

**Naive Bayes** is a probabilistic machine learning algorithm based on Bayes’ Theorem. It assumes that all features are independent of each other given the class label. In text classification, this means that each word contributes independently to the probability of a message being spam or ham.

Naive Bayes is often used in spam detection because it is simple, fast, and highly effective for text data. It performs especially well when combined with bag-of-words or TF-IDF representations, even when the independence assumption is not perfectly true.

**Advantages of Naive Bayes:**
- Very fast to train and predict  
- Works well with high-dimensional and sparse data  
- Requires relatively small amounts of training data  

**Limitations of Naive Bayes:**
- Assumes feature independence, which is not always realistic  
- May perform poorly if important word relationships are ignored  
- Often slightly less accurate than more complex models  

---

## 4. Metrics Discussion

The evaluation of the models was based on **Accuracy, Precision, Recall, F1-Score, and Confusion Matrix**.

- **Random Forest** achieved the highest overall performance, with the best Accuracy and F1-Score.
- **Naive Bayes** performed very well and showed strong Recall and F1-Score, making it highly suitable for spam detection.
- **Logistic Regression** had perfect Precision but lower Recall, meaning it was conservative and missed some spam messages.

The **Confusion Matrix** provided deeper insight into the models’ behavior. All three models showed **zero false positives**, meaning no legitimate (ham) messages were incorrectly classified as spam. This is very important in real-world spam detection systems. The main errors came from **false negatives**, where some spam messages were incorrectly classified as ham. Random Forest produced the fewest false negatives, followed by Naive Bayes and then Logistic Regression.

---

## 5. Findings and Recommendation

Based on the experimental results, **Random Forest** achieved the best numerical performance in terms of Accuracy, Recall, and F1-Score. However, it required dense feature conversion and is computationally heavier for text data. **Naive Bayes** offered an excellent balance between performance, speed, and simplicity, making it a strong and practical choice for spam detection systems.

Therefore, for real-world spam detection, I would recommend **Naive Bayes** due to its efficiency, reliability, and suitability for text data. Logistic Regression is also a strong alternative when interpretability is important. Random Forest can be used when maximum performance is required, but it may not be the most efficient choice for large-scale text-based applications.