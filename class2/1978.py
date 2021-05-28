n = int(input())
nums = list(map(int, input().split()))
cnt = 0

def isPrime(n):
    if n <= 1:
        return False
    i = 2
    while i*i <= n:
        if n % i ==0:
            return False
        i +=1

    return True

for num in nums:
    if isPrime(num):
        cnt += 1

print(cnt)