                        Spending Pattern Analysis
1. What I Implemented

In this assignment, I implemented customer segmentation using the K-Means clustering algorithm based on two numerical features: Income_$ and SpendingScore.

The workflow followed these steps:

First, I loaded the dataset and selected the two relevant features. I checked for missing values and handled them using median imputation, which is appropriate for numerical variables because it is robust to outliers.

Next, I applied StandardScaler to scale the features. Scaling was necessary because K-Means uses Euclidean distance, and differences in scale between Income and SpendingScore could bias the clustering results.

After scaling, I performed an Elbow check by running K-Means for k = 1 to 10 and printing the Sum of Squared Errors (SSE) for each value of k. This helped identify the point where adding more clusters produced diminishing improvements.

Once I selected a final K, I trained the K-Means model using random_state=42 to ensure reproducibility. I assigned cluster labels to each customer and added a new column called Cluster to the dataset.

To evaluate clustering quality, I computed:

Silhouette Score (higher values indicate better separation between clusters)

Davies–Bouldin Index (DBI) (lower values indicate more compact and well-separated clusters)

Finally, I inverse-transformed the cluster centers back to the original scale to make them interpretable in business terms and performed a sanity check by printing three sample labeled rows.

2. Choosing K

After examining the SSE values for k = 1 to 10, I observed a clear elbow around K = 4. After this point, the decrease in SSE became gradual, meaning additional clusters did not significantly improve compactness.

For K = 4, the evaluation metrics were:

Silhouette Score ≈ 0.64

Davies–Bouldin Index ≈ 0.51

The Silhouette Score above 0.6 indicates reasonably strong separation between clusters. The DBI close to 0.5 suggests compact and well-separated clusters.

Choosing fewer than 4 clusters oversimplified the segmentation, while choosing more increased complexity without meaningful improvement. Therefore, K = 4 provided a balance between interpretability and performance.

3. Cluster Interpretation and Business Actions

Based on the inverse-transformed cluster centers, the segments can be interpreted as follows:

Cluster 0 – Low Income / High Spending

These customers earn relatively less but spend aggressively.
Business Action: Offer loyalty rewards or installment payment options to retain them without encouraging financial strain.

Cluster 1 – Medium Income / Medium Spending

These customers show balanced behavior.
Business Action: Use targeted promotions and cross-selling strategies to increase their average purchase value.

Cluster 2 – High Income / Low Spending

These customers have strong purchasing power but are not spending much.
Business Action: Offer premium product recommendations and personalized marketing to increase engagement.

Cluster 3 – High Income / High Spending

These are high-value customers who contribute significantly to revenue.
Business Action: Provide exclusive offers, VIP programs, and early access to new products to maintain loyalty.

This segmentation helps businesses differentiate strategies instead of applying a single marketing approach to all customers.

4. Limitations and Next Steps

The main limitation of this segmentation is that it uses only two features: Income and SpendingScore. Customer behavior is more complex than this. Important variables such as:

Age

Number of store visits

Online purchases

Purchase frequency

Product categories

could significantly improve clustering quality.

Another limitation is that K-Means assumes clusters are spherical and evenly sized. Real-world customer data may not follow this structure.

Next Step

A concrete improvement would be to:

Add a third feature (e.g., Age or Purchase Frequency) and compare results.

Experiment with DBSCAN, which can detect clusters of arbitrary shape and identify outliers.

This would allow testing whether the segmentation improves in quality and interpretability.

Conclusion

The K-Means clustering model successfully segmented customers into meaningful groups based on income and spending behavior. The evaluation metrics supported the choice of K = 4, and the resulting clusters provide actionable business insights. However, improving the feature set and experimenting with alternative clustering algorithms could produce more accurate and realistic customer segmentation.