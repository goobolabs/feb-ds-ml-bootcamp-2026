# Reflection - Lesson 3 Data Preprocessing

## 1. Load & Inspect
Initial inspection revealed missing values in `Odometer_km`, `Location`, and `Price` formatting issues. The dataset contained 145 rows of data with some duplicates and typos in the `Location` column.

## 2. Price Cleaning
Price was stored as a currency string (e.g., "$1,500"). I used regex to remove `$` and `,` before converting to float. The skewness was reported to understand if log transformation would be beneficial (which I later added as `LogPrice`).

## 3. Fixing Categorical Errors
Before imputation, I addressed inconsistencies in `Location`. 
- "Subrb" was mapped to "Suburb".
- Unknown placeholders like "??" were converted to `NaN` using `np.nan`.
This ensures the `mode()` calculation in the next step is accurate and not biased by placeholders.

## 4. Imputation Choices
- **Odometer_km (Median):** Used median because it is robust to outliers, which were present in the odometer readings.
- **Doors, Accidents, Location (Mode):** Used the most frequent value for these columns as they are discrete/categorical. For `Location`, the mode was calculated AFTER fixing typos.

## 5. Duplicate Removal
Removed exact duplicates to ensure the model doesn't overfit to repeated data points.

## 6. Outlier Handling (IQR)
Used the Interquartile Range (IQR) method with $k=1.5$ to clip extreme values in `Price` and `Odometer_km`. Clipping (winsorization) was preferred over removal to maintain the data size while reducing variance.

## 7. One-Hot Encoding
Encoded `Location` into binary columns. This allows the model to interpret categorical data without assuming an ordinal relationship.

## 8. Feature Engineering
Created three new features:
1. **CarAge:** Difference between current year (2026) and car year. Helps capture depreciation.
2. **Km_per_year:** Calculated as `Odometer_km / (CarAge + 1)`. Adding 1 avoids division by zero for new cars.
3. **Is_Urban:** A boolean flag (derived from encoded columns) where 1 indicates City or Suburb.

Added **LogPrice** as an alternative target to normalize the price distribution.

## 9. Feature Scaling
Used `StandardScaler` to standardize continuous features (`Odometer_km`, `Doors`, `Accidents`, `Year`, `CarAge`, `Km_per_year`).
- **Exclusions:** Did not scale `Price` or `LogPrice` (targets) or the dummy variables (0/1 indicators), as scaling binary flags destroys their interpretability without adding value.

## 10. Final Verification
Ensured zero missing values and confirmed that scaled features have a mean of 0 and a standard deviation of 1.
