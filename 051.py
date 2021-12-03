import numpy as np

def isPrime(number):
    for i in range(2, int(np.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def numberToArray(number):
    digitArray = []

    while number >= 1:
        lastDigit = number % 10
        digitArray.append(lastDigit)
        number -= lastDigit
        number /= 10

    return digitArray

def arrayToNumber(array):
    number = 0
    power = 1

    for digit in array:
        number += digit * power
        power *= 10

    return number

def numValidPrimes(digitArray, indexes):
    count = 0

    for i in range(0, 10):
        for index in indexes:
            digitArray[index] = i

        number = arrayToNumber(digitArray)

        if isPrime(number):
            count += 1

    return count


digitArray = numberToArray(56003)

print(numValidPrimes(digitArray, [1, 2]))


# primeList = []

# for i in range(1, 100000):
#     if isPrime(i):
#         primeList.append(i)

# print(primeList)