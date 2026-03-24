# 📝 Reflection Paper – Customer Spending Pattern Analysis

## 1. What did you implement?
In this assignment, I implemented an unsupervised learning workflow to segment customers based on their financial behavior. Specifically, I used the **K-Means Clustering** algorithm to group customers using two key features: `Income_$` and `SpendingScore`. 

The workflow followed these steps:
- **Data Preprocessing:** I handled missing values using the median and standardized the features using `StandardScaler` to ensure the distance-based K-Means algorithm treated both features equally.
- **Optimal Cluster Identification:** I performed the **Elbow Method** by looping through `k` values from 1 to 10 and recording the **Sum of Squared Errors (SSE)**.
- **Model Training:** Based on the SSE results, I selected an optimal `K` and trained the final model.
- **Evaluation:** I evaluated the clustering quality using the **Silhouette Score** and **Davies–Bouldin Index (DBI)**.
- **Labeling:** Finally, I assigned cluster labels back to the original dataset and saved the results.

## 2. Choosing K
I chose **K = 4** as the optimal number of clusters. 

**Justification:**
- **SSE (Elbow Method):** The SSE dropped sharply from `k=1` (400.00) to `k=4` (21.37). After `k=4`, the drop became significantly slower (e.g., `k=5` was 19.09), indicating that `k=4` is the "elbow point."
- **Silhouette Score:** My model achieved a Silhouette Score of **0.729**, which is close to 1, suggesting that the clusters are well-separated and distinct.
- **Davies–Bouldin Index:** The DBI was **0.387** (lower is better), further confirming good cluster separation.

## 3. Cluster Interpretation
Based on the cluster centers in original units, here is an interpretation of the four segments:

| Cluster | Income ($) | Spending Score | Description | Business Action |
|---------|------------|----------------|-------------|-----------------|
| **0** | ~56 | ~54 | **Moderate Income / Moderate Spending** | Targeted loyalty newsletters to maintain engagement. |
| **1** | ~29 | ~20 | **Low Income / Low Spending** | Focus on value-based promotions and essential items. |
| **2** | ~24 | ~83 | **Low Income / High Spending** | Offer flash sales or "buy now, pay later" options. |
| **3** | ~99 | ~79 | **High Income / High Spending** | **Premium Segment:** Exclusive VIP offers and personalized concierge services. |

## 4. Limitations & Next Steps
- **Limitations:** The current model only looks at two features. While useful, it ignores other critical factors like **Age**, **Gender**, or **VisitsPerMonth**, which could provide a richer profile of the customer.
- **Next Steps:** 
  - **Feature Expansion:** In the future, I would include `VisitsPerMonth` and `OnlinePurchases` to better understand behavioral frequency vs. spend amount.
  - **Advanced Algorithms:** I could try **DBSCAN** to see if there are any non-spherical clusters or outliers (noise) that K-Means might be forcing into a cluster.
