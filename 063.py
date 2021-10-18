import math

count = 0
for i in range(1, 10):
    for j in range(1, 100):
        power = int(math.pow(i,j))
        order = len(str(power))
        # print(str(i) + "^" + str(j) + " = " + str(power) + " which is order " + str(order))
        
        if order == j:
            print(str(i) + "^" + str(j) + " = " + str(power))
            count += 1
            
print(count)