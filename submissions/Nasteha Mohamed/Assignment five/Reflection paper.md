1. **What did you implement?**
### In this project, I implemented a spam detection system using three machine learning models: Logistic Regression, Random Forest, and Naive Bayes (MultinomialNB).

- Logistic Regression: This model treats spam detection as a binary classification problem, learning a linear relationship between TF-IDF features of the email messages and the probability of being spam.

- Random Forest: This is an ensemble of decision trees that votes on the class of each message. It can capture non-linear patterns and interactions between words in the emails.

- Naive Bayes: A probabilistic model that calculates the likelihood of a message being spam based on the frequency of words. It assumes feature independence, which simplifies computation and works well for text classification.

### The dataset used contained email messages labeled as spam (0) or ham (1). After preprocessing and transforming the text using TF-IDF vectorization, the three models were trained and evaluated on the test set

2. **Comparison of Models:**

   * Compare the results of the **3 sanity check messages**.
   * Did all models agree? If not, which one gave more realistic predictions?


   For the three sanity check messages, the predictions were:

| Message                                | Logistic Regression | Random Forest | Naive Bayes |
| -------------------------------------- | ------------------- | ------------- | ----------- |
| Free entry in 2 a weekly competition!  | Ham                 | Ham           | Spam        |
| I will meet you at the cafe tomorrow   | Ham                 | Ham           | Ham         |
| Congratulations, you won a free ticket | Ham                 | Ham           | Ham         |

- Logistic Regression and Random Forest both classified all three messages as Ham.

- Naive Bayes only predicted the first message as Spam; the other two messages were predicted as Ham.

  #### This shows that Naive Bayes was slightly more sensitive to the “spammy” wording in the first message, while Logistic Regression and Random Forest were more conservative in these examples

  3. **Understanding Naive Bayes:**

### Naive Bayes is a probabilistic model using Bayes’ theorem with the assumption that features (words) are independent.

- Why used in spam detection: Efficiently estimates the probability of spam based on word occurrences, which is particularly      useful for textual data.

## Advantages:

- Fast training and prediction

- Works well with high-dimensional text features

- Simple implementation

## Limitations:

- Assumes independence between words, which is not always true

- Can be less consistent on borderline case

4. **Metrics Discussion:**

   * Which model had better **Accuracy, Precision, Recall, F1-Score, and Confusion Matrix**?
   * What does the Confusion Matrix tell you about **false positives** and **false negatives**?

- Accuracy: The Random Forest model had the highest accuracy (~0.98), slightly outperforming Logistic Regression (~0.97) and Naive Bayes (~0.96).

- Precision: Random Forest also had the highest precision (~0.98), meaning it made the fewest false positive predictions (ham emails incorrectly labeled as spam).

- Recall: Both Logistic Regression and Random Forest achieved perfect recall (1.00), correctly identifying all spam emails without missing any. Naive Bayes had slightly lower recall (~0.99).

- F1-Score: Random Forest had the best F1-Score (~0.99), indicating the best balance between precision and recall.

- Confusion Matrix Insights

Using Random Forest as an example, the confusion matrix looked like this:

[[130, 36],
 [  0, 966]]

False Positives (FP): 36 legitimate emails (ham) were incorrectly classified as spam.

False Negatives (FN): 0 spam emails were missed, meaning all spam was correctly detected.

5. **Your Findings:**

   * Summarize in 1–2 paragraphs which model you would recommend for spam detection and why.

   ### Random Forest is the recommended model for spam detection because it achieves perfect recall while minimizing false positives, providing both high sensitivity and precision. It can effectively detect all spam messages while misclassifying the fewest legitimate emails as spam.

  ### Naive Bayes is also highly effective, matching Random Forest in recall and overall accuracy, but with slightly more false positives. Logistic Regression remains reliable, with perfect recall but more false positives than the other two models, making it slightly less precise











