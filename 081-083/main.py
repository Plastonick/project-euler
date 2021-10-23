import numpy as np


def split_row(row):
    return row.split(",")


f = open("path_sum", "r")
path = f.read().split("\n")
path = list(map(split_row, path))

minimal_sum = np.zeros([80, 80])
# pre-fill the left and top edges since they work a little differently:
running_sum = 0
for i in range(80):
    running_sum += int(path[i][0])
    minimal_sum[i][0] = running_sum

running_sum = 0
for j in range(80):
    running_sum += int(path[0][j])
    minimal_sum[0][j] = running_sum

# compute the minimal sum to each index
for i in range(1, 80):
    for j in range(1, 80):
        top = minimal_sum[i - 1][j]
        left = minimal_sum[i][j - 1]

        if top < left:
            minimal_sum[i][j] = top + int(path[i][j])
        else:
            minimal_sum[i][j] = left + int(path[i][j])


print(minimal_sum[79][79])
