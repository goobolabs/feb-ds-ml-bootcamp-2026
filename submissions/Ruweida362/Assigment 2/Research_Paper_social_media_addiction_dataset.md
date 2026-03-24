# Predicting Social Media Addiction Based on Usage and Lifestyle

## 1. Title & Collection Method
**Title:** Predicting Social Media Addiction Based on Usage and Lifestyle

**Collection Method:**
The dataset was collected through surveys from 46 participants. Participants provided self-reported information about their social media usage, lifestyle habits, and experiences with social media addiction.

## 2. Description of Features & Labels

| Feature | Description | Type |
|---------|-------------|------|
| `daily_social_media_hours` | Number of hours spent on social media daily (e.g., "1-2 hours", "3-4 hours", "more than 6 hours") | Categorical |
| `sleep_quality_level` | Self-reported quality of sleep (e.g., "Poor", "Good", "Very good") | Categorical |
| `social_media_before_sleep` | Frequency of using social media before sleep (e.g., "Rarely", "Sometimes", "Often") | Categorical |
| `study_work_distraction_level` | Level of distraction during study/work due to social media (e.g., "Sometimes", "Often", "Always") | Categorical |
| `social_media_addiction` | Target label indicating if the participant is addicted to social media (Yes/No) | Categorical |

## 3. Dataset Structure
- **Number of Entries:** 46 participants  
- **Number of Features:** 4 Features + 1  label(target)  
- **Data Type:** All features are categorical, based on self-reported ranges or levels  

**Example Entries (10 samples):**

| daily_social_media_hours | sleep_quality_level | social_media_before_sleep | study_work_distraction_level | social_media_addiction |
|--------------------------|-------------------|---------------------------|-----------------------------|-----------------------|
| 3-4 hours                | Good              | Sometimes                 | Sometimes                   | Yes                   |
| 3-4 hours                | Good              | Rarely                    | Often                       | Yes                   |
| 5-6 hours                | Poor              | Often                     | Always                      | Yes                   |
| 1-2 hours                | Very good         | Rarely                    | Sometimes                   | No                    |
| 3-4 hours                | Good              | Rarely                    | Sometimes                   | Yes                   |
| more than 6 hours        | Poor              | Often                     | Always                      | Yes                   |
| 1-2 hours                | Very good         | Rarely                    | Rarely                      | No                    |
| 5-6 hours                | Poor              | Often                     | Often                       | Yes                   |
| 3-4 hours                | Good              | Sometimes                 | Sometimes                   | Yes                   |
| 1-2 hours                | Very good         | Rarely                    | Rarely                      | No                    |

## 4. Quality Issues

1. Duplicate Responses:
Some participants may have filled out the survey more than once, which can lead to duplicated data and bias the overall results.

2. Inconsistent Response Formatting:
In the daily_social_media_hours feature, similar responses may be written in different formats (e.g., “1–2 hours” vs. “1-2”), causing inconsistency during data collection and requiring additional cleaning.

3. Skipped Questions (Missing Responses):
Some participants may skip certain questions, resulting in incomplete records and potential loss of valuable information.

