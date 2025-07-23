# 절댓값 힙
'''
1. 배열에 정수 x를 넣는다
2. 배열에서 절댓값이 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다.
3. 절댓값이 가장 작은 값이 여러개일 때는, 가장 작은 수를 출력하고 그 값을 배열에서 제거한다
'''

import sys
import heapq
input = sys.stdin.readline

dp = []
n = int(input())

for _ in range(n):
    x = int(input())
    if x != 0:
        heapq.heappush(dp, (abs(x), x))
    else:
        if dp:
            print(heapq.heappop(dp)[1])
        else:
            print(0)
