
# Used Car Price Prediction using Machine Learning

## Project Description

This project builds a machine learning system that predicts the price of a used car based on its characteristics. The goal is to help estimate car prices using historical data such as brand, year, mileage, engine size, and other features.

Two machine learning models were trained and compared:

* Random Forest Regressor
* Gradient Boosting Regressor

After training the models, the best model was deployed using an API built with **FastAPI**. A simple frontend interface was also created to allow users to enter car details and receive a predicted price.

This project demonstrates the full machine learning workflow from data preparation to model deployment.

---

# Dataset

The dataset used in this project contains **10,000 samples** of used cars with different features that affect their price.

## Dataset Features

| Feature      | Description                                |
| ------------ | ------------------------------------------ |
| brand        | Car manufacturer (Toyota, BMW, Ford, etc.) |
| year         | Production year of the car                 |
| engine_size  | Engine capacity                            |
| mileage      | Distance driven by the car                 |
| fuel_type    | Type of fuel used                          |
| transmission | Manual or Automatic                        |
| owner_count  | Number of previous owners                  |
| price        | Target variable representing car price     |

Dataset location in project:

```id="file2"
dataset/used_car_price_dataset.csv
```

---

# Project Structure

```id="file3"
used-car-price-prediction
│
├── api
│   └── app.py
│
├── dataset
│   └── used_car_price_dataset.csv
│
├── frontend
│   └── index.html
│
├── models
│   └── best_model.pkl
│
├── src
│   ├── train.py
│   ├── predict.py
│   └── utils.py
│
├── README.md
└── project_paper.md
```

---

# Machine Learning Models

Two regression algorithms were used:

### Random Forest Regressor

Random Forest is an ensemble learning algorithm that builds multiple decision trees and combines their predictions. It reduces overfitting and improves prediction stability.

### Gradient Boosting Regressor

Gradient Boosting builds decision trees sequentially. Each new tree focuses on correcting the errors of the previous tree, which often results in higher prediction accuracy.

The performance of both models was evaluated using regression metrics.

---

# Model Evaluation

The models were evaluated using the following metrics:

* **MAE (Mean Absolute Error)**
* **RMSE (Root Mean Squared Error)**
* **R² Score**

These metrics help measure how accurately the models predict car prices.

Several sample predictions were also tested to verify that the models produce reasonable outputs.

---

# How to Run the Project

## 1 Install Required Libraries

Run the following command:

```id="file4"
pip install pandas numpy scikit-learn fastapi uvicorn joblib
```

---

## 2 Train the Model

Run the training script:

```id="file5"
python src/train.py
```

This will:

* Train the machine learning models
* Evaluate their performance
* Save the best model in the **models** folder

---

## 3 Test Prediction

Run the prediction script:

```id="file6"
python src/predict.py
```

This will load the trained model and generate a sample prediction.

---

# Running the API

To start the API server run:

```id="file7"
uvicorn api.app:app --reload
```

Open the API documentation in your browser:

```id="file8"
http://127.0.0.1:8000/docs
```

This interactive interface allows users to test the `/predict` endpoint.

---

# Example API Request

Example input JSON:

```id="file9"
{
 "brand": "Toyota",
 "year": 2019,
 "engine_size": 2.0,
 "mileage": 60000,
 "fuel_type": "Petrol",
 "transmission": "Automatic",
 "owner_count": 1
}
```

Example output:

```id="file10"
{
 "predicted_price": 18500
}
```

---

# Frontend Interface

A simple web interface was created to make the prediction system easier to use.

Users can:

1. Enter car details
2. Click the predict button
3. Instantly see the predicted price

Frontend file location:

```id="file11"
frontend/index.html
```

---

# Lessons Learned

This project provided hands-on experience with the full machine learning pipeline including:

* Data preprocessing
* Model training and comparison
* Model evaluation
* API deployment
* Basic frontend integration

It demonstrates how machine learning models can be transformed into usable applications.

---

# Author

Name: **Adam Ibrahim**

Bootcamp Final Project
Machine Learning Model Development and Deployment

---

# Project Repository

GitHub Repository Link:

([Here is my repo link](https://github.com/adameth25-cmd/FINAL-PROJECT-USED-CAR-PRICE-PREDICTION.git))

