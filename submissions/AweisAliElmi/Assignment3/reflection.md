# Reflection: Data Preprocessing Pipeline

This document explains the rationale behind the key decisions made during the preprocessing of the `car_l3_dataset.csv`.

## 1. Handling Missing Values (Imputation)
- **Odometer_km (Median)**: Mileage data typically has a skewed distribution with potential extreme values (e.g., extremely worn-out cars). The median is robust to these outliers, whereas the mean would be biased by them.
- **Doors, Accidents, Location (Mode)**: These are categorical or discrete variables. 
    - You cannot have "3.5 doors", so the mean is invalid. The mode (most frequent value) is the statistically safest assumption for categorical imputation.
    - For `Accidents`, we assumed the most common case (likely 0 or low) applies to missing records.

## 2. Outlier Management (IQR Capping)
- **Method**: We used the Interquartile Range (IQR) method (1.5 * IQR).
- **Decision**: Instead of removing outliers (which deletes data), we **capped** (clipped) them.
- **Reasoning**: Features like `Price` and `Odometer_km` can have genuine high values (luxury cars, high mileage). Removing them biases the model against real-world variance. Capping constrains the extreme influence on linear models (and scaling) while keeping the data point in the set.

## 3. Feature Engineering
We engineered three features to capture more meaningful patterns:
1. **`CarAge`**: Raw `Year` is treated as a number by models, but "Age" (2026 - Year) is more directly correlated with depreciation.
2. **`Km_per_year`**: This interaction feature reveals how intensively a car was used. A 10-year-old car with 100k km is normal; a 2-year-old car with 100k km is a red flag.
3. **`High_Usage`**: A binary flag derived from `Km_per_year`. This helps tree-based models easily split "abused" cars from normal ones without needing complex splits on the continuous variable.
4. **`LogPrice`**: Added as an alternative target. Prices often follow a log-normal distribution; predicting `LogPrice` usually yields lower errors (RMSE) than raw Price.

## 4. Scaling
- **Applied to**: Continuous features (`Odometer_km`, `CarAge`, `Km_per_year`).
- **Excluded**:
    - `Price` / `LogPrice`: These are targets. We do not scale what we predict (unless specifically needed for neural nets), and certainly not for interpretability.
    - `Location_*` (Dummy Variables): These are already 0 or 1. Scaling them destroys their sparse property and interpretability.
