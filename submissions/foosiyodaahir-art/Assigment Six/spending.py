import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, davies_bouldin_score



df = pd.read_csv("spending_l9_dataset.csv")

# print("=== DATA INFO ===")
# print(df.info())
# print("\nFirst 5 rows:")
# print(df.head())




X = df[["Income_$", "SpendingScore"]]


X = X.fillna(X.median())


scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# print("\n=== ELBOW CHECK (SSE) ===")


for k in range(1, 11):
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    kmeans.fit(X_scaled)
    print(f"k={k} → SSE={kmeans.inertia_:.2f}")


K = 3   

kmeans = KMeans(n_clusters=K, random_state=42, n_init=10)
labels = kmeans.fit_predict(X_scaled)

df["Cluster"] = labels
sil_score = silhouette_score(X_scaled, labels)
dbi_score = davies_bouldin_score(X_scaled, labels)

# print("\n=== CLUSTER EVALUATION ===")
# print(f"Silhouette Score : {sil_score:.3f}")
# print(f"Davies–Bouldin   : {dbi_score:.3f}")




centers_scaled = kmeans.cluster_centers_
centers_original = scaler.inverse_transform(centers_scaled)

centers_df = pd.DataFrame(
    centers_original,
    columns=["Income_$", "SpendingScore"]
)

centers_df.index.name = "Cluster"

print("\n=== CLUSTER CENTERS (Original Units) ===")
print(centers_df.round(2))

print("\n=== SANITY CHECK (3 SAMPLE ROWS) ===")
print(df[["Income_$", "SpendingScore", "Cluster"]].sample(3))
df.to_csv("spending_labeled_clusters.csv", index=False)

print("\nFile saved as spending_labeled_clusters.csv")