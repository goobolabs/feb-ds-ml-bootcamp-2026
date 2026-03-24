# Reflection: Data Preprocessing Decisions

This reflection explains the key decisions made during the preprocessing of the car prices dataset and the rationale behind each step. The objective was to prepare realistic, consistent, and model-ready data while minimizing information loss.

## Handling Missing Values

Different imputation strategies were applied based on the nature of each feature.

- **Odometer_km**:  
  Missing values were filled using the **median**. Mileage data often contains extreme values due to very old or heavily used vehicles. The median is more robust to outliers than the mean and therefore provides a more representative central value.

- **Doors**:  
  Although numeric, this feature represents **categories** (e.g., 2-door, 4-door). The **mode** was used because it preserves the most common structural configuration of cars in the dataset.

- **Location**:  
  The **mode** was also used for missing values. Before imputation, spelling mistakes and placeholder values (such as `"Subrb"` and `"??"`) were corrected to ensure consistent categories and avoid inflating the number of unique locations.

- **Accidents**:  
  This feature contained no missing values, so no action was required.

## Managing Outliers

Outliers in **Price** and **Odometer_km** were handled using the **Interquartile Range (IQR)** method.

Instead of removing extreme values, they were **capped** at the lower and upper IQR bounds. This approach reduces the influence of abnormal values while retaining all observations, which is important when the dataset size is limited and extreme values may still reflect real-world cases.

## Encoding and Scaling

- **Categorical Encoding**:  
  The `Location` feature was converted into numerical form using **one-hot encoding**, allowing machine learning models to process categorical data without introducing ordinal bias.

- **Feature Scaling**:  
  Numerical input features were standardized using **StandardScaler** to ensure that differences in scale do not bias model learning.  
  Binary features and the target variable (**Price**) were not scaled to preserve their original meaning.

## Duplicate Removal

Duplicate records were removed to prevent repeated data points from disproportionately influencing the model and to ensure fair representation of unique observations.

## Conclusion

Overall, the preprocessing steps transformed an inconsistent and noisy dataset into a clean, structured, and machine-learning-ready form. Decisions such as median imputation, IQR-based outlier capping, and careful feature encoding were chosen based on data characteristics and standard data science best practices. The resulting dataset is now suitable for reliable analysis and predictive modeling.
