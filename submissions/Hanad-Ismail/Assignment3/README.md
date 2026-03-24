# Lesson 3 — Data Preprocessing Assignment

## Project Overview
This project focuses on building a clean and reproducible data preprocessing pipeline for a messy tabular dataset. The dataset contains car price information with intentional issues such as missing values, inconsistent formatting, typos, outliers, and duplicate records.

The goal is to prepare the dataset for machine learning by cleaning, transforming, and engineering features while avoiding data leakage.

---

## Dataset
**File:** `car_l3_dataset.csv`

### Original Columns
- `Price` — mixed numeric values and currency-formatted strings
- `Odometer_km` — mileage in kilometers (with missing values and outliers)
- `Doors` — number of doors
- `Accidents` — number of accidents
- `Location` — categorical (City, Suburb, Rural) with typos and unknown values
- `Year` — manufacturing year

---

## Preprocessing Steps

1. **Load & Inspect**
   - Loaded dataset using pandas
   - Inspected structure, data types, missing values, and duplicates

2. **Target Cleaning (Price)**
   - Removed currency symbols and commas
   - Converted `Price` to numeric (`float`)
   - Created a log-transformed alternative target (`Log_Price`)

3. **Categorical Cleaning**
   - Fixed typos in `Location` (e.g., `Subrb → Suburb`)
   - Converted unknown values (`??`) to missing

4. **Missing Value Imputation**
   - `Odometer_km` → median
   - `Doors` → mode
   - `Location` → mode

5. **Duplicate Removal**
   - Identified and removed duplicate rows

6. **Outlier Handling (IQR Capping)**
   - Applied IQR-based clipping to:
     - `Price`
     - `Odometer_km`

7. **Encoding**
   - One-hot encoded `Location` using `pd.get_dummies`

8. **Feature Engineering**
   - `Car_age` — current year minus car year
   - `Is_Modern` — whether the car is from 2015 or later
   - `High_Mileage` — mileage greater than 150,000 km
   - `Is_city` — binary indicator for city location
   - `Log_Price` — log-transformed price (alternative target)

9. **Feature Scaling**
   - Standardized numerical features using `StandardScaler`
   - Excluded:
     - Target variables (`Price`, `Log_Price`)
     - One-hot encoded categorical features

10. **Final Output**
    - Clean dataset saved as `car_clean_data.csv`
    - No missing values remain
    - Dataset ready for modeling

---

## Files Included
- `l3_preprocess.py` — preprocessing script
- `car_l3_dataset.csv` — raw dataset
- `car_clean_data.csv` — cleaned dataset
- `reflection.md` — explanation of preprocessing decisions
- `requirements.txt` — Python dependencies and versions

---

