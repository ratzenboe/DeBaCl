import numpy as np
from sklearn.datasets import make_circles, make_blobs
import matplotlib.pyplot as plt


circles = make_circles(500, factor=0.5, noise=0.06, random_state=23)
blob = make_blobs(100, centers=1, center_box=(-1.7, 1.7), cluster_std=0.1,
                  random_state=19)

X = np.vstack((circles[0], blob[0]))
print("Dataset shape:", X.shape)

with plt.style.context('ggplot'):
    fig, ax = plt.subplots(figsize=(6, 4.5))
    ax.scatter(X[:, 0], X[:, 1], c='black', s=50, alpha=0.5)
    fig.show()

import debacl as dcl
tree = dcl.construct_tree(X, k=20)

print(tree)