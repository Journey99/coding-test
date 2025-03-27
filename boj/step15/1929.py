# 소수 구하기
import math

def is_prime(x):
    if x < 2:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(x))+1, 2):
        if x % i == 0:
            return False
    
    return True

m, n = map(int, input().split())

for x in range(m, n+1):
    if is_prime(x):
        print(x)
