# Customer Churn Prediction API

This project builds a machine learning system to predict customer churn based on customer behavior and service usage data. Two models, Logistic Regression and Random Forest, were trained and evaluated using performance metrics. The best-performing model was selected and deployed as a Flask API, allowing real-time predictions through a web interface.

## Project Structure

```text
Customer Churn Prediction API project
├── api/
│   └── app.py                  # FastAPI server providing the /predict endpoint
├── models/                     # Saved artifacts (auto-generated)
│   ├── churn_model.pkl
│   ├── features.pkl
│   └── scaler.pkl
├── dataset/                    # Training data (auto-generated)
│   └── customer_churn_data.csv
├── notebooks/
│   └── churn_training.ipynb    # Jupyter Notebook for exploratory analysis
├── src/
│   └── train.py                # Pipeline script for synthetic data & model training
├── web/
│   └── index.html              # Modern UI dashboard to interact with the API
├── project_paper.md            # Methodology & architectural document
├── requirements.txt            # Python dependencies
└── README.md                   # Setup instructions (this file)
```
## GitHub Repository Link
https://github.com/saarasuwiis9/Customer-Churn-Prediction-System