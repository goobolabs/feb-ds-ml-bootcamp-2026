# 📄 Research Paper: Daily Weather Observations Analysis

**Author:** Maxamed Abdulle  
**Assignment 2:** Practical Data Foundations for Machine Learning  
**Date:** February 7/2/ 2026

---

## 1. Title & Collection Method
* **Project Title:** Daily Weather Observations Dataset for My City.
* **Collection Method:** This dataset was compiled through **Manual Observations** and logging.
* **Process:** The data was recorded daily throughout January 2026, sourcing measurements from local weather reports to track atmospheric changes over time.

---

## 2. Description of Features & Labels
The dataset is structured into input features (X) and a target classification label (y) to facilitate Machine Learning training.

### **Input Features (X):**
* **Date:** The specific day of observation (ranging from 2026-01-01 to 2026-02-01).
* **Temperature (°C):** The daily average thermal measurement.
* **Humidity (%):** The relative moisture content in the air.
* **WindSpeed (km/h):** The average velocity of air movement.
* **CloudCoverage (%):** The estimated percentage of the sky covered by clouds.
* **Rainfall (mm):** The total daily precipitation recorded.

### **Output Label (y):**
* **WeatherCondition:** A categorical label describing the overall day as **Sunny**, **Cloudy**, or **Rainy**.



---

## 3. Dataset Structure
* **Total Rows:** 50 Samples (Minimum requirement).
* **Total Columns:** 6 Features + 1 Label.

### **Sample Table (First 10 Rows)**
| Date | Temp (°C) | Humidity | Wind (km/h) | Clouds | Rain (mm) | Condition ($y$) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 2026-01-01 | 25 | 45 | 12 | 20 | 0 | Sunny |
| 2026-01-01 | 27 | 50 | 15 | 25 | *(null)* | Sunny |
| 2026-01-02 | 23 | 55 | 10 | 30 | 0 | Sunny |
| 2026-01-02 | 22 | 52 | 8 | 35 | 0 | Sunny |
| 2026-01-03 | 20 | 60 | 7 | 40 | 2 | Rainy |
| 2026-01-03 | 21 | 60 | 8 | 40 | 3 | Rainy |
| 2026-01-04 | 19 | 65 | 5 | 50 | 4 | Rainy |
| 2026-01-04 | *(null)* | 68 | 6 | 55 | 5 | Rainy |
| 2026-01-05 | 24 | 48 | 11 | 22 | 0 | Sunny |
| 2026-01-05 | 26 | 50 | 13 | 28 | 0 | Sunny |

---

## 4. Quality Issues (Data Challenges)
The dataset contains real-world "messy" data characteristics that require preprocessing:
1.  **Missing Values:** Certain entries for temperature and rainfall are incomplete.
2.  **Inconsistent Formatting:** Some numerical fields contain extra spaces (e.g., `" 45"`).
3.  **Duplicates:** Multiple data entries exist for the same dates, representing repeated measurements.
4.  **Categorical Data:** The `WeatherCondition` label is in text format and requires numerical encoding.
5.  **Class Imbalance:** There is a higher frequency of "Sunny" labels compared to "Rainy" ones.

---

## 5. Machine Learning Use Cases
This dataset is versatile for various ML tasks, specifically:

* **Primary Use (Clustering):** Grouping days with similar weather patterns based on numeric features like temperature, humidity, and wind speed to find hidden groupings.
* **Classification:** Predicting the `WeatherCondition` category based on atmospheric input features.
* **Regression:** Estimating the exact `Rainfall` amount using other numerical variables.

---