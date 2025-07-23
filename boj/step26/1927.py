# 최소 힙 
'''
1. 배열에 자연수 x를 넣는다
2. 배열에서 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다.
'''

import sys
import heapq
input = sys.stdin.readline

dp = []
n = int(input())

for _ in range(n):
    x = int(input())
    if x != 0:
        heapq.heappush(dp, x)
    else:
        if dp:
            print(heapq.heappop(dp))
        else:
            print(0)