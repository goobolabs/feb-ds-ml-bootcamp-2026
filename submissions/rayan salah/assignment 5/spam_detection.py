
# Assignment – Spam Detection 
# File: spam_detection.py


# 1. Import necessary libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report
from sklearn.pipeline import Pipeline
import warnings
warnings.filterwarnings('ignore') # Si loo qariyo digniinaha aan muhiimka ahayn

def load_and_preprocess_data(filepath):
    """Xogta ayuu soo akhrinayaa wuxuuna sameynayaa nadiifin aasaasi ah."""
    print("Loading and preprocessing dataset...")
    df = pd.read_csv(filepath)
    
    # Handle missing values (replace with empty strings)
    df['Message'] = df['Message'].fillna('').str.strip()
    df['Category'] = df['Category'].fillna('').str.strip()
    
    # Encode labels: spam = 0, ham = 1
    df['Category'] = df['Category'].map({'spam': 0, 'ham': 1})
    
    # Drop rows where category might be null after mapping
    df = df.dropna(subset=['Category'])
    df['Category'] = df['Category'].astype(int)
    
    return df['Message'], df['Category']

def evaluate_model(model_name, y_true, y_pred):
    """Wuxuu xisaabinayaa oo uu soo daabacayaa natiijooyinka model-ka."""
    print(f"{model_name} Performance:")
    
    # We evaluate for spam detection specifically (spam = 0)
    acc = accuracy_score(y_true, y_pred)
    prec = precision_score(y_true, y_pred, pos_label=0)
    rec = recall_score(y_true, y_pred, pos_label=0)
    f1 = f1_score(y_true, y_pred, pos_label=0)
    cm = confusion_matrix(y_true, y_pred)
    
    print(f"  Accuracy  : {acc:.4f}")
    print(f"  Precision : {prec:.4f}")
    print(f"  Recall    : {rec:.4f}")
    print(f"  F1-Score  : {f1:.4f}")
    print(f"  Confusion Matrix:\n    {cm}\n")

def main():
    # 1 & 2. Load Dataset and Preprocess Data
    X, y = load_and_preprocess_data('mail_l7_dataset.csv')
    
    # 3. Split Data (80% training, 20% testing)
    # Using stratify=y maintains the proportion of spam/ham in both splits
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )
    
    # 4. Text Feature Extraction & Model Definition using Pipelines
    # N-grams (1, 2) allows the model to look at 2-word combinations
    tfidf_params = {
        'stop_words': 'english', 
        'max_features': 5000,
        'ngram_range': (1, 2) 
    }
    
    pipelines = {
        "Logistic Regression": Pipeline([
            ('tfidf', TfidfVectorizer(**tfidf_params)),
            ('clf', LogisticRegression(max_iter=1000, random_state=42))
        ]),
        "Random Forest": Pipeline([
            ('tfidf', TfidfVectorizer(**tfidf_params)),
            ('clf', RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1))
        ]),
        "Naive Bayes": Pipeline([
            ('tfidf', TfidfVectorizer(**tfidf_params)),
            ('clf', MultinomialNB(alpha=0.1)) # Optimized alpha parameter
        ])
    }
    
    # 5 & 6. Train Models and Evaluate Performance
    print("Training models...\n")
    for name, pipeline in pipelines.items():
        # Train the model
        pipeline.fit(X_train, y_train)
        
        # Make predictions
        y_pred = pipeline.predict(X_test)
        
        # Print metrics
        evaluate_model(name, y_test, y_pred)

    # 7. Sanity Checks
    sample_messages = [
        "Free entry in 2 a weekly competition!",
        "I will meet you at the cafe tomorrow",
        "Congratulations, you won a free ticket"
    ]
    
    print("Sanity Check Predictions:\n")
    
    for msg in sample_messages:
        print(f"Message: '{msg}'")
        for name, pipeline in pipelines.items():
            # Predict class (0 for Spam, 1 for Ham)
            pred = pipeline.predict([msg])[0]
            label = "Ham" if pred == 1 else "Spam"
            
            # Predict probabilities to show confidence
            prob = pipeline.predict_proba([msg])[0]
            confidence = prob[pred] * 100
            
            print(f"  {name: <20} : {label} ({confidence:.1f}% confidence)")
        print()

# Run the entire pipeline
if __name__ == "__main__":
    main()
