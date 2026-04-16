# Reflection Paper: Spam Detection

## 1. Implementation Process

I loaded the mail dataset with Category (spam=0, ham=1) and Message columns. I cleaned the data by replacing NaN values with empty strings and encoded the labels numerically.

I used TfidfVectorizer to convert text messages into numerical features. TF-IDF measures word importance by considering both term frequency and how rare the word is across all documents. I used an 80/20 train-test split with random_state=42.

I trained three models: Logistic Regression, Random Forest (200 trees), and Naive Bayes (MultinomialNB). All models were evaluated using Accuracy, Precision, Recall, F1-Score, and Confusion Matrix.

## 2. Model Comparison

In the 3 sanity check messages, the models mostly agreed but had some differences. For the message "Free entry in 2 a weekly competition!", Naive Bayes correctly identified it as spam while Logistic Regression and Random Forest were more cautious and marked it as ham.

For "I will meet you at the cafe tomorrow", all three models agreed it was ham (legitimate email). For "Congratulations, you won a free ticket", all models marked it as ham, even though it has spam-like words.

Naive Bayes gave more realistic predictions for obvious spam because it's trained to recognize spam word patterns like "free", "win", and "congratulations". The other models are more conservative to avoid false positives (blocking real emails that users need).

## 3. Naive Bayes Explanation

Naive Bayes is a probabilistic classifier based on Bayes' theorem. It calculates the probability that a message is spam given the words it contains. The "naive" part means it assumes all words are independent of each other.

MultinomialNB works well for text classification because it handles word counts naturally. It's fast to train and works well even with small datasets. Despite the independence assumption being unrealistic, Naive Bayes often performs surprisingly well for spam detection.

## 4. Metrics Discussion

- Accuracy: Overall correctness. Shows how many predictions were right out of total.
- Precision: Of predicted spam, how many are actually spam. High precision means fewer false alarms.
- Recall: Of actual spam, how many did we catch. High recall means fewer missed spam.
- F1-Score: Balance between precision and recall. Useful when both matter.
- Confusion Matrix: Shows the breakdown of predictions.

The Confusion Matrix tells us about mistakes:
- False Positives: Good emails wrongly marked as spam (bad - users miss important emails)
- False Negatives: Spam emails that got through to inbox (annoying - users see junk)

My models had zero false positives (perfect precision of 100%), meaning they never blocked legitimate emails. However, they had some false negatives (19-36 spam messages got through). This is the safer approach - better to let some spam through than block real emails.

## 5. Findings

All three models performed well (96-98% accuracy), showing that TF-IDF features work effectively for spam detection. Random Forest achieved the best overall performance with highest accuracy and recall.

The sanity checks showed models can disagree on edge cases. Some promotional messages are hard to classify because they use legitimate language. Random Forest's ensemble approach helps it handle these ambiguous cases better than single models.

For production spam filters, Random Forest is recommended due to its superior recall and accuracy. However, Naive Bayes could be used when speed and simplicity are priorities.
