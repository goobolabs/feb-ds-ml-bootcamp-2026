import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import MultinomialNB

from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

# Loading dataset
df = pd.read_csv("mail_l7_dataset.csv")

# Handle missing values
df['Message'] = df['Message'].fillna("")

# Encode labels
df['Category'] = df['Category'].map({'spam':0, 'ham':1})

# step 4 spliting data
X = df['Message']
y = df['Category']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

#step 5 Text Feature Extraction
vectorizer = TfidfVectorizer()
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)

#step 6 Train models

# Logistic Regression
log_reg = LogisticRegression()
log_reg.fit(X_train_tfidf, y_train)

# Random Forest
rf = RandomForestClassifier()
rf.fit(X_train_tfidf, y_train)

# Naive Bayes
nb = MultinomialNB()
nb.fit(X_train_tfidf, y_train)


#step 7 Evaluate perfomance
def evaluate_model(model, X_test, y_test, name):
    y_pred = model.predict(X_test)
    print(f"{name} Performance:")
    print("  Accuracy  :", accuracy_score(y_test, y_pred))
    print("  Precision :", precision_score(y_test, y_pred))
    print("  Recall    :", recall_score(y_test, y_pred))
    print("  F1-Score  :", f1_score(y_test, y_pred))
    print("  Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
    print("-"*50)

evaluate_model(log_reg, X_test_tfidf, y_test, "Logistic Regression")
evaluate_model(rf, X_test_tfidf, y_test, "Random Forest")
evaluate_model(nb, X_test_tfidf, y_test, "Naive Bayes")


#step 8 sanity checks
test_messages = [
    "Free entry in 2 a weekly competition!",
    "I will meet you at the cafe tomorrow",
    "Congratulations, you won a free ticket"
]

for msg in test_messages:
    vec = vectorizer.transform([msg])
    print(f"Message: {msg}")
    print("  Logistic Regression:", "Ham" if log_reg.predict(vec)[0]==1 else "Spam")
    print("  Random Forest      :", "Ham" if rf.predict(vec)[0]==1 else "Spam")
    print("  Naive Bayes        :", "Ham" if nb.predict(vec)[0]==1 else "Spam")
    print("-"*50)
