# 다음 소수
import sys
import math

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n))+1, 2): # 홀수
        if n % i == 0:
            return False
    return True


t = int(input())
for _ in range(t):
    n = int(sys.stdin.readline().strip())

    while not is_prime(n):
        n += 1
    print(n)


'''
소수를 판단하는 것은 루트n 까지만 해도 된다

'''