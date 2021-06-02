# count sort를 이용해서 푸는것
# 원소간의 비교가 아니라 각 원소가 몇개 등장하는 갯수를 세서 정렬

import sys

n = int(input())
result = [0] * 10001

for _ in range(n):
    num = int(sys.stdin.readline())
    result[num] += 1

for i in range(1, 10001):
   if result[i] != 0:
       for j in range(result[i]):
           print(i)







"""
메모리 초과, 시간 초과
일반적인 정렬
n = int(input())
numbers = []

for i in range(n):
    numbers.append(int(input()))

numbers.sort()

for num in numbers:
    print(num)

"""