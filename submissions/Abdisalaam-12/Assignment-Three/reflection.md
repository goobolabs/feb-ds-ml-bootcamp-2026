**Reflection on Lesson 3 – Data Preprocessing**

In this assignment, I worked on preparing a car price dataset so it could be used for machine learning. The raw data had several issues including formatting problems, missing values, duplicates and outliers. My main goal was to clean the data while keeping it realistic and useful for modeling.

**Handling Missing Values**

For the Odometer_km column, I filled missing values using the median. I chose the median because odometer values are often skewed and may contain extreme values, so the median gives a more reliable central value than the mean.

 Accidents had no missing values in the dataset, so it did not require imputation . For Doors and Location, I used the mode. Even though Doors is numeric, it represents fixed options (such as 2 or 4 doors), so treating it like a categorical feature makes sense. Using the most common value helps keep the data consistent. I also corrected category errors in Location like “Subrb” and “??” before filling missing values to avoid creating incorrect categories.

**Outlier Treatment**

To reduce the effect of extreme values in Price and Odometer_km, I applied IQR-based capping. This method limits values outside 1.5 times the interquartile range without removing rows. It helps control outliers while preserving all observations in the dataset.

**Feature Engineering**

I created several new features to add more meaning to the data. These include Car_Age, which shows how old the car is, and km_per_year, which explains how heavily the car was used. I also added Price_per_km to relate cost to usage, and Accident_Rate to adjust accident counts based on car age. Binary features like Is_OldCar and Is_Urban were added to capture age and location effects. In addition, I applied a log transformation to price (LogPrice) to reduce skewness.

**Encoding, Scaling, and Final Steps**

I used one-hot encoding for the Location column so it could be used in machine learning models. Only continuous input features were scaled using StandardScaler. I did not scale Price, LogPrice, or dummy variables because scaling them is unnecessary and could reduce interpretability. I also removed duplicate rows to prevent biased results.
**Conclusion**

Overall, the preprocessing steps helped turn a raw and inconsistent dataset into a clean and structured one. Each decision—such as using median imputation, IQR capping, and meaningful feature engineering was based on the nature of the data and best practices.
 The final dataset is now ready for analysis and modeling.

