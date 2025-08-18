# 벽 부수고 이동하기
from collections import deque
import sys
input = sys.stdin.readline

# n : 행(x) / m : 열(y)
n, m  = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]
# visited[x][y][0] = 벽을 안 부수고 방문
# visited[x][y][1] = 벽을 부수고 방문
visited = [[[False] * 2 for _ in range(m)] for _ in range(n)]

queue = deque()
queue.append((0, 0, 1, 0))  # (x, y, 거리, 벽 부쉈는지 여부)
visited[0][0][0] = True

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    x, y, cnt, broken = queue.popleft()

    if x == n - 1 and y == m - 1:
        print(cnt)
        exit(0)

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            
            # 벽이 아닐 때
            if graph[nx][ny] == 0 and not visited[nx][ny][broken]:
                visited[nx][ny][broken] = True
                queue.append((nx, ny, cnt+1, broken))
            # 벽일 때, 아직 부수지 않았다면 부수고 이동
            elif graph[nx][ny] == 1 and broken == 0 and not visited[nx][ny][1]:
                visited[nx][ny][1] = True
                queue.append((nx, ny, cnt + 1, 1))
        

print(-1)