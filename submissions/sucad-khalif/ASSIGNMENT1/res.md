# 1. Definition of Machine Learning

Machine Learning (ML) is a subfield of Artificial Intelligence (AI) that focuses on enabling computer systems to learn patterns from data and improve their performance on a task without being explicitly programmed for every possible scenario. Instead of relying on fixed rules, machine learning models are trained using historical data to identify relationships among variables and make predictions or decisions when exposed to new, unseen data.

### Real-Life Example: Movie Recommendation Systems

A practical real-life application of machine learning is movie recommendation systems used by platforms such as Netflix and Amazon Prime. These platforms collect extensive user data, including viewing history, ratings, watch duration, and search behavior. Machine learning algorithms analyze this data to learn user preferences and suggest movies or series that align with similar viewing patterns.

As more user interaction data becomes available, the recommendation model continuously updates itself, improving the relevance and accuracy of its predictions. This example illustrates the fundamental concept of machine learning: learning from experience (data) and improving performance over time.

# 2. Supervised Learning vs. Unsupervised Learning

Machine learning techniques are generally classified into supervised learning and unsupervised learning, depending on whether labeled data is available during the training process.

### Supervised Learning

Supervised learning uses datasets that include both input features and known output labels. The objective is to learn a mapping between inputs and outputs so that the model can accurately predict results for new data.

**Example:**  
Predicting students’ exam scores based on study hours, attendance, and previous grades.

### Unsupervised Learning

Unsupervised learning works with unlabeled data, where the correct outputs are not known in advance. The model attempts to discover hidden patterns or structures within the data.

**Example:**  
Document clustering for news articles.

### Comparison Table

| Aspect | Supervised Learning | Unsupervised Learning |
|------|-------------------|----------------------|
| Data Type | Labeled data | Unlabeled data |
| Main Goal | Prediction or classification | Pattern discovery |
| Common Algorithms | Linear Regression, Decision Trees, SVM | K-Means, Hierarchical Clustering |
| Example | Spam detection | Document clustering for news articles |

# 3. Overfitting: Causes and Prevention

Overfitting occurs when a machine learning model learns the training data too closely, including noise and random fluctuations, rather than capturing general patterns. As a result, the model performs well on training data but poorly on unseen data.

### Causes of Overfitting

- Using overly complex models  
- Training for too many iterations  
- Presence of irrelevant or noisy features  
- Insufficient training data  

### Prevention Techniques

- Train-test split or cross-validation  
- Regularization techniques (L1, L2)  
- Feature selection  
- Early stopping  
- Increasing dataset size and quality  

# 4. Training Data and Test Data Splitting

In machine learning, datasets are divided into training data and test data. Training data is used to build the model, while test data is used to evaluate how well the model generalizes to unseen data.

Common split ratios include **80% training and 20% testing**. This process is necessary to detect overfitting and ensure reliable performance evaluation.

# 5. Case Study: Machine Learning in Healthcare

A notable application of machine learning in healthcare is the prediction of heart disease. Researchers used datasets from the UCI Machine Learning Repository and applied algorithms such as Logistic Regression, Decision Trees, and Support Vector Machines.

### Key Findings

- Improved prediction accuracy compared to traditional statistical methods  
- Enhanced early detection of heart disease  
- Support for data-driven clinical decision-making  

# 6. Conclusion

Machine learning enables systems to learn from data and improve decision-making without explicit programming. Understanding learning types, overfitting risks, and data splitting techniques is essential for building robust models. Applications in healthcare demonstrate the significant impact of machine learning on society.

# References

- Mitchell, T. M. (1997). *Machine Learning*. McGraw-Hill.  
- Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer.  
- Géron, A. (2019). *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow*. O’Reilly.  
- Detrano, R. et al. (1989). *International application of a new probability algorithm for the diagnosis of coronary artery disease*. American Journal of Cardiology.  
- UCI Machine Learning Repository: https://archive.ics.uci.edu
