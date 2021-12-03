freqs = [
    (1, 2),
    (3, 4),
    (4, 5),
    (6, 2),
    (5, 18),
    (0, 18),
    (9, 18)
]

sortedRanks = sorted(freqs, key=lambda x: (x[1], x[0]))

print(sortedRanks)
