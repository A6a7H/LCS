import numpy as np
import matplotlib.pyplot as plt
import random

class KMeans:

    def __init__(self, k):
        self.k = k
        self.means = None


    def classify(self, inputs):
        return min(range(self.k), key=lambda i: np.linalg.norm(self.means[i] - inputs))



    def train(self, inputs):
        self.means = inputs[np.random.choice(inputs.shape[0], self.k)]
        assignment = None
        while True:
            new_assignment = [self.classify(g) for g in inputs]
            # map(self.classify, inputs)
            if assignment == new_assignment:
                return
            assignment = new_assignment
            for i in range(self.k):
                point = np.array([p for p,a in zip(inputs, assignment) if a == i])
                if len(point) > 0:
                    self.means[i] = point.mean()
            plt.plot(self.means[0][0], self.means[0][1], 'v')
            plt.plot(self.means[1][0], self.means[1][1], 'v')
            plt.plot(self.means[2][0], self.means[2][1], 'v')
            plt.show()



np.random.seed(123)
X1 = np.random.randn(100,2)
X2 = np.random.randn(100,2) - np.array([10,1])
X3 = np.random.randn(100,2) - np.array([1,10])
X = np.vstack((X1,X2,X3))
y = np.array([1]*100 + [2]*100 + [3]*100)
plt.plot(X1[:, 0], X1[:, 1] ,'o', color='yellow')
plt.plot(X2[:, 0], X2[:, 1], 'o', color='green')
plt.plot(X3[:, 0], X3[:, 1], 'o', color='blue')
k_means = KMeans(3)
k_means.train(X)
print(k_means.means)


