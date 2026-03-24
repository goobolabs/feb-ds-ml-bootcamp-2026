# Data Foundations for Machine Learning – Practical Assignment

## Overview

This assignment focuses on understanding the importance of real-world data collection in Machine Learning. The goal is to experience how datasets are created, organized, and prepared before applying any machine learning algorithms.

Students are required to collect their own dataset rather than using existing public datasets. This ensures practical exposure to real data challenges such as missing values, categorical variables, and inconsistent formats.

---

## Dataset Description

The dataset used in this assignment is titled:

**“A Study on Sleep Habits and Daily Energy Levels”**

The data was collected through a survey distributed among university students. Participants provided information regarding their sleeping behavior and daily energy condition.

### Dataset Size

- Total Samples (Rows): 128  
- Total Columns: 7 main features + 1 label  
- Data Type: Survey-based (self-reported)

---

## Features and Label

### Input Variables (Features X)

- Age
- Sleep Duration
- Bedtime
- Screen Time Before Bed
- Sleep Quality
- Wake-up Time

### Output Variable (Label Y)

- Daily Energy Level (Energetic / Tired)

The objective is to use the features to predict the daily energy level of a student.

---

## Purpose of the Assignment

This practical task helps students:

- Understand real-world data collection
- Work with messy datasets
- Identify data quality issues
- Prepare data for machine learning preprocessing
- Recognize the relationship between features and labels

---

## Data Quality Observations

Since the dataset was collected manually, several issues exist:

- Presence of categorical text values
- One empty column
- Age stored as ranges instead of numeric values
- Target column positioned between features
- Possible class imbalance

These issues will be addressed in later lessons through data preprocessing techniques such as cleaning, encoding, and feature engineering.

---

## Potential Machine Learning Applications

This dataset can be used for:

- Classification: Predicting whether a student will feel energetic or tired
- Clustering: Grouping students based on sleep patterns
- Behavioral analysis of sleep habits

---

## Learning Outcome

By completing this assignment, students gain practical experience in:

- Dataset creation
- Feature identification
- Label selection
- Data inspection
- Preparing data for future machine learning workflows
