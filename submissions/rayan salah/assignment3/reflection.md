# Reflection: Car Data Preprocessing Decisions

## 1. Dataset Overview
The dataset contains car price information with 150 rows and 6 columns: Price, Odometer_km, Doors, Accidents, Location, and Year. Initial inspection revealed several data quality issues including mixed data formats, missing values, typos, outliers, and duplicates.

## 2. Imputation Strategy

### 2.1 Odometer_km → Median
- **Reason**: Odometer readings showed a skewed distribution with potential outliers
- **Justification**: Median is robust to extreme values and better represents central tendency for skewed data
- **Alternative considered**: Mean was rejected due to sensitivity to outliers

### 2.2 Doors → Mode
- **Reason**: Doors is a categorical-like feature with limited values (2, 3, 4, 5)
- **Justification**: Most cars have 4 doors, making mode the most representative value
- **Result**: Missing doors were replaced with 4 (the most frequent value)

### 2.3 Location → Mode
- **Reason**: Location is a categorical variable
- **Justification**: "City" was the most frequent location (approximately 40% of cars)
- **Note**: This maintains dataset consistency while being statistically appropriate

## 3. Outlier Handling: IQR Capping

### 3.1 Why IQR Capping?
- **Data preservation**: Unlike removal, capping retains all observations
- **Statistical robustness**: Less sensitive to extreme values than z-score methods
- **Practical application**: Cars with extreme prices/odometer are adjusted to reasonable bounds
- **Model stability**: Prevents outliers from dominating linear models

### 3.2 Implementation Details
- Lower bound = Q1 - 1.5 × IQR
- Upper bound = Q3 + 1.5 × IQR
- Price: Approximately 5% of values were capped
- Odometer: Approximately 3% of values were capped

## 4. Feature Engineering Choices

### 4.1 CarAge (Current Year - Year)
- **Purpose**: Age is more predictive than manufacturing year
- **No leakage**: Used fixed CURRENT_YEAR (2026) instead of current date
- **Business relevance**: Older cars typically have lower prices

### 4.2 Km_per_year (Odometer_km / CarAge)
- **Purpose**: Measures usage intensity rather than total mileage
- **Safe handling**: Added epsilon (1e-6) to prevent division by zero
- **Insight**: High km/year suggests heavy usage (e.g., taxi, rental)

### 4.3 Is_Urban (City or Suburb = 1, Rural = 0)
- **Purpose**: Captures urban/rural distinction affecting car prices
- **Simplification**: Reduces location complexity while preserving key information
- **Business logic**: Urban cars may have different depreciation patterns

### 4.4 LogPrice (log(Price + 1))
- **Purpose**: Alternative target variable for modeling
- **Why log transform?**: Reduces skewness in price distribution
- **Why +1?**: Prevents log(0) issues (though no zero prices existed)
- **Model benefit**: Makes multiplicative differences additive in log space

## 5. Feature Scaling Decisions

### 5.1 Scaled Features
- Continuous numerical features: Odometer_km, Year, CarAge, Km_per_year
- Count features: Doors, Accidents (treated as continuous for scaling)

### 5.2 Not Scaled
- **Price & LogPrice**: Target variables should not be scaled
- **Location dummies**: Binary variables (0/1) don't benefit from standardization
- **Is_Urban**: Already binary; scaling would lose interpretability

### 5.3 StandardScaler Choice
- Centers data around zero with unit variance
- Works well with distance-based algorithms
- Preserves relative distances between data points

## 6. Data Quality Issues Resolved

### 6.1 Major Issues Addressed
1. **Price formatting**: Mixed string/numeric with currency symbols
2. **Missing values**: ~17% of Odometer_km, ~7% of Doors, ~7% of Location
3. **Location typos**: "Subrb" → "Suburb", "??" → missing
4. **Outliers**: Extreme prices (up to $135,000) and odometer readings
5. **Duplicates**: Several identical records removed

### 6.2 Quality Checks Implemented
- Assertions for critical conditions
- Before/after comparisons for each transformation
- Statistical summaries at each processing stage

## 7. Reproducibility Measures

### 7.1 Version Control
- requirements.txt with exact package versions
- Deterministic imputation (median/mode always same)
- No random operations requiring seed setting

### 7.2 Pipeline Design
- Sequential, documented processing steps
- Checkpoints after each major transformation
- Original data preserved through copy operations

## 8. Conclusion
This preprocessing pipeline successfully transformed messy car data into a clean, analysis-ready format. The decisions balanced statistical rigor with practical considerations, ensuring the data is suitable for subsequent modeling while maintaining interpretability and reproducibility. Each step was justified based on data characteristics and intended use cases.
