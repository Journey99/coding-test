# 분해합
## 자연수가 주어졌을 때 가장 작은 생성자를 구하라

n = int(input())

min_value = 1000000
for i in range(1, n):
    sum_i = i + sum(map(int, str(i)))
    if sum_i == n:
        min_value = min(min_value, i)

if min_value == 1000000:
    print(0)
else:
    print(min_value)



# 일부과정 생략 
n = int(input())
for i in range(1, n+1):
    num = sum(map(int, str(i)))
    num_sum = i + num
    if num_sum == n:
        print(i)
        break
    if i == n:
        print(0)
