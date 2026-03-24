# 🎓 Assignment – Spam Detection with Logistic Regression, Random Forest & Naive Bayes

**Due:** Sunday, Feb 22, 2025 — 12:00 PM (Africa/Mogadishu / EAT)

---

## **Part A – Practical (Jupyter Notebook)**

**Objective:**
In this part, you will extend the **Spam Detection Project** by adding a **Naive Bayes classifier**. You will evaluate all three models (Logistic Regression, Random Forest, and Naive Bayes) and compare their performance.

---

### **Instructions**

1. **Notebook Setup**

   * Create a Jupyter Notebook named:
     `spam_detection.ipynb`.

2. **Load Dataset**

   * Use the dataset provided in class: `mail_l7_dataset.csv`.
   * The dataset has two columns:

     * `Category` → target (spam = 0, ham = 1)
     * `Message` → input text

3. **Preprocess Data**

   * Handle missing values (replace with empty strings).
   * Encode labels: spam = 0, ham = 1.
   * Split into features (X = messages) and target (y = category).

4. **Split Data**

   * Use **80% for training** and **20% for testing**.

5. **Text Feature Extraction**

   * Use **TfidfVectorizer** to transform text into numeric vectors.

6. **Train Models**

   * Train a **Logistic Regression** model.
   * Train a **Random Forest Classifier** model.
   * Train a **Naive Bayes (MultinomialNB)** classifier.

7. **Evaluate Performance**

   * For each model, print the following metrics:

     * Accuracy
     * Precision
     * Recall
     * F1-Score
     * Confusion Matrix

8. **Sanity Checks**

   * Perform at least **3 single-message predictions**:

     * Example 1: `"Free entry in 2 a weekly competition!"`
     * Example 2: `"I will meet you at the cafe tomorrow"`
     * Example 3: `"Congratulations, you won a free ticket"`
   * Compare the predictions of Logistic Regression, Random Forest, and Naive Bayes.

---

### **Expected Output**

* Metrics for all three models, e.g.:

```
Logistic Regression Performance:
  Accuracy  : 0.96
  Precision : 0.95
  Recall    : 0.94
  F1-Score  : 0.94
  Confusion Matrix:
    [[480   5]
     [ 12 618]]

Random Forest Performance:
  Accuracy  : 0.97
  Precision : 0.96
  Recall    : 0.95
  F1-Score  : 0.95
  Confusion Matrix:
    [[482   3]
     [ 10 620]]

Naive Bayes Performance:
  Accuracy  : 0.94
  Precision : 0.93
  Recall    : 0.92
  F1-Score  : 0.92
  Confusion Matrix:
    [[470  15]
     [ 18 612]]
```

* Predictions for **3 sample test messages** with labels: Ham or Spam.

---

## **Part B – Reflection Paper**

Write a **short paper (1–2 pages)** answering the following:

1. **What did you implement?**

   * Briefly describe how you used Logistic Regression, Random Forest, and Naive Bayes to detect spam.

2. **Comparison of Models:**

   * Compare the results of the **3 sanity check messages**.
   * Did all models agree? If not, which one gave more realistic predictions?

3. **Understanding Naive Bayes:**

   * Explain in your own words:

     * What is Naive Bayes?
     * Why is it often used in spam detection?
     * What are its advantages and limitations?

4. **Metrics Discussion:**

   * Which model had better **Accuracy, Precision, Recall, F1-Score, and Confusion Matrix**?
   * What does the Confusion Matrix tell you about **false positives** and **false negatives**?

5. **Your Findings:**

   * Summarize in 1–2 paragraphs which model you would recommend for spam detection and why.

---

## **Submission Format**

* `spam_detection.ipynb` (with all code + results).
* `reflection_paper.pdf` or `reflection_paper.md` (your discussion).

---
