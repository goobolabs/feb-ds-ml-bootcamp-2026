import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os


current_dir = os.path.dirname(os.path.abspath(__file__))

DATA_PATH = os.path.join(current_dir, 'cardiovascular_diseases_dv3.csv')

if not os.path.exists(DATA_PATH):
    print(f" Error: The data file was not found in the specified directory {DATA_PATH}")
else:
    df = pd.read_csv(DATA_PATH, sep=';')

    
    X = df.drop(['CARDIO_DISEASE', 'ALCOHOL'], axis=1) 
    y = df['CARDIO_DISEASE']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    lr_model = LogisticRegression(max_iter=1000)
    lr_model.fit(X_train, y_train)
    lr_acc = accuracy_score(y_test, lr_model.predict(X_test))

    
    rf_model = RandomForestClassifier(n_estimators=200, max_depth=15, random_state=42)
    rf_model.fit(X_train, y_train)
    rf_acc = accuracy_score(y_test, rf_model.predict(X_test))

    
    joblib.dump(lr_model, os.path.join(current_dir, "logistic_model.pkl"))
    joblib.dump(rf_model, os.path.join(current_dir, "random_forest_model.pkl"))

    print(f" Logistic Regression Accuracy: {lr_acc:.2%}")
    print(f" Random Forest Accuracy: {rf_acc:.2%}\n")

    
    print(" Model Evaluation: Random Forest")
    rf_y_pred = rf_model.predict(X_test)
    print(classification_report(y_test, rf_y_pred))
    

print("\n Sanity Checks (Sample Predictions)")


feature_names = X.columns.tolist()

sanity_samples = [
    {"desc": "Healthy (Young, Normal BP)", "data": [12000, 1, 160, 55, 110, 70, 1, 1, 0, 1]},
    {"desc": "High Risk (Old, High BP, Smoker)", "data": [22000, 2, 175, 100, 180, 110, 3, 3, 1, 0]},
    {"desc": "Borderline Case", "data": [16000, 1, 165, 75, 130, 85, 2, 1, 1, 1]}
]

for i, sample in enumerate(sanity_samples, 1):
    sample_df = pd.DataFrame([sample["data"]], columns=feature_names)
    
    prediction = rf_model.predict(sample_df)[0]
    status = "Risk" if prediction == 1 else "Healthy"
    print(f"Test {i} [{sample['desc']}]: Result -> {status}")

    import joblib


model_path = 'models/Models/random_forest_model.pkl'
joblib.dump(rf_model, model_path, compress=3)
print(f"Success! The model has been compressed and saved to: {model_path}")