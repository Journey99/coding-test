# 소수
## M이상 N이하의 자연수 중 소수인 것을 모두 골라 합과 최솟값을 출력

def isPrime(n):
    if n <= 1:
        return False
    i = 2
    while i*i <= n:
        if n % i ==0:
            return False
        i +=1

    return True


m = int(input())
n = int(input())
result = []

for i in range(m, n+1):
    if isPrime(i):
        result.append(i)

if result:
    print(sum(result))
    print(min(result))
else:
    print(-1)