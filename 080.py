from decimal import Decimal
from math import sqrt


def sqrt_to_precision(target, precision):
    s = 0
    for _ in range(precision):
        while s ** 2 < target:
            s += 1

        s -= 1
        s *= 10
        target *= 100

    return s


sum = 0
for i in range(1, 101):
    root = sqrt(i)
    if int(root) ** 2 != i:
        precision_root = sqrt_to_precision(i, 100)

        for digit in str(precision_root)[:101]:
            if digit != '.':
                sum += int(digit)


print(sum)
