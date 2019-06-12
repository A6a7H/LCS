import numpy as np
import matplotlib.pyplot as plt
import random

class K_Means:

    def __init__(self, k=2, tol=0.001, max_iter=300):
        self.k = k
        self.tol = tol
        self.max_iter = max_iter

    def fit(self,data):
        self.centroids = {}
        for i in range(self.k):
            self.centroids[i] = data[i]
        for i in range(self.max_iter):
            self.classifications = {}
            for i in range(self.k):
                self.classifications[i] = []
            for featureset in X:
                distances = [np.linalg.norm(featureset-self.centroids[centroid]) for centroid in self.centroids]
                classification = distances.index(min(distances))
                self.classifications[classification].append(featureset)
            prev_centroids = dict(self.centroids)
            for classification in self.classifications:
                self.centroids[classification] = np.average(self.classifications[classification],axis=0)
            optimized = True
            for c in self.centroids:
                original_centroid = prev_centroids[c]
                current_centroid = self.centroids[c]
                if np.sum((current_centroid-original_centroid)/original_centroid*100.0) > self.tol:
                    print(np.sum((current_centroid-original_centroid)/original_centroid*100.0))
                    optimized = False
            if optimized:
                break

    def predict(self,data):
        distances = [np.linalg.norm(data-self.centroids[centroid]) for centroid in self.centroids]
        classification = distances.index(min(distances))
        return classification



np.random.seed(123)
X1 = np.random.randn(100,2)
X2 = np.random.randn(100,2) - np.array([10,1])
X3 = np.random.randn(100,2) - np.array([1,10])
X = np.vstack((X1,X2,X3))
y = np.array([1]*100 + [2]*100 + [3]*100)
plt.plot(X1[:, 0], X1[:, 1] ,'o', color='yellow')
plt.plot(X2[:, 0], X2[:, 1], 'o', color='green')
plt.plot(X3[:, 0], X3[:, 1], 'o', color='blue')
k_means = K_Means(k=3)
k_means.fit(X)
plt.plot(k_means.centroids[0][0], k_means.centroids[0][1], '>', color='yellow')
plt.plot(k_means.centroids[1][0], k_means.centroids[1][1], '>', color='red')
plt.plot(k_means.centroids[2][0], k_means.centroids[2][1], '>', color='blue')
plt.show()
print(k_means)


