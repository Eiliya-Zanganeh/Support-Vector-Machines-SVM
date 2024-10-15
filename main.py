from sklearn import svm
from sklearn.datasets._samples_generator import make_blobs

import matplotlib.pyplot as plt
import numpy as np

x, y = make_blobs(n_samples=40, centers=2, random_state=1, n_features=2)

# model = svm.SVC(kernel='linear')

# print(x.shape)
# print(y.shape)
# print(x[5])
# print(y[5])

# model.fit(x, y)

# plt.scatter(x[:, 0], x[:, 1], c=y, s=30, cmap=plt.cm.Paired)
# plt.show()

# ----------------------------------------------------------------

model = svm.SVC(kernel='linear', C=1000)
model.fit(x, y)

plt.scatter(x[:, 0], x[:, 1], c=y, s=30, cmap=plt.cm.Paired)
ax = plt.gca()
xlim = ax.get_xlim()
ylim = ax.get_ylim()
xx = np.linspace(xlim[0], xlim[1], 30)
yy = np.linspace(ylim[0], ylim[1], 30)
YY, XX = np.meshgrid(yy, xx)
xy = np.vstack([XX.ravel(), YY.ravel()]).T
Z = model.decision_function(xy).reshape(XX.shape)
ax.contour(XX, YY, Z, colors='k', levels=[-1, 0, 1], alpha=0.5, linestyles=['--', '-', '--'])
ax.scatter(model.support_vectors_[:, 0], model.support_vectors_[:, 1], s=100, linewidths=1, facecolors='none')
plt.show()