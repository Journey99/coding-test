M, N = map(int, input().split())

# 에라토스테네스의 체를 이용
def prime_sieve(M, N):
    N += 1
    sieve = [True] * N
    for i in range(2, int(N**0.5)+1):
        if sieve[i]:
            for j in range(2*i, N, i):
                sieve[j] = False
    for i in range(M, N):
        if i > 1:
            if sieve[i]:
                print(i)

prime_sieve(M, N)