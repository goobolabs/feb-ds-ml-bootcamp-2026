import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler 
from sklearn.cluster import KMeans 
from sklearn.metrics import silhouette_score, davies_bouldin_score

df = pd.read_csv("spending_l9_dataset.csv")

df = df.head()

#STEP THREE Prepare Features
X = df[["Income_$", "SpendingScore"]]
# H missing valuse with median
X = X.fillna(X.median())
# Scaling features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

#STEP FOUR Elbow Check (SSE)
max_k = min(10, len(X_scaled))   # make sure k never exceeds number of samples
for k in range(1, max_k + 1):
    kmeans = KMeans(n_clusters=k, random_state=42)
    kmeans.fit(X_scaled)
    print(f"k={k} -> SSE={kmeans.inertia_:.2f}")


#STEP FIVE Model Training (Pick K)
kmeans = KMeans(n_clusters=3, random_state=42)
labels = kmeans.fit_predict(X_scaled)
df["Cluster"] = labels

#STEP SIX Evaluate Clustering
sil = silhouette_score(X_scaled, labels)
dbi = davies_bouldin_score(X_scaled, labels)

print("Silhouette Score :", round(sil, 3))
print("Davies–Bouldin   :", round(dbi, 3))

#STEP SEVEN Cluster Centers (Original Units
centers_scaled = kmeans.cluster_centers_
centers = scaler.inverse_transform(centers_scaled)
centers_df = pd.DataFrame(centers, columns=["Income_$", "SpendingScore"])
print("=== CLUSTER CENTERS (Original Units) ===")
print(centers_df.round(2))

#STEP EIGHT Sanity Check
print(df[["Income_$", "SpendingScore", "Cluster"]].sample(3))

#STEP NINE Save Output
df.to_csv("spending_labeled_clusters.csv", index=False)
