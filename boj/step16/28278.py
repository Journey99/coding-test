# 스택2
import sys

n = int(input())
s = []
for _ in range(n):
    num = sys.stdin.readline().split()
    if num[0] == '1':
        s.append(int(num[1]))
    elif num[0] == '2':
        if s:
            top = s.pop()
            print(top)
        else:
            print(-1)
    elif num[0] == '3':
        print(len(s))
    elif num[0] == '4':
        if s:
            print(0)
        else:
            print(1)
    else:
        if s:
            print(s[-1])
        else:
            print(-1)
