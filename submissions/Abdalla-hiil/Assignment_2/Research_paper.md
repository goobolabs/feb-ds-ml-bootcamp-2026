## Research Paper: Digital Habits and Student Well-being

### 1. Title & Collection Method

**Title:** The Impact of Daily Screen Time on Student Focus and Mood.

**Collection Method:** I used the **Manual Logging** method. I asked 52 students to open the "Screen Time" setting on their smartphones. I recorded their total hours, their most used app category, and then asked them to rate their "Stress Level" at the end of the day.

### 2. Description of Features & Labels

* **Feature 1: Most_Used_App (X1):** The type of app used most (e.g., Social Media, Games, Study, Video).
* **Feature 2: Screen_Hours (X2):** Total hours spent on the phone per day (Numerical).
* **Feature 3: Notifications_Count (X3):** How many times the phone "pinged" or buzzed (Numerical).
* **Feature 4: Exercise_Mins (X4):** Minutes spent moving away from the screen (Numerical).
* **Label (y): Stress_Level:** A category showing if the student feels **Low**, **Medium**, or **High** stress (The result we want to predict).

### 3. Dataset Structure

* **Rows:** 52
* **Columns:** 4 Features + 1 Label.

**Sample Table (First 10 Rows):**

| ID | Top_App | Screen_Hrs | Notifications | Exercise | Stress_Level (y) |
| --- | --- | --- | --- | --- | --- |
| 1 | Social Media | 6 | 120 | 30 | High |
| 2 | Study | 2 | 45 | 60 | Low |
| 3 | Games | 5 | 200 | 15 | High |
| 4 | **Socal Media** | 7 | 150 | 10 | High |
| 5 | Video | **?** | 80 | 45 | Medium |
| 6 | Study | 3 | 30 | **Zero** | Low |
| 7 | Games | 4 | 300 | 20 | High |
| 8 | Social Media | 8 | 180 | 0 | High |
| 9 | Video | 5 | 90 | 40 | **Missing** |
| 10 | Study | 1 | 20 | 90 | Low |

---

### 4. Quality Issues (The "Messy" Data)

* **Typos:** Row 4 says "Socal Media" (spelled wrong).
* **Missing Values:** Row 5 has a "?" for hours, and Row 9 is missing the stress result.
* **Mixed Formats:** Row 6 has "Zero" written as a word instead of "0".
* **Outliers:** Row 7 has 300 notifications, which is very high and might be a mistake or a very busy day.

### 5. Use Case

This is a **Classification** project. We want the computer to learn how digital habits affect our feelings. For example: "If screen time is over 6 hours and exercise is under 20 minutes, the student is likely in the **High Stress** group."

---