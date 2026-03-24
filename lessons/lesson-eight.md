# 📘 Lesson 8 – Clustering (Unsupervised Learning)

✅ In **Lesson 4**, we studied Regression (predicting numbers).
✅ In **Lesson 6**, we studied Classification (predicting categories).
✅ In **Lesson 7**, we practiced Spam Detection with Logistic Regression and Random Forest.

👉 **Now in Lesson 8, we explore Clustering – the first major Unsupervised Learning method.**

---

## 🎯 Learning Objectives

By the end of this lesson, students will be able to:

* Understand what **Clustering** is and how it differs from supervised learning.
* Learn about common **Clustering algorithms**:

  * K-Means
  * Hierarchical Clustering
  * DBSCAN
* Understand how to **evaluate clustering models** using metrics:

  * Elbow Method
  * Silhouette Score
  * Davies–Bouldin Index

---

## 1) Introduction

In supervised learning, we train models with **labeled data** (we know the answers).

But what if we don’t have labels?
👉 That’s where **Unsupervised Learning** comes in.

* **Clustering** = grouping data points into clusters based on similarity.
* The algorithm has no labels; it must **discover hidden patterns**.

---

## 2) What is Clustering?

**Definition:**

* Clustering is a method of unsupervised learning where the algorithm automatically groups data into clusters such that **items in the same cluster are more similar to each other than to those in other clusters**.

---

### Real-World Examples

* 🛒 **Market Segmentation** – group customers by purchasing behavior.
* 📱 **App Users** – group users into active vs casual usage clusters.
* 🧬 **Genetics** – group DNA sequences based on similarity.
* 📷 **Image Segmentation** – group pixels into regions (sky, land, water).

---

### Contrast with Supervised Learning

* **Supervised (Regression/Classification):**

  * Needs **labels** (prices, categories).
  * Example: Spam/Not Spam.

* **Unsupervised (Clustering):**

  * No labels, algorithm finds structure.
  * Example: Grouping customers into segments.

📌 **Key Point:**
Supervised = *with answers*.
Unsupervised = *find the hidden patterns yourself*.

---

## 3) Clustering Algorithms

### a) K-Means Clustering

* **Idea:** Partition data into *k* clusters.
* **Steps:**

  1. Choose number of clusters (*k*).
  2. Randomly assign cluster centers (centroids).
  3. Assign each point to nearest centroid.
  4. Recalculate centroids.
  5. Repeat until stable.
* **Best for:** Spherical/round clusters, large datasets.
* **Limitation:** Must pick *k* beforehand, struggles with irregular shapes & noise.

---

### b) Hierarchical Clustering

* **Idea:** Build a **tree of clusters** (dendrogram).
* **Types:**

  * **Agglomerative (bottom-up):** Start with each point → merge step by step.
  * **Divisive (top-down):** Start with all points → split step by step.
* **Best for:** Understanding data relationships at multiple levels.
* **Limitation:** Computationally expensive, sensitive to noise.

---

### c) DBSCAN (Density-Based Spatial Clustering of Applications with Noise)

* **Idea:** Group dense regions, mark sparse points as noise.
* **Steps:**

  1. Pick ε (neighborhood size) + minPts (minimum points in a dense region).
  2. Core points form clusters if density ≥ minPts.
  3. Points not belonging to any cluster → **noise/outliers**.
* **Best for:** Irregular shapes, outlier detection.
* **Limitation:** Sensitive to parameter choice, struggles if density varies a lot.

---

📌 **Important Note:**
Clustering algorithms are **not limited** to these three.
👉 Others include **Gaussian Mixture Models (GMM), Mean-Shift, Spectral Clustering**.

The key is to **understand how clustering works** and choose the algorithm that fits your data.

---

## 4) Clustering Metrics

Unlike supervised ML (where you check accuracy, precision, etc.), clustering has no “ground truth” labels.
👉 So we use **special metrics** to measure how well clusters are formed.

---

### 1) Elbow Method (for K-Means)

**Goal:** Find the best number of clusters (`k`).

**Steps:**

1. Run K-Means with different values of `k` (e.g., 1 → 10).
2. Calculate **SSE (Sum of Squared Errors)** = how far points are from their cluster centers.
3. Plot `k` vs. SSE.
4. Look for the **“elbow point”** — where SSE stops dropping sharply.

👉 Example:

* k=2 → SSE=400
* k=3 → SSE=250
* k=4 → SSE=180
* k=5 → SSE=175

At **k=4**, improvement slows down → 4 clusters is best.

📌 **Use when:** You want to estimate the right number of clusters for K-Means.

---

### 2) Silhouette Score

**Goal:** Measure how good the cluster separation is.

**Formula (intuitive idea):**

* Score = (Separation from other clusters – Cohesion inside cluster) / max
* Range: **-1 to +1**

**Interpretation:**

* **+1** → Perfect clustering (well-separated).
* **0** → Overlapping clusters.
* **-1** → Wrong clustering (points in wrong groups).

👉 Example:

* Silhouette = 0.65 → Good separation.
* Silhouette = 0.25 → Weak separation.
* Silhouette = -0.1 → Bad clustering.

📌 **Use when:** You want a single number to evaluate cluster quality.

---

### 3) Davies–Bouldin Index

* Measures **average similarity between clusters**.
* Lower score = better separation.

---

### Quick Comparison

| Metric           | What it Measures                | Good Value Means | Typical Use                |
| ---------------- | ------------------------------- | ---------------- | -------------------------- |
| **Elbow Method** | SSE drop vs `k`                 | Clear “bend”     | Finding number of clusters |
| **Silhouette**   | Cohesion + Separation           | Close to +1      | Overall cluster quality    |
| **DB Index**     | Avg similarity between clusters | Lower is better  | Compare clustering models  |

---

👉 **Key Idea:**

* **Elbow Method** = choose best `k`.
* **Silhouette Score** = check cluster quality.
* **DB Index & others** = compare multiple clustering solutions.

---

## ✅ Lesson Summary

* **Clustering** = unsupervised learning for grouping data.
* Main algorithms: **K-Means, Hierarchical, DBSCAN**.
* Evaluation metrics: **Elbow Method, Silhouette Score, Davies–Bouldin Index**.
* Key difference:

  * Supervised = with labels.
  * Unsupervised = without labels.

---

## 🔚 End of Lesson 8

🎉 Congratulations! You’ve completed **Clustering – your first Unsupervised Learning method in Machine Learning.**

---