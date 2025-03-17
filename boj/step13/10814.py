# 나이순 정렬 
import sys

n = int(input())
ls = []

for i in range(n):
    age, name = sys.stdin.readline().split()
    ls.append((int(age), name))

ls.sort(key= lambda x : (x[0]))

for l in ls:
    print(f"{l[0]} {l[1]}")