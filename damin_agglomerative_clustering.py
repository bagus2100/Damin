# -*- coding: utf-8 -*-
"""Damin_Agglomerative_Clustering.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yC2qANHxulLPoQTivqN0YFBemYbkQy28
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#initialize dataset
df = pd.DataFrame({
    'x': [30, 23, 45, 56, 17, 22, 34, 60, 65, 54, 25, 59, 58, 21, 36, 15, 46, 22, 64],
    'y': [68, 54, 23, 12, 35, 74, 28, 53, 78, 21, 64, 24, 67, 20, 18, 63, 54, 78, 81]
})
dataset=df.to_numpy()
print(dataset)

points = dataset
import scipy.cluster.hierarchy as sch
from sklearn.cluster import AgglomerativeClustering

#ilustrasi dendogram dataset
dendrogram = sch.dendrogram(sch.linkage(points, method='ward'))

df.plot.scatter(x='x', y='y')

#agglomerative clustering
hc = AgglomerativeClustering(n_clusters=5, affinity='euclidean', linkage='ward')
#hasil agglomerative clustering
y_hc = hc.fit_predict(points)
print(np.where(y_hc == 0))
print(np.where(y_hc == 1))
print(np.where(y_hc == 2))
print(np.where(y_hc == 3))
print(np.where(y_hc == 4))

#visualisasi clustering
plt.scatter(points[y_hc==0,0], points[y_hc==0,1], s=100, c='black')
plt.scatter(points[y_hc==1,0], points[y_hc==1,1], s=100, c='red')
plt.scatter(points[y_hc==2,0], points[y_hc==2,1], s=100, c='green')
plt.scatter(points[y_hc==3,0], points[y_hc==3,1], s=100, c='blue')
plt.scatter(points[y_hc==4,0], points[y_hc==4,1], s=100, c='yellow')