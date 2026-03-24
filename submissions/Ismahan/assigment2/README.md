# Lifestyle and Sleep Quality Analysis

## Research Paper Dataset

### Title
**The Impact of Social Media Usage and Exercise on Sleep Duration**

---

## 1. Data Collection Method

This dataset was collected using an **online survey questionnaire** (likely Google Forms).  
It captures respondents’ lifestyle habits, including:

- Age  
- Social media usage  
- Daily screen time  
- Exercise frequency  
- Sleep duration  

The participants appear to be a **diverse group**, primarily **young adults and students**, as indicated by the high usage of platforms such as **TikTok** and **YouTube**.

---

## 2. Features and Label Description

The goal of this dataset is to analyze the relationship between **lifestyle habits and sleep quality**.

### Features (X)
| Feature | Description | Type |
|------|-----------|------|
| Age | Respondent's age in years | Numerical |
| Primary Social Media App | Main social media platform used | Categorical |
| Daily Screen Time (Hours) | Time spent on digital devices per day | Numerical |
| Exercise Frequency | Number of days exercised per week | Categorical / Ordinal |

### Label (y)
| Label | Description | Type |
|----|-----------|----|
| Sleep Hours | Number of hours slept the previous night | Numerical |

---

## 3. Dataset Structure

- **Rows:** 51  
- **Columns:** 7  

### Sample Data (First 5 Rows)

| No | Timestamp | Age | Primary Social Media App | Daily Screen Time | Exercise Frequency | Sleep Hours |
|----|---------|-----|-----------------|------------------|------------------|-----------|
| 1 | 2026-02-06 16:07:44 | 27.0 | TikTok | 7.0 | 0 | 5 |
| 2 | 2026-02-06 16:12:36 | 26.0 | TikTok | 3.0 | NaN | 8 |
| 3 | 2026-02-06 16:14:41 | 33.0 | TikTok | 8.0 | 3-4 days | 6 |
| 4 | 2026-02-06 16:15:39 | 26.0 | WhatsApp | 12.0 | 5+ days | 7 |
| 5 | 2026-02-06 16:19:27 | NaN | YouTube | 5.0 | 0 | 6 |

---

## 4. Data Quality Issues

The dataset requires **preprocessing** before analysis or modeling:

### Identified Problems
- **Missing Values**
  - Age: 2 missing values  
  - Daily Screen Time: 4 missing values  
  - Exercise Frequency: 3 missing values  

- **Inconsistent Categorical Values**
  - `"YouTube"` vs `"youtube"` (case sensitivity issue)

- **Column Naming Issues**
  - Extra spaces in column names (e.g. `" Primary Social Media App "`)

- **Mixed Data Types**
  - Exercise frequency contains both numeric values (`0`) and text ranges (`"1-2 days"`, `"3-4 days"`)

### Required Preprocessing
- Handle missing values (imputation or removal)
- Normalize categorical values
- Clean column names
- Encode exercise frequency into numerical format

---

## 5. Potential Use Cases

This dataset is suitable for multiple **Machine Learning** and **Data Analysis** tasks:

### Regression
Predict the **exact number of sleep hours** based on:
- Age  
- Screen time  
- Exercise frequency  
- Social media usage  

### Classification
Classify users into:
- **Healthy Sleepers** (≥ 7 hours)
- **Sleep Deprived** (< 7 hours)

### Clustering
Identify user patterns such as:
- Heavy social media users with low physical activity  
- Active users with moderate screen time  
- High screen time and poor sleep groups  

---

## 6. Technologies Suggested
- Python  
- Pandas & NumPy  
- Matplotlib / Seaborn  
- Scikit-Learn  

---

## 7. Research Objective

To understand how **digital consumption and exercise habits** influence **sleep duration**, and to provide insights that can support healthier lifestyle choices.

---

📌 *This dataset is ideal for academic research, ML practice, and data preprocessing demonstrations.*
