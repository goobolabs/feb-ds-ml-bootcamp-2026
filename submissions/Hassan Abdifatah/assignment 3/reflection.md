# Lesson 3 Reflection: Data Preprocessing for Car Pricing

### 1. Choice of Imputation Methods
For this assignment, I chose different statistical strategies based on the nature of the data:
- **Odometer_km (Median):** I used the median to fill missing values because the odometer readings showed high variance and outliers. The median is robust and prevents extreme values from skewing the average.
- **Doors & Accidents (Mode):** These are discrete/count features. Since a car typically has a standard number of doors (e.g., 2 or 4), the mode (most frequent value) is the most realistic replacement.
- **Location (Mode):** For categorical missing data, the mode was used to assign the most frequent geographic classification (City, Suburb, or Rural).

### 2. Outlier Handling (IQR Capping)
To handle outliers in `Price` and `Odometer_km`, I implemented **IQR Capping**. 
- I calculated the bounds using $[Q1 - 1.5 \times IQR]$ and $[Q3 + 1.5 \times IQR]$.
- Instead of deleting the rows, I **clipped** the values. This keeps the data points in the model but limits their influence, ensuring extreme values do not lead to an overfitted or biased machine learning model.

### 3. Feature Engineering
I created four new features to improve the predictive power of the dataset:
- **CarAge:** Calculated as `2026 - Year`. This is essential because the age of a car is a primary driver of its market value.
- **Km_per_year:** This represents the intensity of use. A high mileage on a young car indicates heavy wear.
- **Is_Urban:** A binary feature derived from the 'City' location to specifically highlight urban driving conditions.
- **LogPrice:** Since the target `Price` was highly skewed (skewness > 7), I added `LogPrice` using `np.log1p`. This normalizes the target distribution, which is a requirement for many regression algorithms.

### 4. Feature Scaling
I applied **StandardScaler** to the continuous input features (X). 
- **Reasoning:** Standardization ensures that features with large ranges (like Odometer) do not dominate features with small ranges (like Doors). 
- **Exclusions:** I intentionally did **not** scale the target (`Price` and `LogPrice`) or the binary dummy columns (0/1) to maintain their logical interpretability.

### 5. Categorical Encoding
I used **One-Hot Encoding** for the `Location` column. This converted the text categories into three separate binary columns (`Loc_City`, `Loc_Rural`, `Loc_Suburb`). This is necessary because machine learning models require numerical input to perform calculations.
