# Reflection Paper – Assignment 05: Spam Detection

## 1. What did you implement?
I extended the spam detection project by training and evaluating three machine learning models: Logistic Regression, Random Forest, and Naive Bayes. Using the dataset `mail_l7_dataset.csv`, I preprocessed the text messages with TF‑IDF vectorization, encoded labels (spam=0, ham=1), and split the data into training and testing sets. Each model was trained and evaluated with accuracy, precision, recall, F1‑score, and confusion matrices. I also tested three sample messages to compare predictions.

## 2. Comparison of Models
For the sanity check messages:
- **“Free entry in 2 a weekly competition!”** → Logistic Regression: Spam, Random Forest: Ham, Naive Bayes: Spam  
- **“I will meet you at the cafe tomorrow”** → All models: Ham  
- **“Congratulations, you won a free ticket”** → Logistic Regression: Spam, Random Forest: Ham, Naive Bayes: Ham  

The models did not always agree. Logistic Regression was the most consistent in flagging spam, Random Forest was more conservative, and Naive Bayes was sensitive but missed borderline spam.

## 3. Understanding Naive Bayes
Naive Bayes is a probabilistic classifier based on Bayes’ theorem, assuming independence between features. In spam detection, it calculates the probability of a message being spam or ham based on word frequencies.  

- **Advantages**: fast, simple, effective with text, requires little training data.  
- **Limitations**: independence assumption is unrealistic, can misclassify when features are correlated.  

## 4. Metrics Discussion
- **Logistic Regression**: Accuracy 0.98, Precision 0.99, Recall 0.99, F1 0.99. Balanced performance, correctly flagged both spam examples.  
- **Random Forest**: Accuracy 0.97, Recall 1.0, F1 0.98. Strong but missed some spam messages.  
- **Naive Bayes**: Accuracy 0.95, Recall 1.0, F1 0.97. More false positives, showing sensitivity to spam.  

Confusion matrices revealed:
- Logistic Regression: few false positives and negatives.  
- Random Forest: almost no false negatives but more false positives.  
- Naive Bayes: highest false positives, mislabeling ham as spam.  

## 5. Findings
I recommend **Logistic Regression** for spam detection. It achieved the best balance of metrics and correctly flagged both spam examples. Random Forest is also strong, especially for minimizing false negatives, but it was conservative in spam detection. Naive Bayes remains a useful baseline due to its simplicity and speed, but it was less reliable for borderline spam.  

Overall, Logistic Regression provides the most consistent and realistic predictions, making it the best choice for deployment in a spam detection system.
