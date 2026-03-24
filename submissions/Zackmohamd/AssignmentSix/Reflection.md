Reflection Paper: K-Means Customer Segmentation
1. What I Implemented

In this project, I implemented a K-Means clustering algorithm to segment customers based on spending behavior. The workflow followed these main steps:

Data Scaling
Before applying K-Means, I scaled the dataset using standardization. Since K-Means is distance based, features with larger numeric ranges can dominate the clustering process. Standard scaling ensured that all variables contributed equally to the model.

SSE Loop (Elbow Method)
I created a loop to calculate the Sum of Squared Errors (SSE) for values of K ranging from 1 to 10. SSE measures the total within-cluster variance. As K increases, SSE decreases. I examined the elbow point where the decrease in SSE slowed down significantly, indicating a reasonable number of clusters.

Evaluation Metrics
To select the best K, I also computed:

Silhouette Score, which measures how well data points fit within their assigned cluster compared to other clusters. Values closer to 1 indicate better clustering.

Davies-Bouldin Index (DBI), which measures cluster separation. Lower values indicate better cluster structure.

Using multiple metrics helped avoid relying on SSE alone.

Labeling Clusters
After choosing the optimal K, I assigned cluster labels to each data point and exported the labeled dataset. This allowed interpretation of each cluster in business terms.

2. Choosing K

After reviewing the results:

The Elbow Method showed a noticeable bend at K = 3.

The Silhouette Score was highest around K = 3.

The Davies-Bouldin Index was lowest near K = 3.

Based on these results, I selected K = 3 as the optimal number of clusters.

This choice balanced cluster compactness, separation, and interpretability.

3. Cluster Interpretation

After analyzing the cluster centroids and feature averages, I interpreted the clusters as follows:

Cluster 0: Low Income, Low Spending

These customers have relatively lower income levels and spend conservatively.

Business Action:
Offer discounts and budget friendly promotions to increase engagement.

Cluster 1: High Income, High Spending

This group consists of customers with higher income and strong purchasing behavior.

Business Action:
Provide loyalty programs, premium membership benefits, and exclusive offers to retain them.

Cluster 2: Moderate Income, Selective Spending

These customers have moderate income but spend strategically or seasonally.

Business Action:
Target them with personalized recommendations and bundle offers to increase basket size.

4. Limitations and Next Steps

Limitations
The clustering was based only on available spending and income features. Important behavioral factors were missing, such as:

Age

Number of store visits

Online purchases

Purchase frequency

Product categories

Including these features could significantly improve segmentation quality.

Next Step
One concrete next step is to:

Add at least one behavioral feature such as Visit Frequency.

Compare results using another clustering method like DBSCAN to see if density based clustering produces better separation.

Experiment with using three or more features to evaluate whether cluster structure improves.