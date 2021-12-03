from fractions import Fraction
import sys

sys.setrecursionlimit(10000)

evs = {}
evs2 = {}


def ev(n_takes, n_gives) -> Fraction:
    if n_takes == 0:
        return 2 ** n_gives

    if n_gives == 0:
        return Fraction(1)

    address = (n_takes, n_gives)
    if address not in evs:
        y = ev(n_takes - 1, n_gives)
        z = ev(n_takes, n_gives - 1)

        # let the bet amount be x, then consider player B
        # either takes or gives. If B takes, then we need
        # the expected value given that situation (y),
        # similarly for the situation in which B gives (z).
        # so our ev before we know what B does is:
        # y * (1 - x) = z * (1 + x)
        # which re-arranges to give the below equation for
        # our optimal bet amount (x).
        # Since both are linear, and one has a positive and
        # one a negative gradient, we know their
        # intersection gives us our maxi-mini.
        bet_amount = Fraction(y - z, y + z)

        evs[address] = Fraction(y * (1 - bet_amount))

    return evs[address]


target = 1.9999
i = 0
while True:
    expected_value = ev(i, i)
    if expected_value > target:
        print(i)
        break

    i += 1
