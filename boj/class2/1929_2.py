# 소수 구하기

m, n = map(int, input().split())

def isPrime(x):
    if x == 1:
        return False
    for i in range(2, int(x ** 0.5) + 1):      # 2부터 x까지 나눠지는지 보는것보다 2부터 x/2까지 나눠지는지만 보면됨.
        if x % i == 0:
            return False
    return True

for i in range(m, n+1):
    if isPrime(i):
        print(i)