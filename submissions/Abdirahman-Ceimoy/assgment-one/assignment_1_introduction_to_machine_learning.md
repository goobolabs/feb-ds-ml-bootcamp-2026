# Research Assignment: Introduction to Machine Learning

## 1. Definition of Machine Learning (with a Real-Life Example)

Machine Learning (ML) is a field of Artificial Intelligence that enables computer systems to learn from data and improve their performance without being explicitly programmed for every task. Instead of following fixed rules, ML systems identify patterns from data and use those patterns to make predictions or decisions.

### Real-Life Example: Email Spam Detection
Email services use machine learning to detect spam messages. When users mark emails as “spam” or “not spam,” the system learns from these examples. Over time, it identifies patterns such as suspicious words, links, or sender behavior and automatically classifies new emails. The system improves as it processes more data.


## 2. Supervised Learning vs Unsupervised Learning

Machine Learning techniques are commonly divided into supervised and unsupervised learning, depending on whether labeled data is used.

### Comparison Table

| Feature | Supervised Learning | Unsupervised Learning |
|------|------------------|--------------------|
| Data type | Labeled data (input with correct output) | Unlabeled data (input only) |
| Goal | Predict known outcomes | Discover hidden patterns |
| Human guidance | High | Low |
| Common tasks | Classification, Regression | Clustering, Association |

### Supervised Learning Example
House price prediction is a supervised learning task. The model is trained using historical data where house features (such as size, location, and number of rooms) and their correct prices are known. The system learns the relationship and predicts prices for new houses.

### Unsupervised Learning Example
Customer segmentation is an example of unsupervised learning. A company provides customer purchase data without labels. The algorithm groups customers based on similar buying behavior, helping businesses understand customer types without predefined categories.


## 3. Overfitting: Causes and Prevention

### What is Overfitting?
Overfitting occurs when a machine learning model learns the training data too well, including noise and unnecessary details. As a result, the model performs well on training data but poorly on new, unseen data.

### Causes of Overfitting
- Using overly complex models
- Small training datasets
- Training the model for too many iterations
- Lack of regularization techniques

### How to Prevent Overfitting
- Increase the amount of training data
- Use simpler models
- Apply regularization methods
- Use cross-validation techniques
- Stop training early (early stopping)


## 4. Training Data and Test Data

### Data Splitting Process
In machine learning, datasets are typically divided into two parts:
- **Training data**: used to train the model
- **Test data**: used to evaluate model performance

A common split ratio is 80% for training and 20% for testing.

### Why Data Splitting is Necessary
Testing a model on unseen data helps measure how well it generalizes to real-world situations. Without data splitting, it would be impossible to know whether the model truly learned useful patterns or simply memorized the training data.


## 5. Case Study: Machine Learning in Healthcare

### Breast Cancer Detection Using Machine Learning

Researchers have applied machine learning techniques to detect breast cancer using medical data such as tumor size, texture, and shape. Supervised learning algorithms like Logistic Regression and Support Vector Machines (SVM) were trained using labeled patient data.

### Findings
- The models achieved accuracy rates above 95% in classifying tumors as benign or malignant.
- Machine learning supported doctors in making faster and more accurate diagnoses.
- The system functioned as a decision-support tool rather than replacing medical professionals.

### Impact
Machine learning improved early cancer detection, reduced diagnostic errors, and enhanced clinical decision-making.


## References

1. Mitchell, T. (1997). *Machine Learning*. McGraw-Hill.
2. Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer.
3. UCI Machine Learning Repository – Breast Cancer Dataset.
4. IBM Cloud Education – Machine Learning Basics.
5. Scikit-learn Documentation.

