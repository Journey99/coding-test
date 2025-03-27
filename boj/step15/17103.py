# 골드바흐 파티션
import sys

def sieve(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False

    for i in range(2, int(limit ** 0.5) + 1):
        if primes[i]:
            for j in range(i*i, limit+1, i):
                primes[j] = False
    return primes

limit = 1000000
is_prime = sieve(limit)

t = int(input())
for _ in range(t):
    n = int(sys.stdin.readline().strip())
    cnt = 0

    if n == 4:
        print(1)
    else:
        for i in range(3, n//2+1, 2):
            if is_prime[i] and is_prime[n-i]:
                cnt += 1
        print(cnt)


