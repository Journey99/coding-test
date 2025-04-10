# 덱 2
from collections import deque
import sys


deq = deque()
n = int(input())

for _ in range(n):
    command = list(map(int, sys.stdin.readline().split()))

    if command[0] == 1:
        deq.appendleft(command[1])
    elif command[0] == 2:
        deq.append(command[1])
    elif command[0] == 3:
        if deq:
            front = deq.popleft()
            print(front)
        else:
            print(-1)
    elif command[0] == 4:
        if deq:
            back = deq.pop()
            print(back)
        else:
            print(-1)   
    elif command[0] == 5:
        print(len(deq))   
    elif command[0] == 6:
        if deq:
            print(0)
        else:
            print(1)   
    elif command[0] == 7:
        if deq:
            print(deq[0])
        else:
            print(-1)   
    elif command[0] == 8:
        if deq:
            print(deq[-1])
        else:
            print(-1)   
    