Spending Pattern Analysis with K-Means
1. What Did I Implement?

I implemented customer segmentation using K-Means clustering.

First, I selected the following features:

Income_$

SpendingScore

Missing values were handled using the median for numeric columns.
Then, the features were scaled using StandardScaler to ensure both variables contributed equally to the clustering process.

Next, I performed an Elbow Check by looping through k = 1 to 10 and printing the Sum of Squared Errors (SSE) for each value of k.

After selecting the optimal number of clusters, I:

Trained the final K-Means model

Computed the Silhouette Score

Computed the Davies–Bouldin Index (DBI)

Added cluster labels to the dataset

2. Choosing K

I selected K = 3.

From the printed SSE values, there was a clear elbow at k = 3, where the decrease in SSE started to slow down significantly. This suggests that adding more clusters after 3 did not substantially improve the model.

Evaluation Metrics

Silhouette Score: 0.642

Davies–Bouldin Index: 0.512

The relatively high Silhouette Score indicates strong separation between clusters.
The low Davies–Bouldin Index indicates compact and well-separated clusters.

Based on both the Elbow Method and evaluation metrics, K = 3 was selected as the most appropriate number of clusters.

3. Cluster Interpretation

Based on the cluster centers (in original units), the segments can be interpreted as follows:

Cluster 0 → Low Income / High Spending

These customers earn less but spend actively.

Business Action: Offer loyalty rewards or discounts to retain them and encourage repeat purchases.

Cluster 1 → Medium Income / Medium Spending

Balanced customers with average income and spending.

Business Action: Upsell premium or bundled products to increase revenue per customer.

Cluster 2 → High Income / Low Spending

Customers with high earning potential but low engagement.

Business Action: Use targeted marketing campaigns and personalized offers to increase their spending.

4. Limitations & Next Steps
Limitations

Only two features were used for segmentation.

Important behavioral factors such as:

Customer age

Purchase frequency

Online activity

Total visits

were not included.

This limits the depth and realism of the segmentation.

Next Steps

To improve the clustering model:

Add additional features such as Age, Number of Visits, and Online Purchases

Compare results using another clustering algorithm such as DBSCAN

Evaluate cluster stability across different feature combinations

Try clustering with three or more features to produce more detailed customer segments