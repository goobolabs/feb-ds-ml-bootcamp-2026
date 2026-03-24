# --------------------------------
# 0) Imports
# --------------------------------
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import MultinomialNB  # NEW (for Assignment 5)

from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
)

RANDOM_STATE = 42  # reproducibility


# --------------------------------
# 1) Load the dataset
# --------------------------------
# Expected columns:
# Category → target (spam = 0, ham = 1)
# Message  → input text

df = pd.read_csv("mail_l7_dataset.csv")

# Show first 5 rows
print("=== FIRST 5 ROWS ===")
print(df.head())

# Check structure
print("\n=== DATA INFO ===")
print(df.info())

# Check missing values
print("\n=== MISSING VALUES ===")
print(df.isnull().sum())


# --------------------------------
# 2) Basic Cleaning
# --------------------------------

# Replace NaN with empty string (important for text processing)
df = df.where(pd.notnull(df), "")

# Encode labels
# df.loc[df["Category"].str.lower().str.strip() == "spam", "Category"] = 0
# df.loc[df["Category"].str.lower().str.strip() == "ham",  "Category"] = 1

# Encode labels safely
df["Category"] = (
    df["Category"]
    .str.lower()
    .str.strip()
    .map({"spam": 0, "ham": 1})
)

# Convert Category to integer
df["Category"] = df["Category"].astype(int)

print("\n=== AFTER CLEANING ===")
print(df.head())


# === FIRST 5 ROWS ===
#   Category                                            Message
# 0      ham  Go until jurong point, crazy.. Available only ...
# 1      ham                      Ok lar... Joking wif u oni...
# 2     spam  Free entry in 2 a wkly comp to win FA Cup fina...
# 3      ham  U dun say so early hor... U c already then say...
# 4      ham  Nah I don't think he goes to usf, he lives aro...


# === DATA INFO ===
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 5572 entries, 0 to 5571
# Data columns (total 2 columns):
#  #   Column    Non-Null Count  Dtype 
# ---  ------    --------------  ----- 
#  0   Category  5572 non-null   object
#  1   Message   5572 non-null   object
# dtypes: object(2)
# memory usage: 87.2+ KB
# None

# === MISSING VALUES ===
# Category    0
# Message     0
# dtype: int64
# ...
# 1         1                      Ok lar... Joking wif u oni...
# 2         0  Free entry in 2 a wkly comp to win FA Cup fina...
# 3         1  U dun say so early hor... U c already then say...
# 4         1  Nah I don't think he goes to usf, he lives aro...
# Output is truncated. View as a scrollable element or open in a text editor. Adjust cell output settings...




# --------------------------------
# 3) Split features (X) and target (y)
# --------------------------------
X = df["Message"].astype(str)   # text
y = df["Category"].astype(int)  # labels

print("X shape:", X.shape)
print("y shape:", y.shape)


# --------------------------------
# 4) Train/Test Split (80% / 20%)
# --------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=RANDOM_STATE,
    stratify=y   # IMPORTANT: keeps spam/ham balance
)

print("\n=== SPLIT SIZES ===")
print("Training samples:", X_train.shape[0])
print("Testing samples :", X_test.shape[0])





# --------------------------------
# 5) Text → TF-IDF Features
# --------------------------------

tfidf = TfidfVectorizer(
    min_df=1,
    stop_words="english",
    lowercase=True
)

# Fit on training data only
X_train_features = tfidf.fit_transform(X_train)

# Transform test data
X_test_features = tfidf.transform(X_test)

print("=== TF-IDF SHAPES ===")
print("X_train:", X_train_features.shape)
print("X_test :", X_test_features.shape)





# --------------------------------
# 6) Train Logistic Regression
# --------------------------------

lr = LogisticRegression(max_iter=1000, random_state=RANDOM_STATE)

lr.fit(X_train_features, y_train)

# Predictions
lr_pred = lr.predict(X_test_features)

print("Logistic Regression training complete.")



# --------------------------------
# 7) Train Random Forest
# --------------------------------

rf = RandomForestClassifier(
    n_estimators=200,
    random_state=RANDOM_STATE
)

# Convert sparse matrix to dense
rf.fit(X_train_features.toarray(), y_train)

# Predictions
rf_pred = rf.predict(X_test_features.toarray())

print("Random Forest training complete.")




# --------------------------------
# 8) Train Naive Bayes (MultinomialNB)
# --------------------------------

nb = MultinomialNB()

nb.fit(X_train_features, y_train)

# Predictions
nb_pred = nb.predict(X_test_features)

print("Naive Bayes training complete.")



# --------------------------------
# 9) Helper functions for evaluation
# --------------------------------

def print_clf_metrics(name, y_true, y_pred, pos_label=0):
    """
    Print Accuracy, Precision, Recall, F1.
    pos_label=0 means Spam is the positive class.
    """
    acc  = accuracy_score(y_true, y_pred)
    prec = precision_score(y_true, y_pred, pos_label=pos_label)
    rec  = recall_score(y_true, y_pred, pos_label=pos_label)
    f1   = f1_score(y_true, y_pred, pos_label=pos_label)

    print(f"\n{name} Performance:")
    print(f"  Accuracy : {acc:.3f}")
    print(f"  Precision: {prec:.3f}  (positive = spam=0)")
    print(f"  Recall   : {rec:.3f}  (positive = spam=0)")
    print(f"  F1-Score : {f1:.3f}  (positive = spam=0)")


def print_confmat(name, y_true, y_pred):
    """
    Confusion matrix with readable labels.
    Rows = Actual, Columns = Predicted
    Order: [Ham(1), Spam(0)]
    """
    cm = confusion_matrix(y_true, y_pred, labels=[1, 0])

    cm_df = pd.DataFrame(
        cm,
        index   = ["Actual: Ham (1)", "Actual: Spam (0)"],
        columns = ["Pred: Ham (1)", "Pred: Spam (0)"]
    )

    print(f"\n{name} – Confusion Matrix:")
    print(cm_df)


    # --------------------------------
# 10) Show Results
# --------------------------------

print_clf_metrics("Logistic Regression", y_test, lr_pred)
print_confmat("Logistic Regression", y_test, lr_pred)

print_clf_metrics("Random Forest", y_test, rf_pred)
print_confmat("Random Forest", y_test, rf_pred)

print_clf_metrics("Naive Bayes", y_test, nb_pred)
print_confmat("Naive Bayes", y_test, nb_pred)



# --------------------------------
# 11) Sanity Check Predictions
# --------------------------------

def label_to_text(value):
    return "Spam (0)" if value == 0 else "Ham (1)"

sample_messages = [
    "Free entry in 2 a weekly competition!",
    "I will meet you at the cafe tomorrow",
    "Congratulations, you won a free ticket"
]

print("\n=== SANITY CHECK PREDICTIONS ===")

for msg in sample_messages:
    # Transform message
    msg_vector = tfidf.transform([msg])

    # Predictions
    lr_prediction = lr.predict(msg_vector)[0]
    rf_prediction = rf.predict(msg_vector.toarray())[0]
    nb_prediction = nb.predict(msg_vector)[0]

    print("\nMessage:", msg)
    print("  Logistic Regression:", label_to_text(lr_prediction))
    print("  Random Forest      :", label_to_text(rf_prediction))
    print("  Naive Bayes        :", label_to_text(nb_prediction))