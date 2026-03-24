# Practical Assignment: Data Foundations for Machine Learning

## Title  
**Market Prices of Essential Goods in Local Shops**

---

## 1. Introduction and Data Collection Method

This assignment focuses on collecting real-world market price data of essential goods sold in local shops.  
The purpose of this dataset is to understand how product prices vary across different shops and locations.

The data was manually collected by visiting various local shops in different areas and recording product details such as product name, shop name, location, category, and price.  
No pre-made datasets from Kaggle, UCI, or other online repositories were used. All data was collected firsthand through direct observation and manual logging.

---

## 2. Description of Features and Label

The dataset contains five variables, which include input features and one output label.

### Features (X)
- **ProductName**: The name of the product sold in the shop (e.g., Rice, Sugar, Milk).
- **ShopName**: The name of the shop where the product was observed.
- **Location**: The area or district where the shop is located.
- **Category**: The type of product such as Food, Beverage, or Household.

### Label (y)
- **Price**: The selling price of the product in the local market.

The Price variable is considered the target label, while the remaining variables are treated as input features.

---

## 3. Dataset Structure

The dataset consists of **50 rows** and **5 columns**.  
Each row represents a single product observed in a specific shop and location.

Due to space limitations, only a small sample of the dataset is shown below.

| ProductName | ShopName | Location | Category | Price |
|------------|----------|----------|----------|-------|
| Rice | Pressbakaaro | Bakaaro | Food | 25 |
| Sugar | Barwaaqo | Bakaaro | Food | 30 |
| Milk | MartiSoor | Karaan | Beverage | 18 |
| Oil | Dagdagsiimo | Madiino | Food | 40 |
| Soap | Barwaaqo2 | Bakaaro | Household | 12 |

The complete dataset containing 50 rows is provided as a separate file.

---

## 4. Data Quality Issues

The dataset reflects real-world data conditions and contains several data quality issues.  
Some records may contain missing values in certain fields such as shop name or category.  
There are inconsistencies in spelling and text formatting across categorical variables such as shop names, locations, and product categories.  
Additionally, numerical values such as prices may appear in mixed formats.

These issues are common in real-world datasets and will be addressed during the preprocessing stage.

---

## 5. Use Case in Machine Learning

This dataset can be used in multiple machine learning applications.  
It can be applied to a **regression task** to predict product prices based on features such as location, shop name, and product category.  
The dataset can also be used for **clustering**, where products or shops are grouped based on similarities in pricing patterns.

Such machine learning models can help identify price trends and variations across different areas and shops.

---

## Conclusion

This assignment provided hands-on experience in real-world data collection.  
By manually collecting and organizing market price data, the dataset demonstrates common data challenges such as missing values and inconsistent formatting.  
The dataset is suitable for preprocessing and machine learning tasks that will be explored in later lessons.
