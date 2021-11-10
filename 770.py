from fractions import Fraction
import sys
sys.setrecursionlimit(10000)

evs = {}


def get_ev(n_takes, n_gives) -> Fraction:
    if n_takes == 0:
        return 2 ** n_gives

    if n_gives == 0:
        return 1

    address = (n_takes, n_gives)
    if address not in evs:
        y = get_ev(n_takes - 1, n_gives)
        z = get_ev(n_takes, n_gives - 1)

        # let the bet amount be x, then consider player B
        # either takes or gives. If B takes, then we need
        # the expected value given that situation (y),
        # similarly for the situation in which B gives (z).
        # so our ev before we know what B does is:
        # y * (1 - x) = z * (1 + x)
        # which re-arranges to give the below equation for
        # our optimal bet amount.
        bet_amount = (y - z) / (y + z)

        evs[address] = Fraction(y * (1 - bet_amount))

    return evs[address]


# At present, this is probably "right" but much too slow!
# It turns out the ev grows very slowly eventually, in
# fact, 2 is _probably_ the limit to what player A can
# expect to make.

target = 1.7
i = 0
while True:
    ev = get_ev(i, i)
    # print(i, float(ev))
    if ev > target:
        print(i, float(ev))
        break

    i += 1
