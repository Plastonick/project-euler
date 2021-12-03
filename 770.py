from fractions import Fraction
import matplotlib.pyplot as plt
import sys
sys.setrecursionlimit(10000)

evs = {}
evs2 = {}


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
        # Since both are linear, and one has a positive and
        # one a negative gradient, we know their
        # intersection gives us our maximum-minimum.
        bet_amount = Fraction(y - z, y + z)

        evs[address] = Fraction(y * (1 - bet_amount))

    return evs[address]


def get_ev_2(n_takes, n_gives):
    if n_takes == 0:
        return (2 ** n_gives, 1)

    if n_gives == 0:
        return (1, 1)

    address = (n_takes, n_gives)
    if address not in evs2:
        y = get_ev_2(n_takes - 1, n_gives)
        z = get_ev_2(n_takes, n_gives - 1)

        y0 = y[0]
        y1 = y[1]
        z0 = z[0]
        z1 = z[1]

        # let the bet amount be x, then consider player B
        # either takes or gives. If B takes, then we need
        # the expected value given that situation (y),
        # similarly for the situation in which B gives (z).
        # so our ev before we know what B does is:
        # y * (1 - x) = z * (1 + x)
        # which re-arranges to give the below equation for
        # our optimal bet amount.
        # Since both are linear, and one has a positive and
        # one a negative gradient, we know their
        # intersection gives us our maximum-minimum.
        # bn = y[0]*z[1] - z[0]*y[1]
        # bd = y[0]*z[1] + z[0]*y[1]

        n = 2 * y0 * z0
        d = (y0 * z1) + (y1 * z0)

        evs2[address] = (n, d)

    return evs2[address]


# At present, this is probably "right" but much too slow!
# It turns out the ev grows very slowly eventually, in
# fact, 2 is _probably_ the limit to what player A can
# expect to make.

get_ev_2(100, 100)

exit()
print(evs2)

for i in range(5):
    print(get_ev_2(i, i))

# plt.plot(points)
# plt.ylabel('some numbers')
# plt.show()

# exit()

target = 1.9999
i = 0
while True:
    ev = get_ev_2(i, i)
    # print(i, float(ev))
    if ev[0] / ev[1] > target:
        print(i, ev)
        break

    i += 1
