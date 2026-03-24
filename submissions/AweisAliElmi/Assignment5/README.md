# Spam Detection - Assignment 5

This folder contains my work for **Assignment 5 – Spam Detection Comparison**. The project explores and compares three machine learning models: Logistic Regression, Random Forest, and Naive Bayes.

## Contents

- **spam_detection.ipynb**  
  Jupyter Notebook containing code for data loading, cleaning, text feature extraction (TF-IDF), model training, and performance evaluation.
  - Compares 3 models: Logistic Regression, Random Forest, and Naive Bayes.
  - Includes metrics (Accuracy, Precision, Recall, F1) and Confusion Matrices.
  - Performs 3 sanity checks on specific messages.

- **reflection_paper.md**  
  A reflection paper answering assignment questions, including:
  - Description of the implementation.
  - Model comparison based on sanity check results.
  - Explanation of Naive Bayes and its role in spam detection.
  - Discussion of evaluation metrics and findings.

## Dataset

- Uses `mail_l7_dataset.csv`, which contains SMS messages labeled as "spam" or "ham".

### NOTE
- This dataset was sourced from the September bootcamp because it has not yet been added to the February bootcamp dataset folder.
  
## Requirements

- Python 3.x
- pandas, numpy, scikit-learn, 
- Jupyter Notebook
