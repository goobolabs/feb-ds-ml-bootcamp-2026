Spam Detection Using Logistic Regression, Random Forest and Naive Bayes
1. What Did I Implement?

In this project, I implemented a spam detection system using three classification algorithms: Logistic Regression, Random Forest, and Naive Bayes. First, I loaded the dataset and cleaned missing values. Then, I encoded the labels (spam = 0, ham = 1).

I converted text messages into numerical features using TF-IDF vectorization. After splitting the data into training (80%) and testing (20%), I trained all three models and evaluated them using Accuracy, Precision, Recall, F1-Score, and Confusion Matrix.

2. Comparison of Models (Sanity Check)

For the three example messages:

“Free entry in 2 a weekly competition!” → predicted as Spam.

“I will meet you at the cafe tomorrow” → predicted as Ham.

“Congratulations, you won a free ticket” → predicted as Spam.

Most models agreed on clearly spam-like and clearly normal messages. In cases where models disagreed, Naive Bayes tended to classify promotional words as spam more aggressively.

3. Understanding Naive Bayes

Naive Bayes is a probabilistic classification algorithm based on Bayes’ Theorem. It assumes that features are independent of each other, which is why it is called “naive.”

It is commonly used in spam detection because:

It works very well with text data.

It is fast and computationally efficient.

It performs well even with high-dimensional data.

Advantages:

Simple and fast

Works well for text classification

Requires less training data

Limitations:

Assumes feature independence

Can struggle with complex relationships between words

4. Metrics Discussion

The Confusion Matrix shows:

False Positives → Ham messages wrongly classified as Spam.

False Negatives → Spam messages classified as Ham.

In spam detection, false negatives are dangerous because spam reaches the user’s inbox. Therefore, a model with higher Recall for spam is often preferred.

Random Forest often achieved the highest overall Accuracy, but Naive Bayes performed very efficiently and competitively.

5. Final Recommendation

Based on the results I would recommend Random Forest for highest accuracy and balanced performance. However, Naive Bayes is also an excellent choice because it is fast, simple and performs very well for text classification tasks like spam detection.