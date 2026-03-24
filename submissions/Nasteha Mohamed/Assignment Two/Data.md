# 1 a Short Research Paper

### Title & Collection Method
### Title:Daily Weather Observations Dataset for My City.
### Collection Method:This dataset is about daily weather observations, collected manually from local weather reports over January 2026. Each day includes measurements of temperature, humidity, wind speed, cloud coverage, and rainfall.

### 2 Description of Features & Labels

### The dataset consists of 6 input features (X) and 1 output variable (y).

### Input Features (X):

### Date – The date of observation (2026-1-1 - 2026-2-1)

### Temperature (°C) – Daily average temperature

### Humidity (%) – Daily relative humidity

### WindSpeed (km/h) – Average wind speed

### CloudCoverage (%) – Estimated cloud coverage

### Rainfall (mm) – Daily rainfall amoun.

## Output Label (y):

- WeatherCondition – Describes the overall weather for the day: Sunny, Cloudy, or Rainy.

3. Dataset Structure

### Sample Table (First 10 Rows)

| Date       | Temperature | Humidity | WindSpeed | CloudCoverage | Rainfall | WeatherCondition |
|------------|------------|---------|-----------|---------------|----------|-----------------|
| 2026-01-01 | 25         | 45      | 12        | 20            | 0        | Sunny           |
| 2026-01-01 | 27         | 50      | 15        | 25            |          | Sunny           |
| 2026-01-02 | 23         | 55      | 10        | 30            | 0        | Sunny           |
| 2026-01-02 | 22         | 52      | 8         | 35            | 0        | Sunny           |
| 2026-01-03 | 20         | 60      | 7         | 40            | 2        | Rainy           |
| 2026-01-03 | 21         | 60      | 8         | 40            | 3        | Rainy           |
| 2026-01-04 | 19         | 65      | 5         | 50            | 4        | Rainy           |
| 2026-01-04 |            | 68      | 6         | 55            | 5        | Rainy           |
| 2026-01-05 | 24         | 48      | 11        | 22            | 0        | Sunny           |
| 2026-01-05 | 26         | 50      | 13        | 28            | 0        | Sunny           


## 4. Quality Issues

1. **Missing values** – Some temperature, humidity, and rainfall entries are empty.  
2. **Inconsistent formatting** – Extra spaces in numeric fields (e.g., `" 49"`).  
3. **Duplicates** – Some dates have repeated entries.  
4. **Typos / irregular entries** –  Blank cells or incorrect formatting in the dataset.  
5. **Class imbalance** – There are more `Sunny` days than `Rainy` days.

## 5 **Use Case:**
### Classification
- Predict **WeatherCondition** (`Sunny`, `Cloudy`, `Rainy`) based on other features.

### Regression
- Predict **Rainfall** or **Temperature** from other features using:  

### Clustering
### Group days with similar weather patterns based on numeric features like temperature, humidity, and wind speed.  

### In this dataset i prefer clustering for grouping days with similar weather patterns based on numeric features like temperature, humidity, and wind speed.