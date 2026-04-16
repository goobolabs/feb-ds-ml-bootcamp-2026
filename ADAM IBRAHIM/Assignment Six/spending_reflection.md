# Spending Pattern Analysis – Reflection

## 1. What I Implemented
I applied **K-Means clustering** to segment customers based on `Income_$` and `SpendingScore`.  
The workflow included:
- Handling missing values with median imputation.
- Scaling features using `StandardScaler`.
- Running an SSE loop for k=1..5 to check the elbow.
- Training K-Means with the chosen k.
- Evaluating clusters using **Silhouette Score** and **Davies–Bouldin Index**.
- Labeling the dataset and saving results.

---

## 2. Choosing K
I selected **K=3** because:
- The SSE curve dropped sharply until k=3, then flattened.
- The Silhouette Score was 0.501, showing moderate separation.
- The Davies–Bouldin Index was 0.083, indicating strong cluster separation.

---

## 3. Cluster Interpretation
- **Cluster 0: Low Income / High Spending**  
  Customers spend heavily despite lower income.  
  *Business Action:* Offer loyalty discounts or budgeting support.

- **Cluster 1: Low Income / Moderate Spending**  
  Customers spend moderately within their means.  
  *Business Action:* Encourage upselling with affordable bundles.

- **Cluster 2: Moderate Income / High Spending**  
  Customers have higher income and spend actively.  
  *Business Action:* Target with premium offers and exclusive promotions.

---

## 4. Limitations & Next Steps
- Current segmentation only uses **Income** and **SpendingScore**.  
- Adding features like **Age**, **Visit Frequency**, or **Online Purchases** could improve insights.  
- Next step: Experiment with **DBSCAN** or include more features for richer segmentation.
