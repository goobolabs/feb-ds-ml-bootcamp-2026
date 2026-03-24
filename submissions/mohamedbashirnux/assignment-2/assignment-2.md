# Research Paper: Student Daily Commute Dataset

**Student:** Mohamed Bashir  
**Date:** February 5, 2026  
**Course:** Data Science & Machine Learning Bootcamp

---

## 1. Title & Collection Method

**Dataset Title:** Student Daily Commute Time Prediction Dataset

**Collection Method:**

This dataset was collected through direct observation and survey of university students over a period of two weeks. Data was gathered by recording daily commute information from 50 different student trips to campus. The collection process involved:

- Asking students about their transportation mode and departure time
- Recording weather conditions on each day
- Measuring approximate distance from home to campus
- Observing traffic conditions during commute hours
- Recording actual travel time in minutes

The data represents real commuting patterns during typical weekdays (Monday to Friday) in February 2026.

---

## 2. Description of Features & Labels

### Features (Input Variables - X):

1. **Transportation_Mode** (Categorical)
   - Type: Nominal categorical variable
   - Values: Private Car, Bus, Walking, Motorbike
   - Description: The mode of transportation used by the student

2. **Departure_Time** (Categorical/Time)
   - Type: Ordinal categorical variable
   - Values: 7:00, 7:15, 7:30, 7:45, 8:00, 8:15
   - Description: Time when student leaves home (24-hour format)

3. **Traffic_Level** (Categorical)
   - Type: Ordinal categorical variable
   - Values: Low, Medium, High
   - Description: Traffic congestion level during commute

4. **Distance_km** (Numerical)
   - Type: Continuous numerical variable
   - Range: 1.0 to 12.0 kilometers
   - Description: Distance from home to campus in kilometers

5. **Weather** (Categorical)
   - Type: Nominal categorical variable
   - Values: Sunny, Rainy, Cloudy
   - Description: Weather condition during the commute

### Label (Output Variable - y):

**Travel_Time_Minutes** (Numerical)
- Type: Continuous numerical variable (target variable)
- Range: 11 to 45 minutes
- Description: Actual time taken to reach campus in minutes

---

## 3. Dataset Structure

### Overview:
- **Total Samples (Rows):** 50
- **Total Features (Columns):** 5 input features + 1 target label = 6 columns
- **Data Format:** CSV (Comma-Separated Values)
- **File Size:** Approximately 2 KB

### Sample Data (First 10 Rows):

| Transportation_Mode | Departure_Time | Traffic_Level | Distance_km | Weather | Travel_Time_Minutes |
|---------------------|----------------|---------------|-------------|---------|---------------------|
| Private Car         | 7:00           | High          | 5           | Sunny   | 25                  |
| Bus                 | 7:30           | High          | 8           | Rainy   | 35                  |
| Walking             | 7:45           | Low           | 2           | Sunny   | 20                  |
| Motorbike           | 8:00           | Medium        | 6           | Cloudy  | 15                  |
| Private Car         | 7:15           | Medium        | 7           | Sunny   | 20                  |
| Bus                 | 7:00           | Low           | 10          | Sunny   | 25                  |
| Walking             | 8:00           | Low           | 1.5         | Cloudy  | 15                  |
| Motorbike           | 7:30           | High          | 8           | Rainy   | 22                  |
| Private Car         | 7:45           | High          | 6           | Rainy   | 30                  |
| Bus                 | 8:15           | Medium        | 9           | Sunny   | 28                  |

---

## 4. Quality Issues

### Identified Problems:

1. **Limited Sample Size**
   - Current dataset has 50 samples, which may not be sufficient for complex machine learning models
   - Recommendation: Collect more data (ideally 200-500 samples) for better model generalization

2. **Categorical Variables**
   - Three features (Transportation_Mode, Traffic_Level, Weather) are categorical text
   - Issue: Machine learning algorithms require numerical input
   - Solution needed: Apply encoding techniques (Label Encoding or One-Hot Encoding)

3. **Feature Scaling Required**
   - Distance_km ranges from 1-12, while Travel_Time_Minutes ranges from 11-45
   - Different scales may cause some algorithms to give unequal weight to features
   - Solution needed: Apply normalization or standardization

4. **Potential Missing Values**
   - While current dataset is complete, real-world collection might have missing entries
   - Future consideration: Implement imputation strategies for missing data

5. **Class Imbalance (Transportation Mode)**
   - Distribution may not be perfectly balanced across all transportation types
   - Some modes might be overrepresented compared to others
   - Impact: Model might be biased toward more frequent transportation modes

6. **Time Format Inconsistency**
   - Departure_Time is stored as text (e.g., "7:00") rather than proper time format
   - Solution needed: Convert to numerical representation (minutes since midnight) or encode categorically

7. **Weather Subjectivity**
   - Weather categories (Sunny, Rainy, Cloudy) are somewhat subjective
   - More precise measurements (temperature, precipitation level) would be better

---

## 5. Machine Learning Use Case

### Problem Type: Regression

This dataset is suitable for a **supervised learning regression** problem, where the goal is to predict continuous numerical values (travel time in minutes).

### Prediction Task:

**Objective:** Predict how long a student's commute will take based on their transportation mode, departure time, traffic conditions, distance, and weather.

**Input:** Transportation mode, departure time, traffic level, distance, weather  
**Output:** Predicted travel time in minutes

### Potential Applications:

1. **Smart Commute Planning**
   - Students can input their planned departure time and transportation mode
   - System predicts expected travel time
   - Helps students decide when to leave home to arrive on time

2. **Transportation Optimization**
   - University can analyze which transportation modes are most efficient
   - Identify peak traffic times and suggest alternative departure times
   - Plan better bus schedules based on predicted demand

3. **Route Recommendation**
   - Compare predicted times for different transportation modes
   - Suggest optimal mode based on weather and traffic conditions
   - Help students make informed decisions

### Suitable Machine Learning Algorithms:

1. **Linear Regression** - Simple baseline model
2. **Decision Tree Regression** - Can handle categorical features well
3. **Random Forest Regression** - More robust, handles non-linear relationships
4. **Gradient Boosting (XGBoost)** - High accuracy for tabular data
5. **K-Nearest Neighbors (KNN)** - Good for pattern-based predictions

### Expected Preprocessing Steps (Lesson 3):

1. Handle any missing values (if they exist)
2. Encode categorical variables (Transportation_Mode, Traffic_Level, Weather, Departure_Time)
3. Scale numerical features (Distance_km)
4. Feature engineering: Create new features like "is_rush_hour" or "is_bad_weather"
5. Split data into training and testing sets (80-20 or 70-30)

---

## Conclusion

This Student Daily Commute dataset provides a practical foundation for learning data preprocessing and machine learning regression techniques. While it contains quality issues typical of real-world data (categorical variables, scaling needs, limited size), these challenges make it an excellent educational resource for understanding the complete machine learning pipeline from data collection to model deployment.

The dataset demonstrates clear relationships between input features and travel time, making it suitable for predictive modeling. In Lesson 3, we will apply preprocessing techniques to prepare this data for machine learning algorithms.

---

**Dataset File:** `student_commute_dataset.csv`  
**Total Samples:** 50  
**Total Features:** 5 (+ 1 target label)  
**Problem Type:** Supervised Learning - Regression

---
