import sys
import matplotlib.pyplot as plt
import numpy as np

max = 200


sys.setrecursionlimit(100000)
cache = {}
reads = {}


def p(target, limit):
    if limit == 0:
        return 0
    if target == 0:
        return 1
    if target < 0:
        return 0

    key = str(target) + "." + str(limit)

    if target not in reads:
        reads[target] = {}
    if limit not in reads[target]:
        reads[target][limit] = 0

    reads[target][limit] += 1

    if key not in cache:
        cache[key] = p(target, limit - 1) + p(target - limit, limit)

    return cache[key]


i = 1

while i < max:
    num_parts = p(i, i)

    if i % 1000 == 0:
        print(str(i) + " -> " + str(num_parts))

    if num_parts % 1_000_000 == 0:
        print(i)
        break

    i += 1

data_x = []
data_y = []
data_z = []

for target in reads:
    for limit in reads[target]:
        data_x.append(target)
        data_y.append(limit)
        data_z.append(1)

plt.scatter(data_x, data_y, data_z)
plt.xlabel("target")
plt.ylabel("limit")
plt.show()
