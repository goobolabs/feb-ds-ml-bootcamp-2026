1️⃣ What I Implemented

In this assignment, I implemented customer segmentation using K-Means clustering based on two features: Income_$ and SpendingScore.

First, I loaded the dataset and selected the required features. I checked for missing values and filled them using the median where necessary. Since K-Means is distance-based, I scaled the features using StandardScaler to ensure both variables contributed equally to the clustering process.

Next, I applied the Elbow Method by running K-Means for k = 1 to 10 and printing the SSE values. After observing the SSE trend, I selected an appropriate number of clusters. I then trained the final model, generated cluster labels, and added a new column called "Cluster" to the dataset.

Finally, I evaluated the model using:

Silhouette Score

Davies–Bouldin Index

I also printed the cluster centers in their original units for interpretation.

2️⃣ Choosing K

After reviewing the printed SSE values, I observed that the decrease in SSE slowed down significantly around K = 3, indicating a possible elbow point.

Additionally:

The Silhouette Score was relatively high, indicating good separation between clusters.

The Davies–Bouldin Index was low, indicating compact and well-separated clusters.

Based on these evaluation metrics, I selected K = 3 as the optimal number of clusters.

3️⃣ Cluster Interpretation

Based on the cluster centers:

🔹 Cluster 0 – Low Income / High Spending

These customers earn less but spend heavily.
Business Action: Offer loyalty programs and installment-based promotions.

🔹 Cluster 1 – Medium Income / Medium Spending

Balanced customers with moderate purchasing behavior.
Business Action: Upsell premium products and offer bundle discounts.

🔹 Cluster 2 – High Income / High Spending

Premium customers with strong purchasing power.
Business Action: Provide VIP memberships, exclusive offers, and personalized services.

4️⃣ Limitations & Next Steps

This segmentation only used two features: Income and Spending Score. Including additional features such as:

Age

VisitsPerMonth

OnlinePurchases

could improve clustering quality and provide deeper customer insights.

🚀 Next Steps

In future work, I would:

Test clustering using three or more features and compare performance metrics.

Experiment with DBSCAN to detect potential outliers or irregular customer groups.

Visualize clusters using 2D or 3D plots for better interpretability.