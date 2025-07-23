# 최대 힙
'''
1. 배열에 자연수 x를 넣는다
2. 배열에서 가장 큰 값을 출력하고, 그 값을 배열에서 제거한다
'''

import sys
import heapq
input = sys.stdin.readline

pq = []
n = int(input())
for _ in range(n):
    x = int(input())
    if x != 0 :
        heapq.heappush(pq, -x)
    else:
        if pq:
            print(-(heapq.heappop(pq)))
        else:
            print(0)