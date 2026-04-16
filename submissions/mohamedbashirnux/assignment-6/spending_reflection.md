# Reflection Paper: Spending Pattern Analysis

## 1. What did I implement?

I implemented customer spending segmentation using K-Means clustering. The workflow included:

1. Loading the spending dataset with Income and SpendingScore features
2. Handling missing values by filling with median
3. Scaling features using StandardScaler to normalize the data
4. Running the Elbow method (SSE loop for k=1 to 10) to find optimal cluster count
5. Training K-Means with chosen K value
6. Evaluating with Silhouette Score and Davies-Bouldin Index
7. Inverse-transforming cluster centers back to original units
8. Adding cluster labels to the dataset and saving the output

## 2. Choosing K

I chose K=3 based on the SSE trend from the Elbow method. After k=3, the SSE decrease slowed significantly, indicating diminishing returns from adding more clusters. This "elbow point" suggests 3 clusters capture the main patterns without over-segmenting.

The Silhouette Score (~0.607) indicates good cluster separation - values above 0.5 mean clusters are well-defined. The Davies-Bouldin Index (~0.554) is relatively low, confirming clusters are distinct and not overlapping. These metrics together validate that K=3 is optimal for this dataset.

## 3. Cluster Interpretation

Based on the cluster centers in original units:

Cluster 0 (High Income / High Spending): These are "VIP Customers" with high income (~$95) and high spending scores (~77). They have money and love to spend it.
- Business Action: Create a premium loyalty program with exclusive perks, early access to new products, and personalized shopping experiences.

Cluster 1 (Low Income / Low Spending): These are "Budget Shoppers" with lower income (~$39) and low spending scores (~32). They are cautious with money.
- Business Action: Offer value bundles, discount programs, and affordable product lines to match their budget constraints.

Cluster 2 (Low Income / High Spending): These are "Enthusiastic Shoppers" with lower income (~$28) but high spending scores (~80). They love shopping despite limited budgets.
- Business Action: Provide flexible payment options like "buy now, pay later", installment plans, and targeted promotions to support their shopping enthusiasm.

## 4. Limitations & Next Steps

Current limitations: We only used Income and SpendingScore. Other factors like Age, VisitsPerMonth, and OnlinePurchases could reveal deeper patterns. For example, younger customers might spend differently than older ones even with similar incomes.

Adding Age could help identify generational spending patterns. VisitsPerMonth could distinguish between frequent small buyers and occasional big spenders. OnlinePurchases could separate digital-first customers from in-store shoppers.

Next Step: Expand clustering to include 3 features (Income, SpendingScore, Age) to create more nuanced customer segments. This would enable more targeted marketing strategies based on both financial capacity and behavioral patterns.
