import numpy as np
from matplotlib.pyplot import figure, show
from scipy.cluster.hierarchy import linkage, dendrogram
from basic_operations import get_matrix

from scipy.spatial.distance import squareform


def draw_dendrogram(x, method='single', metric='euclidean'):
    """
    e.g
    a = \"""o1 o2 o3 o4 o5 o6 o7 o8 o9
o1 0.00 3.85 4.51 4.39 4.08 3.97 2.18 3.29 5.48
o2 3.85 0.00 2.19 3.46 3.66 3.93 3.15 3.47 4.11
o3 4.51 2.19 0.00 3.70 4.30 4.83 3.86 4.48 4.19
o4 4.39 3.46 3.70 0.00 1.21 3.09 4.12 3.22 3.72
o5 4.08 3.66 4.30 1.21 0.00 2.62 4.30 2.99 4.32
o6 3.97 3.93 4.83 3.09 2.62 0.00 4.15 1.29 3.38
o7 2.18 3.15 3.86 4.12 4.30 4.15 0.00 3.16 4.33
o8 3.29 3.47 4.48 3.22 2.99 1.29 3.16 0.00 3.26
o9 5.48 4.11 4.19 3.72 4.32 3.38 4.33 3.26 0.00\"""

    draw_dendrogram(a, method='single')

    :param x:
    :param method: single complete average centroid median ward weighted
    single is min, complete is max
    :param metric:
    :return: prints result
    """
    data = get_matrix(x)
    data = np.array(data)
    z = linkage(squareform(data), method=method, metric=metric, optimal_ordering=True)
    figure(2, figsize=(10, 4))
    dendrogram(z, count_sort='descendent', labels=list(range(1, len(data[0]) + 1)))
    show()


a = """O1 O2 O3 O4 O5 O6 O7 O8 O9 O10
O1 0 8.55 0.43 1.25 1.14 3.73 2.72 1.63 1.68 1.28
O2 8.55 0 8.23 8.13 8.49 6.84 8.23 8.28 8.13 7.66
O3 0.43 8.23 0 1.09 1.10 3.55 2.68 1.50 1.52 1.05
O4 1.25 8.13 1.09 0 1.23 3.21 2.17 1.29 1.33 0.56
O5 1.14 8.49 1.10 1.23 0 3.20 2.68 1.56 1.50 1.28
O6 3.73 6.84 3.55 3.21 3.20 0 2.98 2.66 2.50 3.00
O7 2.72 8.23 2.68 2.17 2.68 2.98 0 2.28 2.30 2.31
O8 1.63 8.28 1.50 1.29 1.56 2.66 2.28 0 0.25 1.46
O9 1.68 8.13 1.52 1.33 1.50 2.50 2.30 0.25 0 1.44
O10 1.28 7.66 1.05 0.56 1.28 3.00 2.31 1.46 1.44 0"""
draw_dendrogram(a, method='average')
