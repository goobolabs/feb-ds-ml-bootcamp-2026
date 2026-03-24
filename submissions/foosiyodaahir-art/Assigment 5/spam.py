import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report


df = pd.read_csv(r"C:\Users\ICT Office\Downloads\Pythone F\Assigment 5\mail_l7_dataset.csv")


tfidf = TfidfVectorizer(stop_words='english', max_features=5000)
X = tfidf.fit_transform(df['Message'])
  
y = df['Category']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

nb = MultinomialNB()
nb.fit(X_train, y_train)
nb_pred = nb.predict(X_test)
# print(" Naive Bayes Accuracy:", accuracy_score(y_test, nb_pred))

lr = LogisticRegression(max_iter=1000)
lr.fit(X_train, y_train)
lr_pred = lr.predict(X_test)
# print(" Logistic Regression Accuracy:", accuracy_score(y_test, lr_pred))

rf = RandomForestClassifier(
    n_estimators=50,      
    n_jobs=-1,             
    random_state=42
)



# rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)
rf_pred = rf.predict(X_test)
# print("Random Forest Accuracy:", accuracy_score(y_test, rf_pred))


print("\nNaive Bayes Report:\n", classification_report(y_test, nb_pred))
print("Logistic Regression Report:\n", classification_report(y_test, lr_pred))
print("Random Forest Report:\n", classification_report(y_test, rf_pred))


def evaluate_model_simple(name, y_true, y_pred):
    print(f"\n{name} Performance:")
    print("Accuracy       :", accuracy_score(y_true, y_pred))
    print("Precision (spam):", precision_score(y_true, y_pred, pos_label='spam'))
    print("Recall (spam)   :", recall_score(y_true, y_pred, pos_label='spam'))
    print("F1-Score (spam) :", f1_score(y_true, y_pred, pos_label='spam'))
    print("Precision (ham) :", precision_score(y_true, y_pred, pos_label='ham'))
    print("Recall (ham)    :", recall_score(y_true, y_pred, pos_label='ham'))
    print("F1-Score (ham)  :", f1_score(y_true, y_pred, pos_label='ham'))

    evaluate_model_simple("Naive Bayes", y_test, nb_pred)
    evaluate_model_simple("Logistic Regression", y_test, lr_pred)
    evaluate_model_simple("Random Forest", y_test, rf_pred)


samples = [
    "Free entry in 2 a weekly competition!",
    "I will meet you at the cafe tomorrow",
    "Congratulations, you won a free ticket"
]



sample_vect = tfidf.transform(samples)
print("\nSample Predictions:")
print("Naive Bayes :", nb.predict(sample_vect))
print("Logistic Regression :", lr.predict(sample_vect))
print("Random Forest :", rf.predict(sample_vect))