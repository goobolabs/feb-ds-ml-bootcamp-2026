# Predicting Wedding Costs Using Key Event Features

## 1. Title & Collection Method

**Title:** Predicting Wedding Costs Based on Event Features

**Collection Method:**  
This dataset was collected directly using **observations, manual logging, and surveys**. I created a **Google Form or KoboToolbox form** with the key questions and shared it with my friends. They filled out the forms based on weddings they had attended or organized, and the responses were collected automatically. This ensured that the data was authentic and diverse.

Data was gathered from the following sources:

- Number of guests (Number_of_Guests)  
- Type of wedding venue (Venue_Type)  
- Type of catering (Catering_Type)  
- Decoration level (Decoration_Level)  
- Wedding duration in hours (Wedding_Duration_Hours)  
- Total wedding cost (Wedding_Price)  

Using a tool like **KoboToolbox** or Google Forms allowed structured data collection, avoiding manual entry errors and making it easier to export the dataset in Excel or CSV format for analysis.

This method ensures the dataset reflects real-world wedding conditions and includes both **numeric and categorical variables** suitable for Machine Learning projects.

## 2. Description of Features & Label

**Features (Independent Variables):**

1. **Number_of_Guests (Numeric):** Number of wedding guests. Directly affects catering, seating, venue, and other services. Example values: 50, 100, 300.  
2. **Venue_Type (Categorical):** Type of wedding venue. Examples: Home, Hotel, Event Hall. Hotel/Hall → expensive, Home → cheaper. Needs **encoding** for ML.  
3. **Catering_Type (Categorical):** Type of catering. Examples: Basic, Standard, Premium. Major impact on total cost. Needs **encoding**.  
4. **Decoration_Level (Categorical):** Level of venue decoration. Examples: Low, Medium, High. Professional decoration → higher cost. Needs **encoding**.  
5. **Wedding_Duration_Hours (Numeric):** Wedding duration in hours. Longer duration → more services, higher venue cost. Examples: 3, 5, 8.  

**Label (Dependent Variable):**

- **Wedding_Price (Numeric):** Total wedding cost in USD. Predicted using the above features. Problem type: **Regression**.

## 3. Dataset Structure

- **Rows:** 50+  
- **Columns:** 6 (5 features + 1 label)  

**Sample Dataset (10 rows):**

| Number_of_Guests | Venue_Type | Catering_Type | Decoration_Level | Wedding_Duration_Hours | Wedding_Price |
|-----------------|------------|---------------|-----------------|----------------------|---------------|
| 100             | Hotel      | Premium       | High            | 6                    | 5200          |
| 50              | Home       | Basic         | Low             | 3                    | 1800          |
| 200             | Event Hall | Standard      | Medium          | 5                    | 4200          |
| 150             | Hotel      | Standard      | High            | 7                    | 4800          |
| 75              | Home       | Standard      | Medium          | 4                    | 2500          |
| 300             | Event Hall | Premium       | High            | 8                    | 6500          |
| 120             | Hotel      | Premium       | Medium          | 5                    | 5000          |
| 90              | Home       | Basic         | Low             | 3                    | 1900          |
| 250             | Event Hall | Standard      | Medium          | 6                    | 5500          |
| 60              | Home       | Premium       | Medium          | 4                    | 2700          |

## 4. Quality Issues

- **Missing Values:** Some entries for guests, catering, or decoration might be incomplete.  
- **Typos / Inconsistent Text:** For example, Event Hall may sometimes be written as Hall.  
- **Duplicates:** Some weddings may appear twice.  
- **Imbalance:** Hotel entries may outnumber Home or Event Hall.  
- **Mixed Formats:** Numeric and categorical values mixed in columns like Venue_Type or Catering_Type.  

These issues can be addressed during **data preprocessing** using methods like encoding categorical variables, filling missing values, and removing duplicates.

## 5. Use Case (Machine Learning Applications)

- **Regression:** Predict **Wedding_Price** using the key features. Models can include Linear Regression, Random Forest Regression, Gradient Boosting.  
- **Classification (Optional):** Categorize weddings as high/mid/low cost.  
- **Clustering (Optional):** Group weddings by similar price, guest count, or decoration level.  

**Benefit:** This project provides valuable insights into wedding costs and helps planners create accurate budgets.
