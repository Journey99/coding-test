# 나이순 정렬
import sys

n = int(input())
age_name = []

for i in range(n):
    ag_na = list(map(str,sys.stdin.readline().split()))
    ag_na[0] = int(ag_na[0])
    age_name.append(ag_na)

age_name.sort(key = lambda x : (x[0]))

for i in age_name:
    print(i[0], i[1])



# lambda example
# map(lambda x : x ** 2, range(5))
# => [0, 1, 4, 9, 16]

