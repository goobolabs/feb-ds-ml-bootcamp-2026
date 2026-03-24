Spending Pattern Analysis with K-Means Clustering

1. What I Implemented

In this assignment, I implemented customer segmentation using the K-Means clustering algorithm. The goal was to group customers based on their annual income (Income_$) and their SpendingScore in order to understand different spending behaviors.

First I loaded the dataset and selected the two relevant features: Income_$ and SpendingScore. Before applying the model, I handled missing values by replacing them with the median of each column. Since K-Means is distance-based and sensitive to scale I standardized the features using StandardScaler. This ensured that both income and spending score contributed equally to the clustering process.

Next, I performed an Elbow Method analysis by looping through values of k from 1 to 10. For each value of k, I trained a K-Means model and printed the SSE (Sum of Squared Errors). This helped me observe how the within-cluster variance changed as the number of clusters increased.

After selecting an appropriate value for k, I trained the final K-Means model, generated cluster labels, and added them to the original dataset. Finally, I evaluated the clustering performance using the Silhouette Score and the Davies–Bouldin Index (DBI), and I printed the cluster centers in their original units to interpret the results clearly.

2.Choosing the Value of K

After reviewing the printed SSE values, I observed a clear “elbow” around K = 3. The SSE decreased significantly up to k=3, but after that, the improvement became smaller. This indicated that adding more clusters did not significantly improve the model.

In addition to SSE, I also checked

Silhouette Score – which measures how well each data point fits within its assigned cluster compared to other clusters. A higher value indicates better separation.

Davies–Bouldin Index (DBI) – which measures cluster similarity. A lower value indicates better clustering.

For K = 3, the Silhouette Score was relatively high, and the DBI was low compared to nearby values of k. This combination confirmed that three clusters provided a good balance between simplicity and cluster quality.

Therefore, I selected K = 3 as the final number of clusters.

3.Cluster Interpretation

After examining the cluster centers in their original units, I interpreted the clusters as follows:

Cluster 0 – Low Income / High Spending

These customers have lower annual income but relatively high spending scores. This suggests they may be impulsive buyers or highly engaged with the brand.

Business Action:
Offer loyalty rewards or special discounts to retain them and prevent churn. Since they already spend actively, retention strategies would be effective.

Cluster 1 – Medium Income / Medium Spending

These customers show balanced income and spending behavior They likely represent regular and stable customers.

Business Action
Promote bundled products or personalized recommendations to gradually increase their spending.

Cluster 2 – High Income / Low Spending

These customers earn high income but have lower spending scores. This means they have purchasing power but are not fully engaged.

Business Action
Target them with premium product campaigns, exclusive offers, or personalized marketing to encourage higher spending.

4.Limitations and Next Steps

One limitation of this analysis is that it only uses two features: income and spending score. Customer behavior is more complex than just these two variables. Important information such as age, frequency of visits, online purchases, product preferences, or customer loyalty history could significantly improve segmentation quality.

Another limitation is that K-Means assumes clusters are spherical and evenly sized, which may not always reflect real customer behavior.

As a next step, I would

Add more features such as Age, OnlinePurchases, and VisitFrequency.

Experiment with clustering using three or more dimensions.

Try a different clustering algorithm like DBSCAN to compare results.

Overall, this project helped me understand how unsupervised learning can be used in real business scenarios to identify patterns and support data-driven marketing strategies.