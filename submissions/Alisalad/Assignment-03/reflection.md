# Reflection — Lesson 3 Data Preprocessing

This assignment required building a reproducible pipeline to clean and prepare the car price dataset. Below I explain the reasoning behind each major decision.

**Target Cleaning (Price)**  
The `Price` column contained currency symbols and commas. I stripped these and converted to float to ensure numeric consistency. Skewness was high, so I added a log‑transformed version (`LogPrice`) to stabilize variance for modeling.

**Category Normalization**  
`Location` had typos (“Subrb”) and placeholders (“??”). I standardized text to lowercase, mapped typos to correct values, and treated unknowns as missing. This ensured categories were consistent before imputation.

**Imputation Choices**  
- `Odometer_km`: Median was chosen because it is robust to outliers and better represents central tendency in skewed distributions.  
- `Doors` and `Accidents`: Mode was used since these are discrete/categorical counts where the most frequent value is a sensible default.  
- `Location`: Mode was used to fill missing values, reflecting the most common location type.

**Duplicates**  
Duplicates were removed to avoid bias and redundancy. This step ensures each observation contributes unique information.

**Outlier Handling (IQR Capping)**  
I applied IQR capping to `Price` and `Odometer_km`. This method clips extreme values without discarding data, preserving sample size while reducing distortion from unrealistic outliers.

**Encoding**  
`Location` was one‑hot encoded into dummy variables. This allows categorical information to be represented numerically for machine learning models.

**Feature Engineering**  
I added several features to enrich the dataset:  
- `CarAge = CURRENT_YEAR - Year` (captures depreciation/age effect).  
- `Mileage_per_Year = Odometer_km / CarAge` (usage intensity, safely handled for zero age).  
- `Is_FourDoor` (binary flag for common sedan type).  
- `Has_Accidents` (binary accident history).  
- `Is_City` (urban indicator from location dummy).  
Additionally, `LogPrice` was created as an alternative target to reduce skew.

**Scaling**  
Continuous features were standardized to mean ≈ 0 and std ≈ 1. I excluded targets (`Price`, `LogPrice`), discrete counts (`Doors`, `Accidents`), and dummy/binary flags, since scaling them would distort their meaning.

**Final Checks**  
Assertions confirmed: `Price` is float, `LogPrice` exists, no missing values remain, at least one `Location_*` dummy column exists, and scaled features have mean ≈ 0 and std ≈ 1. The cleaned dataset was saved to `car_l3_clean_ready.csv`.

---

Overall, each step was chosen to balance robustness, interpretability, and reproducibility. The pipeline ensures the dataset is clean, consistent, and ready for modeling.
