import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import confusion_matrix


df = pd.read_csv('mail_l7_dataset.csv')

# print(df.head())


# df.loc[df["Category"].str.lower().str.strip() == "spam", "Category"] = 0
# df.loc[df["Category"].str.lower().str.strip() == "ham", "Category"] = 1


df.columns = ['Category', 'Message']

df['Category'] = df['Category'].str.lower().str.strip()

df['Category'] = df['Category'].map({'spam': 0, 'ham': 1})


# print(df.head())


X = df['Message'].astype(str)
y = df['Category'].astype(int)


X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# print("Training set size:", len(X_train))
# print("Testing set size:", len(X_test))


tfid = TfidfVectorizer(min_df=1, stop_words='english', lowercase=True)


X_train_tfid = tfid.fit_transform(X_train)
X_test_tfid = tfid.transform(X_test)


lr = LogisticRegression(max_iter=1000, random_state=42)
lr.fit(X_train_tfid, y_train)
y_pred_lr = lr.predict(X_test_tfid)


# print("Logistic Regression Performance:")
# print("Accuracy:", accuracy_score(y_test, y_pred_lr))


rf = RandomForestClassifier(n_estimators=1000, random_state=42)
rf.fit(X_train_tfid, y_train)
y_pred_rf = rf.predict(X_test_tfid)

# print("Random Forest Performance:")
# print("Accuracy:", accuracy_score(y_test, y_pred_rf))


def print_metrics(Name, y_true, y_pred, pos_label=0):
    acc = accuracy_score(y_true, y_pred)
    prec = precision_score(y_true, y_pred, pos_label=pos_label)
    rec = recall_score(y_true, y_pred, pos_label=pos_label)
    f1 = f1_score(y_true, y_pred, pos_label=pos_label)

    print(f"{Name}")
    print(f"Accuracy: {acc:.4f}")
    print(f"Precision: {prec:.4f}")
    print(f"Recall: {rec:.4f}")
    print(f"F1 Score: {f1:.4f}")
    print()


# print_metrics("Logistic Regression Performance:",
#               y_test, y_pred_lr)
# print_metrics("Random Forest Performance:", y_test, y_pred_rf)


def print_confusion_matrix(name, y_true, y_pred):
    cm = confusion_matrix(y_true, y_pred, labels=[0, 1])
    cm_df = pd.DataFrame(
        cm,
        index=['Actual ham (1)', 'Actual spam (0)'],
        columns=['Predicted ham (1)', 'Predicted spam (0)']
    )

    print(f"{name} Confusion Matrix:{cm_df}")


# print_confusion_matrix("Logistic Regression Performance: ",
#                        y_test, y_pred_lr)
# print_confusion_matrix("Random Forest Performance: ",
#                        y_test, y_pred_rf)


i = 14

Sample_Message = X_test.iloc[i]
True_Label = y_test.iloc[i]
Predicted_Label_LR = y_pred_lr[i]
Predicted_Label_RF = y_pred_rf[i]

print(f"Sample Message: {Sample_Message}")
print(f"True Label: {True_Label}")
print(f"Predicted Label (Logistic Regression): {Predicted_Label_LR}")
print(f"Predicted Label (Random Forest): {Predicted_Label_RF}")
