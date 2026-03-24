# Reflection on Lesson 3 – Data Preprocessing

In this assignment, I worked on preparing a car price dataset so it could be used for machine learning. The raw data had several issues including formatting problems, missing values, duplicates, and outliers. My main goal was to clean the data while keeping it realistic and useful for modeling.

## Handling Missing Values

For the Odometer_km column, I filled missing values using the median. I chose the median because odometer values are often skewed and may contain extreme values, so the median gives a more reliable central value than the mean. Accidents had no missing values in the dataset, so it did not require imputation. For Doors and Location, I used the mode. Even though Doors is numeric, it represents fixed options (such as 2 or 4 doors), so treating it like a categorical feature makes sense. Using the most common value helps keep the data consistent. I also corrected category errors in Location like “Subrb” and “??” before filling missing values to avoid creating incorrect categories.

## Outlier Treatment

To reduce the effect of extreme values in Price and Odometer_km, I applied IQR-based capping. This method limits values outside 1.5 times the interquartile range without removing rows. It helps control outliers while preserving all observations in the dataset.

## Feature Engineering

I created several new features to make the dataset more informative. Car Age was calculated as the difference between the current year and the car’s year. Kilometers per year gave an idea of how much each car was driven annually. Price per km and log of the price were added to make features more suitable for modeling. I also calculated accident rate as accidents divided by car age, and added binary flags for old cars (older than 15 years) and urban location. These new features can help identify trends and patterns in the data and provide useful inputs for machine learning algorithms.

## One-Hot Encoding and Scaling

I converted the categorical Location column into one-hot encoded columns for City, Suburb, and Rural areas. Numeric columns (except target columns like Price) were scaled using StandardScaler. This ensures that all features are on a comparable scale, which is important for many machine learning algorithms.

## Learning Points

Through this process, I learned the importance of careful data cleaning and preprocessing. Handling missing values, duplicates, outliers, and incorrect categories is essential to produce reliable results. Feature engineering and scaling can improve model performance and make the dataset more informative. I also realized that spending time understanding the data before modeling is crucial. Overall, this assignment gave me practical experience in preparing real-world data for analysis and predictive modeling.