# 1 Definition of Machine Learning

**Machine Learning (ML)** is a subfield of Artificial Intelligence that focuses on developing algorithms capable of learning from data and improving their performance over time without explicit rule-based programming. Instead of encoding fixed instructions, ML systems infer relationships and patterns directly from examples, enabling them to make predictions or decisions when exposed to new data.

This data-driven learning paradigm is especially useful for complex problems where defining rules manually is impractical, such as **image recognition**, **speech processing**, and **medical diagnosis**.

---

## Real-Life Example

A **credit card fraud detection system** uses machine learning to identify suspicious transactions. By analyzing historical transaction data labeled as *fraudulent* or *legitimate*, the system learns spending patterns. When a new transaction deviates significantly from a user’s typical behavior, the model flags it for further verification.

This adaptive learning allows banks to detect fraud in real time while reducing false alarms.

---

# 2 Supervised Learning vs Unsupervised Learning

Machine learning methods can be categorized based on whether labeled output data is available during training.

| Aspect | Supervised Learning | Unsupervised Learning |
|------|-------------------|---------------------|
| **Training Data** | Labeled (input–output pairs) | Unlabeled (only inputs) |
| **Learning Goal** | Learn a mapping from inputs to known outputs | Discover hidden structure or patterns |
| **Typical Tasks** | Classification, regression | Clustering, dimensionality reduction |
| **Human Guidance** | High (labels provided) | Low (no predefined labels) |

---

## Example of Supervised Learning

**House price prediction**

A dataset contains house features such as:
- Size  
- Location  
- Number of rooms  

along with known prices. The model learns the relationship between features and prices and predicts the price of a new house based on its characteristics.

---

## Example of Unsupervised Learning

**Market basket analysis**

Retailers analyze customer purchase data without predefined categories. Unsupervised algorithms group frequently co-purchased items together, revealing patterns such as products that are often bought together. This helps optimize:
- Store layout  
- Product placement  
- Promotions  

---

# 3 Overfitting

## What Causes Overfitting?

**Overfitting** occurs when a model learns the training data too precisely, including random noise and minor fluctuations, instead of capturing general trends. As a result, the model performs well on training data but poorly on unseen data.

**Common causes include:**
- Excessively complex models relative to the dataset size  
- Too many features compared to the number of training samples  
- Insufficient or noisy training data  
- Training for too many iterations without validation  

---

## How Overfitting Can Be Prevented

- **Regularization**: Penalizes overly complex models to encourage simpler solutions  
- **Cross-validation**: Evaluates performance across multiple data splits  
- **Early stopping**: Halts training when validation performance stops improving  
- **Feature selection**: Removes irrelevant or redundant features  
- **Increasing training data**: Reduces the impact of noise  

---

# 4 Training Data and Test Data Split

## How the Split Works

In machine learning, datasets are typically divided into:
- **Training set**: Used to train the model  
- **Test set**: Used to evaluate the model’s performance on unseen data  

A common split ratio is **80% training** and **20% testing**, though this may vary depending on dataset size.

---

## Why the Split Is Necessary

- **Generalization assessment**: Measures how well the model performs on new data  
- **Prevents misleading accuracy**: Training accuracy alone does not reflect real-world performance  
- **Model comparison**: Enables fair evaluation of different algorithms  

Without this separation, models may appear accurate but fail in real applications.

---

# 5 Case Study: Machine Learning in Healthcare

## Predicting Diabetes Using Machine Learning

A study published in the **Journal of Biomedical Informatics** explored the use of machine learning models to predict **Type 2 diabetes** using patient health records.

### Study Overview
- Dataset included patient attributes such as age, BMI, glucose levels, blood pressure, and family history  
- Several ML algorithms were evaluated, including:
  - Logistic regression  
  - Decision trees  
  - Support vector machines  
- The models achieved higher predictive accuracy than traditional statistical methods  

---

### Key Findings
- Machine learning models effectively identified high-risk patients before clinical diagnosis  
- Early detection enabled timely lifestyle and medical interventions  
- The study demonstrated that ML can **support clinicians** in decision-making rather than replace them  

This case highlights the practical value of machine learning in improving healthcare outcomes through early risk prediction.

---

# References

1. Mitchell, T. M. (1997). *Machine Learning*. McGraw-Hill Education.  
2. Bishop, C. M. (2006). *Pattern Recognition and Machine Learning*. Springer.  
3. Géron, A. (2022). *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow* (3rd ed.). O’Reilly Media.  
4. Hastie, T., Tibshirani, R., & Friedman, J. (2009). *The Elements of Statistical Learning*. Springer.  
5. Kavakiotis, I., et al. (2017). “Machine Learning and Data Mining Methods in Diabetes Research.” *Journal of Biomedical Informatics*, 70, 1–16.  
6. Goodfellow, I., Bengio, Y., & Courville, A. (2016). *Deep Learning*. MIT Press.