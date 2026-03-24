# Reflection – Data Preprocessing Decisions

In this preprocessing task, I prepared the car dataset carefully to ensure it is clean, consistent, and suitable for machine learning.

1. Loading & Inspection  
I first inspected the dataset using head(), shape, and info() because understanding the structure, data types, and missing values is essential before making any changes. This step helps prevent incorrect assumptions about the data.

2. Cleaning the Target (Price)  
The Price column contained symbols such as "$" and commas. I removed them using regex and converted the column to float because machine learning models require numerical input. Keeping formatting symbols would prevent correct mathematical operations.

3. Fixing Category Errors  
I corrected invalid category values such as "Subrb" and "??" before imputing missing values. I did this because incorrect categories would distort the mode calculation and create inconsistent dummy variables later.

4. Missing Value Imputation  
For Odometer_km, I used the median instead of the mean because the median is less sensitive to extreme values and provides a more stable central estimate when outliers exist.  
For Location and Doors, I used the mode because categorical variables should be filled with the most frequent valid category to preserve realistic distribution.

5. Removing Duplicates  
I removed duplicate rows because repeated records can bias the model and artificially influence learning patterns.

6. Outlier Treatment (IQR Capping)  
I applied the IQR method to Price and Odometer_km because IQR is a robust statistical approach for detecting extreme values. Instead of removing rows, I clipped values to lower and upper bounds to reduce outlier impact while keeping all observations.

7. One-Hot Encoding  
I used one-hot encoding for the Location variable because machine learning algorithms cannot interpret text categories directly. Converting them into 0/1 dummy variables makes them mathematically usable.

8. Feature Engineering  
I created the following features:

- Car_year = 2026 - Year  
  I created this because vehicle age is more meaningful for pricing than the raw manufacturing year.

- Km_per_year = Odometer_km / Car_year  
  I engineered this to measure usage intensity, which may better reflect car condition than total kilometers alone.

- Is_Rural  
  I created this binary feature to simplify the rural vs non-rural effect, which may influence car pricing patterns.

- LogPrice  
  I applied log1p to Price because price distributions are often right-skewed. Log transformation helps stabilize variance and improve regression model performance.

All features were engineered carefully to avoid data leakage, meaning no future or target-dependent information was used improperly.

9. Feature Scaling  
I applied StandardScaler only to continuous numerical input features because many models perform better when features are standardized.  
I excluded Price and LogPrice (targets) because scaling the target can distort interpretation. I also excluded dummy variables and Is_Rural because binary indicators do not require scaling.

10. Final Validation  
Finally, I performed describe(), info(), and isnull().sum() to confirm that:
- No missing values remain
- Data types are correct
- All features are numeric and model-ready

The cleaned dataset was saved as car_l3_clean_ready.csv for reproducibility and future modeling.
