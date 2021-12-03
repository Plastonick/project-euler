def digitSum(number) -> int:
    digitSum = 0
    for char in str(number):
        digitSum += int(char)

    return digitSum


maxsum = 0

for i in range(1, 100):
    for j in range(1, 100):
        power = pow(i, j)
        sum = digitSum(power)

        # print(power)
        # print(sum)
        # print()

        # exit()

        if sum > maxsum:
            maxsum = sum

print(maxsum)
