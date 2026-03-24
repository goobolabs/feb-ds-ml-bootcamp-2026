import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import MultinomialNB

from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
)

RANDOM_STATE = 42  
CSV_PATH = r"C:\Users\hp\Documents\sucad-khalif\ds-ml-bootcamp\submissions\sucad-khalif\ASSIGNMENT5\mail_l7_dataset.csv"
df = pd.read_csv(CSV_PATH)
#Replace nan with empty 
df = df.where(pd.notnull(df), "")

# Encode labels: spam -> 0, ham -> 1  
df.loc[df["Category"].str.lower().str.strip() == "spam", "Category"] = 0
df.loc[df["Category"].str.lower().str.strip() == "ham",  "Category"] = 1

print(df.head())


#  Split features (X) and target (y)

X = df["Message"].astype(str)
y = df["Category"].astype(int)


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=RANDOM_STATE
)

print("=== SPLIT SIZES ===")
print("Train:", X_train.shape[0], " | Test:", X_test.shape[0])


#  Text → TF-IDF features

tfidf = TfidfVectorizer(min_df=1, stop_words="english", lowercase=True)
X_train_features = tfidf.fit_transform(X_train)
X_test_features  = tfidf.transform(X_test)

print("\n=== TF-IDF SHAPES ===")
print("X_train:", X_train_features.shape, " | X_test:", X_test_features.shape)

# --------------------------------
# 1) Train Logistic Regression (baseline)
# --------------------------------
lr = LogisticRegression(max_iter=1000, random_state=RANDOM_STATE)
lr.fit(X_train_features, y_train)
lr_pred = lr.predict(X_test_features)


# 2) Train Random Forest

rf = RandomForestClassifier(n_estimators=200, random_state=RANDOM_STATE)
rf.fit(X_train_features, y_train)
rf_pred = rf.predict(X_test_features.toarray())

# 3) TRAIN Naivy Byes 

nb = MultinomialNB()
nb.fit(X_train_features, y_train)
nb_pred = nb.predict(X_test_features)


def print_clf_metrics(name, y_true, y_pred, pos_label=0):
    """Print Accuracy, Precision, Recall, F1. pos_label=0 means 'spam' is positive."""
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
    Rows = Actual, Cols = Predicted
    Order: [Ham(1), Spam(0)] so you can see both classes clearly.
    """
    cm = confusion_matrix(y_true, y_pred, labels=[1, 0])
    cm_df = pd.DataFrame(
        cm,
        index   = ["Actual: Ham (1)",  "Actual: Spam (0)"],
        columns = ["Pred: Ham (1)",    "Pred: Spam (0)"]
    )
    print(f"\n{name} – Confusion Matrix:\n{cm_df}")


# 8) Show results for both models 

print_clf_metrics("Logistic Regression", y_test, lr_pred, pos_label=0)
print_confmat("Logistic Regression", y_test, lr_pred)

print_clf_metrics("Random Forest", y_test, rf_pred, pos_label=0)
print_confmat("Random Forest", y_test, rf_pred)

print_clf_metrics("Naivy Byes", y_test, nb_pred, pos_label=0)
print_confmat("Naivy Byes", y_test, nb_pred)



# 9) Single-message sanity check 

i = 5 
sample_text = X_test.iloc[i]
true_label  = y_test.iloc[i]

# Predict with both models
lr_pred_one = int(lr.predict(tfidf.transform([sample_text]))[0])
rf_pred_one = int(rf.predict(tfidf.transform([sample_text]).toarray())[0])
nb_pred_one = int(nb.predict(tfidf.transform([sample_text]))[0])


def lab2str(v):  # same readable output style
    return "Spam (0)" if v == 0 else "Ham (1)"

print("\n=== SINGLE MESSAGE CHECK ===")
snippet = (sample_text[:160] + "...") if len(sample_text) > 160 else sample_text
print("Text snippet:", snippet)
print("Actual      :", lab2str(true_label))
print("LR Pred     :", lab2str(lr_pred_one))
print("RF Pred     :", lab2str(rf_pred_one))
print("NB Pred     :", lab2str(nb_pred_one))