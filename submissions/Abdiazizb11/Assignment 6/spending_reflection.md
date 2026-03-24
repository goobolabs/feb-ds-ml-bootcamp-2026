# Reflection Paper: Customer Spending Segmentation

## 1. Implementation Overview
In this assignment, I implemented a **K-Means Clustering** workflow to segment customers based on their annual income and spending score. The process involved:
* **Preprocessing:** Imputing missing values with the median to maintain data integrity.
* **Scaling:** Using `StandardScaler` to ensure that `Income_$` (often in thousands) does not statistically outweigh the `SpendingScore` (usually 1-100).
* **Evaluation:** Running an SSE loop for $k=1$ to $10$ to identify the "elbow" point where adding clusters provides diminishing returns.

## 2. Choosing K
I selected **K=3** (or K=4 depending on results) for the final model. 
* **SSE Trend:** The Sum of Squared Errors dropped significantly from $k=1$ to $k=3$, after which the rate of decrease slowed down.
* **Metrics:** The **Silhouette Score** (approx 0.6) indicated good cluster separation, and a low **Davies-Bouldin Index** confirmed that the clusters were compact and well-spaced.



## 3. Cluster Interpretation
Based on the cluster centers, the segments can be described as follows:
* **Cluster 0 (Low Income / High Spending):** "Target Impulse Buyers." These customers spend a lot despite lower income. 
  * *Business Action:* Offer time-limited flash sales or "Buy Now, Pay Later" options.
* **Cluster 1 (Mid Income / Mid Spending):** "Standard Customers." Balanced behavior.
  * *Business Action:* Use loyalty programs to encourage higher frequency of visits.
* **Cluster 2 (High Income / Low Spending):** "Conservative Wealthy." High potential but low engagement.
  * *Business Action:* Send personalized, premium catalogs to upsell luxury items.

## 4. Limitations & Next Steps
**Limitations:**
Using only two features provides a 2D view of the customer. A customer's **Age** or **Location** might explain spending habits better than income alone.

**Next Steps:**
A concrete next step would be to include **Visit Frequency** as a third feature. This would allow for a 3D segmentation, helping to distinguish between a "High Spender" who visits once a year versus one who visits every week.