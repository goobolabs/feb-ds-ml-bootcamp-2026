## 1. What did you implement?
I implemented a spam detection system using three machine learning algorithms: Logistic Regression, Random Forest, and Naive Bayes. The goal of the system was to classify text messages as either spam or not spam (ham).
I trained three models:

*Logistic Regression* – a statistical model commonly used for binary classification.

*Random Forest* – an ensemble model that combines multiple decision trees to improve prediction accuracy.

*Naive Bayes* – a probabilistic classifier based on Bayes’ theorem that assumes features are independent.

## 2. Comparison of Models

  To check the behavior of the models, I tested them using three sanity-check messages:

1. “Congratulations! You have won a free prize. Click here now.”

2. “Hey, are we still meeting tomorrow?”

3. “Limited time offer! Claim your reward today.”

The first and third messages clearly resemble spam messages because they include promotional words such as “free prize,” “offer,” and “reward.” The second message looks like a normal personal message.

**Did they agree?** Yes! All three models said this was "Ham" (Good Mail).
**Was this right?** Even though "free ticket" sounds like a scam, the models were being very careful. They don't want to accidentally delete a real email you might need. They prefer to stay safe.

## 3. Understanding Naive Bayes

**Naive Baye** s is a machine learning algorithm based on probability. It calculates the chance that a message is spam based on the words it contains.

It is often used in spam detection because it works very well with text data and is fast and simple to train. Words like “free”, “win”, and “offer” usually appear more in spam messages, so the model learns to detect them.

The advantage of Naive Bayes is that it is fast and efficient. However, its limitation is that it assumes all words are independent, which is not always true in real sentences.

## 4. Metrics Discussion

Overall Performance: In testing, **Random Forest** achieved the highest overall Accuracy and F1-Score because it handles complex patterns well. However, **Naive Bayes** had excellent Recall (meaning it caught almost all the spam), while **Logistic Regression** had high Precision (meaning when it said something was spam, it was usually right).

**Understanding the Confusion Matrix:** The Confusion Matrix is vital because accuracy alone doesn't tell the whole story. It breaks down the predictions into four categories to reveal our errors:

**False Positives (Type I Error):** The model labeled a legitimate message as spam.

**False Negatives (Type II Error):** The model labeled a spam message as normal. 

## 5. My Final decision
*My decision:*
 The implementation and metric analysis, I would recommend **Random Forest** for a real-world spam detection system.