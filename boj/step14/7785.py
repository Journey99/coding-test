# 회사에 있는 사람
import sys

n = int(input())
logs = dict()

for _ in range(n):
    name, status = sys.stdin.readline().split()
    if status == 'enter':
        logs[name] = status
    else:
        del logs[name]

sort_name = sorted(logs.keys(), reverse=True)

for s in sort_name:
    print(s)