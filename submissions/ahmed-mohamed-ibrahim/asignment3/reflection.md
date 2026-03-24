# Lesson 3 Data Preprocessing Reflection  
## Step 1  Load & Inspect  
Loaded `car_l3_dataset.csv` and explored shape, head, info, missing counts, and `Location` values. Found mixed `Price` types, missing values, typos, duplicates, and outliers.  
## Step 2  Clean Target Formatting  
Removed `$`, `,`, `USD` from `Price` and converted invalid entries (`??`) to missing. Ensured `Price` is numeric and ready for modeling.  
## Step 3  Fix Category Errors  
Normalized `Location` (strip, capitalize), corrected typos (`Subrb → Suburb`), and set unknowns to missing. This ensures categorical consistency before imputation.  
## Step 4  Impute Missing Values  
 Continuous: `Odometer_km → median` (robust to outliers)  
 Discrete/Categorical: `Doors/Accidents → mode`  
 Categorical: `Location → mode`  
 Target: `Price → median` (cannot drop rows)  
Median preserves distribution for numeric features; mode ensures categorical consistency.  
## Step 5  Remove Duplicates  
Dropped exact duplicates to reduce redundancy while preserving data integrity.  
## Step 6  Outliers (IQR Capping)  
Used IQR to compute lower/upper bounds for `Price` and `Odometer_km` and clipped extreme values. Preserves dataset size while limiting outlier influence.  
## Step 7  One-Hot Encoding  
Encoded `Location` into `Location_City`, `Location_Suburb`, `Location_Rural`. Maintains categorical info without introducing ordinal relationships. Values are 0/1.  
## Step 8  Feature Engineering  
`CarAge = 2026 − Year` → vehicle age  
`Km_per_year = Odometer_km / CarAge` → usage intensity (safe divide-by-zero)  
`Is_Urban = 1 if City/Suburb else 0` → urban influence  
`LogPrice = log(Price + 1)` → reduces skew, helps linear models  
No leakage; features derived from known inputs only.  
## Step 9  Feature Scaling  
Standardized continuous inputs (`Odometer_km`, `CarAge`, `Km_per_year`) with mean ≈ 0, std ≈ 1. Did not scale `Price`, `LogPrice`, or dummy variables.  
## Step 10  Final Checks & Save  
Verified all non-target missing values are gone, scaled features are correct, and one-hot encoding is accurate. Saved as `car_l3_clean_ready.csv`.  
### Summary of Decisions  
 **Median vs Mode:** Median for numeric features with outliers, mode for categorical/discrete.  
 **IQR Capping:** Limits extreme influence without dropping data.  
 **Feature Engineering:** Added meaningful, non-leaking features capturing age, usage, and urban/rural info.  
 **Price Handling:** Median imputation for missing targets to maintain dataset size.