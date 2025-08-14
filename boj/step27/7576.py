# 토마토
from collections import deque
import sys
input = sys.stdin.readline


# n : 행 / m : 열
m, n = map(int, input().split())
visited = [[False] * m for _ in range(n)]
graph = [list(map(int, input().split())) for _ in range(n)]

queue = deque()
for i in range(n):
    for j in range(m):
        if graph[i][j] == 1: 
            queue.append((i, j, 0))
            visited[i][j] = True

        if graph[i][j] == -1:
            visited[i][j] = True

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
days = 0

while queue:
    x, y, day = queue.popleft()
    days = max(days, day) # 최소 날짜 갱신

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = True
            queue.append((nx, ny, day + 1))

if all(all(row) for row in visited):
    print(days)  # 모두 익음
else:
    print(-1)    # 안 익은 토마토 있음