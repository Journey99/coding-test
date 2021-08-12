# 최소 힙

import heapq
import sys

input = sys.stdin.readline
N = int(input())
queue = []

for i in range(N):
    x = int(input())
    if x == 0:
        if queue:
            print(heapq.heappop(queue))
        else:
            print(0)
    else:
        heapq.heappush(queue, x)