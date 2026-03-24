# Reflection: Data Preprocessing Decisions


**Date:** February 22, 2026  
**Assignment:** Lesson 3 - Data Preprocessing

---

## Step 2: Clean Target Formatting (Price)

**Decision:** Removed currency symbols ($) and commas, then converted to numeric float.

**Reasoning:** Machine learning algorithms require numerical input. The mixed format (strings with "$1,500" and plain numbers like 1500.0) would cause errors. Converting everything to float ensures consistency and enables mathematical operations. The high positive skewness (>2) indicates a right-tailed distribution, which is common for price data where most cars are cheaper with few expensive outliers.

---

## Step 3: Fix Category Errors Before Imputation

**Decision:** Normalized Location text (strip whitespace, title case), mapped typos ("Subrb" → "Suburb"), and converted unknowns ("??", empty strings) to NaN before imputation.

**Reasoning:** Fixing typos before imputation prevents creating incorrect categories. If we imputed first, "Subrb" would remain as a separate category, fragmenting the data. Converting "??" to NaN allows proper imputation with the mode, rather than treating unknown as a valid location. This ensures clean categorical data for encoding.

---

## Step 4: Impute Missing Values

**Decisions:**
- **Odometer_km → Median**
- **Doors → Mode**
- **Accidents → Mode**
- **Location → Mode**

**Reasoning:**

**Median for Odometer_km:** Mileage data often contains outliers (very high or very low values). The median is robust to outliers, unlike the mean which would be skewed by extreme values. This provides a more representative "typical" mileage.

**Mode for Doors:** Most cars have 4 doors. Using the most common value is logical since door count is discrete and clustered around standard values (2, 4, 5). The mode represents the most likely configuration.

**Mode for Accidents:** Most cars have 0 or 1 accident. The mode (most frequent value) is the safest assumption when accident history is unknown. Using mean would give fractional values which don't make sense for count data.

**Mode for Location:** When location is unknown, assuming the most common location (likely "City" or "Suburb") is more reasonable than random assignment. This minimizes bias while maintaining data distribution.

---

## Step 5: Remove Duplicates

**Decision:** Dropped exact duplicate rows.

**Reasoning:** Duplicate entries can artificially inflate certain patterns, leading to overfitting. They don't add new information and can bias the model toward memorizing repeated examples. Removing them ensures each data point contributes unique information.

---

## Step 6: Outliers (IQR Capping)

**Decision:** Used IQR (Interquartile Range) method to cap outliers in Price and Odometer_km at lower_bound = Q1 - 1.5×IQR and upper_bound = Q3 + 1.5×IQR.

**Reasoning:**

**Why IQR over removal:** Capping preserves data points while limiting extreme influence. Removing outliers reduces dataset size and may discard legitimate edge cases. Capping retains the information that a value was extreme while preventing it from dominating the model.

**Why 1.5×IQR:** This is a standard statistical threshold that balances outlier detection sensitivity. It's aggressive enough to catch true outliers but conservative enough to avoid flagging normal variation.

**Why Price and Odometer_km:** These continuous variables are most susceptible to outliers (e.g., luxury cars with $135,000 price, or cars with 395,000 km). Outliers in these features can disproportionately affect distance-based algorithms and regression models.

---

## Step 7: One-Hot Encoding

**Decision:** Applied one-hot encoding to Location without dropping any category (drop_first=False).

**Reasoning:** One-hot encoding converts categorical text into binary (0/1) columns that algorithms can process. I kept all categories (City, Suburb, Rural) rather than dropping one because:
1. It makes the data more interpretable (each location explicitly represented)
2. The slight multicollinearity is acceptable for tree-based models
3. It's clearer for feature importance analysis

Each Location_* column is binary (0 or 1), indicating presence/absence of that location type.

---

## Step 8: Feature Engineering

**Decisions:** Created four new features and one alternative target.

**Features Created:**

1. **CarAge = 2026 - Year**
   - **Why:** Age is more meaningful than year for predicting price. Older cars typically depreciate.
   - **No leakage:** Uses only historical information (manufacturing year).

2. **Km_per_year = Odometer_km / (CarAge + 1)**
   - **Why:** Average annual mileage indicates usage intensity, which affects value.
   - **Safe handling:** Added +1 to denominator to avoid division by zero for brand new cars.
   - **No leakage:** Derived from existing features only.

3. **Is_Urban = 1 if Location_City, else 0**
   - **Why:** Urban vs non-urban distinction may affect pricing (city cars face more wear).
   - **No leakage:** Based on location, which is known at prediction time.

4. **High_Mileage = 1 if Odometer_km > 150,000, else 0**
   - **Why:** High mileage is a critical threshold for car value depreciation.
   - **No leakage:** Threshold based on domain knowledge, not target variable.

**Alternative Target:**

5. **LogPrice = log(Price + 1)**
   - **Why:** Log transformation reduces skewness in price distribution, which can improve linear model performance.
   - **Not a feature:** This is an alternative target variable, NOT used as input (X).
   - **+1 added:** Prevents log(0) errors if any prices were zero.

---

## Step 9: Feature Scaling

**Decision:** Standardized continuous features (Odometer_km, Doors, Accidents, Year, CarAge, Km_per_year) using StandardScaler. Did NOT scale Price, LogPrice, or binary dummies.

**Reasoning:**

**Why standardize:** Distance-based algorithms (KNN, SVM) and gradient-based models (Linear Regression, Neural Networks) are sensitive to feature scales. Standardization (mean=0, std=1) ensures all features contribute equally.

**Why exclude Price/LogPrice:** These are target variables (y), not features (X). Scaling targets can complicate interpretation and isn't necessary for most algorithms.

**Why exclude binary dummies:** Location_*, Is_Urban, and High_Mileage are already on a 0-1 scale. Standardizing them would make them harder to interpret without improving model performance.

**StandardScaler vs MinMaxScaler:** StandardScaler is more robust to outliers (which we already capped) and is the default choice for most ML algorithms. It centers data around zero, which helps gradient descent converge faster.

---

## Final Checks

**Verification:**
- ✅ No missing values remain (all imputed)
- ✅ Price and LogPrice are numeric floats
- ✅ Location encoded as binary dummies
- ✅ Scaled features have mean ≈ 0 and std ≈ 1
- ✅ Dataset saved as `car_l3_clean_ready.csv`

**Outcome:** The preprocessing pipeline successfully transformed messy raw data into a clean, model-ready dataset. All decisions were made to balance data quality, interpretability, and model performance while avoiding data leakage.

---

## Summary

This preprocessing pipeline demonstrates best practices in data cleaning:
1. **Systematic approach:** Each step builds on the previous one
2. **Justified decisions:** Every choice has a clear rationale
3. **No data leakage:** All engineered features use only available information
4. **Reproducibility:** Clear documentation enables replication
5. **Robustness:** Handles missing values, outliers, and categorical data appropriately

The cleaned dataset is now ready for machine learning model training in future lessons.
