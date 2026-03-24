# Reflection Paper: Spending Pattern Analysis

## 1. What Did I Implement?
In this assignment, I implemented an unsupervised learning approach to segment customers based on their spending patterns using the **K-Means clustering** algorithm. 
First, I loaded the dataset (`spending_l9_dataset.csv`) and extracted the core features: `Income_$` and `SpendingScore`. To ensure the distance-based algorithm calculated clusters fairly, I filled any potential missing values with the median and applied `StandardScaler` to normalize the data. I then utilized the **Elbow Method** to calculate the Sum of Squared Errors (SSE) for `k=1` through `k=10`. Finally, I trained the K-Means model with my chosen `K`, assigned the resulting cluster labels back to the original dataset, and evaluated the model's performance using clustering metrics before saving the labeled output.

## 2. Choosing K
I chose **K = 5** for my final model. 
This decision was driven primarily by the **Elbow Method**. When evaluating the SSE values, there was a steep and significant drop from `k=1` (400) down to `k=5` (65.57). After `k=5`, the reductions became very minimal and linear (e.g., dropping only to 54.96 for `k=6`). This characteristic "bend" at 5 indicated that adding more clusters would not provide meaningful structural improvements.
Furthermore, evaluating the model at `K=5` yielded strong validation metrics: a **Silhouette Score of 0.555** (indicating good cohesion and separation) and a **Davies–Bouldin Index (DBI) of 0.573** (a low score, confirming the clusters are distinct from one another).

## 3. Cluster Interpretation & Business Actions
Based on the inverse-transformed cluster centers, the 5 customer segments can be clearly defined:

1. **Cluster 0: Average Income / Average Spending** (`Income_$` ~ $55k, `Spending` ~ 50)
   * **Action:** Send them standard, broad promotional material. Keep them engaged with regular newsletters to gently push them toward higher spending categories.
2. **Cluster 1: High Income / High Spending** (`Income_$` ~ $86k, `Spending` ~ 82)
   * **Action:** Treat these as VIP customers. Offer them exclusive early access to premium products and dedicated, personalized loyalty rewards to maintain this highly profitable relationship.
3. **Cluster 2: Low Income / High Spending** (`Income_$` ~ $25k, `Spending` ~ 79)
   * **Action:** These customers are highly engaged but budget-constrained. Target them with frequent small discounts, installment payment options (like Buy-Now-Pay-Later), or flash sales.
4. **Cluster 3: High Income / Low Spending** (`Income_$` ~ $88k, `Spending` ~ 17)
   * **Action:** This is an untapped market with high purchasing power. Deploy aggressive re-engagement campaigns or surveys to figure out what they want, or cross-sell luxury/niche items they haven't tried yet.
5. **Cluster 4: Low Income / Low Spending** (`Income_$` ~ $26k, `Spending` ~ 20)
   * **Action:** Avoid spending significant marketing budget here. Focus on low-cost, automated retention strategies or clearance promotions.

## 4. Limitations & Next Steps
**Limitations:** K-Means assumes spherical clusters and relies heavily on the distance metric, which can struggle with outliers or irregular groupings. Additionally, leveraging only two features (Income and Spending) provides a severely limited, one-dimensional view of a customer. 

**Next Steps:** To improve the segmentation, I would incorporate more rich, behavioral data into the model (e.g., `Age`, `Website Visits`, `Cart Abandonment Rate`, `Online Purchases`). Moving from 2 features to a multidimensional space could reveal much deeper, more actionable personas. As an algorithmic next step, I would experiment with **DBSCAN** to identify density-based anomalies that might be throwing off the spherical assumptions of K-Means.
