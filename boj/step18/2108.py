# 통계학
import sys

n = int(input())
numbers = []

for _ in range(n):
    numbers.append(int(sys.stdin.readline().strip()))

numbers.sort()
## 산술평균
mean = round(sum(numbers) / n)
## 중앙값  
median = numbers[n // 2]
## 최빈값
mode = []
count = {}
for n in numbers:
    if n in count:
        count[n] += 1
    else:
        count[n] = 1
max_count = max(count.values())
for k, v in count.items():
    if v == max_count:
        mode.append(k)
mode.sort()     

if len(mode) > 1:   
    mode = mode[1]              
else:
    mode = mode[0]

## 범위
range = max(numbers) - min(numbers)

print(mean)
print(median)
print(mode)
print(range)