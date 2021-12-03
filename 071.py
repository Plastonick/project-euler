from fractions import Fraction
from math import ceil, floor

comparison = Fraction(3, 7)

best = Fraction(0, 1)
for denominator in range(1, 1000000):
    numerator_low = int(floor(denominator * comparison))

    frac = Fraction(numerator_low, denominator)

    if frac < comparison and frac > best:
        best = frac

print(best)
