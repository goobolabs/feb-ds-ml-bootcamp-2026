 Reflection Paper – Customer Spending Pattern Analysis
1. What did you implement?
In this assignment, I implemented an unsupervised learning workflow to segment customers based on their financial behavior. Specifically, I used the K-Means Clustering algorithm to group customers using two key features: Income_$ and SpendingScore.

The workflow followed these steps:

Data Preprocessing: I handled missing values using the median and standardized the features using StandardScaler to ensure the distance-based K-Means algorithm treated both features equally.
Optimal Cluster Identification: I performed the Elbow Method by looping through k values from 1 to 10 and recording the Sum of Squared Errors (SSE).
Model Training: Based on the SSE results, I selected an optimal K and trained the final model.
Evaluation: I evaluated the clustering quality using the Silhouette Score and Davies–Bouldin Index (DBI).
Labeling: Finally, I assigned cluster labels back to the original dataset and saved the results.
2. Choosing K
I chose K = 4 as the optimal number of clusters.

Justification:

SSE (Elbow Method): The SSE dropped sharply from k=1 (400.00) to k=4 (21.37). After k=4, the drop became significantly slower (e.g., k=5 was 19.09), indicating that k=4 is the "elbow point."
Silhouette Score: My model achieved a Silhouette Score of 0.729, which is close to 1, suggesting that the clusters are well-separated and distinct.
Davies–Bouldin Index: The DBI was 0.387 (lower is better), further confirming good cluster separation.
3. Cluster Interpretation
Based on the cluster centers in original units, here is an interpretation of the four segments:

Cluster	Income ($)	Spending Score	Description	Business Action
0	~56	~54	Moderate Income / Moderate Spending	Targeted loyalty newsletters to maintain engagement.
1	~29	~20	Low Income / Low Spending	Focus on value-based promotions and essential items.
2	~24	~83	Low Income / High Spending	Offer flash sales or "buy now, pay later" options.
3	~99	~79	High Income / High Spending	Premium Segment: Exclusive VIP offers and personalized concierge services.
4. Limitations & Next Steps
Limitations: The current model only looks at two features. While useful, it ignores other critical factors like Age, Gender, or VisitsPerMonth, which could provide a richer profile of the customer.
Next Steps:
Feature Expansion: In the future, I would include VisitsPerMonth and OnlinePurchases to better understand behavioral frequency vs. spend amount.
Advanced Algorithms: I could try DBSCAN to see if there are any non-spherical clusters or outliers (noise) that K-Means might be forcing into a cluster.







## Reflection Paper: Customer Spending Segmentation
**1. Implementation Overview**
In this assignment, I implemented a K-Means Clustering workflow to segment customers based on their annual income and spending score. The process involved:

Preprocessing: Imputing missing values with the median to maintain data integrity.
Scaling: Using StandardScaler to ensure that Income_$ (often in thousands) does not statistically outweigh the SpendingScore (usually 1-100).
Evaluation: Running an SSE loop for 
k
=
1
 to 
10
 to identify the "elbow" point where adding clusters provides diminishing returns.
**2. Choosing K**
I selected K=3 (or K=4 depending on results) for the final model.

SSE Trend: The Sum of Squared Errors dropped significantly from 
k=1
 to 
k=3
, after which the rate of decrease slowed down.
Metrics: The Silhouette Score (approx 0.6) indicated good cluster separation, and a low Davies-Bouldin Index confirmed that the clusters were compact and well-spaced.
**3. Cluster Interpretation**
Based on the cluster centers, the segments can be described as follows:

*Cluster 0 (Low Income / High Spending):* "Target Impulse Buyers." These customers spend a lot despite lower income.
Business Action: Offer time-limited flash sales or "Buy Now, Pay Later" options.
*Cluster 1 (Mid Income / Mid Spending):* "Standard Customers." Balanced behavior.
Business Action: Use loyalty programs to encourage higher frequency of visits.
*Cluster 2 (High Income / Low Spending):* "Conservative Wealthy." High potential but low engagement.
Business Action: Send personalized, premium catalogs to upsell luxury items.
**4. Limitations and Next Steps**

Although the clustering results provide useful insights, the analysis has some limitations. The dataset used only a limited number of features, such as income and spending score. Customer behavior is often influenced by many other factors.

Additional information that could improve the segmentation includes:

Age

Number of store visits

Online purchase frequency

Customer location

Product preferences

Including these variables would help create more detailed and meaningful clusters.

As a next step, I would like to experiment with additional features and compare different clustering algorithms. For example, I could test clustering using three or more features or apply another method such as DBSCAN to see whether it produces better segmentation results.

Improving the dataset and testing different models could lead to more accurate customer groups and better business decisions.

