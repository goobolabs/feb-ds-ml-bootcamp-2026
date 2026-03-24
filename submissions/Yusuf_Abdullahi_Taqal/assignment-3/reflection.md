## Reflection (≤ 1 page)

**Step 1 – Load & inspect**  
I printed head/tail, shape, info, and missing counts to understand column types, the extent of missing data, and category issues in `Location`. This guided the cleaning and imputation choices.

**Step 2 – Clean target formatting (`Price`)**  
`Price` arrived as mixed strings with currency symbols and commas. I stripped non-numeric characters, converted to numeric, and checked skewness to understand the distribution before any outlier handling.

**Step 3 – Fix category errors before imputation**  
I standardized `Location` by lowercasing and stripping whitespace, then mapped typos like `subrb` → `suburb` and invalid values like `??`/`unknown` to missing. This avoids incorrectly imputing or encoding noisy categories.

**Step 4 – Impute missing values (why median vs mode)**  
For `Odometer_km`, I used the **median** because mileage is continuous and skewed, and the median is robust to outliers. For `Doors` and `Location`, I used the **mode** because they are discrete/categorical values where the most frequent choice is a sensible default.  
Accidents had no missing values, so no imputation was needed.

**Step 5 – Remove duplicates**  
Dropping duplicates prevents repeated rows from biasing summary statistics and model training. I reported the count removed to make the step auditable.

**Step 6 – Outliers (IQR capping)**  
I applied IQR capping to `Price` and `Odometer_km`. This keeps all rows but limits extreme values that could distort scaling and modeling. IQR is a standard, distribution-agnostic method suitable for skewed data.

**Step 7 – One-hot encoding**  
`Location` was converted into 0/1 dummy columns to make the feature usable by models that require numeric inputs and to avoid imposing an ordinal relationship between categories.

**Step 8 – Feature engineering (what and why)**  
I engineered:
1. `CarAge` = current year − `Year`, capturing vehicle age directly.
2. `Km_per_year` = `Odometer_km` / `CarAge`, representing usage intensity.
3. `Is_Urban` = 1 if `Location_city` else 0, capturing a simple urban signal.
4. `LogPrice` = log(Price + 1), a stabilized alternative target for modeling skewed prices.

**Step 9 – Feature scaling**  
I standardized continuous predictors (`Odometer_km`, `CarAge`, `Km_per_year`) to mean ~0 and std ~1 so models sensitive to scale perform better. I did **not** scale `Price`/`LogPrice` or one-hot columns.

**Step 10 – Final checks & save**  
I verified data types, missing values (all zero), and summaries, then saved the final dataset to `data/processed/car_l3_clean_ready.csv`.
