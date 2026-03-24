# A Study on Daily Habits and Productivity Using a Self-Collected Dataset

## 1. Introduction and Dataset Collection Method

The purpose of this research is to study how daily habits such as sleep, work or study hours, coffee consumption, and exercise relate to a person’s productivity level. Instead of using an existing dataset from online sources, this dataset was collected manually as part of a Machine Learning assignment.

The data was collected through a small informal survey. Participants included friends, classmates, and young professionals. Each participant was asked a set of simple questions about their daily routine and their self-perceived productivity level. The responses were recorded manually. This approach ensured that the dataset is original and suitable for learning data preprocessing and machine learning concepts.

---

## 2. Description of Features and Label

The dataset contains both numerical and categorical variables.

### Input Features (X)

The input variables (features) used in this dataset are:

- **Age**: The age of the participant (numerical)
- **Gender**: Gender of the participant (categorical: Male/Female)
- **Sleep_Hours**: Average number of hours slept per day (numerical)
- **Study_Work_Hours**: Number of hours spent studying or working daily (numerical)
- **Coffee_Cups**: Number of coffee cups consumed per day (numerical)
- **Exercise**: Whether the participant exercises regularly (categorical: Yes/No)

### Output Variable (y)

- **Productivity_Level**: Self-reported productivity level of the participant  
  (categorical: Low, Medium, High)

This variable can be used as the target label in a machine learning model.

---

## 3. Dataset Structure

The dataset has the following structure:

- **Number of rows:** 50  
- **Number of columns:** 7  

Below is a small sample of the dataset (first 8 rows):

| Age | Gender | Sleep_Hours | Study_Work_Hours | Coffee_Cups | Exercise | Productivity_Level |
|----:|--------|------------:|-----------------:|------------:|----------|--------------------|
| 21 | Male | 6 | 7 | 2 | Yes | Medium |
| 22 | Female | 7 | 6 | 1 | No | Medium |
| 20 | Male | 5 | 8 | 3 | No | Low |
| 23 | Female | 8 | 5 | 0 | Yes | High |
| 24 | Male | 6 | 9 | 2 | Yes | High |
| 21 | Female | 7 | 6 | 1 | Yes | Medium |
| 22 | Male | 4 | 10 | 4 | No | Low |
| 25 | Female | 8 | 7 | 1 | Yes | High |

---

## 4. Data Quality Issues

Since the dataset was collected manually, several quality issues are present:

- **Missing values**: Some entries in the `Exercise` column are missing.
- **Categorical data**: Variables such as Gender, Exercise, and Productivity_Level need to be encoded before modeling.
- **Possible imbalance**: The number of samples in each productivity category (Low, Medium, High) may not be perfectly balanced.
- **Self-reported bias**: Productivity levels are subjective and may vary based on personal perception.
- **Small dataset size**: With only 50 records, the dataset is mainly suitable for learning and experimentation rather than large-scale prediction.

These issues make the dataset useful for practicing data cleaning and preprocessing techniques.

---

## 5. Potential Use Cases in Machine Learning

This dataset can be used in several machine learning tasks:

### Classification
The dataset can be used as a **classification problem**, where the goal is to predict the `Productivity_Level` (Low, Medium, or High) based on daily habits.

### Regression
By converting productivity into numerical values (e.g., Low = 1, Medium = 2, High = 3), the dataset can also be explored as a **regression problem**.

### Clustering
The dataset can be used for **unsupervised learning**, such as clustering individuals based on similar daily habits without using productivity labels.

---

## 6. Conclusion

This research presented a self-collected dataset focused on daily habits and productivity. Despite being small and imperfect, the dataset is well-suited for learning fundamental machine learning concepts such as data preprocessing, feature encoding, handling missing values, and basic model training. The dataset demonstrates how real-world data often contains noise and inconsistencies that must be addressed before building effective machine learning models.
