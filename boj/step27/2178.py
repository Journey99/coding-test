# 미로 탐색
from collections import deque
import sys
input = sys.stdin.readline

# n : 행의 개수 m : 열의 개수
n, m = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        a, b = queue.popleft()

        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 1:
                graph[nx][ny] = graph[a][b] + 1
                queue.append((nx, ny))
    
    return graph[n-1][m-1]

print(bfs(0, 0))
