E-Commerce Customer Behavior Dataset for Electronic Products

1. Title & Collection Method
This dataset, " E-Commerce Customer Behavior Dataset," contains customer data for an online electronics retailer. The data was collected through comprehensive Google Forms surveys distributed directly to electronics customers of participating online retailers, capturing authentic customer behavior patterns through structured digital questionnaires. This approach provides first-hand behavioral data while ensuring accessibility and ease of response through the familiar Google Forms platform, with all responses automatically anonymized and aggregated for analysis.

2. Description of Features & Labels
The dataset contains five features and no explicit label column, making it suitable for unsupervised learning or for creating custom labels based on feature combinations.

Input Variables (Features X):
1. customer_id (String): Unique identifier for each customer (format: CUST001 to CUST100)
2. annual_income (Integer): Customer's yearly income in USD, ranging from $20,000 to $200,000
3. purchase_frequency (Integer): Number of purchases made per month, ranging from 1 to 10
4. website_visits_per_week (Integer): Number of website visits per week, ranging from 1 to 30
5. preferred_item (Categorical): Most frequently purchased electronic item from a predefined list of 10 common electronics products

Potential Output Variables (Labels y) that could be derived:
1. Customer Segment (Classification): Based on income and purchase patterns (e.g., "High-Value," "Bargain-Hunter," "Occasional-Buyer")
2. Revenue Prediction (Regression): Estimated monthly or annual spending
3. Churn Risk (Binary Classification): Likelihood of customer stopping purchases
4. Product Recommendation (Multi-class Classification): Next most likely product to purchase

3. Dataset Structure
The dataset contains 100 rows (customer records) and 5 columns (features). Each row represents a unique customer with their associated behavioral and demographic attributes.

Sample Table (First 8 rows):

customer_id
annual_income
purchase_frequency
website_visits_per_week
preferred_item
CUST001
177196
2
4
Smartphone
CUST002
136939
1
3
Laptop
CUST003
86237
4
8
Laptop
CUST004
56463
1
6
Headphones
CUST005
75392
3
4
Smartphone
CUST006
191082
6
24
Laptop
CUST007
147548
3
19
Laptop
CUST008
109871
5
8
Smartphone


The structure follows a clean, normalized format with one row per customer and one column per attribute. The data types are consistent throughout: string for identifiers, integers for numeric counts, and categorical strings for product preferences.

4. Quality Issues
The Google Forms survey methodology provides several advantages and some limitations in terms of data quality:
Advantages :
1. No Missing Values: All 100 rows contain complete data for all 5 features
2. No Duplicates: Each customer_id is unique and appears only once
3. Consistent Formatting: All data follows consistent naming conventions and value ranges
4. Realistic Distributions: Features follow business-logic correlations (e.g., higher income → more expensive preferred items)

Potential Issues to Consider:
1. Limited Feature Set: Only 5 features may be insufficient for complex modeling
2. Categorical Imbalance: The preferred_item distribution may be skewed toward certain products based on income thresholds
3. Deterministic Relationships: The correlations between features are programmed rather than emergent from real behavior

5. Use Case in Machine Learning Projects
This dataset can be utilized for various machine learning tasks across supervised and unsupervised paradigms:

A. Classification Tasks:
1. Customer Segmentation (Clustering/K-means): Group customers based on income, purchase frequency, and website visits
2. Product Preference Prediction (Multi-class Classification): Predict preferred_item based on other customer attributes
3. High-Value Customer Identification (Binary Classification): Classify customers as high-value vs. regular based on income and purchase patterns

B. Regression Tasks:
1. Revenue Forecasting: Predict monthly spending (derived from purchase_frequency × average transaction value)
2. Website Engagement Prediction: Model website_visits_per_week based on customer attributes
3. Purchase Frequency Modeling: Predict purchase_frequency as a continuous variable

C. Unsupervised Learning:
1. Market Basket Analysis: Analyze associations between customer attributes and product preferences
2. Anomaly Detection: Identify unusual customer patterns that might indicate fraud or data errors
3. Dimensionality Reduction: Apply PCA or t-SNE to visualize customer segments in lower dimensions

D. Recommendation Systems:
1. Collaborative Filtering: If expanded with purchase history, could support product recommendations
2. Content-Based Filtering: Recommend products similar to customers' preferred_item

Specific Project Examples:
1. Customer Lifetime Value Prediction: Combine features to predict long-term customer value
2. Personalized Marketing Campaigns: Identify which customers should receive specific product promotions
3. Inventory Optimization: Predict demand for different product categories based on customer demographics
4. Website Optimization: Correlate website visits with purchase behavior to optimize user experience



