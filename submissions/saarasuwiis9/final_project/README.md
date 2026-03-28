# Customer Churn Prediction API

A complete machine learning project featuring data synthesis, a scikit-learn training pipeline, a FastAPI prediction server, and a beautiful web interface.

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
