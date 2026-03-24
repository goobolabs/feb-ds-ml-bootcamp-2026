# House Price Prediction Project

## Overview
This project implements regression models to predict house prices using a cleaned dataset.

The goal is to compare two models:
- Linear Regression
- Random Forest Regressor

---

## Dataset
The dataset used:
clean_house_l5_dataset.csv

Target variable:
- Price

Features:
- All columns except Price and LogPrice

---

## Steps Performed

1. Loaded the dataset using pandas  
2. Split data into features (X) and target (y)  
3. Performed train/test split (80% / 20%)  
4. Trained two models:
   - Linear Regression  
   - Random Forest (n_estimators=100)  
5. Evaluated models using:
   - R²
   - MAE
   - MSE
   - RMSE  
6. Performed a single-row sanity check  

---

## Results
Both models were tested on unseen data.

- Linear Regression works well for simple relationships  
- Random Forest performs better for complex patterns  

Random Forest achieved better accuracy and lower error.

---

## Conclusion
Random Forest is more suitable for house price prediction because it handles multiple factors and non-linear relationships better than Linear Regression.

---

## Files Included

- house_price_prediction.ipynb → Main notebook  
- reflection_paper.md → Short explanation of the work  
- clean_house_l5_dataset.csv → Dataset used  
