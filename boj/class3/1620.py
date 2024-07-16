# 나는야 포켓몬 마스터 이다솜

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = [0]
dic = {}

for i in range(1, n+1):
    name = input().rstrip()
    lst.append(name)
    dic[name] = i

for _ in range(m):
    p = input().rstrip()
    if p.isdigit():
        print(lst[int(p)])
    else:
        print(dic[p])
