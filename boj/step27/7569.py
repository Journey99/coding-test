# 토마토
from collections import deque
import sys
input = sys.stdin.readline

def all_ripe(visited):
    for z in visited:
        for row in z:
            for cell in row:
                if not cell:
                    return False
    return True

# m : 열 / n : 행
m, n, h = map(int, input().split())
graph = [list(list(map(int, input().split())) for _ in range(n)) for _ in range(h)]
visited = [[[False for _ in range(m)] for _ in range(n)] for _ in range(h)]

queue = deque()
for z in range(h):
    for x in range(n):
        for y in range(m):
            if graph[z][x][y] == 1:
                queue.append((z, x, y, 0))
                visited[z][x][y] = True
            
            if graph[z][x][y] == -1:
                visited[z][x][y] = True
    
dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, -1, 1, 0, 0]
dz = [0, 0, 0, 0, -1, 1]
days = 0

while queue:
    z, x, y, day = queue.popleft()
    days = max(days, day)

    for i in range(6):
        nx = dx[i] + x
        ny = dy[i] + y
        nz = dz[i] + z

        if 0<= nx < n and 0<= ny < m and 0<= nz < h and not visited[nz][nx][ny]:
            visited[nz][nx][ny] = True
            queue.append((nz, nx, ny, day+1))


if all_ripe(visited):
    print(days)
else:
    print(-1)