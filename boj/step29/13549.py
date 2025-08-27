# 숨바꼭질 3

import sys
from collections import deque

input = sys.stdin.readline

def bfs(n, k):
    MAX = 100000
    dist = [-1] * (MAX + 1)  # 방문 및 최단시간 기록
    dq = deque()
    dq.append(n)
    dist[n] = 0

    while dq:
        x = dq.popleft()

        if x == k:
            return dist[x]

        # 2*x 이동 (시간 0초) → deque 앞쪽에 추가
        if 0 <= x*2 <= MAX and dist[x*2] == -1:
            dist[x*2] = dist[x]
            dq.appendleft(x*2)

        # x-1 이동 (시간 1초)
        if 0 <= x-1 <= MAX and dist[x-1] == -1:
            dist[x-1] = dist[x] + 1
            dq.append(x-1)

        # x+1 이동 (시간 1초)
        if 0 <= x+1 <= MAX and dist[x+1] == -1:
            dist[x+1] = dist[x] + 1
            dq.append(x+1)

n, k = map(int, input().split())
print(bfs(n, k))
