# Reflection — Data Preprocessing Assignment

**STEP 1: Load & Inspect**  
- Daalac head, shape, info, missing values si aan u fahanno cilladaha dataset-ka.  
- Typos: Subrb → Suburb, unknowns ?? → NaN.

**STEP 2: Clean Price**  
- Ka saaray `$` iyo `,` si Price uu noqdo numeric.  
- Skewness waxaa loo tixgeliyey si target modeling u fududaado.

**STEP 3: Fix Categories**  
- Location typo’s iyo unknowns la saxay ka hor One-Hot Encoding.

**STEP 4: Imputation**  
- Odometer_km → median  
- Doors & Accidents → mode  
- Location → mode

**STEP 5: Remove Duplicates**  
- Ka saaray rows duplicated si bias uusan u dhicin.

**STEP 6: Outlier Capping (IQR)**  
- Price & Odometer_km capps garay bounds IQR si extreme values loo xakameeyo.

**STEP 7: One-Hot Encoding**  
- Location → 0/1 dummies (`Location_City`, `Location_Suburb`, `Location_Rural`)

**STEP 8: Feature Engineering**  
- CarAge, Km_per_year, Is_Urban, LogPrice

**STEP 9: Feature Scaling**  
- Continuous: Odometer_km, CarAge, Km_per_year  
- StandardScaler: mean≈0, std≈1

**STEP 10: Final Checks & Save**  
- Missing values=0, Price numeric, LogPrice numeric

**Summary:**  
- Decisions waxay ku saleysan yihiin type-ka data: median for skewed numeric, mode for categorical, IQR for outliers.  
- Feature engineering waxay abuurtaa predictive features oo aan leakage ku jirin.
