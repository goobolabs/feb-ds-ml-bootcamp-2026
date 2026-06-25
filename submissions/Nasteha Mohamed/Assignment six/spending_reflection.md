## 1. What did you implement?

I implemented customer spending segmentation using the K-Means clustering algorithm. 
The dataset was loaded and the features Income_$ and SpendingScore were selected for clustering. 
Missing values were handled using the median method to ensure data consistency. 
The features were then scaled using StandardScaler to normalize the values and avoid bias from different scales.

Next, I evaluated different values of k using the Elbow Method by printing the SSE values for k from 1 to 10. 
Based on the trend of SSE, a reasonable number of clusters was selected. 
The K-Means model was then trained using the selected k value and cluster labels were assigned to each customer. 
Finally, clustering quality was evaluated using Silhouette Score and Davies–Bouldin Index.

## 2. Choosing K
I selected K = 4 as the number of clusters. Based on the SSE values from the elbow method, the difference between k = 4 and k = 5 was very small, meaning that adding an extra cluster did not significantly reduce the SSE.

The evaluation metrics were:
- Silhouette Score: higher values indicate better cluster separation.
- Davies–Bouldin Index: lower values indicate better cluster separation.

## 3. Cluster Interpretation

Cluster 0: Low Income – High Spending  
These customers spend a lot despite having lower income.  
Business action: Offer loyalty rewards and promotions to maintain engagement.

Cluster 1: Medium Income – Medium Spending  
These are average customers with balanced income and spending.  
Business action: Provide targeted marketing campaigns and discounts.

Cluster 2: High Income – Low Spending  
These customers have high income but spend less.  
Business action: Offer premium products and personalized recommendations to increase spending.

## 4. Limitations and Next Steps

The segmentation was based only on income and spending score, which limits the understanding of customer behavior.

Additional features such as:
- Purchase frequency
- Online purchases
- Customer visits

could improve the segmentation quality.

As a next step, I would try clustering with three or more features and also experiment with other clustering algorithms such as DBSCAN to compare results.