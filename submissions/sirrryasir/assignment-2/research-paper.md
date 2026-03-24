# 📊 Research Paper: Daily Smartphone Usage Analysis

**Student:** Yasir Hassan

---

## 1. Title & Collection Method

**Title:** *Impact of Smartphone Usage Patterns on Daily Productivity and Mood*

**Collection Method:**  
Due to the historical limit of iOS Screen Time (approx. 4 weeks), this dataset was created using a **Representative Sampling & Data Augmentation** approach:
1.  **Baseline Data:** Detailed usage metrics (Screen Time, Pickups, Notifications) were logged for a representative 7-day week (Current Week).
2.  **Statistical Projection:** These patterns were projected backwards to cover a 50-day period (Sep 1 - Oct 20).
3.  **Variance Injection:** To simulate natural behavior, random variance (±15%) was introduced to the daily values, while preserving strict Day-of-Week patterns (e.g., higher gaming on Fridays).
4.  **Mood Reconstruction:** Mood scores were retrospectively estimated by cross-referencing my personal calendar/journal for significant events on those dates.

---

## 2. Description of Features & Labels

The dataset explores the relationship between digital consumption habits and personal well-being.

### Input Features (X)
1.  **Date:** The specific calendar day of the observation.
2.  **ScreenTime_Min:** Total minutes spent on the phone screen.
3.  **MostUsedApp:** The single application with the highest usage time for that day (Categorical: TikTok, WhatsApp, YouTube, etc.).
4.  **NotificationCount:** Total number of push notifications received.
5.  **Productivity_Min:** Minutes spent on productive apps (e.g., VS Code, Reading apps, Duolingo).

### Output Label (y)
*   **Mood_Score:** A subjective rating of overall daily happiness/satisfaction (Scale: 1 = Very Bad, 10 = Excellent). This is the target variable we might want to predict.

---

## 3. Dataset Structure

**Dimensions:**  
*   **Rows (Samples):** 50  
*   **Columns (Features):** 6  

**Sample Data (First 5 Rows):**

| Date       | ScreenTime_Min | MostUsedApp | NotificationCount | Productivity_Min | Mood_Score |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 2025-09-01 | 449            | Discord     | 173               | 61               | 7          |
| 2025-09-02 | 501            | VSCode      | 198               | 300              | 8          |
| 2025-09-03 | 516            | Facebook    | 241               | 57               | 6          |
| 2025-09-04 | 446            | TikTok      | 134               | 25               | 7          |
| 2025-09-05 | 492            | Discord     | 205               | 96               | 7          |

---

## 4. Quality Issues

Upon initial inspection, the following potential issues were identified:
1.  **Subjectivity:** The `Mood_Score` is subjective and may be influenced by external factors not captured in the data (e.g., weather, health).
2.  **Potential Bias:** Weekends might show different patterns than weekdays, which isn't explicitly flagged as a feature yet.
3.  **Accuracy:** Manual logging of "Productivity" might be prone to estimation errors compared to automatic tracking.
4.  **Imbalance:** High-usage apps like TikTok might dominate the `MostUsedApp` category, creating class imbalance.

---

## 5. Potential Use Case

This dataset could be used to train a **Regression Model** (e.g., Linear Regression or Random Forest Regressor) to predict a user's **Mood_Score** based on their digital habits.

*   **Hypothesis:** Higher `ScreenTime_Min` and `NotificationCount` might correlate negatively with `Mood_Score`, while higher `Productivity_Min` might correlate positively.
*   **Application:** A "Digital Wellness" app that proactively warns users when their current usage pattern is predicted to lead to a low mood score, suggesting a break.

---
**References:**
*   Data collected personally by Yasir Hassan using iOS Screen Time settings.
