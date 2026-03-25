# 🎓 Spending Pattern Analysis with K-Means – Reflection Paper

**Student:** Najmo Muxudiin  
**Course:** Machine Learning – Clustering  
**Date:** February 2025  

---

## 1️⃣ What Did I Implement?

In this assignment, I implemented a **K-Means clustering model** to segment customers based on their income and spending behavior. The objective was to group customers into meaningful clusters without using a target variable (unsupervised learning).

First, I loaded the dataset using Pandas and selected two numerical features: `Income_$` and `SpendingScore`. I checked for missing values and handled them using **median imputation** to ensure clean and consistent data.

Since K-Means is a distance-based algorithm, I scaled the features using `StandardScaler`. Scaling was necessary to ensure that both features contributed equally to the clustering process.

Next, I applied the **Elbow Method** by training K-Means models for values of k from 1 to 10. I printed the **Sum of Squared Errors (SSE)** for each value to observe how clustering compactness improved as the number of clusters increased.

After analyzing the SSE trend, I selected **K = 6** as a reasonable number of clusters. I then trained the final K-Means model and added the cluster labels to the dataset in a new column called `Cluster`.

To evaluate clustering quality, I calculated:

- **Silhouette Score**
- **Davies–Bouldin Index (DBI)**

Finally, I converted the cluster centers back to their original units to make interpretation easier and printed sample rows to confirm correct labeling.

---

## 2️⃣ Choosing K

I selected **K = 6** based on the Elbow Method results and evaluation metrics.

The SSE values showed a noticeable decrease at lower values of k, and around k = 6 the improvement became smaller. This indicated a good balance between model simplicity and clustering quality.

- The **Silhouette Score** (higher is better) showed acceptable separation between clusters.
- The **Davies–Bouldin Index** (lower is better) indicated reasonable distinction among clusters.

Based on these observations, K = 6 provided meaningful and well-separated customer segments.

---

## 3️⃣ Cluster Interpretation

After converting the cluster centers back to original income and spending values, I interpreted the clusters as follows:

- **Low Income – High Spending**  
  These customers earn less but spend actively.  
  *Business Action:* Offer loyalty programs and flexible payment options.

- **High Income – Low Spending**  
  Customers with strong earning power but cautious spending habits.  
  *Business Action:* Promote premium or high-quality products.

- **Medium Income – Medium Spending**  
  Balanced and stable customers.  
  *Business Action:* Maintain engagement through regular promotions.

- **High Income – High Spending**  
  High-value customers.  
  *Business Action:* Provide VIP membership and exclusive benefits.

- **Low Income – Low Spending**  
  Low engagement group.  
  *Business Action:* Offer discounts and awareness campaigns.

- **Moderate Income – Selective Spending**  
  Customers who spend strategically.  
  *Business Action:* Use targeted marketing based on behavior.

These segments can help businesses design effective marketing strategies.

---

## 4️⃣ Limitations & Next Steps

### Limitations

- Only two features were used (`Income_$` and `SpendingScore`).
- Customer behavior depends on additional factors such as age, frequency of visits, and online purchases.
- K-Means assumes spherical clusters, which may not always represent real-world patterns.





## ✅ Conclusion

This project demonstrates how unsupervised learning can uncover hidden patterns in customer data. K-Means clustering successfully segmented customers into meaningful groups that can support data-driven marketing and business decision-makin

