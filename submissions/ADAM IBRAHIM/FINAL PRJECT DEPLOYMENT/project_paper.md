
# Used Car Price Prediction Using Machine Learning

## 1. Introduction

Machine learning is widely used today to solve real-world problems by learning patterns from data. One common problem in the automotive market is determining the fair price of a used car. Buyers often struggle to know whether a car price is reasonable, and sellers want to price their vehicles competitively.

The purpose of this project is to build a machine learning model that can predict the price of a used car based on its characteristics. By using historical car data such as brand, year, mileage, engine size, and other attributes, the model can estimate the expected market price.

In this project, two machine learning algorithms were implemented and compared: Random Forest Regressor and Gradient Boosting Regressor. These algorithms were chosen because they are powerful ensemble learning techniques commonly used in regression tasks. The final trained model was then deployed using an API so that predictions can be made through a simple web interface.

This project demonstrates the full machine learning workflow including data preparation, model training, evaluation, and deployment.

---

# 2. Dataset

The dataset used in this project contains information about used cars and their prices. The dataset includes 10,000 samples with several features that influence car price.

## Dataset Features

The dataset contains the following variables:

| Feature      | Description                                           |
| ------------ | ----------------------------------------------------- |
| brand        | The manufacturer of the car (Toyota, BMW, Ford, etc.) |
| year         | The production year of the car                        |
| engine_size  | The engine capacity of the car                        |
| mileage      | The distance the car has been driven                  |
| fuel_type    | Type of fuel used (Petrol, Diesel, Hybrid)            |
| transmission | Manual or Automatic transmission                      |
| owner_count  | Number of previous owners                             |
| price        | Target variable representing the car price            |

The dataset contains both **numerical features** (year, mileage, engine size) and **categorical features** (brand, fuel type, transmission). Before training the machine learning models, categorical variables were converted into numerical form using **One-Hot Encoding**.

The dataset was divided into:

* **Training set (80%)**
* **Testing set (20%)**

This allows the models to learn patterns from the training data and then be evaluated on unseen data.

---

# 3. Models

Two machine learning models were used in this project:

### 3.1 Random Forest Regressor

Random Forest is an ensemble learning algorithm that builds multiple decision trees and combines their predictions. Each tree is trained on a random subset of the data, which helps reduce overfitting and improves generalization.

Random Forest works using a technique called **bagging (bootstrap aggregation)**. The idea is that many weak models (decision trees) are combined to create a stronger model.

Advantages of Random Forest:

* Handles complex relationships in data
* Reduces overfitting
* Works well with mixed data types
* Requires little parameter tuning

In this project, Random Forest was used as the baseline model for predicting car prices.

---

### 3.2 Gradient Boosting Regressor

Gradient Boosting is another ensemble learning method but uses a different strategy called **boosting**.

Instead of building trees independently, Gradient Boosting builds trees sequentially. Each new tree focuses on correcting the errors made by the previous trees. This iterative improvement allows the model to achieve higher accuracy.

Advantages of Gradient Boosting:

* High prediction accuracy
* Captures complex patterns
* Works well with structured data

In many machine learning competitions and real-world applications, boosting algorithms often outperform other models.

---

# 4. Results

To evaluate the models, three common regression metrics were used:

| Metric | Description                  |
| ------ | ---------------------------- |
| MAE    | Mean Absolute Error          |
| RMSE   | Root Mean Squared Error      |
| R²     | Coefficient of Determination |

### Model Performance

The results showed that both models performed well on the dataset. However, Gradient Boosting generally achieved better performance due to its ability to correct previous prediction errors.

Random Forest provided strong baseline performance, while Gradient Boosting produced more accurate predictions overall.

### Sanity Check Predictions

To ensure the model works correctly, several sample predictions were tested.

Example input:

```
Brand: Toyota
Year: 2019
Engine Size: 2.0
Mileage: 60000
Fuel Type: Petrol
Transmission: Automatic
Owner Count: 1
```

The model successfully returned a predicted car price based on these features. Similar tests were performed with different car attributes to confirm that the model behaves as expected.

These sanity checks help confirm that the trained model can generate reasonable predictions.

---

# 5. Deployment

After training the machine learning model, it was deployed using an API built with **FastAPI**.

The API exposes a prediction endpoint:

```
POST /predict
```

Users can send a JSON request containing the car features, and the API returns the predicted car price.

Example request:

```json
{
 "brand": "BMW",
 "year": 2020,
 "engine_size": 3.0,
 "mileage": 30000,
 "fuel_type": "Petrol",
 "transmission": "Automatic",
 "owner_count": 1
}
```

Example response:

```json
{
 "predicted_price": 42000
}
```

To make the project more user-friendly, a simple web interface was created using HTML and JavaScript. The frontend allows users to enter car information and instantly receive a predicted price by communicating with the API.

This demonstrates how machine learning models can be integrated into real applications.

---

# 6. Lessons Learned

During this project, several important lessons were learned about building and deploying machine learning systems.

First, data preprocessing plays a critical role in model performance. Proper handling of categorical variables and feature preparation ensures that the algorithms can effectively learn patterns from the data.

Second, comparing multiple models is important. Different algorithms may perform differently depending on the dataset. By evaluating Random Forest and Gradient Boosting, it was possible to determine which model produced better results.

Third, deploying a machine learning model makes it more practical and usable. By creating an API and frontend interface, the model can now be used interactively rather than just running predictions in code.

Finally, this project demonstrated the full machine learning pipeline from data preparation to deployment, which is an important skill for real-world machine learning applications.

---

# 7. Conclusion

This project developed a machine learning system capable of predicting used car prices based on several important features. Two ensemble learning algorithms, Random Forest and Gradient Boosting, were implemented and compared.

The results showed that both models performed well, with Gradient Boosting providing slightly better predictive performance. The final model was deployed through an API and integrated with a simple web interface, allowing users to make predictions easily.

This project demonstrates how machine learning techniques can be applied to solve practical problems and highlights the importance of model evaluation, deployment, and documentation in the machine learning development process.
