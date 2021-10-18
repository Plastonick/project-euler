import numpy as np

max_val = 0
max_i = 0

def phi(n): 
    num = 0
    for i in range(1, n):
        if np.gcd(i, n) == 1:
            num += 1
            
    return num

for i in range(2, 1000000):
    phi_n = phi(i)
    
    if i / phi_n > max_val:
        max_i = i
        max_val = i / phi_n
    
print(max_i)
print(max_val)
        