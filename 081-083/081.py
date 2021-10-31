import numpy as np
from numpy.core.numeric import Inf


def split_row(row):
    return row.split(",")


f = open("path_sum", "r")
path = f.read().split("\n")
path = list(map(split_row, path))

minimal_sum = np.zeros([80, 80])

# compute the minimal sum to each index
for i in range(0, 80):
    for j in range(0, 80):
        if i == 0 and j == 0:
            minimal_sum[i][j] = int(path[i][j])
            continue

        if i == 0:
            minimal_sum[i][j] = minimal_sum[i][j - 1] + int(path[i][j])
            continue

        if j == 0:
            minimal_sum[i][j] = minimal_sum[i - 1][j] + int(path[i][j])
            continue

        shortest_path = min(minimal_sum[i][j - 1], minimal_sum[i - 1][j])
        minimal_sum[i][j] = shortest_path + int(path[i][j])


print(minimal_sum[79][79])
