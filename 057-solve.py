from fractions import Fraction
from math import log10

def resolveIteration(iter: int) -> Fraction:
    value = Fraction(1, 2)

    for i in range(0, iter - 1):
        value = Fraction(1, 2 + value)

    return 1 + value

numExceeding = 0
for i in range(1, 1001):
    fraction = resolveIteration(i)
    print(i)
    print(fraction)
    
    numeratorDigits = int(log10(fraction.numerator))
    denominatorDigits = int(log10(fraction.denominator))

    if numeratorDigits > denominatorDigits:
        numExceeding += 1

print(numExceeding)