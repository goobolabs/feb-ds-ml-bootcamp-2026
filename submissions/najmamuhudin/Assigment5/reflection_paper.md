Reflection Paper – Spam Detection Using Machine Learning

1️ What Did I Implement?

In this project, I implemented a spam detection system using three different machine learning algorithms:

Logistic Regression

Random Forest

Naive Bayes (MultinomialNB)

First, I loaded the dataset and handled missing values by replacing them with empty strings. Then, I converted the text messages into numerical vectors using TF-IDF (Term Frequency–Inverse Document Frequency).

After splitting the dataset into training and testing sets (80% training and 20% testing), I trained all three models using the training data.

Finally, I evaluated each model using the following performance metrics:

Accuracy

Precision

Recall

F1-Score

Confusion Matrix

2️ Comparison of Models (Sanity Check Messages)

The three test messages were:

"Free entry in 2 a weekly competition!"

"I will meet you at the cafe tomorrow"

"Congratulations, you won a free ticket"

Most models predicted:

The first message as Spam

The second message as Ham

The third message as Spam

In general:

Logistic Regression and Naive Bayes often agreed in their predictions.

Random Forest sometimes behaved slightly differently depending on the dataset distribution.

The predictions were realistic because promotional, prize-related, and “free” messages were correctly identified as spam, while normal conversational text was classified as ham.

3️ Understanding Naive Bayes

Naive Bayes is a probabilistic classification algorithm based on Bayes’ Theorem. It assumes that features (words in a message) are independent of each other. This strong independence assumption is why it is called “naive.”

Why is Naive Bayes commonly used in spam detection?

It works very well with text data.

It is fast and computationally efficient.

It performs well even with relatively small datasets.

It handles high-dimensional feature spaces effectively.

Advantages

Simple and easy to implement

Very fast training and prediction

Works well with high-dimensional text data

Strong baseline model for text classification

Limitations

Assumes independence between words (which is not always realistic)

May struggle with complex relationships between features

Performance can drop when word dependencies are important

4️ Metrics Discussion

Among the three models, Random Forest often achieved the highest overall accuracy. However, Logistic Regression also performed very well and was more stable across different data splits.

The Confusion Matrix provided deeper insight into model performance by showing:

False Positives (FP): Ham messages incorrectly classified as Spam

False Negatives (FN): Spam messages incorrectly classified as Ham

In spam detection systems, false negatives are particularly dangerous, because spam messages may pass through the filter and reach users. Therefore, Recall is especially important when evaluating spam classifiers.

Balancing precision and recall using the F1-Score helps ensure that the model performs well overall.

5️ My Findings

Based on the experimental results, Random Forest achieved slightly higher performance in terms of accuracy. However, Logistic Regression was more consistent and computationally efficient. Naive Bayes also performed well and was extremely fast.

If I had to recommend one model for real-world spam detection, I would choose:

Logistic Regression for balanced performance and stability

Naive Bayes for speed and simplicity in large-scale systems

Both models are efficient, reliable, and well-suited for text classification tasks such as spam detection.