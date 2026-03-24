# Lesson 3 — Data Preprocessing Reflection  
Name: Abdinajib Hussein Mohamed  

## 1. Initial Inspection

After loading the dataset, I inspected the structure using head(), shape, info(), and missing value counts. I identified several issues:
- The `Price` column contained mixed formats (currency symbols and commas).
- Missing values existed in `Odometer_km`, `Doors`, and `Location`.
- The `Location` column contained typos such as “Subrb” and unknown values like “??”.
- There were duplicate rows.
- The distribution of `Price` was highly skewed.

These issues required structured cleaning before modeling.


## 2. Cleaning the Target (Price)

The `Price` column was cleaned by removing currency symbols and commas, then converting it to numeric format. This ensured proper mathematical operations such as IQR and log transformation could be applied.

Skewness was checked, and since it was high, I later created `LogPrice = log(Price + 1)` as an alternative target to stabilize variance.


## 3. Fixing Categorical Errors Before Imputation

Before imputing missing values, I standardized the `Location` column by:
- Normalizing capitalization
- Correcting typos (e.g., Subrb → Suburb)
- Converting unknown values (e.g., “??”) into missing values

This step was important to prevent incorrect mode calculation during imputation.


## 4. Missing Value Imputation

Different strategies were used based on data type:

- `Odometer_km` → Median  
  Median is robust to outliers and better for skewed numerical data.

- `Doors` and `Accidents` → Mode  
  These are discrete variables, so the most frequent category is appropriate.

- `Location` → Mode  
  Since it is categorical, mode preserves the most common class.

After imputation, all missing values were confirmed to be zero.


## 5. Removing Duplicates

Duplicate rows were removed to prevent bias in model training and ensure each observation represents a unique car.


## 6. Outlier Treatment (IQR Capping)

Outliers in `Price` and `Odometer_km` were handled using the Interquartile Range (IQR) method.

Instead of removing extreme values, I applied capping (clipping) to the calculated lower and upper bounds. This approach preserves dataset size while reducing distortion caused by extreme values.

IQR was chosen because it is robust and does not assume normal distribution.


## 7. One-Hot Encoding

The `Location` categorical variable was converted into binary (0/1) dummy variables using one-hot encoding. This allows machine learning models to process categorical data without introducing artificial ordinal relationships.


## 8. Feature Engineering (No Data Leakage)

I engineered the following features:

- `CarAge` = Current Year − Year  
  Captures vehicle depreciation effect.

- `Km_per_year`  
  Measures vehicle usage intensity.

- `Is_Urban`  
  Indicates whether the car is located in City/Suburb.

- `LogPrice`  
  Created as an alternative modeling target to reduce skewness.

No engineered feature used future or target-leaking information.


## 9. Feature Scaling

Continuous features were standardized using StandardScaler to ensure equal contribution to modeling. Binary dummy variables and target columns were intentionally excluded from scaling.

After scaling, the selected features had mean approximately 0 and standard deviation approximately 1.


## 10. Final Validation

Final checks confirmed:
- `Price` is numeric
- `LogPrice` exists
- No missing values remain
- Dummy variables exist
- Scaled features are standardized

The cleaned dataset was saved as `car_l3_clean_ready.csv`, ensuring reproducibility.

### Conclusion

This preprocessing pipeline ensures the dataset is clean, consistent, and model-ready. Each transformation was applied in a logical order to prevent bias, data leakage, and distortion, resulting in a reliable foundation for machine learning modeling.