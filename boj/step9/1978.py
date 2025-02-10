# 소수 찾기
## 주어진 수 n개 중에서 소수가 몇 개인지 찾아서 출력

n = int(input())
nums = list(map(int, input().split()))

cnt = 0
for n in nums:
    chk = 0
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                chk += 1
    if chk == 0:
        cnt += 1
    
print(cnt)


## 위처럼 할 경우 많은 연산을 해야함
## 자기 자신의 제곱근까지만 해도 소수 판별 가능

def isPrime(n):
    if n <= 1:
        return False
    i = 2
    while i*i <= n:
        if n % i ==0:
            return False
        i +=1

    return True
