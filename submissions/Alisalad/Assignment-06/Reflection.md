# Reflection Paper – Assignment 06: Spending Pattern Analysis with K-Means

## 1. Implementation
I applied K-Means clustering to segment customers based on two features: Income_$ and SpendingScore. The workflow included:
- Handling missing values
- Scaling features with StandardScaler
- Running an SSE loop for k=1..10 to identify the elbow point
- Evaluating the chosen clustering solution with Silhouette Score and Davies–Bouldin Index
- Labeling the dataset with cluster assignments and saving the output

## 2. Choosing K
The SSE values decreased sharply until k=3, after which improvements were smaller. Based on the elbow method, I selected K=3. The evaluation metrics supported this choice:
- Silhouette Score = 0.607 (good separation)
- Davies–Bouldin Index = 0.554 (low overlap between clusters)

## 3. Cluster Interpretation
- **Cluster 0 (High Income / High Spending)**: Customers with strong purchasing power and high spending.  
  *Business action*: offer premium services and exclusive loyalty programs.
- **Cluster 1 (Mid Income / Low Spending)**: Customers with moderate income but conservative spending.  
  *Business action*: targeted promotions to encourage higher engagement.
- **Cluster 2 (Low Income / High Spending)**: Customers with lower income but high spending behavior.  
  *Business action*: retention strategies and affordable loyalty offers to sustain their engagement.

## 4. Limitations & Next Steps
The analysis only used Income and SpendingScore. Adding more features such as Age, VisitsPerMonth, and OnlinePurchases could improve segmentation. As a next step, I would experiment with clustering using three or more features, and also try alternative algorithms like DBSCAN to capture non-linear cluster shapes.
