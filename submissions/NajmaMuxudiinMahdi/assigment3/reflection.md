1️⃣ Data Loading and Initial Inspection
Loaded dataset using pandas
Displayed head(), info(), missing values
Identified formatting issues, missing data, duplicates, and outliers

2️⃣ Target Cleaning (Price Formatting)
Removed currency symbols and commas using regex
Converted Price to float
Ensured consistent numeric format


3️⃣ Categorical Error Correction
Fixed typos in Location (e.g., Subrb → Suburb)
Converted unknown values ("??") to missing
Standardized categorical entries before imputation


4️⃣ Missing Value Imputation
Imputed Odometer_km using median
Imputed Doors using mode
Imputed Location using mode


5️⃣ Duplicate Removal
Checked dataset shape before and after
Removed duplicate rows to prevent bias


6️⃣ Outlier Treatment using IQR Capping
Computed IQR bounds for Price and Odometer_km
Applied clipping instead of removing rows
Reduced impact of extreme values


7️⃣ One-Hot Encoding of Categorical Features
Converted Location into binary dummy variables
Preserved non-ordinal representation


8️⃣ Feature Engineering
Created age_of_car
Created odometer_per_year
Created log_price as alternative target

9️⃣ Feature Scaling (Input Features Only)
Identified continuous numeric features
Applied StandardScaler
Excluded target columns and dummy variables


🔟 Final Validation and Export
Confirmed no missing values remain
Verified data types
Saved cleaned dataset to CSV