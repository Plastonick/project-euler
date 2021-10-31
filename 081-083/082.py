import numpy as np
import sys

from numpy.core.numeric import Inf
sys.setrecursionlimit(10000)

# actually did 83 before this, then adapted 83 for this problem.


def split_row(row):
    return row.split(",")


f = open("081-083/path_sum", "r")
path = f.read().split("\n")
path = list(map(split_row, path))

minimal_sum = np.zeros([80, 80])

# for i in range(80):
#     minimal_sum[i][0] = int(path[i][0])


def get_minimal_sum_value(i, j):
    if i < 0 or i > 79:
        return None

    if j < 0 or j > 79:
        return None

    return minimal_sum[i][j]


def get_path_value(i, j):
    if i < 0 or i > 79:
        return None

    if j < 0 or j > 79:
        return None

    return int(path[i][j])


class Path:
    i = 0
    j = 0
    cost = 0

    def __init__(self, i, j, cost):
        self.i = i
        self.j = j
        self.cost = cost

    def move(self, d_i, d_j):
        move_point = get_minimal_sum_value(self.i + d_i, self.j + d_j)
        # cost_point = get_path_value(self.i + d_i, self.j + d_j)

        # check it's a valid direction to move to
        if move_point is not None and move_point == 0.0:
            return Path(self.i + d_i, self.j + d_j, self.cost + int(path[self.i + d_i][self.j + d_j]))
        else:
            return None

    def get_next_resistance(self):
        best = Path(0, 0, Inf)

        # don't check left for problem 82
        # left = self.move(0, -1)
        # if left:
        #     best = left

        right = self.move(0, 1)
        if right and right.cost < best.cost:
            best = right

        up = self.move(-1, 0)
        if up and up.cost < best.cost:
            best = up

        down = self.move(1, 0)
        if down and down.cost < best.cost:
            best = down

        if best.cost != Inf:
            return best
        else:
            return None


paths: list[Path] = []
for i in range(80):
    paths.append(Path(i, 0, int(path[i][0])))


def hydrate_minimal_sum():
    best_progression = Path(0, 0, Inf)
    dead_ends = []
    for i, path in enumerate(paths):
        next_path = path.get_next_resistance()

        # there's no where valid for this path to go
        if next_path is None:
            dead_ends.append(i)

        # this is possibly the best path going forward
        elif next_path.cost < best_progression.cost:
            best_progression = next_path

    # we've not found a progression!
    if best_progression.cost == Inf:
        return

    # we have found the next best progression
    # remove dead ends from our paths, reverse order
    # so we don't muck with the indexing
    dead_ends.sort(reverse=True)
    for i in dead_ends:
        del paths[i]

    # add our best path to the list, and hydrate minimal_sum
    paths.append(best_progression)
    minimal_sum[best_progression.i][best_progression.j] = best_progression.cost

    # keep going!
    hydrate_minimal_sum()


hydrate_minimal_sum()

min = Inf
for i in range(80):
    if minimal_sum[i][79] < min:
        min = minimal_sum[i][79]

print(min)
