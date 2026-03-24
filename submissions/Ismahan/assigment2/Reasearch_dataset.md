# Research Paper: Lifestyle and Sleep Quality Analysis

## 1. Title & Collection Method

**Title:** The Impact of Social Media Usage and Exercise on Sleep Duration  

**Collection Method:**  
This dataset was collected using an online Survey Questionnaire (likely Google Forms). The data captures personal habits, including age, digital consumption, physical activity, and sleep patterns. The respondents appear to be a diverse group, primarily young adults and students, given the high prevalence of TikTok usage.

---

## 2. Description of Features & Labels

To analyze the relationship between lifestyle and sleep, the variables are defined as follows:

### Features (X):

- **Age:** The respondent's age in years (Numerical).
- **Primary Social Media App:** The main platform used by the respondent (Categorical).
- **Daily Screen Time (Hours):** Time spent on digital devices (Numerical).
- **How many days do you exercise per week?:** Physical activity frequency (Categorical/Ordinal).

### Label (y):

- **How many hours did you sleep last night?:** The target variable representing sleep quantity (Numerical).

---

## 3. Dataset Structure

The dataset contains **51 rows and 7 columns**. Below is a sample of the first 5 rows:

| No | Timestamp | Age | Primary Social Media App | Daily Screen Time | Exercise Frequency | Sleep Hours |
|----|-----------|-----|------------------------|-------------------|--------------------|-------------|
| 1 | 2026-02-06 16:07:44 | 27.0 | TikTok | 7.0 | 0 | 5 |
| 2 | 2026-02-06 16:12:36 | 26.0 | TikTok | 3.0 | NaN | 8 |
| 3 | 2026-02-06 16:14:41 | 33.0 | TikTok | 8.0 | 3-4 days | 6 |
| 4 | 2026-02-06 16:15:39 | 26.0 | WhatsApp | 12.0 | 5+ days | 7 |
| 5 | 2026-02-06 16:19:27 | NaN | YouTube | 5.0 | 0 | 6 |

---

## 4. Quality Issues

The dataset is "messy" and requires preprocessing before modeling:

- **Missing Values:**  
  There are missing values in Age (2), Daily Screen Time (4), and Exercise per week (3).

- **Inconsistent Naming:**  
  In the "Primary Social Media App" column, "YouTube" is recorded as both "YouTube" and "youtube" (case sensitivity issue).

- **Structural Issues:**  
  Column names contain leading/trailing spaces (e.g., `Primary Social Media App`), which can cause errors in coding.

- **Mixed Data Types:**  
  The Exercise column contains a mix of integers (0) and string ranges ("1-2 days"), requiring transformation into a consistent format.

---

## 5. Use Case

This dataset is well-suited for several Machine Learning tasks:

- **Regression:**  
  To predict the exact number of hours a person will sleep (y) based on their age, screen time, and exercise habits (X).

- **Classification:**  
  To categorize individuals into "Healthy Sleepers" (e.g., ≥7 hours) vs. "Sleep Deprived" (<7 hours) based on their lifestyle features.

- **Clustering:**  
  To identify distinct groups of users, such as "Heavy Social Media Users with Low Activity" vs. "Active Users with Moderate Screen Time."
