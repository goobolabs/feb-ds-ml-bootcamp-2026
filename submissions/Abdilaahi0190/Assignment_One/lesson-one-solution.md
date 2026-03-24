# Research Assignment: Introduction to Machine Learning

**Name:** Abdulaahi Ahmed Jimaale
**Date:** February 2, 2026

## 1. Defining Machine Learning
Machine Learning (ML) is a branch of Artificial Intelligence (AI) that provides systems the ability to automatically learn and improve from experience without being explicitly programmed.

**Example:** A spam filter is an ML application. By looking at thousands of emails that have been marked as spam by users, the system learns to identify patterns (like certain keywords or sender addresses) and can then predict whether a new incoming email is spam or not.

## 2. Supervised vs. Unsupervised Learning

| Feature | Supervised Learning | Unsupervised Learning |
| :--- | :--- | :--- |
| **Data** | Uses labeled data (input and correct output). | Uses unlabeled data (only input). |
| **Goal** | To predict an outcome or classify data. | To find hidden patterns or structures in data. |
| **Example** | Predicting house prices based on size and location. | Clustering customers based on their shopping habits. |

## 3. Overfitting in Machine Learning
Overfitting occurs when a model learns the training data "too well," including the noise and random fluctuations, rather than just the underlying pattern. As a result, the model performs excellently on the training data but poorly on new, unseen data.

**How to prevent it:**
*   **More Data:** Providing more training examples can help the model generalize better.
*   **Regularization:** Techniques that penalize overly complex models.
*   **Cross-Validation:** Splitting the data multiple times to ensure the model's performance is consistent.

## 4. Training vs. Test Data
In ML, the dataset is usually split into two parts:
*   **Training Set (e.g., 80%):** Used to "teach" the model. The model learns the relationships within this data.
*   **Test Set (e.g., 20%):** Used to evaluate the model's performance on data it hasn't seen before. This step is crucial to ensure the model can generalize to real-world situations.

## 5. Case Study: Machine Learning in E-commerce
**Industry:** E-commerce (e.g., Amazon, Netflix).
**Application:** Recommendation Systems.

E-commerce platforms use ML to analyze a user's browsing history, past purchases, and even how long they look at a specific item. By comparing this data with millions of other users, the system can recommend products that the user is likely to buy. This significantly increases sales and improves the customer experience.

---

## References
*   IBM Cloud Education. (2020). *What is Machine Learning?*
*   Scikit-Learn Documentation. *Supervised learning vs Unsupervised learning*.
*   Netflix Technology Blog. (2021). *Learning a Personalized Homepage*.
