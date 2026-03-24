# Reflection on Data Cleaning and Preparation (Step 1–10)

During this assignment, I worked on cleaning, preprocessing, and preparing a car dataset (`car_l3_dataset.csv`) for further analysis or machine learning modeling. The process involved multiple steps, each focusing on improving the quality and usability of the data.

---

## Step 1: Loading and Understanding the Data
- Loaded the CSV dataset into a Pandas DataFrame.  
- Explored the data using `.head()`, `.shape()`, `.info()`, and `.isnull().sum()`.  
- Identified columns with string formatting issues (like `Price` with `$` signs and commas) and numerical columns with missing values (`Odometer_km`, `Doors`).  

---

## Step 2: Cleaning Price Column
- Removed `$` and `,` from the `Price` column using regex.  
- Converted the column to numeric type.  
- Filled any resulting NaNs with the median of the `Price`.  
- Calculated skewness to understand the distribution.  

> **Lesson learned:** Always clean and standardize numeric columns with special characters before processing.

---

## Step 3: Handling Location Data
- Lowercased all location entries and corrected typos (`subrb → suburb`).  
- Converted unknown values (`??`) to NaN.  
- Filled missing locations with the mode.  

> **Lesson learned:** Categorical data needs careful standardization.

---

## Step 4: Handling Missing Values
- Filled missing values for `Odometer_km` with the median.  
- Filled `Doors` and `Accidents` using mode.  

> **Lesson learned:** Choosing the appropriate method (median, mode, or mean) depends on the data type and distribution.  

---

## Step 5: Removing Duplicates
- Checked for and dropped duplicate rows to avoid bias in analysis.  

---

## Step 6: Handling Outliers
- Detected outliers in `Price` and `Odometer_km` using IQR (Interquartile Range).  
- Clipped extreme values to reduce their impact.  

> **Lesson learned:** Outlier handling ensures statistical summaries and models are not distorted by extreme values.

---

## Step 7: One-Hot Encoding
- Converted the categorical `Location` column into numeric dummy variables (`Location_city`, `Location_rural`, `Location_suburb`).  
- Ensured conversion to `0/1` type for machine learning compatibility.  

---

## Step 8: Feature Engineering
- Created new features:  
  - `CarAge` = 2026 − Year  
  - `Km_per_year` = Odometer_km ÷ CarAge  
  - `Is_Urban` = 1 if Location is City or Suburb, else 0  
  - `LogPrice` = log transformation of Price  

> **Lesson learned:** Feature engineering creates meaningful attributes that improve analysis and modeling.

---

## Step 9: Scaling Numerical Features
- Standardized `Odometer_km`, `Km_per_year`, and `CarAge` using `StandardScaler`.  

> **Lesson learned:** Scaling prevents features with larger ranges from dominating.

---

## Step 10: Final Dataset Preparation
- Saved the cleaned, engineered, and scaled dataset into `car_l3_dataset_step10.csv`.  
- Verified all missing values were handled and data types were correct.  

> **Lesson learned:** Documenting each step and saving the final dataset ensures reproducibility and integrity.

---

## Overall Reflection
- Gained practical understanding of **data cleaning, preprocessing, and feature engineering**.  
- Learned how to handle messy datasets: missing values, typos, duplicates, outliers, and inconsistent formatting.  
- Practiced using **Pandas**, **NumPy**, and **Scikit-Learn** for preprocessing, encoding, and scaling.  
- Faced challenges with chained assignment warnings and learned correct Pandas practices.  
- Reinforced the importance of **clean, structured datasets** for reliable analysis and machine learning.


