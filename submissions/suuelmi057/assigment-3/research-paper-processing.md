# Assignment 3: Student Habits Data Processing

## 1️⃣ Original Dataset
File: `Student_Habits_and_Academic_Success.csv`  
- 50 rows, 5 features + 1 label
- Features: Major, Sleep_Hrs, Coffee_Cups, Study_Hrs
- Label: Grade

## 2️⃣ Cleaning & Processing
1. **Fix typos:** "Engineeing" → "Engineering"  
2. **Convert words to numbers:** "six" → 6  
3. **Handle missing values:** Sleep_Hrs & Grade filled with median  
4. **Outliers:** Coffee_Cups > 10 capped at 10  

## 3️⃣ Feature Engineering
- Sleep_Category (Low, Medium, High)  
- Coffee_per_StudyHr = Coffee_Cups / Study_Hrs  
- One-hot encode Sleep_Category  
- Scaled numeric features: Sleep_Hrs, Coffee_Cups, Study_Hrs, Coffee_per_StudyHr

## 4️⃣ Final Output
- Processed dataset saved as `Student_Habits_Processed.csv`
- Ready for machine learning / regression analysis
