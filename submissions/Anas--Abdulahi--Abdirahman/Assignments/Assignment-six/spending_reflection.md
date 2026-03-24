# Spending Pattern Analysis with K-Means Clustering  
## Reflection Paper

---

## 1. Overview of Implementation

In this assignment, I implemented customer segmentation using the K-Means clustering algorithm based on two features: **Income_$** and **SpendingScore**. The objective was to group customers into meaningful segments based on their spending behavior.

First, I loaded the dataset and selected only the required features. I checked for missing values and handled them using the **median**, since the median is less sensitive to extreme values and provides a more stable central tendency for numeric data.

Next, I applied **StandardScaler** to normalize the features. Scaling was necessary because K-Means relies on distance calculations, and differences in feature ranges could affect clustering results. Standardization ensured both Income and SpendingScore contributed equally.

To determine the appropriate number of clusters, I implemented the **Elbow Method** by looping K from 1 to 10 and printing the SSE (Sum of Squared Errors). After analyzing the SSE trend, I selected **K = 3** and trained the final K-Means model.

I then:
- Generated cluster labels  
- Added a `Cluster` column to the dataset  
- Evaluated the clustering using Silhouette Score and Davies–Bouldin Index (DBI)  
- Inverse-transformed cluster centers back to original units  
- Saved the labeled dataset as `spending_labeled_clusters.csv`

---

## 2. Choosing the Number of Clusters (K)

I selected **K = 3** because:

- The SSE showed an elbow around K = 3.
- The Silhouette Score was relatively high.
- The Davies–Bouldin Index was relatively low.

These metrics together indicated that three clusters provided a good balance between compactness and separation.

---

## 3. Cluster Interpretation and Business Insight

**Cluster 0 – Low Income / High Spending**  
Customers with lower income but high spending behavior.  
*Business action:* Offer loyalty programs and flexible payment options.

**Cluster 1 – Medium Income / Medium Spending**  
Average customers with balanced spending.  
*Business action:* Use targeted promotions to increase engagement.

**Cluster 2 – High Income / Low Spending**  
Higher income customers who spend less.  
*Business action:* Promote premium products and exclusive offers.

---

## 4. Limitations and Future Improvements

This segmentation used only two features. Including additional variables such as Age, purchase frequency, or online activity could improve clustering quality.

As a next step, I would experiment with adding more features or testing another clustering algorithm such as DBSCAN to compare results.

