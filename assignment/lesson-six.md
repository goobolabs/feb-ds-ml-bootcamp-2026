# 🎓 Assignment – Spending Pattern Analysis with K-Means (Clustering)

**Due:** **Thursday, Feb 26, 2025 — 12:00 PM (Africa/Mogadishu / EAT)**

## **Part A – Practical (Jupyter Notebook)**

**Objective:**
Implement **customer spending segmentation** using **K-Means** on `Income_$` and `SpendingScore`. Evaluate multiple values of **k**, choose the best based on printed metrics, and label the dataset.

---

### **Instructions**

1. **Notebook Setup**

   * Create a Jupyter Notebook named:
     `spending_clustering.ipynb`.

2. **Load Dataset**

   * Use the provided dataset: `dataset/spending_l9_dataset.csv`.

3. **Prepare Features**

   * Features (`X`) = `["Income_$", "SpendingScore"]`.
   * Handle any missing values via **median** (numeric only).
   * Scale features with `StandardScaler`.

4. **Elbow Check (SSE)**

   * Loop `k = 1..10`, fit KMeans, **print**:
     `k=… → SSE=…` (no plots).

5. **Model Training (Pick K)**

   * Choose a reasonable **K** (e.g., 2–5) based on your SSE trend.
   * Fit final `KMeans(n_clusters=K, random_state=42)` and get labels.
   * Add `Cluster` column to the DataFrame.

6. **Evaluate Clustering**

   * Compute and print:

     * **Silhouette Score** (higher → better separation)
     * **Davies–Bouldin Index (DBI)** (lower → better separation)

7. **Cluster Centers (Original Units)**

   * Inverse-transform the cluster centers back to original units.
   * Print a small table of **centers for each cluster** (rounded).

8. **Sanity Check**

   * Print **three sample rows** (any indices) with `Income_$`, `SpendingScore`, and `Cluster`.

9. **Save Output**

   * Save the labeled file as: `spending_labeled_clusters.csv`.

---

### **Expected Output**

* Printed **SSE** for `k = 1..10` (Elbow check).
* Printed **Silhouette** and **DBI** for your chosen `K`. Example:

  ```
  Silhouette Score : 0.642
  Davies–Bouldin   : 0.512
  ```
* Printed **cluster centers** in original units, e.g.:

  ```
  === CLUSTER CENTERS (Original Units) ===
           Income_$  SpendingScore
  Cluster
  0           28.75          82.10
  1           56.30          52.40
  2           92.20          21.15
  ```
* **Sanity check** table with three customers and their assigned clusters.
* Saved file: `spending_labeled_clusters.csv`.

---

## **Part B – Reflection Paper**

Write **1–2 pages** (Markdown or PDF) answering:

1. **What did you implement?**
   Briefly describe your K-Means workflow (scaling, SSE loop, metrics, labeling).

2. **Choosing K:**

   * Which **K** did you pick and **why**?
   * Refer to **SSE**, **Silhouette**, and **DBI** you printed.

3. **Cluster Interpretation:**

   * Describe each cluster in plain language (e.g., **Low Income / High Spending**).
   * Suggest **one business action** per cluster (e.g., loyalty offer, upsell, retention).

4. **Limitations & Next Steps:**

   * What information might improve segmentation (e.g., **Age**, **Visits**, **OnlinePurchases**)?
   * One concrete next step (try 3 features, try DBSCAN, etc.).

---

### **Submission Format**

* `spending_clustering.ipynb` (all code + printed outputs)
* `spending_labeled_clusters.csv`
* `spending_reflection.md` **or** `spending_reflection.pdf`

---
