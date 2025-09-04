# 소수의 연속합

def sieve(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False  # 0과 1은 소수가 아님

    for i in range(2, int(limit**0.5) + 1):
        if primes[i]:
            for j in range(i * i, limit + 1, i):
                primes[j] = False  # i의 배수들은 소수가 아님

    return primes   

n = int(input())
primes_ls = sieve(n)

nums = [i for i in range(2, n+1) if primes_ls[i]]

left, right = 0, 0
current_sum = 0
cnt = 0

while True:
    if current_sum >= n:
        if current_sum == n:
            cnt += 1
        current_sum -= nums[left]
        left += 1
    elif right == len(nums):
        break
    else:
        current_sum += nums[right]
        right += 1

print(cnt)
        
