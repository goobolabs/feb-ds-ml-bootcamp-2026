# Reflection on Data Cleaning, Feature Engineering, and Scaling

## 1. Load & Inspect
I first explored the dataset to understand its structure, missing values, and categorical distributions. Examining `head()`, `info()`, and value counts for `Location` helped identify typos and inconsistencies that required cleaning before analysis.

## 2. Clean Target Formatting
The `Price` column contained symbols and commas, so I removed them and converted it to numeric. This ensures downstream calculations (IQR capping, log-transform) can be applied correctly.

## 3. Fix Categorical Issues
I normalized the `Location` column by correcting typos (e.g., `Subrb → Suburb`) and converting unknown values (`??`) to missing. This improves consistency and avoids errors during encoding or imputation.

## 4. Impute Missing Values
- **Median** was used for `Odometer_km` because it is continuous and skewed; median reduces the influence of outliers.  
- **Mode** was used for `Doors`, `Accidents`, and `Location` because these are categorical or discrete values, and the most frequent value is the safest replacement.

## 5. Remove Duplicates
Duplicate rows were removed to prevent biasing model training and to ensure each car listing is counted only once.

## 6. Outlier Handling (IQR Capping)
I applied IQR capping to `Price` and `Odometer_km` to limit extreme outliers. This prevents extreme values from disproportionately affecting model performance, while still retaining most of the data.

## 7. One-Hot Encoding
`Location` was one-hot encoded to convert categorical text into numerical format for modeling. I kept all 0/1 columns separate to avoid assuming ordinal relationships.

## 8. Feature Engineering
I engineered the following features to enhance predictive power while avoiding target leakage:  
- **CarAge:** captures the age of the car, which strongly influences price.  
- **Km_per_year:** average kilometers driven per year; provides a measure of usage intensity.  
- **Is_Urban:** indicates if a car is listed in a city/urban area, which may affect pricing trends.  
- **LogPrice:** log transformation of `Price` to stabilize skewness and improve model performance on skewed targets.

These features were chosen because they are interpretable, do not directly leak the target, and can improve model understanding of car value.

## 9. Feature Scaling
Continuous numeric features (`Odometer_km`, `CarAge`, `Km_per_year`) were standardized using `StandardScaler` to ensure they contribute equally to model training.  
- **Excluded from scaling:** `Price`, `LogPrice`, 0/1 dummies (`Location_*`, `Is_Urban`) because scaling binary variables or targets is unnecessary and may distort their meaning.

## 10. Final Checks & Save
After all preprocessing steps, I verified that all missing values were handled, features were correctly scaled, and the dataframe was consistent. The cleaned dataset was saved for modeling as `car_l3_clean_ready.csv`.
