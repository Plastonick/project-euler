def get_combinations(target: int, minimum: int) -> set[str]:
    count = 0

    for i in range(minimum, target + 1):
        if target == i:
            count += 1
        else:
            count += get_combinations(target - i, i)

    return count


for t in range(100, 101):
    print(t, get_combinations(t, 1) - 1)
