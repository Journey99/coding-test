# 베르트랑 공준
import math
import sys

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


while True:
    n = int(sys.stdin.readline().strip())
    cnt = 0
    if n == 0:
        break

    for i in range(n+1, 2*n +1):
        if is_prime(i):
            cnt += 1
    
    print(cnt)
