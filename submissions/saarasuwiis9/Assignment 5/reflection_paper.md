# Reflection Paper: Spam Detection Project

1. What I Implemented

In this project, I extended the spam detection system by implementing three different machine learning models: **Logistic Regression**, **Random Forest**, and **Naive Bayes (MultinomialNB)** . The goal was to classify email messages as either **spam (0)** or **ham (1)**.

First, I loaded the dataset `mail_l7_dataset.csv`, which contains two columns: *Category* (target) and *Message* (text input). I handled missing values by replacing them with empty strings. The labels were encoded so that spam = 0 and ham = 1.

Next, I split the dataset into features (X = messages) and target (y = category). The data was divided into 80% training and 20% testing sets. I then applied **TF-IDF vectorization** to convert text data into numerical features suitable for machine learning models.

After preprocessing, I trained:

* Logistic Regression
* Random Forest Classifier
* Multinomial Naive Bayes

Each model was evaluated using Accuracy, Precision, Recall, F1-Score, and Confusion Matrix.


2. Comparison of Models (Sanity Checks)

Three example messages were tested:

1. "Free entry in 2 a weekly competition!"
2. "I will meet you at the cafe tomorrow"
3. "Congratulations, you won a free ticket"

For the first and third messages, all models predicted **Spam**, which is realistic because they contain promotional and prize-related words commonly associated with spam emails.

For the second message, all models predicted **Ham**, which is correct since it represents a normal conversation.

In general, the models mostly agreed. If there were minor differences, Random Forest and Logistic Regression tended to produce more stable and realistic predictions compared to Naive Bayes. However, Naive Bayes still performed reasonably well.

 3. Understanding Naive Bayes

 What is Naive Bayes?

Naive Bayes is a probabilistic classification algorithm based on **Bayes' Theorem**. It calculates the probability that a message belongs to a certain class (spam or ham) based on the presence of words in the message.

It is called "naive" because it assumes that all features (words) are independent of each other given the class label. In reality, words are often related, so this assumption is not fully accurate.

 Why is it often used in spam detection?

Naive Bayes is widely used in spam detection because:

* It works very well with text data.
* It handles high-dimensional data efficiently.
* It is fast and requires relatively low computational resources.
* It provides strong baseline performance.

Advantages

* Simple to implement
* Fast training and prediction
* Performs well with large vocabularies
* Works effectively even with limited training data

Limitations

* Assumes independence between words
* May perform worse when word relationships are important
* Can be less accurate than more complex models

---

 4. Metrics Discussion

Among the three models:

* **Random Forest** achieved the highest overall accuracy and F1-score.
* **Logistic Regression** performed very closely to Random Forest.
* **Naive Bayes** had slightly lower accuracy but remained competitive.

The **Confusion Matrix** helps identify false positives and false negatives:

* **False Positives**: Legitimate emails incorrectly classified as spam.
* **False Negatives**: Spam emails incorrectly classified as ham.

In spam detection, false negatives are especially risky because spam messages may bypass filtering. However, too many false positives can frustrate users by blocking important emails.

Random Forest showed a better balance between minimizing false positives and false negatives.

---

 5. My Findings and Recommendation

Based on the results, Random Forest provided the best overall performance in terms of accuracy, precision, recall, and F1-score. It handled complex patterns in text data more effectively than the other models.

However, Logistic Regression performed almost as well while being computationally simpler and faster. Naive Bayes was the fastest and simplest model, but its independence assumption limits its performance compared to the others.

If computational resources are available, I would recommend **Random Forest** for deployment because it provides the strongest classification performance. If efficiency and scalability are more important, **Logistic Regression** would be a practical and balanced alternative.