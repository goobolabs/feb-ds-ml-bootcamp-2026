
# Reflection — Lesson 3 Data Preprocessing

This reflection explains the reasoning behind each major preprocessing decision applied to the car price dataset.

---

## Price Cleaning
The `Price` column contained currency symbols and commas, which prevented numeric operations. These characters were removed using regular expressions, and the column was converted to `float`. A log-transformed version (`Log_Price`) was created to reduce skewness and provide an alternative modeling target for algorithms sensitive to non-normal distributions.

---

## Handling Categorical Errors
The `Location` column included typos (e.g., *Subrb*) and unknown values (`??`). These inconsistencies were corrected or converted to missing values before imputation. Fixing categorical errors before imputation ensures that incorrect categories do not dominate the mode calculation.

---

## Missing Value Imputation
- **Odometer_km:** Imputed using the median because mileage is often skewed and affected by extreme values.
- **Doors:** Imputed using the mode since it is a discrete variable with limited valid values.
- **Location:** Imputed using the mode, assuming the most frequent category is the most reasonable default.

These choices balance robustness and simplicity while preserving data integrity.

---

## Duplicate Removal
Duplicate rows were removed to prevent biased model training and duplicated influence of identical observations.

---

## Outlier Treatment
IQR-based capping was applied to `Price` and `Odometer_km`. Instead of removing outliers, clipping preserves all records while limiting the influence of extreme values. This approach is especially useful when data size is limited.

---

## Encoding
The `Location` feature was one-hot encoded to convert categorical data into a numeric format suitable for machine learning models. Binary dummy variables ensure no ordinal meaning is incorrectly implied.

---

## Feature Engineering
Several features were engineered to add domain-relevant information:
- **Car_age:** Represents vehicle depreciation over time.
- **Is_Modern:** Captures newer vehicle trends.
- **High_Mileage:** Flags cars likely to have lower resale value.
- **Is_city:** Simplifies location information into an urban indicator.

These features are derived solely from existing inputs and do not introduce data leakage.

---

## Feature Scaling
Standardization was applied only to continuous input features. Target variables and dummy variables were excluded to maintain interpretability and correctness. Scaling ensures that models sensitive to feature magnitude (e.g., linear regression, k-means) perform optimally.

---

## Conclusion
The preprocessing pipeline produces a clean, consistent, and model-ready dataset. Each decision prioritizes robustness, reproducibility, and alignment with machine learning best practices.
