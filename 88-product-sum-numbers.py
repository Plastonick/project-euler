from functools import reduce
from __future__ import annotations

def validSet(set: list[int]) -> int:
    setSum = sum(set)
    setProduct = reduce((lambda x, y: x * y), set)

    if setSum > setProduct:
        return 1
    elif setSum == setProduct:
        return 0
    else:
        return -1

def getMinimumProductSumNumber(size: int) -> int:
    set = [1 for i in range(size)]

    print(set)

    return 0

getMinimumProductSumNumber(5)