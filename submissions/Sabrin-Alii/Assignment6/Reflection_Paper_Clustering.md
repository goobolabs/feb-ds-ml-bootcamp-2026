# Spending Pattern Analysis using K-Means Clustering

## 1. What Did I Implement?

In this assignment, I implemented customer segmentation using the K-Means clustering algorithm based on two numerical features: Income_$ and SpendingScore.

First, I loaded the dataset and selected the relevant features. I handled missing values using median imputation to ensure numeric stability. Since K-Means is distance-based, I scaled the features using StandardScaler to prevent Income_$ from dominating SpendingScore due to scale differences.

Next, I performed an Elbow check by looping k from 1 to 10 and printing SSE (Sum of Squared Errors). Based on the clear drop in SSE values and the elbow trend, I selected K = 4.

After fitting the final KMeans model with random_state=42, I added the cluster labels to the dataset. I then evaluated clustering quality using:

- Silhouette Score
- Davies–Bouldin Index (DBI)

Finally, I inverse-transformed the cluster centers back to their original units to make interpretation meaningful.

---

## 2. Choosing K

I selected K = 4 based on the SSE trend. The largest reductions in SSE occurred between k=1 and k=4. After k=4, the decrease became gradual, indicating diminishing returns.

Additionally, evaluation metrics supported this choice:

Silhouette Score: 0.729  
Davies–Bouldin Index: 0.387  

The high Silhouette Score indicates strong separation between clusters, while the low DBI confirms compact and well-separated clusters.

---

## 3. Cluster Interpretation

Cluster 0 – Middle Income / Medium Spending  
Customers with moderate income and balanced spending behavior.  
Business Action: Offer bundle deals or loyalty rewards to increase retention.

Cluster 1 – Low Income / Low Spending  
Price-sensitive customers with conservative spending.  
Business Action: Provide discounts and budget-friendly promotions.

Cluster 2 – Low Income / High Spending  
Customers with lower income but high spending activity.  
Business Action: Introduce installment options or targeted promotional campaigns.

Cluster 3 – High Income / High Spending  
Premium customers with high purchasing power and strong engagement.  
Business Action: Offer VIP programs, exclusive offers, and premium services.

---

## 4. Limitations & Next Steps

This segmentation only used two features (Income and SpendingScore). Including additional variables such as Age, VisitsPerMonth, or OnlinePurchases could improve segmentation quality.

A concrete next step would be to:
- Try clustering with three or more features.
- Compare K-Means with DBSCAN.
- Evaluate cluster stability across different random states.

---

## Conclusion

The K-Means model successfully segmented customers into four meaningful spending groups. The strong Silhouette Score and low Davies–Bouldin Index confirm high-quality clustering.

Overall, this approach provides actionable insights that can support targeted marketing and strategic decision-making.