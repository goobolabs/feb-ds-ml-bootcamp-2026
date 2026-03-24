# Assignment 3 – Data Preprocessing Reflection

**1. Missing Values**
- Odometer_km: filled with median to handle outliers without skewing mean.
- Doors & Accidents: filled with mode since these are categorical-like features.
- Location: filled with mode to replace unknown/missing categories.

**2. Target Cleaning**
- Removed "$" and "," from Price, converted to float.
- Checked skewness.

**3. Category Fixes**
- Corrected typos like "Subrb" → "Suburb".
- Unknowns ("??") converted to missing.

**4. Duplicate Removal**
- Dropped exact duplicates to avoid bias in models.

**5. Outlier Handling**
- Used IQR clipping on Price and Odometer_km to limit extreme values.

**6. Encoding**
- One-hot encoded Location to avoid ordinal assumptions.

**7. Feature Engineering**
- `CarAge = 2026 - Year`
- `Km_per_year = Odometer_km / CarAge` (avoid division by zero)
- `Is_Urban = City/Suburb flag`
- `LogPrice = log(Price + 1)` for alternative target.

**8. Feature Scaling**
- Standardized numeric features only (excluded Price, LogPrice, Location dummies).

**9. Final Checks**
- No missing values, all features properly scaled/encoded.
