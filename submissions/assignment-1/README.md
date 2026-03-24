&nbsp;Assignment 1: Machine Learning Research Report

Student Name:\[Sara Mohamed Nur]





1\. Concept of Machine Learning

Machine Learning (ML) is basically the science of getting computers to act without being explicitly programmed. In traditional computing, we provide the rules, but in ML, we provide the data, and the system finds the patterns.



Practical Example: A good example is Credit Card Fraud Detection , When you use your card, the bank's system checks if the transaction matches your usual behavior (like where you shop or how much you spend). If I suddenly buy something very expensive in another country, the system flags it as fraud. It learns this from millions of previous data points.



2\. Comparing Learning Paradigms: Supervised and Unsupervised

In my research, I found that the primary difference between these two types of learning is the presence of a target or "teacher" during the training process.



Supervised Learning (Learning with Guidance): This method relies on labeled datasets. It is like a student learning from a textbook that has the answers at the back. The model makes a prediction and is corrected if it's wrong.



Real-world Example: Email Spam Filtering. The system is fed thousands of emails that humans have already marked as "Spam" or "Not Spam." Through this, it learns the characteristics of unwanted mail so it can categorize future emails.



Unsupervised Learning (Finding Hidden Structures): Unlike supervised learning, this type works with unlabeled data. There is no "correct answer" provided. Instead, the algorithm tries to find inherent groupings or patterns within the data.



Real-world Example: Customer Persona Analysis. A retail company might have data on 10,000 customers but no labels for them. Unsupervised learning (like Clustering) can group these customers into segments, such as "High-spenders" or "Discount-hunters," based purely on their buying habits.|



&nbsp;3. The Problem of Overfitting

Overfitting happens when a model is "too smart" for its own good. It memorizes the training data perfectly, including the noise, but fails when it sees new, real-world data. It's like a student who memorizes an exam paper but doesn't understand the subject.



How to fix it:

Cross-Validation: Testing the model on different parts of the data.

Regularization: Making the model simpler so it doesn't over-complicate things.

More Data: Sometimes the best fix is just giving the model more examples.



4\. Why we Split Data (Train vs. Test)

In every ML project, we split data into two: Training (usually 80%) and Testing (20%).

We do this because we need to see how the model behaves on data it has never seen before. If we test it with the same data we used to train it, we are just checking its memory, not its intelligence.



&nbsp;5. Case Study: Machine Learning in Healthcare

I researched how ML is used in Cancer Detection. According to several papers (like those from Google Health), Deep Learning models are now used to scan X-rays and MRI images.

The Result: These models can find tiny tumors that doctors might miss. They sometimes reach an accuracy of 99% (AUC), helping doctors make faster and more accurate decisions.



&nbsp;References

1\. Mitchell, T. (1997). Machine Learning. McGraw-Hill.

2\. Bishop, C. (2006). Pattern Recognition and Machine Learning. Springer.

3\. Recent studies in AI-based Medical Imaging (2023-2024).

