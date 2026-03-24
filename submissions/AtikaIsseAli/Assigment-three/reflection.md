# Reflection: Data Preprocessing for Car Prices

### 1. Handling Missing Values
- **Odometer_km (Median)**: I used the median because mileage data is often skewed by extreme outliers, and the median is more "robust" than the mean.
- **Doors/Accidents/Location (Mode)**: These are categorical or discrete counts. I used the mode (the most common value) to ensure the imputed data stayed realistic.

### 2. Outlier Management
- I used **IQR Capping** for Price and Odometer. This prevents extreme "noise" from ruining the model while keeping all 52 rows of data intact.

### 3. Feature Engineering Decisions
- **CarAge**: Vital for calculating depreciation.
- **Km_per_year**: This helps distinguish between a car that is old but rarely driven versus a new car driven heavily.
- **LogPrice**: This alternative target was created to reduce price skewness.

### 4. Scaling
- I used **StandardScaler** to ensure features like Odometer (large numbers) and Doors (small numbers) are treated with equal importance by the model.