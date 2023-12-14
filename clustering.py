import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

# Tạo dữ liệu mẫu
np.random.seed(42)
data, labels = make_blobs(n_samples=300, centers=5, random_state=42)

# Áp dụng thuật toán K-Means với k=4
kmeans = KMeans(n_clusters=5)
kmeans.fit(data)
cluster_centers = kmeans.cluster_centers_
cluster_labels = kmeans.labels_

# Hiển thị kết quả phân cụm
plt.scatter(data[:, 0], data[:, 1], c=cluster_labels, cmap='viridis', edgecolor='k')
plt.scatter(cluster_centers[:, 0], cluster_centers[:, 1], c='red', marker='X', s=200, label='Centroids')
plt.title('K-Means Clustering')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.show()

# Hiển thị các trung tâm phân cụm
print("Cluster Centers:")
print(cluster_centers)

# Hiển thị các nhãn phân cụm cho từng điểm dữ liệu
print("\nCluster Labels:")
print(cluster_labels)
