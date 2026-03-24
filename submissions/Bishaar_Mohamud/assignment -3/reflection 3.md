
# **Lesson 3 — Data Preprocessing Reflection**

**Name: Bishaar Mohamud**



## 1. Initial Inspection

After loading the dataset, I performed an initial inspection using `head()`, `shape`, `info()`, and missing value analysis.

Several data quality issues were identified:

* The `Price` column contained mixed formats (currency symbols and commas).
* Missing values existed in `Odometer_km`, `Doors`, and `Location`.
* The `Location` column included typographical errors such as *“Subrb”* and ambiguous values like *“??”*.
* Duplicate rows were present.
* The `Price` distribution was highly skewed.

These issues required structured preprocessing before modeling.



## 2. Cleaning the Target (Price)

The `Price` column was cleaned by:

* Removing currency symbols and commas
* Converting values to numeric format

This ensured compatibility with mathematical operations such as IQR calculation and log transformation.

Since skewness was high, I created an alternative target variable:

```
LogPrice = log(Price + 1)
```

This transformation helps stabilize variance and improve model performance.



## 3. Fixing Categorical Errors Before Imputation

Before imputing missing values, I standardized the `Location` column by:

* Normalizing capitalization
* Correcting typographical errors (e.g., *Subrb → Suburb*)
* Converting ambiguous entries (e.g., *“??”*) into missing values

This step was essential to avoid incorrect mode calculation during imputation.


## 4. Missing Value Imputation

Different imputation strategies were applied based on variable type:

* **`Odometer_km` → Median**
  The median is robust to outliers and appropriate for skewed numerical data.

* **`Doors` and `Accidents` → Mode**
  These are discrete variables; therefore, the most frequent value is suitable.

* **`Location` → Mode**
  As a categorical variable, mode preserves the most common category.

After imputation, all missing values were successfully eliminated.



## 5. Removing Duplicates

Duplicate rows were removed to prevent bias during model training and to ensure that each record represents a unique vehicle.



## 6. Outlier Treatment (IQR Capping)

Outliers in `Price` and `Odometer_km` were handled using the **Interquartile Range (IQR)** method.

Instead of removing extreme observations, I applied **capping (clipping)** at the calculated lower and upper bounds.

This approach:

* Preserves dataset size
* Reduces distortion from extreme values

IQR was selected because it is robust and does not assume normal distribution.



## 7. One-Hot Encoding

The categorical variable `Location` was transformed into binary dummy variables using **one-hot encoding**.

This prevents the introduction of artificial ordinal relationships and allows machine learning algorithms to process categorical data effectively.


## 8. Feature Engineering (No Data Leakage)

The following features were engineered:

* **`CarAge` = Current Year − Year**
  Captures vehicle depreciation.

* **`Km_per_year`**
  Represents usage intensity.

* **`Is_Urban`**
  Indicates whether a car is located in a City or Suburb.

* **`LogPrice`**
  An alternative target to reduce skewness.

No engineered feature introduced future information or target leakage.



## 9. Feature Scaling

Continuous variables were standardized using **StandardScaler** to ensure equal contribution during modeling.

Binary dummy variables and target columns were intentionally excluded from scaling.

After scaling:

* Mean ≈ 0
* Standard deviation ≈ 1



## 10. Final Validation

Final validation confirmed:

* `Price` is numeric
* `LogPrice` exists
* No missing values remain
* Dummy variables were successfully created
* Scaled features are standardized

The cleaned dataset was saved as:

```
car_l3_clean_ready.csv
```

ensuring reproducibility and consistency.


## Conclusion

This preprocessing pipeline ensures that the dataset is clean, consistent, and fully prepared for modeling.

Each transformation was applied in a logical sequence to prevent bias, avoid data leakage, and reduce distortion. The final dataset provides a reliable and structured foundation for machine learning development.




