# Reflection Paper – Spam Detection Using Machine Learning

## 1. What Did I Implement?

In this project, I implemented a complete spam detection system using three different machine learning models: Logistic Regression, Random Forest, and Naive Bayes. The goal of the project was to classify SMS messages as either spam or ham (not spam).

First, I loaded the dataset and cleaned it by selecting only the necessary columns (Category and Message). I then converted the labels into numerical values, where:

- Ham = 0  
- Spam = 1  

After preprocessing, I split the dataset into training and testing sets using an 80/20 ratio. To prepare the text data for machine learning models, I transformed the messages into numerical features using TF-IDF (Term Frequency–Inverse Document Frequency). This allowed the models to understand the importance of words in each message.

Finally, I trained and evaluated three classification models and compared their performance.

---

## 2. Comparison of Models

After training the models, I evaluated them using accuracy as the main performance metric.

The results were:

- Logistic Regression: 0.9677
- Random Forest: 0.9785
- Naive Bayes: 0.9767

From these results, Random Forest achieved the highest accuracy. However, Naive Bayes performed almost equally well, with only a small difference in performance. Logistic Regression also performed strongly and provided a solid baseline model.

When comparing predictions, Random Forest generally produced slightly more accurate classifications, especially in borderline cases. Naive Bayes performed very efficiently and consistently, while Logistic Regression showed strong linear decision-making behavior.

Overall, Random Forest gave the most realistic and highest-performing results.

---

## 3. Understanding Random Forest

Random Forest is an ensemble learning method that combines multiple decision trees to improve prediction accuracy.

Instead of relying on a single decision tree, Random Forest builds many decision trees during training. Each tree makes its own prediction. For classification tasks, the final prediction is determined by majority voting among all trees.

This approach reduces overfitting and improves generalization. Because each tree sees slightly different data (through bootstrapping and feature randomness), the model becomes more stable and less sensitive to noise.

In simple terms, Random Forest works by:
1. Creating many decision trees.
2. Allowing each tree to make a prediction.
3. Combining all predictions using majority voting.

This ensemble approach explains why Random Forest achieved the highest accuracy in this project.

---

## 4. Metrics Discussion

In this classification task, accuracy was used to compare the models. Random Forest achieved the highest accuracy (97.85%), followed closely by Naive Bayes (97.67%), and then Logistic Regression (96.77%).

These results show:

- Logistic Regression performs well when the relationship between features and labels is relatively linear.
- Naive Bayes is very effective for text classification because it works well with word frequency features and assumes conditional independence between features.
- Random Forest is powerful because it captures complex, non-linear patterns in the data.

The slightly higher performance of Random Forest suggests that the dataset contains patterns that benefit from ensemble learning rather than relying on a single linear model.

---

## 5. My Findings and Conclusion

Based on the results, I prefer Random Forest for this spam detection task because it achieved the highest accuracy and demonstrated strong overall performance. It handled the TF-IDF features effectively and produced stable predictions.

However, I also recognize that Naive Bayes is highly efficient and nearly as accurate. For large-scale or real-time systems where computational efficiency matters, Naive Bayes may be a very practical choice.

Logistic Regression remains a strong baseline model due to its simplicity and interpretability.

In conclusion, while all three models performed well, Random Forest provided the best balance between accuracy and robustness in this spam classification project.