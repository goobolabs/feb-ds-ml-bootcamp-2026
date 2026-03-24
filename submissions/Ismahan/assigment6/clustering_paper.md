# Clustering in Machine Learning – Assignment 6

## 1. Introduction to Clustering

**Clustering** is an **unsupervised learning** technique in Machine Learning that groups data points into clusters based on similarity. Unlike supervised learning, clustering does **not require labeled data**; instead, it identifies inherent patterns or structures within the dataset. 

In contrast, **supervised learning** uses labeled data to train models to predict outcomes. For example:  

- **Clustering example:** Segmenting customers based on purchasing behavior without predefined categories.  
- **Supervised learning example:** Predicting whether an email is spam or not (classification) using labeled data.

The main goal of clustering is to ensure that data points within the same cluster are **similar to each other** and **different from points in other clusters**. This technique is widely used in exploratory data analysis and pattern discovery.

---

## 2. Clustering Algorithms

### **2.1 K-Means**

**How it works:**  
K-Means partitions data into *k* clusters by assigning each point to the nearest cluster centroid and updating centroids iteratively until convergence. The algorithm minimizes the **within-cluster sum of squares (WCSS)**.

**Real-world use case:**  
Customer segmentation in marketing, e.g., grouping customers based on purchase frequency and spending habits.

**Advantages:**  
- Simple and fast  
- Scales well with large datasets  

**Limitations:**  
- Requires the number of clusters (k) to be specified  
- Sensitive to outliers  
- Assumes clusters are spherical and equally sized  

---

### **2.2 Hierarchical Clustering**

**How it works:**  
Hierarchical clustering builds a **tree-like structure (dendrogram)**. There are two approaches:  
- **Agglomerative (bottom-up):** Starts with each data point as its own cluster and merges closest clusters iteratively.  
- **Divisive (top-down):** Starts with all points in one cluster and splits iteratively.

**Real-world use case:**  
Grouping genes with similar expression patterns in bioinformatics.

**Advantages:**  
- Does not require specifying the number of clusters initially  
- Provides a visual hierarchy of clusters  

**Limitations:**  
- Computationally expensive for large datasets  
- Sensitive to noise and outliers  

---

### **2.3 DBSCAN (Density-Based Spatial Clustering of Applications with Noise)**

**How it works:**  
DBSCAN groups points that are **densely packed** and marks points in low-density regions as outliers. It uses two parameters: **eps** (distance threshold) and **min_samples** (minimum points to form a cluster).

**Real-world use case:**  
Identifying areas of high crime density in city maps or detecting anomalies in network traffic.

**Advantages:**  
- Can detect arbitrarily shaped clusters  
- Robust to outliers  

**Limitations:**  
- Choosing appropriate eps and min_samples can be difficult  
- Not suitable for datasets with varying density  

---

## 3. Clustering Metrics

### **3.1 Elbow Method**
Measures the **within-cluster sum of squares (WCSS)** for different k values. The "elbow" point suggests the optimal number of clusters.  
- **Good value:** At the point where WCSS decrease slows (elbow).  
- **Use:** Helps determine the number of clusters for K-Means.  

### **3.2 Silhouette Score**
Measures how similar a point is to its own cluster compared to other clusters. Ranges from -1 to 1.  
- **Good value:** Close to 1 → well-clustered; negative → misclassified.  
- **Use:** Evaluates cluster quality for any clustering algorithm.  

### **3.3 Davies–Bouldin Index (DBI)**
Measures **average similarity between clusters** (ratio of intra-cluster distance to inter-cluster distance).  
- **Good value:** Lower DBI → better clustering  
- **Use:** Compares clustering quality across different models.

| Metric               | Measures                                | Good Value                 | Most Useful For                    |
|---------------------|----------------------------------------|----------------------------|-----------------------------------|
| Elbow Method         | Within-cluster sum of squares           | “Elbow point”              | Choosing k for K-Means            |
| Silhouette Score     | Cluster cohesion and separation         | Close to 1                 | Evaluating cluster quality        |
| Davies–Bouldin Index | Inter-cluster vs intra-cluster distance | Low                        | Comparing different clustering models |

---

## 4. Challenges in Clustering

Clustering is **harder than supervised learning** because:

1. There is **no ground truth**. Metrics are often heuristic.  
2. Algorithms are sensitive to initialization, parameters, and noise.

**Common challenges:**

- **Choosing the right number of clusters (k):** Too few clusters may group distinct patterns together; too many may overfit.  
- **Handling noise and outliers:** Outliers can distort cluster centroids or density measures.  
- **High-dimensional data:** Distance-based clustering may perform poorly due to the curse of dimensionality.  

---

## 5. Real-World Case Study

**Project:** Customer Segmentation for E-commerce Platform  

**Goal:**  
Identify distinct customer groups to tailor marketing strategies and improve engagement.

**Data Used:**  
Purchase history, frequency, product categories, and customer demographics (~50,000 customers).

**Clustering Model Applied:**  
- **K-Means** with k=5  
- Metrics used: Elbow method to choose k, silhouette score to validate clusters  

**Key Results / Insights:**  
- Identified 5 segments: high-spending loyal, bargain hunters, occasional buyers, new customers, and inactive users.  
- Marketing campaigns were personalized per cluster, increasing engagement by 20% and repeat purchases by 15%.  

**Conclusion:**  
Clustering enabled the business to uncover hidden patterns in customer behavior and target strategies effectively.

---

*End of Clustering Paper*