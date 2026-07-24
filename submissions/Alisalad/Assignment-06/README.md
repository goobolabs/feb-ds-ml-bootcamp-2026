# Lesson 06 – Spending Pattern Analysis with K-Means

## Files
- `spending_clustering.ipynb` → Notebook with full workflow
- `spending_l9_dataset.xlsx` → Original dataset
- `spending_labeled_clusters.csv` → Output with cluster labels
- `spending_reflection.md` → Reflection paper

## Workflow
1. Loaded dataset and selected features (`Income_$`, `SpendingScore`)
2. Scaled features with StandardScaler
3. Ran SSE loop for k=1..10 (Elbow check)
4. Chose K=3 based on elbow method
5. Evaluated clustering with Silhouette Score (0.607) and Davies–Bouldin Index (0.554)
6. Printed cluster centers in original units
7. Saved labeled dataset

## Results
- **Cluster 0**: High income / high spending (~95.5, ~76.7)
- **Cluster 1**: Mid income / low spending (~39.3, ~31.9)
- **Cluster 2**: Low income / high spending (~28.5, ~80.1)

## Key Takeaway
K-Means successfully segmented customers into three distinct groups, providing actionable insights for targeted marketing strategies.
