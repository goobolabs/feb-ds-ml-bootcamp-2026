# Local Market Food Prices Dataset for Machine Learning

## Title & Collection Method

This dataset is about **food prices in local Somali markets**.  
The purpose of collecting this dataset is to understand how prices change depending on the product type, location, weekly variation, and demand.

The dataset was collected using **manual observation and logging**.  
Prices were recorded from different markets and cities in Somalia by checking weekly prices of common food items such as rice, sugar, flour, beans, pasta, and cooking oil.

This dataset reflects real-world conditions because prices may vary by region and demand, and data may contain missing or inconsistent entries.

---

## Description of Features (X) and Label (y)

In Machine Learning, we use:

- **Features (X):** Input variables  
- **Label (y):** Output variable we want to predict

### Features (X)

| Feature Name     | Description |
|-----------------|-------------|
| Product_Type     | Type of food product (Rice, Sugar, Flour, etc.) |
| Market_Location  | City/market where price was recorded |
| Week_Number      | Week of the year (1–12) |
| Quantity_kg      | Quantity measured in kilograms |
| Demand_Level     | Demand category (Low, Medium, High) |

### Label (y)

| Label Name | Description |
|-----------|-------------|
| Price_USD | Price of the product in US dollars |

So:

- **X = Product_Type, Market_Location, Week_Number, Quantity_kg, Demand_Level**
- **y = Price_USD**

---

## Dataset Structure

The dataset contains:

- **50 rows (samples)**
- **6 columns (5 features + 1 label)**

### Sample Table (First 10 Rows)

| Product_Type | Market_Location | Week_Number | Quantity_kg | Demand_Level | Price_USD |
|------------|----------------|------------|------------|-------------|----------|
| Rice       | Mogadishu      | 1          | 5          | High        | 7.50     |
| Sugar      | Hargeisa       | 1          | 3          | Medium      | 4.20     |
| Flour      | Baidoa         | 2          | 10         | High        | 12.00    |
| Cooking Oil| Mogadishu      | 2          | 2          | Low         | 5.00     |
| Rice       | Kismayo        | 3          | 5          | Medium      | 8.10     |
| Beans      | Hargeisa       | 3          | 4          | High        | 6.80     |
| Sugar      | Mogadishu      | 4          | 3          | High        | 4.50     |
| Flour      | Kismayo        | 4          | 8          | Medium      | 10.30    |
| Oil        | Baidoa         | 5          | 1          | Low         | 3.20     |
| Rice       | Hargeisa       | 5          | 5          | High        | 7.90     |

---

## Quality Issues

Because this dataset was collected manually, several real-world data quality problems may exist:

- **Missing values:** Some markets may not report prices every week  
- **Typos:** Product names may have inconsistent spelling  
- **Duplicates:** Same observation could be entered twice  
- **Categorical variables:** Product_Type and Demand_Level require encoding  
- **Imbalance:** Some products appear more often than others  

These issues will be handled in Lesson 3 through preprocessing.

---

## Use Case in Machine Learning

This dataset can be used in multiple ML projects:

### Regression

Predict food prices:

- Inputs: product type, market, demand, quantity  
- Output: Price_USD  
Models: Linear Regression, Random Forest Regressor

### Classification

Classify demand level based on pricing patterns:

- Output: Low / Medium / High demand

### Clustering

Group markets with similar price behavior:

- Example: K-Means clustering to identify expensive vs affordable cities

---

## Conclusion

This dataset provides a realistic example of economic and market data.  
It includes numerical and categorical variables, making it useful for practicing data preprocessing, encoding, scaling, and Machine Learning modeling.

In Lesson 3, this dataset will be cleaned and prepared for training ML models.
